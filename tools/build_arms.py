#!/usr/bin/env python3
"""Assemble arms/<type>/<arm>.md from arms/_src/.

Every arm file starts with the same task framing (arms/_src/FRAMING.md), so the only difference
between arms on one type is the guidance. Arm A is the framing alone. Arm D adds the outside GTM
skill (arms/_src/vendor/D-social-SKILL.md, as published). Arm F, on shaping types only, adds the
Superpowers Elements of Style skill as listed: its SKILL.md followed by its elements-of-style.md.
Provenance, commits and licences: arms/_src/vendor/SOURCES.md.
Run before sign; the built files, not the sources, are what HASHES.json freezes.
"""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "arms" / "_src"
TYPES = [f"T{i}" for i in range(1, 9)]
SHAPING = {"T1", "T2", "T6"}  # PREREG.md section 5
HEAD = "\n\n## Writing guidance\n\n"

def main() -> int:
    framing = (SRC / "FRAMING.md").read_text().strip()
    v = SRC / "vendor"
    d = (v / "D-social-SKILL.md").read_text().strip()
    f = (v / "F-SKILL.md").read_text().strip() + "\n\n" + (v / "F-elements-of-style.md").read_text().strip()
    for t in TYPES:
        out = ROOT / "arms" / t
        out.mkdir(parents=True, exist_ok=True)
        arms = {"A": framing,
                "B": framing + HEAD + (SRC / "B" / f"{t}.md").read_text().strip(),
                "C": framing + HEAD + (SRC / "C" / f"{t}.md").read_text().strip()}
        if d: arms["D"] = framing + HEAD + d
        if f and t in SHAPING: arms["F"] = framing + HEAD + f
        for a, text in arms.items():
            (out / f"{a}.md").write_text(text + "\n")
        print(t, " ".join(sorted(arms)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
