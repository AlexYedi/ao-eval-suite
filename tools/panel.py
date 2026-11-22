#!/usr/bin/env python3
"""Three-judge author-read panel (deviation D3). Not part of the signed manifest.

For every sample the author read would cover (graded fail, or code-vs-blind disagreement; PREREG section 9),
three judges on different models answer the author's question: is this a genuine instance of the habit?

  auto-accept  all three say genuine=yes with high confidence, no code/blind disagreement, no quoted-only match
  raised       anything else: dissent, unsure, medium/low confidence, disagreement, quoted-only match
  audit        a 10% random sample of auto-accepted items (seeded from the item ids), mixed in unmarked

  python3 tools/panel.py run <phase_dir> [-j 4]       -> <phase_dir>/panel/... + review.md + panel-key.json
  python3 tools/panel.py calibrate results/phase1     -> compare with author-grades.json
"""
import concurrent.futures as cf, hashlib, json, math, pathlib, random, re, sys, tempfile

sys.dont_write_bytecode = True
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import screen  # noqa: E402

JUDGES = ["claude-sonnet-5-5", "claude-opus-5-5", "claude-fable-5-2"]
PROMPT = (ROOT / "tools" / "panel_prompt.md").read_text().replace(
    "{{PRECEDENTS}}", (ROOT / "tools" / "panel_precedents.md").read_text().strip())


def items(phase_dir):
    out = []
    for gp in sorted(phase_dir.glob("grades/T*/*/rep*.json")):
        g = json.load(open(gp))
        if g["final"] == "fail" or g["code_blind_disagree"]:
            t, arm, rep = gp.parts[-3], gp.parts[-2], gp.stem
            s = json.load(open(phase_dir / "samples" / t / arm / f"{rep}.json"))
            out.append({"id": f"{t}/{arm}/{rep}", "type": t, "arm": arm, "rep": rep, "grade": g, "text": s.get("text") or ""})
    return out


def judge(it, model, preds):
    ev = "; ".join(x for x in (f"code: {it['grade']['code']['evidence']}",
                               f"blind: {(it['grade'].get('blind') or {}).get('evidence', '')}") if x)
    q = (PROMPT.replace("{{FIXTURE}}", (ROOT / "fixtures" / it["type"] / "prompt.md").read_text())
         .replace("{{SAMPLE}}", it["text"]).replace("{{HABIT}}", preds[it["type"]]["name"])
         .replace("{{PREDICATE}}", preds[it["type"]]["predicate"]).replace("{{EVIDENCE}}", ev))
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        (d / "sys.md").write_text("")
        (d / "q.md").write_text(q)
        (d / "o.json").parent.mkdir(exist_ok=True)
        import subprocess
        subprocess.run(["bash", str(screen.SAMPLE_SH), str(d / "sys.md"), str(d / "q.md"), str(d / "o.json"), model],
                       capture_output=True, text=True)
        r = json.load(open(d / "o.json"))
    m = re.search(r"\{.*\}", r.get("text") or "", re.S)
    try:
        v = json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        v = {}
    ok = v.get("genuine") in ("yes", "no", "unsure") and v.get("confidence") in ("high", "medium", "low")
    return {"model": model, "served": r.get("models_served"), "ok": ok, "cost_usd": r.get("cost_usd"),
            **({k: v.get(k) for k in ("genuine", "confidence", "evidence", "reason")} if ok else {"genuine": "unsure",
                                                                                              "confidence": "low",
                                                                                              "evidence": "",
                                                                                              "reason": "judge output unreadable"})}


def decide(it, votes):
    quoted = "inside quotation" in it["grade"]["code"]["evidence"]
    if it["grade"]["code_blind_disagree"]:
        return "raised", "code and blind grader disagree"
    if quoted:
        return "raised", "match only inside quoted material"
    if all(v["genuine"] == "yes" and v["confidence"] == "high" for v in votes):
        return "accepted", "3/3 genuine, high confidence"
    no = sum(v["genuine"] == "no" for v in votes)
    return "raised", f"{no} judge(s) say not the habit" if no else "a judge is unsure or below high confidence"


def run(phase_dir, jobs=4):
    preds = screen.predicates_from_prereg()
    its = items(phase_dir)
    pd = phase_dir / "panel"
    pd.mkdir(exist_ok=True)

    def one(it):
        p = pd / f"{it['id'].replace('/', '_')}.json"
        if p.exists():
            return json.load(open(p))
        votes = [judge(it, m, preds) for m in JUDGES]
        status, why = decide(it, votes)
        rec = {"id": it["id"], "status": status, "why": why, "votes": votes}
        json.dump(rec, open(p, "w"), indent=1)
        return rec

    with cf.ThreadPoolExecutor(jobs) as ex:
        recs = list(ex.map(one, its))
    accepted = sorted(r["id"] for r in recs if r["status"] == "accepted")
    seed = int(hashlib.sha256("\n".join(sorted(r["id"] for r in recs)).encode()).hexdigest()[:12], 16)
    audit = sorted(random.Random(seed).sample(accepted, math.ceil(0.10 * len(accepted)))) if accepted else []
    raised = sorted(r["id"] for r in recs if r["status"] == "raised")
    review = raised + audit
    random.Random(seed + 1).shuffle(review)
    by = {r["id"]: r for r in recs}
    txt = {it["id"]: it["text"] for it in its}
    lines = [f"# Author review ({phase_dir.name}, deviation D3)\n",
             f"{len(review)} items. For each: **keep** the fail grade, or **overturn** with a one-line reason.\n"]
    for n, i in enumerate(review, 1):
        r = by[i]
        lines.append(f"## {n}. {i}\n")
        lines.append("\n".join("> " + ln for ln in txt[i].splitlines()) + "\n")
        for v in r["votes"]:
            lines.append(f"- **{v['model']}**: {v['genuine']} ({v['confidence']}) · {v.get('evidence')!r} · {v.get('reason')}")
        lines.append("\n**Decision:** keep / overturn: ____\n")
    (phase_dir / "review.md").write_text("\n".join(lines))
    key = {"seed": seed, "n_items": len(recs), "accepted": accepted, "raised": raised, "audit": audit,
           "cost_usd": round(sum((v.get("cost_usd") or 0) for r in recs for v in r["votes"]), 3)}
    json.dump(key, open(phase_dir / "panel-key.json", "w"), indent=1)
    print(f"panel: {len(recs)} items · accepted {len(accepted)} · raised {len(raised)} · audit {len(audit)} · "
          f"cost ${key['cost_usd']}")
    return recs, key


def calibrate(phase_dir):
    recs, key = run(phase_dir)
    author = {f"{a['type']}/A/{a['rep']}": a for a in json.load(open(phase_dir / "author-grades.json"))["items"]}
    rows, miss = [], 0
    for r in sorted(recs, key=lambda r: r["id"]):
        a = author[r["id"]]["author"]
        overturned = a.startswith("overturn")
        bad = overturned and r["status"] == "accepted"         # the failure that matters: a real overturn auto-accepted
        miss += bad
        if overturned or r["status"] == "raised":
            rows.append(f"| {r['id']} | {a} | {r['status']} | {r['why']} |{' **MISS**' if bad else ''}")
    md = ("# Panel calibration on Phase 1 (deviation D3)\n\n"
          f"{key['n_items']} items the author read covered. Panel: accepted {len(key['accepted'])}, raised "
          f"{len(key['raised'])}. Author overturns auto-accepted by the panel (must be 0): **{miss}**.\n\n"
          "Baseline: a do-nothing reviewer that accepts every fail would have accepted the author's 1 overturn "
          "(T1/A/rep14) and raised nothing.\n\n"
          "| Item | Author decision | Panel | Why |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
    (phase_dir / "panel-calibration.md").write_text(md)
    print(md)
    return miss


if __name__ == "__main__":
    j = int(sys.argv[sys.argv.index("-j") + 1]) if "-j" in sys.argv else 4
    if sys.argv[1] == "calibrate":
        sys.exit(1 if calibrate(ROOT / sys.argv[2]) else 0)
    run(ROOT / sys.argv[2], j)
