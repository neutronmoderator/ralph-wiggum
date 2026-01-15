#!/usr/bin/env bash
# ralph.sh - Single iteration of ralph-wiggum with visible output
set -e

echo "=== Starting ralph-wiggum ==="

result=$(claude --dangerously-skip-permissions -p \
"@PRD.md @progress.txt
1. Decide which task to work on next.
   This should be the one YOU decide has the highest priority,
   not necessarily the first in the list.
2. Check any feedback loops, such as types and tests.
3. Append your progress to the progress.txt file.
4. Make a git commit of that feature.

ONLY WORK ON A SINGLE FEATURE.

If all work is complete, output <promise>COMPLETE</promise>.
" 2>&1 | tee /dev/stderr)

echo ""
echo "=== End ==="

if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
  echo "PRD complete!"
  exit 0
fi
