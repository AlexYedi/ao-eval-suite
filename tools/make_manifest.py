#!/usr/bin/env python3
"""Write or check prereg/HASHES.json, the registration manifest (PREREG.md section 15).

  tools/make_manifest.py          write HASHES.json and print the registration hash (run at sign)
  tools/make_manifest.py --check  exit 1 if any frozen file differs from HASHES.json (run before every sample)

The manifest holds the sha256 of PREREG.md with its sign-date and hash fields blanked, of
failure-type-selection.md, of runner/PIN, and of every file under arms/, fixtures/ and graders/;
plus the pinned model id and the pinned CLI's `--version`. The registration hash is the sha256
of the manifest serialised as sorted, compact JSON.
"""
import hashlib, json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "prereg" / "HASHES.json"
BLANK = [(re.compile(r"^\| Sign date \|.*$", re.M), "| Sign date | |"),
         (re.compile(r"^\| Registration hash \|.*$", re.M), "| Registration hash | |"),
         (re.compile(r"^Date:.*$", re.M), "Date:"),
         (re.compile(r"^Registration hash:.*$", re.M), "Registration hash:")]

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def pin():
    vals = dict(re.findall(r"^(\w+)=(.*)$", (ROOT / "runner" / "PIN").read_text(), re.M))
    return {k: v.strip("\"'").replace("$HOME", str(pathlib.Path.home())) for k, v in vals.items()}

def build():
    prereg = (ROOT / "prereg" / "PREREG.md").read_text()
    for rx, sub in BLANK:
        prereg = rx.sub(sub, prereg)
    files = {"prereg/PREREG.md (hash and date fields blank)": sha(prereg.encode()),
             "prereg/failure-type-selection.md": sha((ROOT / "prereg" / "failure-type-selection.md").read_bytes()),
             "runner/PIN": sha((ROOT / "runner" / "PIN").read_bytes())}
    for d in ("arms", "fixtures", "graders"):
        for f in sorted((ROOT / d).rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts and f.name != ".DS_Store":
                files[str(f.relative_to(ROOT))] = sha(f.read_bytes())
    p = pin()
    version = subprocess.run([p["PINNED_CLAUDE_BIN"], "--version"], capture_output=True, text=True).stdout.strip()
    return {"model": p["PINNED_MODEL"], "claude_version": version, "files": files}

def reg_hash(m):
    return sha(json.dumps(m, sort_keys=True, separators=(",", ":")).encode())

if __name__ == "__main__":
    m = build()
    if "--check" in sys.argv:
        frozen = json.loads(OUT.read_text())
        bad = sorted(k for k in set(frozen["manifest"]["files"]) | set(m["files"])
                     if frozen["manifest"]["files"].get(k) != m["files"].get(k))
        bad += [k for k in ("model", "claude_version") if frozen["manifest"][k] != m[k]]
        if bad:
            print("manifest mismatch; refusing to sample:\n  " + "\n  ".join(bad)); sys.exit(1)
        print("manifest ok", frozen["registration_hash"]); sys.exit(0)
    OUT.write_text(json.dumps({"registration_hash": reg_hash(m), "manifest": m}, indent=1, sort_keys=True) + "\n")
    print(reg_hash(m))
