#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
if [ -d /results ] && [ -w /results ]; then
  OUT=/results
else
  OUT="$HERE/../results"
  mkdir -p "$OUT"
fi
python3 "$HERE/checker.py" "$HERE"/fixtures/*.json --json | tee "$OUT/suite_output.jsonl"
cmp "$OUT/suite_output.jsonl" "$HERE/reference/suite_output_reference.jsonl"
printf 'PASS: 18-case output matches the archived reference output exactly.\n' > "$OUT/regression_status.txt"
