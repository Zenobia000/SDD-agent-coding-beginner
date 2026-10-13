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

# --- 給學員的範本 hook（curriculum/2-templates/hooks/）的回歸規格 ----------------------
# 不需要 jq：範本 hook 刻意不依賴它，學員機器上不一定有。
for t in curriculum/2-templates/hooks/test-*.sh; do
  [ -f "$t" ] || continue
  run "$t" bash "$t"
done

# --- Starter 專案的測試 -------------------------------------------------------
# 需要先在 leavebot/ 建好 .venv（見 leavebot/README.md）。沒建就明講略過，不假裝綠。
if [ -x leavebot/.venv/bin/pytest ]; then
  run "leavebot pytest" bash -c 'cd leavebot && .venv/bin/pytest -q'
else
  printf '! 略過 starter 測試：找不到 leavebot/.venv（照 leavebot/README.md 建一次）\n'
fi

# --- 檢查腳本自己的回歸規格 -------------------------------------------------
for t in scripts/test-*.sh; do
  [ -f "$t" ] || continue
  run "$(basename "$t")" bash "$t"
done

exit $fail
