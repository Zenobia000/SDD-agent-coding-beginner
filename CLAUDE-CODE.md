# Claude Code 官方元件速成手冊

這是本課第一冊，也是官方元件速成唯一要照著走的文件。你不需要先背 prompt，也不需要先做完整專案；全書用同一個案例 **SmartTrip FX**，帶你親手辨認 Claude Code 的官方元件、觀察載入方式，並知道什麼時候該用哪一個。

核心練習全部是唯讀。你會執行查詢與安全的 hook 測試，但不會建立 App、不會新增外部連線、不會對外寫入、不會 commit，也不會 push。

## 完成後，你要能回答

1. `CLAUDE.md`、Rules、Skills 分別該放什麼，為什麼不能混成一大份 prompt。
2. Settings、Permissions 與 Hooks 的控制力有什麼不同。
3. 什麼工作留在主 session，什麼工作交給 Subagent。
4. MCP 是 Claude 的外部連接，不等於產品執行時的 API client。
5. 什麼時候才值得做 Plugin 或啟用實驗性的 Agent teams。
6. 如何用 Plan mode、session 管理與 worktree 保持工作乾淨。

## 全書共用案例

SmartTrip FX 是一個旅費工具。它可能需要：

- 專案長期遵守「金額計算必須 deterministic」。
- 一條可重複執行的需求訪談與實作流程。
- 一位只讀的探索者，先找出匯率程式與測試。
- 一個永遠攔截 credential 與高風險命令的閘門。
- 讓 Claude 在工作時查詢外部文件或匯率工具。
- 把成熟的工程設定分享給其他 repo。

每一章都用同一個案例回答一個問題，不要求你把產品做出來。

## 本書怎麼用

每章固定六格：

1. **你要學會**：這章唯一目標。
2. **先看**：先讀哪個本地檔案。
3. **照貼照跑**：標示「終端機」就貼在 shell；標示「Claude Code」就貼進 Claude。
4. **你應看到**：輸出不用逐字相同，但核心意思要一致。
5. **通過**：可以明確打勾的條件。
6. **卡住就貼**：不必自己重寫問題，整段貼給 Claude。

建議時間是 2.5–3 小時。先走完主線，再回頭看進階選修。

---

## 第 0 章｜先看懂 Claude Code 在做什麼

### 你要學會

Claude Code 不是只回文字的聊天室。它會反覆進行一個 agent loop：讀取 context、判斷下一步、呼叫工具、觀察結果，再決定是否繼續。你負責給目標、邊界與驗收；Claude 負責在授權範圍內執行。

### 先看

```text
README.md
CLAUDE.md
.claude/settings.json
.claude/rules/engineering-workflow.md
```

### 照貼照跑：終端機

```bash
git --version
claude --version
git status --short
```

前兩個命令要顯示版本。全新 clone 的第三個命令通常沒有輸出；若有既存改動，保留它們，不要為了上課刪除或還原。

接著啟動：

```bash
claude
```

### 照貼照跑：Claude Code

```text
先不要修改任何檔案，也不要 commit。
請根據實際 repo，用 5 行告訴我：
1. 這份教材的學習目標。
2. 你啟動時已經取得哪些 project context。
3. 你能使用哪幾類工具。
4. 哪些動作需要 permission 或會被 hook 檢查。
5. 現在最小的下一步。
每一行都附來源路徑；找不到就寫「尚未驗證」。
```

### 你應看到

- 目標是學會官方元件，不是立刻生成 SmartTrip FX。
- Claude 能讀專案檔案、執行允許的 shell / Git 查詢，並看到 Git 狀態。
- `CLAUDE.md` 提供 context；`.claude/settings.json` 設定 permissions 與 hooks。
- 它沒有開始改檔。

### 通過

- [ ] 能用一句話說出 agent loop：讀 context → 行動 → 看結果 → 繼續或停止。
- [ ] Claude 的回答有本地路徑，不是只靠記憶描述這個 repo。
- [ ] `git status --short` 沒有因這個練習多出新檔案。

### 卡住就貼

```text
停止推測。只讀 CLAUDE.md、.claude/settings.json 與
.claude/rules/engineering-workflow.md，重新回答；不要修改檔案。
```

官方延伸：[How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)、[Best practices](https://code.claude.com/docs/en/best-practices)

---

## 第 1 章｜Instructions 與 Memory：每次要記得什麼

### 你要學會

把內容放在正確的記憶層，不要把所有知識塞進 `CLAUDE.md`。

| 元件 | 適合內容 | 載入方式 |
|---|---|---|
| `CLAUDE.md` | 每次工作都適用的專案指令 | session 啟動時載入 |
| `.claude/rules/*.md` | 主題規則；也可用 `paths` 只套用特定檔案 | 符合範圍時載入 |
| Auto memory | Claude 從工作中保留的筆記 | 跨 session 自動管理 |
| Skill | 特定任務才需要的程序與參考 | 被呼叫或符合情境時載入 |

`CLAUDE.md` 是 context，不是強制執行器。像「絕不能寫入 `.env`」這類安全要求，不能只寫一句提醒，後面要交給 permission 或 hook。

### 先看

```text
CLAUDE.md
.claude/rules/engineering-workflow.md
.claude/skills/workflow/SKILL.md
```

### 照貼照跑：Claude Code

先輸入：

```text
/context
```

再貼：

```text
只讀分析，不要修改檔案。
比較 CLAUDE.md、.claude/rules/engineering-workflow.md、
.claude/skills/workflow/SKILL.md：
- 哪些內容每個 session 都需要？
- 哪些內容只有做特定任務才需要？
- 哪一條安全規則不能只靠文字提醒？
請用三列表格回答：內容、正確元件、理由。
```

### 你應看到

- `/context` 列出這個 session 已載入的 instruction / memory 來源。
- 回覆規則與專案邊界屬於 `CLAUDE.md` 或 Rules。
- `/workflow` 的路由程序只在需要選路時才載入，屬於 Skill。
- 敏感檔案與破壞性操作要靠 permission / hook，而不是期待模型永遠記住。

你也可以輸入 `/memory` 查看記憶來源；先不要編輯 Auto memory。

### 通過

- [ ] 能解釋「always loaded」與「on demand」的差別。
- [ ] 知道官方建議讓 `CLAUDE.md` 保持精簡，任務流程移到 Skills。
- [ ] 不把 Auto memory 當成團隊共享規格。
- [ ] 不把文字 instructions 說成安全沙箱。

### 卡住就貼

```text
請先用 /context 確認這個 session 真正載入的來源。
再把「長期 context」「按需程序」「機械式強制」分開，不要混成同一層。
```

官方延伸：[Manage Claude's memory](https://code.claude.com/docs/en/memory)

---

## 第 2 章｜Settings、Permissions 與 Plan mode：先決定能做什麼

### 你要學會

Settings 是設定容器，Permissions 決定工具使用的 allow / ask / deny，Plan mode 則讓 Claude 先分析與規劃、不直接修改專案。

| 範圍 | 典型位置 | 是否適合進 Git |
|---|---|---|
| User | `~/.claude/settings.json` | 否，個人設定 |
| Project | `.claude/settings.json` | 是，團隊共享 |
| Project local | `.claude/settings.local.json` | 否，個人且只限本 repo |

### 先看

```text
.claude/settings.json
.gitignore
```

### 照貼照跑：終端機

```bash
python3 -m json.tool .claude/settings.json
```

### 照貼照跑：Claude Code

輸入 `/permissions` 查看目前規則，離開畫面後貼：

```text
不要修改設定。請逐項解釋 .claude/settings.json：
1. 哪些唯讀 Git / 搜尋命令可直接使用。
2. 哪些敏感路徑禁止讀取。
3. Bash、Edit、Write 在執行前會經過哪個 hook。
4. allow、ask、deny 各自代表什麼。
最後指出一個「permission 允許，但 hook 仍可能擋下」的例子。
```

要處理陌生、多檔或高風險任務時，可從終端機用 Plan mode 啟動：

```bash
claude --permission-mode plan
```

在互動 session 中也可用 `Shift+Tab` 切換 permission mode。這裡只要知道入口，不必重開 session。

### 你應看到

- `git status`、`git diff`、`rg` 等唯讀操作可以低摩擦執行。
- `.env`、private key 與 `secrets/` 等路徑被 deny。
- Bash 進入 `guard-bash.py`；Edit / Write 進入 `guard-write.py`。
- Hook 在工具執行前仍可回傳 `ask` 或 `deny`。

### 通過

- [ ] 能分辨 settings 檔案與 permission 規則不是同義詞。
- [ ] 知道團隊設定與個人 local 設定的差別。
- [ ] 知道 Plan mode 適合先探索，卻不等於驗證已完成。
- [ ] 沒有為了方便而放寬或刪除既有 deny 規則。

### 卡住就貼

```text
只根據 .claude/settings.json 的實際 JSON 回答。
請分成「設定位置」「permission 決策」「hook 決策」三層，不要修改任何內容。
```

官方延伸：[Claude Code settings](https://code.claude.com/docs/en/settings)、[Configure permissions](https://code.claude.com/docs/en/permissions)、[Permission modes](https://code.claude.com/docs/en/permission-modes)

---

## 第 3 章｜Skills：把重複工作變成按需能力

### 你要學會

Skill 是一個資料夾，入口為 `SKILL.md`。它可以只有一份指令，也可以帶 scripts、模板與參考檔。Claude 只在相關時載入內容，因此比把完整流程塞進 `CLAUDE.md` 更省 context。

專案 Skill 放在：

```text
.claude/skills/<skill-name>/SKILL.md
```

### 先看

```text
.claude/skills/workflow/SKILL.md
.claude/skills/tdd/SKILL.md
.claude/skills/worktree-strategy/SKILL.md
```

### 照貼照跑：終端機

```bash
sed -n '1,35p' .claude/skills/workflow/SKILL.md
sed -n '1,35p' .claude/skills/tdd/SKILL.md
```

先看 YAML frontmatter：`name`、`description` 與呼叫控制欄位都在最上方。這個 repo 的 `/workflow` 使用 `disable-model-invocation: true`，所以只有使用者能主動啟動；`tdd` 則能在相關工作中由 Claude 載入。

### 照貼照跑：Claude Code

```text
/workflow 我想替 SmartTrip FX 加入即時匯率，但還沒決定資料源、
失敗時的 fallback，也還沒決定核心流程能不能連網。先不要實作，
只推薦一條路並告訴我什麼條件會讓建議改變。
```

### 你應看到

回覆應只有三件事：建議的 Skill / 路線、根據目前資訊的理由、會讓建議翻盤的條件。它很可能先建議需求訪談，而不是直接建立 API client。

Skill 的重點不是 slash command 本身，而是「可重複的程序知識」。需要副作用的發佈、commit 或部署流程，適合設為只有使用者能呼叫。

### 通過

- [ ] 找得到 `SKILL.md` 與 frontmatter。
- [ ] 能解釋 `disable-model-invocation: true` 的用途。
- [ ] `/workflow` 只推薦路線，沒有自行啟動另一條 user-only workflow。
- [ ] 知道特定任務流程放 Skill，不放進常駐 `CLAUDE.md`。

### 卡住就貼

```text
請重新讀 .claude/skills/workflow/SKILL.md 的 frontmatter 與「輸出」段落。
只依它規定的三行格式回答，不要實作、不要寫檔。
```

官方延伸：[Extend Claude with skills](https://code.claude.com/docs/en/skills)

---

## 第 4 章｜Subagents：把大量探索隔離出去

### 你要學會

Subagent 有自己的 system prompt、工具與獨立 context。它適合會產生大量搜尋結果的探索、review 或研究；主 session 最後只接收摘要，避免被中間雜訊塞滿。

專案 Subagent 放在：

```text
.claude/agents/<agent-name>.md
```

### 先看

```text
.claude/agents/code-explorer.md
.claude/agents/standards-reviewer.md
.claude/agents/spec-reviewer.md
.claude/agents/security-reviewer.md
```

### 照貼照跑：Claude Code

```text
請使用 code-explorer subagent，只讀探索這個 repo：
找出 /workflow 如何連到其他 Skills，以及哪兩個檔案負責阻擋高風險工具操作。
主對話只保留 8 行內摘要，每一項附 path:line。不要修改檔案。
```

### 你應看到

- Claude 明確派出 `code-explorer`，而不是把所有搜尋內容灌回主對話。
- 摘要指出 `.claude/skills/workflow/SKILL.md` 的路由關係。
- 摘要指出 `.claude/hooks/guard-bash.py` 與 `guard-write.py`。
- 沒有檔案被修改。

目前版本輸入 `/agents` 會提示 Subagent 定義位置，不再開啟管理面板；要查看背景工作用 `/tasks`。Subagent 可以在前景或背景執行；需要結果才能繼續時用前景，互不依賴的研究才適合背景。

### 通過

- [ ] 能說出 Subagent 的價值是 context isolation，不是「名字比較專業」。
- [ ] 任務有清楚的唯讀範圍與輸出上限。
- [ ] 不把互相依賴的實作假裝成可平行工作。
- [ ] `git status --short` 沒有因探索多出改動。

### 卡住就貼

```text
請明確委派給 project subagent `code-explorer`。
它只可讀取與搜尋；主 session 只接收有 path:line 的 8 行摘要。
```

官方延伸：[Create custom subagents](https://code.claude.com/docs/en/sub-agents)

---

## 第 5 章｜Hooks：把「每次都必須做」變成事件閘門

### 你要學會

Hook 在特定事件發生時自動執行。它可以跑 command、HTTP、MCP tool、prompt 或 agent；需要 deterministic guardrail 時，優先使用可測試的 command hook。

本 repo 使用 `PreToolUse`：工具真正執行前，hook 可以回傳 allow、ask 或 deny。

### 先看

```text
.claude/settings.json
.claude/hooks/guard-bash.py
.claude/hooks/guard-write.py
```

### 照貼照跑：Claude Code

```text
/hooks
```

確認 `PreToolUse` 已註冊 Bash 與 Edit / Write 後，離開畫面。

### 照貼照跑：終端機

下面只是把假資料送進 hook，不會真的建立 `.env`：

```bash
printf '%s\n' '{"tool_input":{"file_path":".env","content":"DEMO=value"}}' | python3 .claude/hooks/guard-write.py
```

再測合法的範例檔：

```bash
printf '%s\n' '{"tool_input":{"file_path":".env.example","content":"DEMO=fake-value"}}' | python3 .claude/hooks/guard-write.py
```

### 你應看到

第一個命令會輸出包含以下欄位的 JSON：

```json
{
  "permissionDecision": "deny",
  "permissionDecisionReason": "已擋下寫入 .env……"
}
```

實際 JSON 外面還有 `hookSpecificOutput`。第二個命令不輸出 deny，代表假值範例檔可通過。

### 通過

```bash
test "$(printf '%s\n' '{"tool_input":{"file_path":".env","content":"DEMO=value"}}' | python3 .claude/hooks/guard-write.py | python3 -c 'import json,sys; print(json.load(sys.stdin)["hookSpecificOutput"]["permissionDecision"])')" = "deny"
```

- [ ] 上面命令 exit 0。
- [ ] 沒有真的建立 `.env`。
- [ ] 能解釋 hook 比「請記得不要寫秘密」更可靠，因為它在事件點執行。

### 卡住就貼

```text
請只讀 .claude/settings.json 與 .claude/hooks/guard-write.py，
找出 hook 期待的 stdin JSON 與 deny 輸出格式；不要真的寫入任何檔案。
```

官方延伸：[Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)、[Hooks reference](https://code.claude.com/docs/en/hooks)

---

## 第 6 章｜MCP：讓 Claude 連接外部工具與資料

### 你要學會

MCP（Model Context Protocol）讓 Claude Code 連接外部服務、資料庫與工具。MCP server 提供能力；Skill 則教 Claude 何時、如何組合這些能力。兩者可以一起用，但不是同一件事。

### 先看

這個 repo 刻意沒有 `.mcp.json`。核心課先學會判斷，不要求你註冊服務、登入帳號或放入 API key。

### 照貼照跑：終端機

```bash
claude mcp list
```

### 照貼照跑：Claude Code

```text
/mcp
```

如果尚未設定 server，看到空清單是正確結果。

接著貼：

```text
先不要新增 MCP server。請判斷以下三件事各該用什麼：
1. Claude 在開發時要查公司內部的匯率規範。
2. SmartTrip FX 成品在使用者執行程式時，要取得即時匯率。
3. 團隊想固定「查規範 → 比對程式 → 產 review」的重複流程。
只能從 MCP、產品 API client、Skill、MCP + Skill 中選，逐項說明理由。
```

### 你應看到

| 情境 | 正確方向 |
|---|---|
| Claude 工作時查外部規範 | MCP |
| App 執行時取得即時匯率 | 產品本身的 API client，不因使用 Claude 就變成 MCP |
| 固定如何查詢與 review | MCP + Skill |

MCP 有三種常用 scope：local（本機、此專案）、project（專案根目錄 `.mcp.json`，可共享）、user（本機所有專案）。Project 設定進入 repo 前仍需要信任確認；不要把 token 寫進版本控制。

### 通過

- [ ] `claude mcp list` 能正常執行；空清單也算通過。
- [ ] 能分辨「提供工具」與「教會工作流程」。
- [ ] 能分辨 Claude 的 MCP 與產品執行時 integration。
- [ ] 沒有為了完成本章新增 server 或 credential。

### 卡住就貼

```text
不要設定或連線。請先區分「Claude Code 開發環境需要的工具」與
「最終產品 runtime 需要的功能」，再判斷 MCP 是否適用。
```

官方延伸：[Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)

---

## 第 7 章｜Plugins、Agent teams 與其他官方介面

### 你要學會

不是每個官方功能都該在第一天啟用。這章只學封裝與選型邊界。

### Plugins：分享一整套元件

當一組 Skills、Subagents、Hooks 或 MCP 設定已在多個 repo 重複使用，才考慮封裝 Plugin。最小結構概念如下：

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── skills/
├── agents/
├── hooks/
└── .mcp.json
```

元件目錄在 plugin 根目錄，只有 manifest 放在 `.claude-plugin/`。本機可用 `claude --plugin-dir ./my-plugin` 測試；安裝後 Skill 會用 `/plugin-name:skill-name` namespace，避免撞名。

本 repo 目前是直接放進專案的 `.claude/` harness，還不到必須封裝 Plugin 的階段。

### Agent teams：多個獨立 session 協作

Agent team 由 lead 協調多個 teammate；每個 teammate 有自己的 context，彼此可以傳訊息並共享 task list。它和 Subagent 的差別：

| 需求 | 優先選擇 |
|---|---|
| 把一段探索隔離，結果回主 session | Subagent |
| 多個獨立 session 需要互相溝通與協調 | Agent team |

Agent teams 目前是實驗性功能、預設停用。初學者先用 Subagents；只有工作真的能分成多條獨立路徑時，再評估 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`。

### Commands 與 Output styles

| 介面 | 用途 | 不該拿來做什麼 |
|---|---|---|
| Custom commands | 舊的 `.claude/commands/` 仍可用；新重複流程優先做 Skill | 不要複製兩份相同 workflow |
| Output styles | 調整 Claude 的回覆風格與格式 | 不提供 permission 或安全強制 |

### 目前官方另有的進階介面

這些功能是真正的官方介面，但不是初學者建立 project harness 的必要元件：

| 介面 | 解決什麼 | 何時再學 |
|---|---|---|
| Code intelligence / LSP | 精準跳到定義、找 references、取得型別診斷 | 大型 typed codebase 只靠文字搜尋不夠時 |
| Artifacts | 把 HTML / Markdown 發成可互動、可分享的私人頁面 | session 輸出需要視覺化分享時 |
| Agent view（`claude agents`） | 由人派發、監看多個背景 session；目前是 Research preview | 你要管理數個獨立任務，而不是讓 Claude 當 team lead 時 |
| Dynamic workflows | 用 script 編排大量 Subagents 並交叉驗證 | 工作已超過少量 Subagents、需要可重跑編排時 |
| `/batch` | 以 Skill 將大型變更拆成多個 worktree-isolated PR | 明確的大規模 migration；不是一般功能開發預設 |

辨識它們即可。它們不會改變前面的基本判斷：context、workflow、isolation、enforcement、connection、distribution 仍要先分清楚。

### 照貼照跑：Claude Code

```text
只做架構判斷，不要建立檔案：
如果這套 .claude 設定只在本 repo 使用、確定要讓第 2 個 repo
長期共用，以及要提供給 20 個團隊安裝，三個階段各應維持
project config、暫時手動複製，還是封裝 Plugin？請各給一個理由與升級條件。
```

### 你應看到

- 單一 repo：維持 project config 最簡單。
- 第二個 repo 確定長期共用：開始封裝 Plugin；手動複製只適合短期驗證。
- 多團隊安裝、版本化與更新：用 Plugin 與 marketplace 管理分發。
- 不會因為「官方有功能」就建議全部啟用。

### 通過

- [ ] 能說出 Plugin 是 package / distribution layer，不是新的推理能力。
- [ ] 能分辨 Subagent 與 Agent team。
- [ ] 知道 Agent teams 目前是實驗性功能。
- [ ] 知道 Output style 不能取代 Hooks 或 Permissions。

### 卡住就貼

```text
先用「是否跨 repo 發佈」「是否需要獨立 context 互相溝通」兩個問題判斷。
不要因為功能存在就建議啟用；請指出最小可用方案。
```

官方延伸：[Create plugins](https://code.claude.com/docs/en/plugins)、[Run agents in parallel](https://code.claude.com/docs/en/agents)、[Orchestrate teams](https://code.claude.com/docs/en/agent-teams)、[Claude Code directory](https://code.claude.com/docs/en/claude-directory)

---

## 第 8 章｜把元件放進日常工作流

### 你要學會

官方元件不是八個獨立玩具。它們共同服務一條短迴圈：

```text
探索 → 計畫 → 實作 → 驗證 → 提交
  ↑                         │
  └────── 用證據修正 ──────┘
```

### 元件選擇表

| 你現在缺什麼 | 先選什麼 |
|---|---|
| 每次都要知道的專案背景 | `CLAUDE.md` / Rules |
| 可直接使用、詢問或禁止的工具範圍 | Permissions |
| 可重複但只在特定任務使用的流程 | Skill |
| 大量搜尋、研究或 review 的隔離 context | Subagent |
| 每次事件都必須執行的 deterministic guardrail | Hook |
| Claude 工作時需要外部工具或資料 | MCP |
| 一整套元件要版本化分發 | Plugin |
| 多個獨立 session 要互相協調 | Agent team（實驗性） |

Code intelligence 與 Artifacts 不在這張 extension decision table：前者改善 code navigation，後者負責發布 session 輸出；它們不取代上面任何一層。

### 照貼照跑：Claude Code

```text
只做設計，不要修改檔案。以 SmartTrip FX 為例，產出一張 8 列表格：
CLAUDE.md / Rules、Permissions、Skill、Subagent、Hook、MCP、Plugin、Agent team。
每列只能寫：這個案例是否需要、負責什麼、不需要時為什麼不加。
原則是使用最少元件，不准為了湊滿表格而啟用功能。
```

### 你應看到

- 專案邊界放 `CLAUDE.md` / Rules。
- 重複的需求到實作路線放 Skill。
- 只讀 codebase 探索可交給 Subagent。
- credential 與破壞性操作由 Permission / Hook 防護。
- 只有 Claude 真要連外部工具時才需要 MCP。
- 單一 repo 不急著做 Plugin。
- 一般教學專案不需要實驗性 Agent team。

### Session 與 context 維護

| 情況 | 命令 / 動作 |
|---|---|
| 同一任務延續上一個 session | `claude --continue` |
| 從歷史 session 選一個恢復 | `claude --resume` |
| 已切換成完全不同的任務 | `/clear` |
| 同一任務 context 太長 | `/compact` |
| 陌生、多檔、風險高，先別改 | Plan mode |

同一路徑修正兩次仍偏離時，先 `/clear`，用更精準的 scope、證據與通過條件重新開始，不要在污染的 context 裡無限補 prompt。

### Worktree 與平行工作（選修，不要在核心課執行）

當兩個任務互不依賴、而且都會寫檔時，不能讓它們共用同一個 working tree。Claude Code 可用：

```bash
claude --worktree smarttrip-live-fx
```

它會建立隔離的 Git worktree 與 session。這不代表任務自動可平行；先確認 dependencies、write set 與 side effects 不重疊，再依 `.claude/skills/parallel-work/` 和 `.claude/skills/worktree-strategy/` 規劃。

如果由人管理多個獨立 session，可再評估 Research preview 的 `claude agents`；如果使用 Agent team，teammates 不會自動獲得 worktree 隔離，必須明確分割檔案 ownership。平行 session 也會成倍增加 token 使用量。

### 最終通過

- [ ] 不看答案，也能為一個需求選出最小的官方元件。
- [ ] 能說出 instruction、workflow、isolation、enforcement、connection、distribution 六種責任。
- [ ] 知道何時 `/clear`、何時 resume、何時才開 worktree。
- [ ] 核心課程沒有修改產品碼、沒有新增 MCP server、沒有對外寫入、沒有新增秘密。

### 卡住就貼

```text
請用這個順序重新判斷：
長期 context → 按需 workflow → 隔離工作 → 強制閘門 → 外部連接 → 跨 repo 分發。
每一層只有在前一層無法解決時才新增元件，最後只給一個下一步。
```

官方延伸：[Features overview](https://code.claude.com/docs/en/features-overview)、[Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees)、[Common workflows](https://code.claude.com/docs/en/common-workflows)、[Best practices](https://code.claude.com/docs/en/best-practices)

---

## 一頁複習：遇到需求時先問六題

1. 這是每次都要知道的 context，還是特定任務才需要？
2. 這是模型可以判斷的流程，還是每次都必須機械式執行？
3. 這份工作會產生大量中間資訊，需要隔離 context 嗎？
4. Claude 需要連外部工具，還是最終 App 自己需要 runtime integration？
5. 任務真的互不依賴，值得用 worktree / 多 session 嗎？
6. 這套設定已經需要跨 repo 版本化分發了嗎？

能回答這六題，你就不是在堆設定，而是在設計 Claude Code 的工作環境。

## 官方來源索引

- [Claude Code overview](https://code.claude.com/docs/en/overview)
- [Features overview](https://code.claude.com/docs/en/features-overview)
- [Memory and CLAUDE.md](https://code.claude.com/docs/en/memory)
- [Settings and permissions](https://code.claude.com/docs/en/settings)
- [Skills](https://code.claude.com/docs/en/skills)
- [Subagents](https://code.claude.com/docs/en/sub-agents)
- [Hooks](https://code.claude.com/docs/en/hooks-guide)
- [MCP](https://code.claude.com/docs/en/mcp)
- [Plugins](https://code.claude.com/docs/en/plugins)
- [Agent teams](https://code.claude.com/docs/en/agent-teams)
- [Agents and parallel work](https://code.claude.com/docs/en/agents)
- [Worktrees](https://code.claude.com/docs/en/worktrees)
- [Artifacts](https://code.claude.com/docs/en/artifacts)

最後核對日期：2026-07-31。若本書與官方文件衝突，以官方文件為準，並回報教材章節與官方 URL。

---

## 下一步｜進入本專案實戰

完成官方元件速成後，回到 [`BUILD.md`](./BUILD.md)，依序完成 SmartTrip FX 的 project contract、需求訪談、spec、tickets、TDD、review 與 commit。速成手冊教你「元件負責什麼」；專案實戰讓你證明「會把它們用在真工作裡」。
