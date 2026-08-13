#!/usr/bin/env bash
# check-on-stop.sh 的回歸規格。四條路徑，每條在暫存假 repo 裡搭場景：
# hook 用 cd "$(dirname "$0")/.." 定位 repo，所以複製它進 fixture 就能完全控制
# 表面髒淨與 check.sh 紅綠 — 不需要在生產碼上開注入點。
# 執行：bash hooks/test-check-on-stop.sh（scripts/check.sh 會跑）
set -u
cd "$(dirname "$0")"
HOOK="$PWD/check-on-stop.sh"

fail=0

# run_case <名稱> <payload> <表面髒?0/1> <check綠?0/1> <want ALLOW|BLOCK>
run_case() {
  local name="$1" payload="$2" dirty="$3" green="$4" want="$5"
  local tmp; tmp=$(mktemp -d)
  (
    cd "$tmp" || exit 9
    git init -q
    mkdir hooks scripts skills
    cp "$HOOK" hooks/
    if [ "$green" = 1 ]; then
      printf '#!/usr/bin/env bash\nexit 0\n' > scripts/check.sh
    else
      printf '#!/usr/bin/env bash\necho "  ✗ 假違規"\nexit 1\n' > scripts/check.sh
    fi
    echo x > skills/probe.md
    if [ "$dirty" = 0 ]; then
      git add skills scripts hooks
      git -c user.email=t@t -c user.name=t commit -qm fixture
    fi
    printf '%s' "$payload" | bash hooks/check-on-stop.sh >/dev/null 2>&1
  )
  local code=$?
  local got=ALLOW
  [ "$code" = 2 ] && got=BLOCK
  if [ "$got" = "$want" ]; then
    printf '  ✓ %-5s %s\n' "$want" "$name"
  else
    printf '  ✗ want=%s got=%s(exit %s)  %s\n' "$want" "$got" "$code" "$name"
    fail=1
  fi
  rm -rf "$tmp"
}

run_case "stop_hook_active=true 防迴圈：即使髒且紅也放行" '{"stop_hook_active":true}' 1 0 ALLOW
run_case "表面乾淨：check 紅也放行（沒動技能就不歸它管）"  '{}'                        0 0 ALLOW
run_case "表面髒且 check 紅：擋下，不准收工"                '{}'                        1 0 BLOCK
run_case "表面髒但 check 綠：放行"                          '{}'                        1 1 ALLOW

exit $fail
