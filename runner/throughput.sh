#!/usr/bin/env bash
# Throughput test: N samples at concurrency C. Synthetic prompt; not study data.
# Usage: throughput.sh N C outdir
set -uo pipefail
N=$1; C=$2; OUT=$3; HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"
printf 'You write short B2B LinkedIn posts.' > "$OUT/sys.txt"
printf 'Write a 120-word LinkedIn post about what a field sales team learned from piloting an AI note-taker for one quarter. Synthetic scenario; invent no real company names.' > "$OUT/usr.txt"
date +%s > "$OUT/t0"
seq -w 1 "$N" | xargs -P "$C" -I{} "$HERE/sample.sh" "$OUT/sys.txt" "$OUT/usr.txt" "$OUT/s{}.json"
date +%s > "$OUT/t1"
python3 "$HERE/summarize_throughput.py" "$OUT"
