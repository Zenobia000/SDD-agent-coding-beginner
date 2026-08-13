#!/usr/bin/env bash
# guard-secrets.sh 的回歸規格。每條在暫存假 repo 裡 stage 一段內容再餵指令進去 —
# 判準是「這顆 commit 引入了什麼」，所以測試必須有真的 staged diff，不能只餵字串。
# 行為變更必須先改這張表 — 沒有檢查的規則不是規則，是願望。
# 執行：bash hooks/test-guard-secrets.sh（scripts/check.sh 會跑）
set -u
cd "$(dirname "$0")"
HOOK="$PWD/guard-secrets.sh"

fail=0

# run_case <名稱> <指令> <暫存內容> <want ALLOW|BLOCK> [暫存路徑]
run_case() {
  local name="$1" cmd="$2" staged="$3" want="$4" path="${5:-payload.py}"
  local tmp; tmp=$(mktemp -d)
  (
    cd "$tmp" || exit 9
    git init -q
    git config core.autocrlf false
    printf 'seed\n' > seed.txt
    git add seed.txt
    git -c user.email=t@t -c user.name=t commit -qm fixture
    if [ -n "$staged" ]; then
      mkdir -p "$(dirname "$path")"
      printf '%s\n' "$staged" > "$path"
      git add "$path"
    fi
    jq -n --arg c "$cmd" '{tool_input:{command:$c}}' | bash "$HOOK" >/dev/null 2>&1
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

C='git commit -m "x"'

# 這場事故的原樣：evidence/alex-2026-08-11 的 run_cases.py:56
run_case "密碼字面值（本案原樣）"        "$C" 'TEST_PW = "UatTest#2026"'                        BLOCK
run_case "JWT secret 字面值"             "$C" 'API_JWT_SECRET_KEY = "s3cret-value-here"'        BLOCK
run_case "JSON 形狀"                     "$C" '{"password": "UatTest#2026"}'                    BLOCK
run_case "小寫 api_key"                  "$C" 'api_key = "sk-abcdefghijklmnop"'                 BLOCK
run_case "串接時也擋"                    'git status && git commit -m "x"' 'TOKEN = "abcd1234"'  BLOCK

run_case "讀環境變數"                    "$C" 'TEST_PW = os.environ["UAT_TEST_PW"]'             ALLOW
run_case "執行時隨機產生"                "$C" 'SECRET = os.environ.get("X") or token_urlsafe(24)' ALLOW
run_case "樣板佔位"                      "$C" 'PASSWORD = "${VAULT_PW}"'                        ALLOW
run_case "已遮罩"                        "$C" 'PASSWORD = "REDACTED"'                           ALLOW
run_case "散文提到 password"             "$C" '# set the password in uat-creds.env before running' ALLOW
run_case "變數名相符但值是變數"          "$C" 'TEST_PW = cfg.password'                          ALLOW
run_case "非 commit 指令不歸它管"        'git status'  'TEST_PW = "UatTest#2026"'               ALLOW
run_case "暫存區乾淨"                    "$C" ''                                                ALLOW

# 這支閘自己的兩個檔要寫得出它抓的形狀，否則規則無法定義 — 依路徑排除，不是依標記
run_case "閘自己的實作不自擋"            "$C" 'TEST_PW = "UatTest#2026"' ALLOW hooks/guard-secrets.sh
run_case "閘自己的測試不自擋"            "$C" 'TEST_PW = "UatTest#2026"' ALLOW hooks/test-guard-secrets.sh
# setup-skills 會把副本抄進目標專案的 .claude/hooks/ — 副本提交自己時同樣不得自擋
run_case "副本在 .claude/hooks/ 不自擋"  "$C" 'TEST_PW = "UatTest#2026"' ALLOW .claude/hooks/guard-secrets.sh

exit $fail
