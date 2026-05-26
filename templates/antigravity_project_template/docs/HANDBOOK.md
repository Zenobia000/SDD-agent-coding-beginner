# Antigravity CLI 操作手冊（給 Vibe Coding 學員）

> 這份文件是給「已經會用 AI Studio / Antigravity 桌面版，現在想轉到 Antigravity CLI（`agy`）」的學員。
> 讀完你會知道：每個檔案在做什麼、什麼時候該打開哪個工具、怎麼讓 AI 變成你的長期協作者。
>
> **如果你還沒裝 Antigravity CLI**，先回去看 [`README.md`](../README.md) 三步驟。

---

## 0. 先講背景：為什麼是 Antigravity CLI 不是 Gemini CLI？

2026 年 5 月 19 日 Google I/O 宣布把 **Gemini CLI 統一到 Antigravity 平台**：CLI 命令從 `gemini` 改為 `agy`、用 Go 重寫（啟動毫秒級、佔用幾 MB RAM）、與 Antigravity 桌面版共用 agent runtime。Gemini CLI 個人版（AI Pro / Ultra / 免費 Code Assist 帳號）將於 **6 月 18 日停止服務**。企業版 Gemini Code Assist Standard / Enterprise 不受影響。

對學員的意義：今天教的就是業界 6 月後唯一可用的 Google 終端 agent，學了不會浪費。

---

## 1. 這份手冊在解決什麼問題

Antigravity 桌面版 / AI Studio 是「點選式」工具，畫面長什麼樣 AI 就吃什麼。Antigravity CLI 不一樣——**它是純文字介面，所有規則、工具、記憶都靠檔案配置**。

第一次從 IDE 轉到 CLI 的學員最常踩三個雷：

1. **不知道 AI 到底讀到了什麼** —— 它有沒有看到我的 PRD？有沒有遵守我寫的規則？
2. **不知道工具該裝多少** —— 看到 MCP、Skill 兩個名詞混在一起，不知道差在哪
3. **不知道怎麼跟 AI「長期協作」** —— 每次重開 CLI 都要從頭講一遍偏好

這份手冊用 **harness engineering**（協作環境工程）的角度，告訴你怎麼把 Antigravity CLI 設定成「**會記得你、會自己用對工具、會跟著你的工作流**」的長期搭檔。

---

## 2. 30 秒看完整張圖

```
你的專案資料夾/
│
├── AGENTS.md ◄──────── AI 啟動時自動讀，叫做「站立規則」（業界統一規範）
│
├── docs/
│   ├── PRD.md          需求規格（@docs/PRD.md 引用給 AI 看）
│   └── HANDBOOK.md     ◄── 你正在看的這份
│
└── .agents/
    ├── settings.json   ◄── 基礎建設（沙箱、checkpoint、MCP 開關）
    │
    ├── 兩大原語：
    ├── MCP.md          ◄── 外部能力通道（連 GitHub / 開瀏覽器 / 查文件）
    ├── SKILLS.md       ◄── 知識封裝 + slash command（AI 自動觸發 or 手動 /xxx）
    ├── skills/         ◄── 實際的 skill 檔案放這裡
    │
    ├── rules/          AI 寫 code 時的硬約束
    ├── prompts/        常用對話開場白
    └── memory/         長期記憶說明
```

**心智模型**：

- `AGENTS.md` + `settings.json` = AI 的「身份證 + 出生環境」（每次都會讀）
- `MCP / Skill` = AI 的「外掛能力 + 知識 / 快捷指令」（按需啟用）
- `rules/ + prompts/` = 給人類看的書（怎麼問問題、AI 卡關時該翻哪頁）

> **Antigravity vs Gemini CLI 的差別**：Antigravity 把 Gemini CLI 的 `commands/.toml` 與 `skills/SKILL.md` 兩個原語**合併成單一 Skill 原語**。同一份 markdown 既能讓 AI 自動觸發、也能讓你打 `/skill-name` 手動觸發。比 Gemini CLI 簡單。

---

## 3. 協作環境的三層基礎建設

### 3.1 站立規則：`AGENTS.md`

每次你打 `agy` 啟動 CLI 時，它會**自動掃這些位置**，依序合併成 system instruction：

| 階層         | 路徑                                    | 適合放                |
| ---------- | ------------------------------------- | ------------------ |
| Global     | `~/.gemini/antigravity-cli/AGENTS.md` | 個人偏好（語言、tone、習慣套件）|
| Project    | `<repo>/AGENTS.md`                    | 專案規範（角色、技術棧、禁止項）  |
| Subdir     | `<repo>/src/AGENTS.md`                | 模組級別 invariants    |

> 過渡期說明：全域目錄沿用 `~/.gemini/antigravity-cli/`（Google 為了讓 `agy plugin import gemini` 一鍵搬遷舊有 `~/.gemini/`）。專案目錄統一改成 `AGENTS.md`（業界規範，Cursor / OpenAI Codex / Antigravity 都認）。

**怎麼確認 AI 真的有讀到？**

在 CLI 內打：

```
/memory show
```

會列出當下實際載入的合併內容。如果你剛改了 `AGENTS.md`，但 `/memory show` 還是舊的，跑：

```
/memory refresh
```

強制重新掃描。

**進階技巧**：`AGENTS.md` 內可以用 `@path/to/file.md` 把其他檔案內嵌進來，例如：

```markdown
請遵守以下細則：
@.agents/rules/01-keep-it-simple.md
@.agents/rules/02-coding-style.md
```

這樣規則檔可以拆得乾淨，又能保證每次都被載入。

---

### 3.2 基礎建設：`.agents/settings.json`

這是「**Antigravity CLI 本身的行為**」的設定檔（不是給 AI 看的，是給 CLI 程式看的）。最關鍵的幾個欄位：

| 欄位 | 用途 | 初學者建議 |
|---|---|---|
| `model.name` | 用哪個模型 | `gemini-3.0-flash`（快、便宜、夠用） |
| `checkpointing.enabled` | 修檔前自動快照 | **強烈建議 true**，跑壞了可以 `/restore` |
| `context.fileFiltering.respectGitIgnore` | 搜檔時跳過 `.gitignore` | `true`（預設） |
| `mcpServers` | MCP 工具清單 | 預設空 `{}`，要啟用就從 `.agents/MCP.md` 複製整段貼進去 |

**Checkpointing 是初學者的救命繩**：

```
（你叫 AI 改了 5 個檔案）
（發現它把樣式搞砸了）
你打：/restore
（CLI 列出剛剛的快照清單）
你選：1
（5 個檔案瞬間回到改之前）
```

沒開 checkpointing 的話，這 5 個檔案就要手動 `git checkout` 一個一個救。

---

### 3.3 兩大原語：MCP / Skill 各管什麼

這是這份手冊**最核心的章節**。兩個名詞看起來都像「擴充工具」，但角色完全不同：

| 原語 | 一句話定位 | 適合包 | 觸發方式 |
|---|---|---|---|
| **MCP** | 外部能力通道 | 連網路、開瀏覽器、操作 GitHub、查資料庫 | AI 自己判斷該不該叫工具 |
| **Skill** | 程序知識 + slash command | 複雜流程、審查 checklist、固定 prompt | AI 看 description 自動匹配 / 使用者打 `/<name>` 手動觸發 |

**用「廚房」做比喻**：

- **MCP = 烤箱、攪拌機、冰箱**：實際的「能做事的硬體」。沒有它，AI 就只能用基本刀工
- **Skill = 食譜本 + 廚房 hot key**：教 AI「做這道菜要怎麼分步驟」。AI 看你說「我想吃義大利麵」會自己翻書；你也可以按「義大利麵」hot key 直接觸發

**什麼時候開哪個？看下面決策樹**：

```
你想擴充 AI 的能力
   │
   ├─ 是要連「外部世界」嗎？（網路、API、瀏覽器、DB）
   │       │
   │       └─ Yes → 用 MCP   （詳見 .agents/MCP.md）
   │
   └─ 是「自己會判斷該不該做」或「我打一句就要跑」的流程嗎？
           │
           └─ Yes → 用 Skill （詳見 .agents/SKILLS.md）
```

**反模式**（看到自己這樣寫就要警惕）：

- ❌ 把 MCP 當 Skill 用：「我想要一個會自動審查 code 的 MCP」——這是 Skill 該做的，MCP 是給外部能力用的
- ❌ 把 Skill 當文件用：寫一個塞滿 1000 行的 Skill 包山包海——Skill 應該只放「該執行什麼」，不是知識庫

---

## 4. Vibe Coding 五步流程怎麼跟 CLI 接軌

`AGENTS.md` 規定了「Vibe Coding 五步流程」（重述需求 → 列計畫 → 寫 code → 帶測試 → 等回報）。在 CLI 裡，每一步都有對應的工具讓你跑得更順：

### 第 1 步：重述需求 → 用 `@` 引用 PRD

不要自己用嘴巴重講需求，直接打：

```
@docs/PRD.md 請用 5 行內告訴我你理解的需求是什麼
```

`@檔案路徑` 會把整份檔案塞進 prompt。AI 重述完你看不對，就改 PRD，不是改 prompt。

### 第 2 步：列計畫 → 用 Skill 標準化（`/vibe:plan`）

本模板已附 `.agents/skills/vibe/plan.md`，打 `/vibe:plan` 就會：

- 列出要新增 / 修改 / 刪除的檔案
- 每個檔案說一句為什麼
- 列出風險
- **停下來等你說 OK 才動手**

### 第 3 步：寫 code → checkpointing 保命

確認 `.agents/settings.json` 內 `checkpointing.enabled: true`。AI 改錯了你只要打：

```
/restore
```

選快照編號回滾。比 `git reset` 安全（不會動到 git 歷史）。

### 第 4 步：帶你測試 → Playwright MCP 截圖驗證

Vibe Coding 的測試標準是「打開瀏覽器看到東西」。Playwright MCP 讓 AI 自己開瀏覽器跑你的 `index.html`：

```
你：把 index.html 用 playwright 打開，截圖給我看畫面長怎樣
AI：（呼叫 playwright MCP 啟動 chromium → 開啟檔案 → 截圖 → 把畫面回傳）
```

詳見 [`.agents/MCP.md`](../.agents/MCP.md) 的 playwright 段落。

### 第 5 步：等回報 → `/memory add` 累積偏好

使用者說「我習慣用 pnpm 不是 npm」時，AI 不該只記在這次對話。打：

```
/memory add 我習慣用 pnpm 不是 npm
```

這條會寫到全域記憶，下次重開 CLI、開新專案也會帶著。

---

## 5. 每天會用到的指令速查

把這頁釘在你的螢幕邊：

| 指令 | 用途 | 範例 |
|---|---|---|
| `agy` | 啟動 TUI 互動模式 | 主要入口 |
| `agy "..."` | 一次性 prompt | `agy "把這段中文翻成英文：你好"` |
| `echo ... \| agy` | stdin pipe | `cat news.txt \| agy "用三句話摘要"` |
| `agy --headless "..."` | 無互動腳本模式 | CI / cron 用 |
| `agy plugin import gemini` | 從 Gemini CLI 搬遷 | 一鍵帶走 settings / MCP / commands |
| `@<file>` | 引用檔案到當前 prompt | `@docs/PRD.md 重述需求` |
| `/memory show` | 看 AI 現在到底讀到什麼 | debug AGENTS.md 沒生效時必用 |
| `/memory refresh` | 強制重讀 AGENTS.md | 改完規則要立刻生效時 |
| `/memory add <fact>` | 加一條長期記憶到全域 | `/memory add 我用 zsh` |
| `/mcp` | 看當下 MCP server 狀態 | 連不上 GitHub MCP 時用 |
| `/restore` | 回滾 checkpoint 快照 | AI 改壞檔案的救命繩 |
| `/clear` | 清空對話從頭來 | 上下文亂掉 / token 燒太兇時 |
| `/<skill-name>` | 手動觸發任何 skill | `/test`、`/git:commit`、`/vibe:plan` |
| `/help` | 列內建指令 | 忘記內建指令時打它 |

**進階一點**：`/compress` 把舊對話壓縮，保留摘要省 token。

---

## 6. 兩大原語的相互關係（一張圖）

```
        ┌──────────────────────────────┐
        │      你的自然語言問題           │
        └──────────────┬───────────────┘
                       │
                       ▼
              ┌──────────────────────┐
              │ Antigravity CLI 核心  │
              └────┬───────────┬─────┘
                   │           │
        ┌──────────┘           └──────────┐
        ▼                                  ▼
   AI 判斷「該叫工具？」             AI 判斷「該翻食譜？」
        │                                  │
        ▼                                  ▼
   ┌──────────┐                      ┌──────────────────┐
   │   MCP    │                      │  Skill           │
   │（外部能力）│                      │ （AI 自動觸發或   │
   └──────────┘                      │   /skill 手動觸發） │
                                     └──────────────────┘
```

**搭配實例**：寫一個「自動審查 PR」流程

1. **Skill** `pr-review/SKILL.md` 定義流程：先看 diff → 檢查命名 → 跑測試 → 寫評論
2. **MCP** github 提供「讀 PR / 留評論」的能力

協同：你打 `/pr-review 123` → skill 指示 AI 呼叫 github MCP 拉 diff → 依 SKILL.md 內定義的 checklist 跑審查 → 留評論。

---

## 7. 常見故障與處理

### 7.1 「AI 好像沒讀到我的規則」

```bash
# Step 1: 確認 AGENTS.md 內容真的存在
cat AGENTS.md | head -20

# Step 2: 進 CLI 確認載入
agy
> /memory show
```

如果 `/memory show` 沒看到你的內容：

- 檢查你是不是在錯的資料夾啟動 CLI（不是 repo root 就掃不到 project AGENTS.md）
- 跑 `/memory refresh` 強制重讀

### 7.2 「MCP server 掛掉了」

進 CLI 打 `/mcp`，看狀態：

- `connected` → 沒事
- `disconnected` → `npx` 套件可能裝失敗。手動跑一次 `.agents/settings.json` 內的 `command + args` 看錯誤訊息
- `error: ENOENT` → `command` 路徑錯誤（例如沒裝 `node` / `python`）
- `error: missing env var` → 環境變數沒設（GitHub MCP 需要 `GITHUB_TOKEN`）

### 7.3 「checkpoint 太多想清」

```bash
# 快照存在 ~/.gemini/antigravity-cli/checkpoints/<project-hash>/
du -sh ~/.gemini/antigravity-cli/checkpoints/

# 太大就刪舊的（保留最近 7 天）
find ~/.gemini/antigravity-cli/checkpoints/ -mtime +7 -delete
```

### 7.4 「token 燒得太兇」

- 每次跑 `/compress` 壓縮舊對話
- 把不必要的 MCP 從 `mcpServers` 整段刪掉（每個 server 都會吃 token 描述自己）
- `AGENTS.md` 不要塞太多細節，用 `@file` 引用代替
- 切換到 `gemini-3.0-flash`（比 pro 便宜很多，初學者夠用）

### 7.5 「Skill 沒被自動觸發」

- 確認 SKILL.md 的 `description` frontmatter 有寫清楚「什麼時候該用」
- 自然語言問題要包含 description 內的關鍵字
- 直接打 `/skill-name` 手動觸發驗證 skill 本身能跑
- 重啟 CLI 確認 skill 被掃到

### 7.6 「我以前 Gemini CLI 的設定怎麼辦？」

```bash
agy plugin import gemini
```

會把 `~/.gemini/` 內 settings、MCP servers、custom commands、memory 全部一對一搬到 `~/.gemini/antigravity-cli/`。**舊資料夾不會刪**，可先審查再決定要不要清。**截止日 2026-06-18 前個人版 Gemini CLI 還能用**，給你緩衝。

---

## 8. 從 IDE → CLI 的心態調整清單

最後給你一張過渡 checklist：

- [ ] 接受「畫面上沒有按鈕，所有事都靠打字 + 規則檔」
- [ ] 把 `AGENTS.md` 當「給 AI 的合約」而不是文件——它每次都會讀
- [ ] 不要每次重講偏好，**用 `/memory add` 寫進長期記憶**
- [ ] 不要每次手動列計畫，**用 `/vibe:plan` skill 標準化開場**
- [ ] 不要憑記憶改檔，**用 `@file` 引用 + checkpointing 保命**
- [ ] 不要裝一堆 MCP「以防萬一」，**用一個關一個，token 是你的成本**
- [ ] 不要把所有規則塞進 `AGENTS.md`，**拆到 `rules/` 用 `@import` 引用**

---

## 9. 延伸閱讀

> 這份手冊綜合了下列來源整合重寫。深入學習推薦這條路徑：

**官方文件**

- [Transitioning Gemini CLI to Antigravity CLI（Google Developers Blog, 2026-05-19）](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [Migrating from Gemini CLI（官方 migration 指南）](https://antigravity.google/docs/gcli-migration)
- [Antigravity CLI Skills 官方文件](https://antigravity.google/docs/skills)

**社群入門**

- [Getting started with Antigravity CLI（Rich Rose, Google Cloud Community）](https://medium.com/google-cloud/getting-started-with-antigravity-cli-3565d5db1e92)
- [Antigravity CLI: A Hands-On Guide（DEV Community）](https://dev.to/arindam_1729/antigravity-cli-a-hands-on-guide-to-googles-terminal-coding-agent-5bc7)
- [Antigravity CLI Deep Dive（agentpedia, 2026-05）](https://agentpedia.codes/blog/antigravity-cli-deep-dive)
- [How to Build Custom Skills in Google Antigravity（Medium）](https://medium.com/google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d)

**遷移與時程**

- [Bye-bye, Gemini CLI（The Register, 2026-05-20）](https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/)
- [Migration Guide (June 18, 2026 Deadline)](https://agentpedia.codes/blog/gemini-cli-to-antigravity-cli-migration)

**安全參考（建議在裝 MCP 前讀）**

- [MCP Horror Stories: GitHub Prompt Injection (Docker Blog)](https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/)
- [Anthropic Git MCP CVE-2025-68143/68144/68145 (The Register)](https://www.theregister.com/2026/01/20/anthropic_prompt_injection_flaws/)

---

## 10. 下一步

讀完這份，建議照順序動手：

1. **跑 `agy` 完成首次啟動三步驟**（配色、條款、資料夾信任）
2. **跑 `/memory show`** 確認你的 `AGENTS.md` 真的被載入
3. **打開 [`.agents/MCP.md`](../.agents/MCP.md)**，啟用「初學者四件套」（filesystem + fetch + context7 + playwright）
4. **照 [`.agents/SKILLS.md`](../.agents/SKILLS.md)** 寫你的第一個自訂 Skill
5. **直接試打** `/test`、`/explain`、`/vibe:plan` 等本模板附的 skill
6. **回到 [`README.md`](../README.md)**，正式開始你的專案

祝 vibe coding 順利。
