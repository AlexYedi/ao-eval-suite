#!/usr/bin/env bash
# Clean sampling: one completion with no memory, settings, MCP or tools.
# Usage: sample.sh <system_prompt_file> <user_prompt_file> <out_file> [model]
set -euo pipefail
SYS="$(cat "$1")"; USR="$(cat "$2")"; OUT="$(cd "$(dirname "$3")" && pwd)/$(basename "$3")"; MODEL="${4:-sonnet}"
WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
cd "$WORK"
START=$(python3 -c 'import time;print(time.time())')
# Retry up to 2 times on empty/failed output (seen 2/100 at startup, 11/10).
# Every attempt is counted and published; retries are a logged deviation class.
ATTEMPTS=0
for i in 1 2 3; do
  ATTEMPTS=$i
  CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude -p --model "$MODEL" \
    --system-prompt "$SYS" --setting-sources "" --strict-mcp-config \
    --mcp-config '{"mcpServers":{}}' --tools "" --output-format json \
    "$USR" > "$OUT.raw" 2>> "$OUT.err" || echo "EXIT $? attempt $i" >> "$OUT.err"
  python3 -c 'import json,sys;r=json.load(open(sys.argv[1]));sys.exit(0 if not r.get("is_error") and r.get("result","").strip() else 1)' "$OUT.raw" 2>/dev/null && break
  echo "empty-or-error attempt $i" >> "$OUT.err"; sleep $((i*3))
done
END=$(python3 -c 'import time;print(time.time())')
python3 - "$OUT" "$START" "$END" "$ATTEMPTS" <<'PY'
import json,sys
out,s,e,a=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4])
try: r=json.load(open(out+".raw")); ok=not r.get("is_error",False); text=r.get("result","")
except Exception as ex: r={}; ok=False; text=""
json.dump({"ok":ok,"attempts":a,"start":s,"end":e,"secs":round(e-s,2),"text":text,
  "usage":r.get("usage"),"cost_usd":r.get("total_cost_usd")},open(out,"w"),indent=1)
PY
