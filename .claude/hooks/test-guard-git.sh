#!/usr/bin/env bash
# guard-git.sh 的回歸規格。每列：預期判決 <TAB> 指令。
# 行為變更必須先改這張表 — 沒有檢查的規則不是規則，是願望。
# 執行：bash hooks/test-guard-git.sh（scripts/check.sh 會跑）
set -u
cd "$(dirname "$0")"

fail=0
while IFS=$'	' read -r want cmd; do
  [ -z "$want" ] && continue
  if jq -n --arg c "$cmd" '{tool_input:{command:$c}}' | bash guard-git.sh >/dev/null 2>&1; then
    got=ALLOW
  else
    got=BLOCK
  fi
  if [ "$got" = "$want" ]; then
    printf '  ✓ %-5s %s\n' "$want" "$cmd"
  else
    printf '  ✗ want=%s got=%s  %s\n' "$want" "$got" "$cmd"
    fail=1
  fi
done <<'CASES'
ALLOW	git reset --hard HEAD
BLOCK	git reset --hard
BLOCK	git reset --hard HEAD~1
BLOCK	git reset --hard origin/main
ALLOW	git status && git reset --hard HEAD
BLOCK	git reset --hard HEAD && git reset --hard abc123
ALLOW	git commit -m "do not mention git reset --hard here"
ALLOW	git reset HEAD~1
BLOCK	git add -A
BLOCK	git add .
ALLOW	git add file.txt other/file.md
BLOCK	git push --force origin main
BLOCK	git push -f
BLOCK	git commit --no-verify -m "x"
BLOCK	gh pr merge 100 --merge
BLOCK	gh pr merge --squash --delete-branch
BLOCK	gh pr view 100 --json state && gh pr merge 100
BLOCK	gh api repos/o/r/pulls/100/merge --method PUT
ALLOW	gh pr view 100 --json state,mergedAt
ALLOW	gh pr create --title "x" --body-file body.md
ALLOW	git commit -m "tell the user to run gh pr merge themselves"
ALLOW	gh api repos/o/r/pulls/100 --jq .mergeable
CASES

exit $fail
