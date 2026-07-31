# 04 — 寫一個 hook

## 這是什麼

**在特定事件自動執行的腳本。六種資產裡唯一「AI 沒得選」的那一種。**

---

## 什麼時候用它而不是別的

判斷標準只有一個：**這件事做錯了能不能還原？**

```
可逆   → rule 就好（約 70% 順從率，夠用）
不可逆 → hook（100%）
```

寫進文件的規則有約 30% 的機率不被遵守。
`rm -rf`、force push、secret 外洩 —— **這些不能賭那 30%**。

hook 的另外兩個用途（不是為了擋東西）：
- **注入**：每輪對話補上狀態（你在第幾站、現在幾點、待辦有什麼）
- **自動化**：把「每次都要記得做」的雜事搬到系統（格式化、更新索引）

完整決策樹 → [`07-choose-which.md`](./07-choose-which.md)

---

## 最小可跑範例

### 兩個檔案

**① 註冊在 `.claude/settings.json`**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash",
            "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/my-hook.sh"],
            "timeout": 10,
            "statusMessage": "檢查中"
          }
        ]
      }
    ]
  }
}
```

> **用 `command` + `args` 的 exec 形式**，不要把整個路徑塞進 `command` 字串 ——
> 路徑有空白時會壞。

**② 腳本 `.claude/hooks/my-hook.sh`**
```bash
#!/usr/bin/env bash
set -uo pipefail

INPUT=$(cat)                                          # stdin 是一包 JSON
CMD=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty')

if printf '%s' "$CMD" | grep -q 'dangerous-thing'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "說清楚為什麼擋，以及該怎麼做"
    }
  }'
fi
exit 0
```

記得 `chmod +x`。

---

## 五種事件

| 事件 | 何時觸發 | stdin 有什麼 | 典型用途 |
|---|---|---|---|
| `UserPromptSubmit` | 你送出訊息 | `.prompt` | **注入**狀態 |
| `PreToolUse` | 工具執行前 | `.tool_name` `.tool_input` | **擋** |
| `PostToolUse` | 工具執行後 | 上述 + `.tool_output` | **自動化** |
| `Stop` | 回合結束 | `.last_assistant_message` `.turn_number` | **收尾提醒** |
| `SessionStart` | session 開始 | 共通欄位 | 載入環境資訊 |

**共通欄位**（所有事件都有）：`session_id`、`cwd`、`hook_event_name`、`permission_mode`。

### matcher 支援哪些事件

只有**工具事件**（`PreToolUse` / `PostToolUse` 等）支援 `matcher`，用來過濾 `tool_name`：

```json
"matcher": "Bash"              // 單一
"matcher": "Edit|Write"        // 多個
"matcher": "mcp__figma__.*"    // 正則
"matcher": "*"                 // 全部（或省略）
```

`UserPromptSubmit` 和 `Stop` **沒有 matcher**，一定會觸發。

---

## 輸出契約

### 退出碼

| exit | 意思 |
|---|---|
| `0` | 通過。stdout 若是特定 JSON 會被解讀為決策 |
| `2` | **阻擋**。stderr 內容回饋給 Claude |
| 其他 | 非阻擋錯誤，動作照常進行 |

### 擋東西的兩種寫法

```bash
# 寫法 A：exit 2 + stderr（簡單）
echo "不准這樣做" >&2
exit 2

# 寫法 B：exit 0 + JSON（推薦，訊息更結構化）
jq -n '{hookSpecificOutput:{hookEventName:"PreToolUse",
        permissionDecision:"deny",permissionDecisionReason:"理由"}}'
exit 0
```

`permissionDecision` 可以是 `allow` / `deny` / `ask` / `defer`。

### 注入內容給 Claude 看

```bash
# UserPromptSubmit：exit 0 時，stdout 直接變成 context
echo "【目前進度】S4 迴圈開工"
exit 0

# 其他事件：用 additionalContext
jq -n '{hookSpecificOutput:{hookEventName:"PostToolUse",
        additionalContext:"要餵給 Claude 的訊息"}}'
```

---

## 填空模板

```bash
#!/usr/bin/env bash
# <事件> — <一句話說明這個 hook 在做什麼>
#
# 為什麼用 hook 而不是寫進 CLAUDE.md：
#   <你的理由。通常是「這件事不可逆」>
#
# 契約：
#   stdin  : JSON，含 <你會用到的欄位>
#   exit 0 : <通過時的行為>
set -uo pipefail

INPUT=$(cat)
VALUE=$(printf '%s' "$INPUT" | jq -r '<你的 jq 路徑> // empty')
[ -z "$VALUE" ] && exit 0                # 拿不到就安靜放行

# ── 你的邏輯 ──
if <條件>; then
  jq -n --arg reason "<擋下的理由，要說清楚該怎麼做>" '{
    hookSpecificOutput: {
      hookEventName: "<事件名>",
      permissionDecision: "deny",
      permissionDecisionReason: $reason
    }
  }'
  exit 0
fi

exit 0
```

---

## 三個常見錯誤

### ① 忘記重開

**九成的「我的 hook 沒反應」都是這個。**
hook 在 session 啟動時載入，改完一定要重開 `claude`。

### ② 正則太寬，誤殺正常操作

```bash
❌ grep -q 'rm'        # 連 npm run rm-cache、format 都會中
✅ grep -Eq '\brm\b[^|;&]*-[a-zA-Z]*[rR][a-zA-Z]*f'
```

**寫完一定要測一個「該放行」的案例。** 只測擋得下來是不夠的。

### ③ 沒處理空值

```bash
❌ CMD=$(echo "$INPUT" | jq -r '.tool_input.command')
   # 欄位不存在時會拿到字串 "null"，然後你的 grep 就對 "null" 做比對

✅ CMD=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty')
   [ -z "$CMD" ] && exit 0
```

---

## 怎麼驗證它真的生效

### 第一層：直接餵 JSON（不用開 claude）

```bash
# 該擋的
echo '{"tool_input":{"command":"rm -rf /tmp/x"}}' \
  | bash .claude/hooks/my-hook.sh
# 預期：印出 permissionDecision: "deny"

# 該放行的 ← 這條最常被跳過
echo '{"tool_input":{"command":"ls -la"}}' \
  | bash .claude/hooks/my-hook.sh
echo "exit=$?"
# 預期：無輸出，exit=0
```

**兩個案例都要測。**

### 第二層：在真實對話中觸發

```bash
claude    # 重開
```
```
> 幫我跑 rm -rf /tmp/test
```
應該被擋下並顯示你寫的理由。

### 第三層：確認註冊正確

```bash
claude --debug
```
看啟動 log 有沒有載入你的 hook。

### 除錯

```bash
bash -x .claude/hooks/my-hook.sh <<< '{"tool_input":{"command":"test"}}'
```

---

## 安全提醒

- hook **跟著 git 走，團隊都看得到** —— 不要放 secret
- 用 `${CLAUDE_PROJECT_DIR}`，不要寫絕對路徑
- 裝第三方的 hook 前**先讀那個 .sh** —— 它會被執行
- hook 的 `timeout` 要設。卡住的 hook 會拖慢每一次操作

---

## 本專案的五個 hook 可以直接讀

| 檔案 | 型態 | 學什麼 |
|---|---|---|
| `inject-station.sh` | 注入 | `UserPromptSubmit` 怎麼把狀態餵進 context |
| `block-dangerous-bash.sh` | 擋 | 四類危險指令的正則寫法 |
| `block-secret-write.sh` | 擋 | 怎麼避免誤殺佔位符 |
| `autoformat.sh` | 自動化 | 靜默執行、工具沒裝就跳過 |
| `remind-verify.sh` | 收尾 | 用旗標檔避免重複提醒 |

路徑：`templates/claude_project_template/.claude/hooks/`

---

## 下一步

打開 `block-dangerous-bash.sh`，加一條你自己的規則，然後跑上面「第一層」的兩個測試。
