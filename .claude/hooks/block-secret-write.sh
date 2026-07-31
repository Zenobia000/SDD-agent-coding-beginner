#!/usr/bin/env bash
# PreToolUse(Write|Edit) — 擋下把 secret 寫進檔案的動作。
#
# 這是「擋」型 hook，是三層防線的第一層：
#   ① 本 hook       —— 寫入當下就擋（最早，成本最低）
#   ② .githooks/pre-commit —— commit 時擋（人和 agent 都適用）
#   ③ /sec-scan     —— 交付前全面掃描（會查歷史）
#
# 為什麼不只靠 CLAUDE.md 寫規則：規則順從率約 ~70%，外洩是不可逆的。
#
# 契約（見 docs/authoring/04-write-a-hook.md）：
#   stdin  : JSON，含 .tool_input.file_path 與 .tool_input.content / .new_string
#   exit 0 + permissionDecision:"deny" : 阻擋
set -uo pipefail

INPUT=$(cat)
FILE=$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // empty')
BODY=$(printf '%s' "$INPUT" | jq -r '[.tool_input.content, .tool_input.new_string] | map(select(. != null)) | join("\n")')

deny() {
  jq -n --arg reason "$1" '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: $reason
    }
  }'
  exit 0
}

# ① 直接寫 .env
case "$FILE" in
  *.env|*.env.*)
    case "$FILE" in
      *.env.example|*.env.sample|*.env.template) ;;   # 範本檔放行
      *) deny "已擋下寫入 $FILE。.env 應由使用者手動建立，且不進版控。要給範本請寫 .env.example。" ;;
    esac
    ;;
esac

[ -z "$BODY" ] && exit 0

# ② 內容裡有看起來像真 key 的東西
#    只擋「明確的供應商格式」與「長度足夠的賦值」，避免誤殺 placeholder
if printf '%s' "$BODY" | grep -Eq 'sk-[A-Za-z0-9_-]{20,}|sk-ant-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|AIza[A-Za-z0-9_-]{30,}|AKIA[A-Z0-9]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----'; then
  deny "偵測到疑似真實憑證。請改用環境變數：os.environ[\"X\"] / process.env.X，並把範例值寫進 .env.example。"
fi

# ③ 硬編碼賦值：KEY = "長字串"，但排掉明顯的佔位符
if printf '%s' "$BODY" | grep -Eiq '(api[_-]?key|secret|password|token|passwd)[[:space:]]*[:=][[:space:]]*["'"'"'][^"'"'"']{16,}["'"'"']'; then
  if ! printf '%s' "$BODY" | grep -Eiq 'your[_-]?|xxx|placeholder|example|<[a-z_]+>|\$\{|os\.environ|process\.env|getenv'; then
    deny "偵測到疑似硬編碼的密鑰賦值。請改從環境變數讀取。若這是佔位符，請用 YOUR_API_KEY_HERE 之類明顯的假值。"
  fi
fi

exit 0
