#!/usr/bin/env bash
# pytest-on-stop.sh 的回歸規格。四條路徑，每條在暫存假 repo 裡搭情境。
# 用 PYTEST_CMD 換掉真的 pytest，所以不需要安裝 Python 套件也能跑。
#
# 全過 exit 0；任何一條不符預期 exit 1，並印出哪一條。

set -uo pipefail
HOOK="$(cd "$(dirname "$0")" && pwd)/pytest-on-stop.sh"
fail=0

mkrepo() {
  local d
  d=$(mktemp -d)
  git -C "$d" init -q
  git -C "$d" -c user.email=t@t -c user.name=t commit -q --allow-empty -m init
  printf '%s' "$d"
}

expect() {   # 名稱 預期exit 實際exit
  if [ "$2" != "$3" ]; then
    printf 'FAIL  %s：預期 exit %s，實際 %s\n' "$1" "$2" "$3"
    fail=1
  fi
}

# 1. 已經在處理上一次的阻擋 → 放行，避免無限迴圈
d=$(mkrepo); echo 'x=1' > "$d/a.py"
(cd "$d" && echo '{"stop_hook_active": true}' | PYTEST_CMD=false bash "$HOOK" 2>/dev/null); expect loop_guard 0 $?

# 2. 沒有改到 .py → 不跑測試，放行
d=$(mkrepo); echo 'hi' > "$d/notes.md"
(cd "$d" && echo '{}' | PYTEST_CMD=false bash "$HOOK" 2>/dev/null); expect no_python_change 0 $?

# 3. 改了 .py 而且測試紅 → 擋下（exit 2）
d=$(mkrepo); echo 'x=1' > "$d/a.py"
(cd "$d" && echo '{}' | PYTEST_CMD=false bash "$HOOK" 2>/dev/null); expect red_blocks 2 $?

# 4. 改了 .py 而且測試綠 → 放行
d=$(mkrepo); echo 'x=1' > "$d/a.py"
(cd "$d" && echo '{}' | PYTEST_CMD=true bash "$HOOK" 2>/dev/null); expect green_passes 0 $?

exit $fail
