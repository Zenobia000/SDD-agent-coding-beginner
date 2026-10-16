#!/usr/bin/env bash
# 這個 repo 的全部檢查，一個入口。CI 與 PR 前跑這支就好。
#
# 檢查項目用找的，不用列的 —— 新增一支 scripts/check-*.sh 或一支
# hooks/test-*.sh，它自己就會被跑到，不必回來改這個檔案。
#
# 全綠 exit 0；任何一項紅了 exit 1，且會把每一項的判決列出來。

set -uo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

fail=0

run() {
  local name=$1; shift
  local out status
  out=$("$@" 2>&1); status=$?
  if [ $status -eq 0 ]; then
    printf '✓ %s\n' "$name"
  else
    printf '✗ %s\n' "$name"
    printf '%s\n' "$out" | sed 's/^/    /'
    fail=1
  fi
}

# --- repo 自己的檢查 --------------------------------------------------------
for s in scripts/check-*.sh; do
  [ -f "$s" ] || continue
  run "$(basename "$s")" bash "$s"
done

# --- 護欄 hook 的回歸規格 ---------------------------------------------------
# 不變量：每支 hooks/<name>.sh 都有 hooks/test-<name>.sh，由這裡跑。
if command -v jq >/dev/null 2>&1; then
  while IFS= read -r t; do
    run "${t#.claude/skills/}" bash "$t"
  done < <(find .claude/skills -path '*/hooks/test-*.sh' | sort)
else
  printf '! 略過 hook 測試：找不到 jq\n'
fi

# --- 檢查腳本自己的回歸規格 -------------------------------------------------
for t in scripts/test-*.sh; do
  [ -f "$t" ] || continue
  run "$(basename "$t")" bash "$t"
done

exit $fail
