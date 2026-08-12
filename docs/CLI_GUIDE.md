# Antigravity CLI（`agy`）與 `.agents/` 速查

> 隨查用的速查表，不是要照走的章節。第一次學習請走 [`../ANTIGRAVITY.md`](../ANTIGRAVITY.md)；安裝與認證見 [`./INSTALL.md`](./INSTALL.md)。

**證據標記**（2026-08-12，對應 `agy` 1.1.12）：
【本機實測】= 在這台機器跑過，貼的是真實輸出。
【內建規格】= 隨 binary 出貨的 `~/.gemini/antigravity-cli/builtin/skills/` 原文。
【依文件】= 只有 antigravity.google 這樣說，本機未實測。
⚠️ 官方文件未載明 = 查不到，本文不猜。

⚠️ 這台是**沒有圖形介面的遠端 Linux 主機**，所有 TUI（互動介面）內的行為都無法在本機實測。凡標【依文件】或「未載明」的項目，請以你自己畫面上 `/help` 列出的內容為準。

---

## 1. 啟動與離開

| 動作 | 做法 | 來源 |
|---|---|---|
| 啟動 | 在 **repo 根目錄**執行 `agy` | 【本機實測】 |
| 看指令清單 | TUI 內輸入 `/help` | 【內建規格】`cli.md` §2 |
| 離開 | `Ctrl+D Ctrl+D`，或 `/exit`、`/quit` | 【內建規格】`cli.md` §1 原文：`Exit: Ctrl+D Ctrl+D (or /exit or /quit)` |
| 登出 | `/logout` | 【依文件】 |

⚠️ **一定要在 repo 根目錄啟動。** `agy` 從當前目錄往上走到 repo root（含 `.git` 的目錄）尋找 `AGENTS.md` 與 `.agents/`，在子目錄啟動會漏掉設定。

⚠️ **第一次在一個 repo 啟動會問你信不信任這個資料夾，一定要選信任。** 未信任的 workspace，`.agents/` 底下全部不載入**而且不報錯**。要確認信任狀態，讀 `~/.gemini/antigravity-cli/settings.json` 的 `trustedWorkspaces`。

---

## 2. `.agents/` 設定與元件責任

Antigravity 啟動時讀根目錄的 `AGENTS.md` 與 `.agents/`。

```text
my-project/
├── AGENTS.md                   # 目錄層級長期 context，永遠 active、不支援 frontmatter
└── .agents/
    ├── skills/                 # 按需載入的程序知識
    │   └── <skill-name>/SKILL.md
    ├── agents/                 # Subagent 定義
    │   └── <agent-name>/agent.md
    ├── rules/                  # 可條件觸發的長期紀律（平放的 .md）
    │   └── <name>.md
    ├── hooks.json              # 具名 hook 註冊
    ├── hooks/                  # hook 實際執行的腳本
    └── mcp_config.json         # MCP server 宣告
```

### 2.1 元件責任對照表

| 元件 | 路徑 | 責任與使用時機 | 來源 |
|---|---|---|---|
| **目錄層級 context** | `AGENTS.md`（或 `GEMINI.md`） | 長期專案背景與規範。**不支援 frontmatter**，對所在目錄與所有子目錄永遠 active。是 context，不是安全強制 | 【內建規格】`docs/rules.md` |
| **Rules** | `.agents/rules/*.md` | 可條件觸發的長期紀律。有 frontmatter，`trigger: always_on` 才無條件載入 | 【已驗證】binary 有 `always_on` / `model_decision` 字串 |
| **Skills** | `.agents/skills/<name>/SKILL.md` | 按需載入的 SOP。frontmatter **只有 `name` 與 `description`，兩個都必填** | 【內建規格】`docs/skills.md` |
| **Subagents** | `.agents/agents/<name>/agent.md` | 隔離 context 的委派工作者。⚠️ 官方文件未載明檔案格式，`agent.md` 是高信心推論 | 【已驗證】路徑字串；檔名為推論 |
| **Hooks** | `.agents/hooks.json` + `.agents/hooks/` | **事件驅動、唯一能做 deterministic 硬性攔截的元件。** top-level key 是 **hook 名稱**不是事件名稱；`command` 的相對路徑以 **`.agents/`**（`hooks.json` 所在目錄）為基準 | 【內建規格】`docs/hooks.md` |
| **MCP** | `.agents/mcp_config.json` | 外部工具與資料連線 | 【內建規格】`docs/mcp_servers.md` |

> 🔴 **Antigravity 的 workspace 沒有 `settings.json`**（binary 內 `.agents/settings.json` 出現 0 次，【已驗證的負面結論】）。權限由使用者在 `/permissions` 自行設定，能寫進版控的硬性攔截只有 `hooks.json`。

### 2.2 寫一個 Skill

每個 Skill 是一個資料夾，入口檔名固定 `SKILL.md`，frontmatter 只有兩欄且都必填（【內建規格】`docs/skills.md`）：

```markdown
---
name: build-check
description: 執行目前專案的語法與編譯檢查。當使用者要求驗證程式碼、或實作完成要確認能否編譯時使用。
---

# Build Check

1. 讀專案契約拿到 build 命令；讀不到就回報 `unknown`，不要猜。
2. 執行該命令。
3. 失敗時回報錯誤原文與檔案行號。
```

> 🚨 **常見陷阱**：`description` 是 agent 判斷要不要啟用這個 skill 的**唯一依據**，必須同時寫清楚 **what** 與 **when**。只寫 what（例如「TDD 流程」）的 skill 幾乎不會被啟用。

### 2.3 `hooks.json` 的最小形狀

```json
{
  "my-guard": {
    "enabled": true,
    "PreToolUse": [
      {
        "matcher": "run_command|shell_exec|send_command_input",
        "hooks": [{ "type": "command", "command": "python3 ./hooks/guard.py", "timeout": 10 }]
      }
    ]
  }
}
```

三個最容易寫錯的點（【內建規格】`docs/hooks.md`）：

1. `"my-guard"` 是**你自己取的 hook 名稱**，不是事件名稱。事件名稱在下一層。
2. `PreToolUse` / `PostToolUse` 是 **grouped**（`matcher` + `hooks` 包一層）；`PreInvocation` / `PostInvocation` / `Stop` 是 **flat**（直接放 handler 陣列，`matcher` 被忽略）。
3. working directory 是 `hooks.json` 所在目錄（`.agents/`），**不是 repo root**。

---

## 3. Slash commands（TUI 內）

**權威清單來源**：官方 CLI Features 頁（【依文件】）。要看你自己環境實際支援什麼，在 TUI 內跑 `/help`——【內建規格】`cli.md` §2 明說 `/help` 才是那台機器的權威清單。

| 指令 | 用途 | 來源 |
|---|---|---|
| `/help` | 列出這個版本實際可用的所有 slash command | 【內建規格】 |
| `/skills` | 列出已載入的 skills | 【依文件】 |
| `/agents` | 列出 subagents | 【依文件】。⚠️ 本機實測 shell 端的 `agy agents` **exit 0、零輸出**，不可拿來當驗收；TUI 內的 `/agents` 無法在本機驗證 |
| `/mcp` | MCP server 狀態 | 【依文件】 |
| `/permissions` | 權限設定 | 【依文件】 |
| `/model` | 切換模型 | 【依文件】 |
| `/tasks` | 查看背景任務 | 【依文件】 |
| `/diff` | 檢視變更 | 【依文件】 |
| `/open` | 開啟檔案 | 【依文件】 |
| `/usage` | 額度用量 | 【依文件】 |
| `/resume`（`/switch`） | 恢復先前對話 | 【依文件】 |
| `/rewind`（`/undo`） | 收回上一步 | 【依文件】 |
| `/rename` | 重新命名對話 | 【依文件】 |
| `/keybindings` | 快捷鍵設定 | 【依文件】 |
| `/statusline` | 狀態列設定 | 【依文件】 |
| `/logout` | 登出 | 【依文件】 |
| `/exit`、`/quit` | 離開 | 【內建規格】 |

⚠️ **官方文件未載明**：`/context`、`/hooks`、`/clear`、`/compact`、`/quota`。這些在其他 AI CLI 常見，但不在 Antigravity 的權威清單裡，本文不描述它們的行為。你的環境如果 `/help` 有列出來，以畫面為準。

**快捷鍵**（【依文件】）：`Ctrl+J` 跳到待批准項目、`Ctrl+K` 立即批准。

---

## 4. 常用 shell 命令（唯讀，不消耗 AI credits）

```bash
agy --version          # 版本號
agy models             # 列出可用模型；印得出清單 = 認證有效
agy plugin list        # 已匯入的 plugin；乾淨環境印 "No imported plugins."
agy --help             # 所有 flag 與 subcommand
agy help plugin        # 單一 subcommand 的說明
```

⚠️ **不要用 `agy -p "hello"` 之類的命令「測試安裝」**——那會真的呼叫模型並消耗額度。上面五個命令已足以證明安裝與認證成功。

---

## 5. 學生實戰建議

1. **最小元件原則**：不要為了湊齊功能而建立所有元件。簡單專案只需要 `AGENTS.md`；有固定重複流程時再加 `.agents/skills/`。
2. **認清元件責任**：規範寫 `AGENTS.md`；重複 SOP 寫 `.agents/skills/`；外部資料連線寫 `.agents/mcp_config.json`；**不能只靠模型記得的硬性規則寫 `.agents/hooks.json`**。
3. **路徑只認 `.agents/`**：Antigravity 的 workspace customization 只從 `AGENTS.md` 與 `.agents/` 載入（binary 內大量出現 `.agents/` 路徑字串，其他 AI CLI 的設定目錄字串 0 次，【已驗證】）。放在別的目錄不會被讀到。

---

## 下一步

- 安裝與環境驗證：[`INSTALL.md`](./INSTALL.md)
- 官方元件速成（第一冊）：[`../ANTIGRAVITY.md`](../ANTIGRAVITY.md)
- 本 repo harness 架構：[`../.agents/README.md`](../.agents/README.md)
