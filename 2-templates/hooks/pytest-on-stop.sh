#!/usr/bin/env bash
# Claude Code Stop hook：改過 .py 而測試沒過，就不准 agent 說「完成」。
#
# 合約：exit 2 = 擋下，agent 繼續工作；stderr 是給 agent 看的理由。
# 用法見同目錄的 README.md。
#
# PYTEST_CMD 可覆寫測試指令（預設 pytest -q），回歸規格靠它換成假指令。

input=$(cat)

# 上一次阻擋還在處理中 → 放行，避免無限迴圈。不依賴 jq。
printf '%s' "$input" | grep -qE '"stop_hook_active"[[:space:]]*:[[:space:]]*true' && exit 0

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

# 沒有改到 Python 檔，就不跑測試。
git status --porcelain -- '*.py' 2>/dev/null | grep -q . || exit 0

cmd=${PYTEST_CMD:-pytest -q}

if ! out=$($cmd 2>&1); then
  {
    echo "測試沒有通過（$cmd）。修好實作再結束；不准修改或跳過測試來讓它通過："
    printf '%s\n' "$out" | tail -30
  } >&2
  exit 2
fi

exit 0
