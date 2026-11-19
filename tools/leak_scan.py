#!/usr/bin/env python3
"""Static leak scan (PREREG.md section 8). Run over fixtures/, results/ and reports/ before every publish.

Fails on: email addresses, phone numbers, local filesystem paths, URLs, and any capitalised
name-like pair of words that is not in fixtures/NAMES.txt (the allowlist of invented names and
ordinary phrases). Exit 0 = clean, 1 = findings.
"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
ALLOW = {l.strip() for l in (ROOT / "fixtures" / "NAMES.txt").read_text().splitlines()
         if l.strip() and not l.startswith("#")}
CHECKS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"),
    "phone": re.compile(r"(?<!\d)(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?!\d)"),
    "path": re.compile(r"(?:/Users/|/home/|[A-Z]:\\\\)"),
    "url": re.compile(r"https?://"),
}
NAME = re.compile(r"\b[A-Z][a-z]+(?:-[A-Z][a-z]+)?(?:\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)?)+\b")

def scan(paths):
    out = []
    for base in paths:
        for f in sorted((ROOT / base).rglob("*")):
            if not f.is_file() or f.name == "NAMES.txt" or f.suffix not in {".md", ".json", ".txt"}:
                continue
            text = f.read_text(errors="replace")
            for kind, rx in CHECKS.items():
                out += [(f, kind, m.group(0)) for m in rx.finditer(text)]
            for m in NAME.finditer(text):
                words = m.group(0).split()
                if not any(" ".join(words[i:j]) in ALLOW for i in range(len(words)) for j in range(i + 1, len(words) + 1) if j - i >= 1) \
                   and m.group(0) not in ALLOW:
                    out.append((f, "name", m.group(0)))
    return out

if __name__ == "__main__":
    targets = sys.argv[1:] or ["fixtures", "results", "reports"]
    findings = scan([t for t in targets if (ROOT / t).exists()])
    for f, kind, val in findings:
        print(f"{f.relative_to(ROOT)}\t{kind}\t{val}")
    print(f"{len(findings)} finding(s)")
    sys.exit(1 if findings else 0)
