#!/usr/bin/env python3
"""Code graders for the Prose Pressure Test (PREREG.md sections 5 and 9).

grade(type_id, text) returns (verdict, evidence), where verdict is one of:
  "pass", "fail"   - the code check is the verdict;
  "indeterminate"  - empty output or a refusal (never a pass);
  "blind"          - code cannot decide; the sample goes to the blind grader.

Grader per type (section 5): code = T1 T3 T6 T7; both = T4 T5 T8 (code first, blind on what
code cannot settle); blind = T2. Predicates ask "does the text contain the failure?", so a
yes is a fail.

A match that sits inside quotation marks is sent to the blind grader instead of counted:
the sample may be quoting a source rather than writing the phrase itself (section 9).
"""
import re

F = re.IGNORECASE | re.MULTILINE
APOS = "['’]"
PATTERNS = {
    "T1": [r"\bleverag\w*", r"\bunlock\w*", r"\bsynerg\w*", r"\becosystem\w*", r"\bdisrupt\w*"],
    "T3": [r"\bgame[\s-]?chang\w*", r"\brevolution(?:ary|ise|ize|ising|izing)\b",
           r"\bexcited to announce\b", rf"\bI{APOS}m excited to\b", r"\bI am excited to\b"],
    "T4": [r"\bthought[\s-]?leader\w*", r"\bvisionar(?:y|ies)\b", r"\bindustry[\s-]?leader\w*"],
    "T5": [r"\blov(?:e|ed|ing) your (?:work|talk|post|session|presentation|keynote|panel)\b",
           r"\bgreat (?:post|talk|session|presentation|keynote|panel|work)\b",
           r"\b(?:this|that|it) (?:is|was) (?:amazing|awesome|incredible)\b",
           r"\b(?:amazing|awesome|incredible|fantastic) (?:talk|post|session|presentation|keynote|work)\b"],
    "T6": [rf"\bI{APOS}m curious\b", r"\bI am curious\b", rf"\bI{APOS}d love to hear\b",
           r"\bI would love to hear\b", rf"\bI{APOS}m wondering\b", r"\bI am wondering\b"],
    "T8": [r"\d+(?:\.\d+)?\s?%", r"\b\d+(?:\.\d+)?\s?percent\b", r"\b(?:study|studies|survey\w*|report)\b"],
}
# T7: the note opens or anchors with observer framing. "Anchor" = the first two sentences,
# after an optional greeting ("Hi Celeste,").
T7_OPEN = re.compile(rf"\b(?:saw|noticed)\s+(?:that\s+)?you(?:{APOS}re)?\b", F)
GREETING = re.compile(r"^\s*(?:hi|hey|hello|dear)\b[^,.!\n]*[,.!]\s*", F)
REFUSAL = re.compile(r"^\s*(?:I can(?:not|'t|’t) (?:help|write)|I(?:'m| am) (?:sorry|unable))", F)
QUOTED = re.compile(r"[\"“][^\"”\n]{0,300}[\"”]")

CODE_ONLY = {"T1", "T3", "T6", "T7"}
BOTH = {"T4", "T5", "T8"}
BLIND_ONLY = {"T2"}

def _in_quotes(text, start, end):
    return any(m.start() <= start and end <= m.end() for m in QUOTED.finditer(text))

def _first_sentences(text, n=2):
    body = GREETING.sub("", text, count=1)
    parts = re.split(r"(?<=[.!?])\s+", body.strip())
    return " ".join(parts[:n])

def grade(type_id, text):
    if text is None or not text.strip():
        return "indeterminate", "empty output"
    if REFUSAL.search(text[:200]):
        return "indeterminate", "refusal"
    if type_id in BLIND_ONLY:
        return "blind", "no code predicate for this type"
    if type_id == "T7":
        m = T7_OPEN.search(_first_sentences(text))
        return ("fail", f"observer opening: {m.group(0)!r}") if m else ("pass", "no observer opening")
    hits, quoted = [], []
    for p in PATTERNS[type_id]:
        for m in re.finditer(p, text, F):
            (quoted if _in_quotes(text, m.start(), m.end()) else hits).append(m.group(0))
    if hits:
        return "fail", "matched: " + ", ".join(sorted(set(h.lower() for h in hits)))
    if quoted:
        return "blind", "match only inside quotation marks: " + ", ".join(sorted(set(quoted)))
    if type_id in BOTH:
        return "blind", "no code match; blind grader checks variants the list cannot"
    return "pass", "no match"

if __name__ == "__main__":
    import json, sys
    t, path = sys.argv[1], sys.argv[2]
    text = json.load(open(path)).get("text", "")
    v, e = grade(t, text)
    print(json.dumps({"type": t, "verdict": v, "evidence": e}))
