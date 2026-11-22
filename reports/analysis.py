#!/usr/bin/env python3
"""The analysis in PREREG.md section 12, run once on the sealed results. Writes reports/RESULTS.md.

Final grade per sample = the pre-read grade (results/phaseN/grades), with the author's overturns applied
(results/phaseN/author-grades.json). Determinate samples only in every test.
"""
import glob, json, math, pathlib, re, statistics, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RES = ROOT / "results"


def final_grades(phase):
    pd = RES / f"phase{phase}"
    ov = {}
    ap = pd / "author-grades.json"
    if ap.exists():
        for it in json.load(open(ap))["items"]:
            if it["author"].startswith("overturn"):
                ov[(it["type"], it.get("arm", "A"), it["rep"])] = "pass"
    cells = {}
    for gp in sorted(pd.glob("grades/T*/*/rep*.json")):
        g = json.load(open(gp))
        t, arm, rep = gp.parts[-3], gp.parts[-2], gp.stem
        s = json.load(open(pd / "samples" / t / arm / f"{rep}.json"))
        cells.setdefault((t, arm), []).append({"final": ov.get((t, arm, rep), g["final"]), "text": s.get("text") or "",
                                               "usage": s.get("usage") or {}, "disagree": g["code_blind_disagree"]})
    return cells


def counts(rows):
    det = [r for r in rows if r["final"] != "indeterminate"]
    return sum(r["final"] == "fail" for r in det), len(det), len(rows) - len(det)


def fisher_two_sided(a, b, c, d):
    """2x2 [[a, b], [c, d]]; sum of hypergeometric probabilities <= observed (relative tolerance 1e-7)."""
    r1, r2, c1, n = a + b, c + d, a + c, a + b + c + d

    def p(x):
        return math.comb(r1, x) * math.comb(r2, c1 - x) / math.comb(n, c1)
    obs = p(a)
    lo, hi = max(0, c1 - r2), min(r1, c1)
    return min(1.0, sum(p(x) for x in range(lo, hi + 1) if p(x) <= obs * (1 + 1e-7)))


def wilson(k, n, z=1.959964):
    if n == 0:
        return 0.0, 1.0
    ph = k / n
    den = 1 + z * z / n
    mid = (ph + z * z / (2 * n)) / den
    half = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return max(0.0, mid - half), min(1.0, mid + half)


def newcombe(k1, n1, k2, n2):
    """Risk difference p1 - p2 with the Newcombe hybrid (Wilson-score) 95% interval."""
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    d = p1 - p2
    return d, d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2), d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj, run = [0.0] * len(ps), 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = run
    return adj


def variance(rows):
    first = {re.sub(r"\W+", " ", (r["text"].strip().splitlines() or [""])[0].lower()).strip() for r in rows}
    bins = {len(r["text"]) // 50 for r in rows}
    return len(first), len(bins)


def med_tokens(rows):
    v = [sum((r["usage"].get(k) or 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
         for r in rows]
    return int(statistics.median(v)) if v else 0


def compare(cells, t, x, y):
    kx, nx, _ = counts(cells[(t, x)])
    ky, ny, _ = counts(cells[(t, y)])
    p = fisher_two_sided(ky, ny - ky, kx, nx - kx)           # rows: y (baseline) then x
    d, lo, hi = newcombe(ky, ny, kx, nx)                     # baseline minus arm: positive = arm fails less
    zero_var = variance(cells[(t, x)])[0] == 1 and variance(cells[(t, y)])[0] == 1 and kx in (0, nx) and ky in (0, ny) \
        and kx == ky
    noinfo = abs(d) <= 0.10 or zero_var
    return {"t": t, "x": x, "y": y, "kx": kx, "nx": nx, "ky": ky, "ny": ny, "p": p, "d": d, "lo": lo, "hi": hi,
            "noinfo": noinfo}


def main():
    p1 = final_grades(1)
    p2 = final_grades(2)
    red = [t for t in sorted({t for t, _ in p1}) if counts(p1[(t, "A")])[0] >= 5 and counts(p1[(t, "A")])[1] >= 12]
    phase1_result = (RES / "phase1" / "RESULT.md").read_text()
    exploratory = {t for t in red if re.search(rf"^\| {t} \|.*exploratory", phase1_result, re.M)}
    p2_result = RES / "phase2" / "RESULT.md"
    if p2_result.exists():
        exploratory |= {t for t in red if re.search(rf"^\| {t} \|.*exploratory", p2_result.read_text(), re.M)}
    confirm = [t for t in red if t not in exploratory]
    arms = sorted({a for t, a in p2 if t in red})

    out = ["# Results (PREREG section 12)\n",
           "Run once on the sealed results. Every rate is shown with its denominator. Baselines: arm A in the same type "
           "for every arm; chance for every agreement statistic. A difference within 0.10 of its baseline is reported "
           "as \"no information\".\n",
           "## Phase 1 (screen)\n", "| Type | k_A / n_det_A (16) | Status |", "|---|---|---|"]
    for t in sorted({t for t, _ in p1}):
        k, n, _ = counts(p1[(t, "A")])
        out.append(f"| {t} | {k} / {n} (16) | {'RED' if t in red else 'not RED'}"
                   f"{' · exploratory' if t in exploratory else ''} |")
    out += ["\n## Phase 2 cells\n",
            "| Type | Arm | Fails k / n_det (16) | Indeterminate | Distinct first lines | Length bins | Median input tokens |",
            "|---|---|---|---|---|---|---|"]
    for t in red:
        for a in arms:
            if (t, a) in p2:
                k, n, ind = counts(p2[(t, a)])
                fl, lb = variance(p2[(t, a)])
                out.append(f"| {t} | {a} | **{k} / {n} (16)** | {ind} | {fl} | {lb} | {med_tokens(p2[(t, a)])} |")

    def fmt(c, padj, label):
        verdict = "no information" if c["noinfo"] else ("fewer failures" if c["d"] > 0 else "more failures")
        return (f"| {c['t']} | {c['x']} vs {c['y']} | {c['kx']}/{c['nx']} vs {c['ky']}/{c['ny']} | "
                f"{c['d']:+.2f} [{c['lo']:+.2f}, {c['hi']:+.2f}] | {c['p']:.4g} | {padj:.4g} | {verdict} | {label} |")
    out += ["\n## Primary (H2): B vs A, Holm across confirmatory RED types\n",
            "Risk difference = baseline (A) fail rate minus arm fail rate; positive means the arm fails less.\n",
            "| Type | Comparison | Fails | Risk difference [95% Newcombe] | p | Holm p | Reading | Label |",
            "|---|---|---|---|---|---|---|---|"]
    prim = [compare(p2, t, "B", "A") for t in confirm]
    for c, pa in zip(prim, holm([c["p"] for c in prim])):
        out.append(fmt(c, pa, "confirmatory"))
    for t in sorted(exploratory):
        c = compare(p2, t, "B", "A")
        out.append(fmt(c, c["p"], "exploratory (uncorrected)"))
    out += ["\n## Secondary (H3, H4): within each type, Holm across its comparisons\n",
            "| Type | Comparison | Fails | Risk difference [95% Newcombe] | p | Holm p (within type) | Reading | Label |",
            "|---|---|---|---|---|---|---|---|"]
    for t in red:
        sec = [compare(p2, t, x, y) for x, y in (("C", "A"), ("D", "A"), ("F", "A"), ("C", "B"))
               if (t, x) in p2 and (t, y) in p2]
        for c, pa in zip(sec, holm([c["p"] for c in sec])):
            out.append(fmt(c, pa, "secondary"))
    out.append("\n**Input length.** Arms B and C add under 150 words; arm D about 2,800. A D-vs-A difference cannot be "
               "attributed to content alone, because length and content vary together.\n")
    (ROOT / "reports" / "RESULTS.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
