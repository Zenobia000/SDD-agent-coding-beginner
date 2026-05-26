# Gemini CLI 操作手冊（給 Vibe Coding 學員）

> 這份文件是給「已經會用 AI Studio / Antigravity，現在想轉到 Gemini CLI」的學員。
> 讀完你會知道：每個檔案在做什麼、什麼時候該打開哪個工具、怎麼讓 AI 變成你的長期協作者。
>
> **如果你還沒裝 Gemini CLI**，先回去看 [`README.md`](../README.md) 三步驟。

---

## 1. 這份手冊在解決什麼問題

Antigravity / AI Studio 是「點選式」工具，畫面長什麼樣 AI 就吃什麼。Gemini CLI 不一樣——**它是純文字介面，所有規則、工具、記憶都靠檔案配置**。

第一次從 IDE 轉到 CLI 的學員最常踩三個雷：

1. **不知道 AI 到底讀到了什麼** —— 它有沒有看到我的 PRD？有沒有遵守我寫的規則？
2. **不知道工具該裝多少** —— 看到 MCP、command、skill 三個名詞混在一起，不知道差在哪
3. **不知道怎麼跟 AI「長期協作」** —— 每次重開 CLI 都要從頭講一遍偏好

這份手冊用 **harness engineering**（協作環境工程）的角度，告訴你怎麼把 Gemini CLI 設定成「**會記得你、會自己用對工具、會跟著你的工作流**」的長期搭檔。

---

## 2. 30 秒看完整張圖

```
你的專案資料夾/
│
├── GEMINI.md ◄──────── AI 啟動時自動讀，叫做「站立規則」
│
├── docs/
│   ├── PRD.md          需求規格（@docs/PRD.md 引用給 AI 看）
│   └── HANDBOOK.md     ◄── 你正在看的這份
│
└── .gemini/
    ├── settings.json   ◄── 基礎建設（沙箱、checkpoint、MCP 開關）
    │
    ├── 三大原語：
    ├── MCP.md          ◄── 外部能力通道（連 GitHub / 開瀏覽器 / 查文件）
    ├── SKILLS.md       ◄── 進階知識封裝（讓 AI 自動觸發複雜流程）
    ├── commands/       ◄── 快捷 prompt（你打一句就跑一段腳本）
    │
    ├── rules/          AI 寫 code 時的硬約束
    ├── prompts/        常用對話開場白
    └── memory/         長期記憶說明
```

**心智模型**：

- `GEMINI.md` + `settings.json` = AI 的「身份證 + 出生環境」（每次都會讀）
- `MCP / Skill / Command` = AI 的「外掛能力 + 知識 + 快捷鍵」（按需啟用）
- `rules/ + prompts/` = 給人類看的書（怎麼問問題、AI 卡關時該翻哪頁）

---

## 3. 協作環境的三層基礎建設

### 3.1 站立規則：`GEMINI.md`

每次你打 `gemini` 啟動 CLI 時，它會**自動掃這些位置**，依序合併成 system instruction：

| 階層         | 路徑                    | 適合放                |
| ---------- | --------------------- | ------------------ |
| Global     | `~/.gemini/GEMINI.md` | 個人偏好（語言、tone、習慣套件）|
| Project    | `<repo>/GEMINI.md`    | 專案規範（角色、技術棧、禁止項）  |
| Subdir     | `<repo>/src/GEMINI.md`| 模組級別 invariants    |

**怎麼確認 AI 真的有讀到？**

在 CLI 內打：

```
/memory show
```

會列出當下實際載入的合併內容。如果你剛改了 `GEMINI.md`，但 `/memory show` 還是舊的，跑：

```
/memory refresh
```

強制重新掃描。

**進階技巧**：`GEMINI.md` 內可以用 `@path/to/file.md` 把其他檔案內嵌進來，例如本模板的 `GEMINI.md` 可以加：

```markdown
請遵守以下細則：
@.gemini/rules/01-keep-it-simple.md
@.gemini/rules/02-coding-style.md
```

這樣規則檔可以拆得乾淨，又能保證每次都被載入。

---

### 3.2 基礎建設：`.gemini/settings.json`

這是「**Gemini CLI 本身的行為**」的設定檔（不是給 AI 看的，是給 CLI 程式看的）。最關鍵的幾個欄位：

| 欄位 | 用途 | 初學者建議 |
|---|---|---|
| `model` | 用哪個模型 | `gemini-2.0-flash`（快、便宜、夠用） |
| `checkpointing.enabled` | 修檔前自動快照 | **強烈建議 true**，跑壞了可以 `/restore` |
| `sandbox` | 把 CLI 跑在 Docker 容器內 | 沒裝 Docker 先 `false`，正式專案再 `true` |
| `fileFiltering.respectGitIgnore` | 搜檔時跳過 `.gitignore` | `true`（預設） |
| `contextFileName` | 哪些檔名會被當 GEMINI.md 讀 | `["GEMINI.md"]`（本模板專注 Gemini CLI，只用一個來源） |
| `telemetry` | 稽核（**不會記錄你的 prompt 內容**） | 看公司政策 |
| `mcpServers` | MCP 工具清單 | 一開始全 `enabled: false`，按需打開 |

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

### 3.3 三大原語：MCP / Skill / Command 各管什麼

這是這份手冊**最核心的章節**。三個名詞看起來都像「擴充工具」，但角色完全不同：

| 原語 | 一句話定位 | 適合包 | 觸發方式 |
|---|---|---|---|
| **MCP** | 外部能力通道 | 連網路、開瀏覽器、操作 GitHub、查資料庫 | AI 自己判斷該不該叫工具 |
| **Skill** | 進階知識封裝 | 複雜流程、審查 checklist、設計步驟 | AI 看你問的問題自動匹配 |
| **Command** | 快捷 prompt | 你常重複講的指令、需要參數的腳本 | 你手動打 `/xxx` |

**用「廚房」做比喻**：

- **MCP = 烤箱、攪拌機、冰箱**：實際的「能做事的硬體」。沒有它，AI 就只能用基本刀工
- **Skill = 食譜本**：教 AI「做這道菜要怎麼分步驟」。AI 看你說「我想吃義大利麵」，自己會去翻
- **Command = 廚房 hot key**：你按一下「義大利麵」按鈕，整套流程自動跑

**什麼時候開哪個？看下面決策樹**：

```
你想擴充 AI 的能力
   │
   ├─ 是要連「外部世界」嗎？（網路、API、瀏覽器、DB）
   │       │
   │       └─ Yes → 用 MCP   （詳見 .gemini/MCP.md）
   │
   ├─ 是要 AI「自己會判斷該不該做」的複雜流程嗎？
   │       │
   │       └─ Yes → 用 Skill （詳見 .gemini/SKILLS.md）
   │
   └─ 是「我打一句話就要跑一段固定 prompt」嗎？
           │
           └─ Yes → 用 Command（詳見 .gemini/commands/README.md）
```

**反模式**（看到自己這樣寫就要警惕）：

- ❌ 把 MCP 當 Skill 用：「我想要一個會自動審查 code 的 MCP」——這是 Skill 該做的，MCP 是給外部能力用的
- ❌ 把 Command 當 Skill 用：「我建了 `/review` command 但希望 AI 自己決定要不要用」——Command 是手動觸發，自動匹配要用 Skill
- ❌ 把 Skill 當文件用：寫一個塞滿 1000 行的 Skill 包山包海——Skill 應該只放「該執行什麼」，不是知識庫

---

## 4. Vibe Coding 五步流程怎麼跟 CLI 接軌

`GEMINI.md` 規定了「Vibe Coding 五步流程」（重述需求 → 列計畫 → 寫 code → 帶測試 → 等回報）。在 CLI 裡，每一步都有對應的工具讓你跑得更順：

### 第 1 步：重述需求 → 用 `@` 引用 PRD

不要自己用嘴巴重講需求，直接打：

```
@docs/PRD.md 請用 5 行內告訴我你理解的需求是什麼
```

`@檔案路徑` 會把整份檔案塞進 prompt。AI 重述完你看不對，就改 PRD，不是改 prompt。

### 第 2 步：列計畫 → 用 Custom Command 標準化

每次都要 AI「先列計畫再動手」很煩。建一個 `.gemini/commands/plan.toml`：

```toml
description = "請先列計畫等我確認，不要直接動手"
prompt = """
依據我們剛剛討論的需求：
1. 列出你打算新增 / 修改 / 刪除的所有檔案
2. 每個檔案說一句為什麼
3. 列出可能的風險
4. 停下來等我說 "OK" 才開始實作
"""
```

之後每次只要打 `/plan`，AI 就會乖乖列計畫。

### 第 3 步：寫 code → checkpointing 保命

確認 `.gemini/settings.json` 內 `checkpointing.enabled: true`。AI 改錯了你只要打：

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

詳見 [`.gemini/MCP.md`](../.gemini/MCP.md) 的 playwright 段落。

### 第 5 步：等回報 → `/memory add` 累積偏好

使用者說「我習慣用 pnpm 不是 npm」時，AI 不該只記在這次對話。打：

```
/memory add 我習慣用 pnpm 不是 npm
```

這條會寫到全域 `GEMINI.md`，下次重開 CLI、開新專案也會帶著。

---

## 5. 每天會用到的 10 個指令速查

把這頁釘在你的螢幕邊：

| 指令 | 用途 | 範例 |
|---|---|---|
| `@<file>` | 引用檔案內容到當前 prompt | `@docs/PRD.md 重述需求` |
| `!<cmd>` | 跑 shell 指令並把結果丟給 AI 看 | `!git diff` |
| `/memory show` | 看 AI 現在到底讀到什麼 | debug GEMINI.md 沒生效時必用 |
| `/memory refresh` | 強制重讀 GEMINI.md | 改完規則要立刻生效時 |
| `/memory add <fact>` | 加一條長期記憶到全域 GEMINI.md | `/memory add 我用 zsh` |
| `/mcp` | 看當下 MCP server 狀態 | 連不上 GitHub MCP 時用 |
| `/restore` | 回滾 checkpoint 快照 | AI 改壞檔案的救命繩 |
| `/clear` | 清空對話從頭來 | 上下文亂掉 / token 燒太兇時 |
| `/chat save <name>` | 把當下對話存檔，下次能載回來 | 跨天接續任務 |
| `/help` | 列所有可用指令 | 忘記就打它 |

**進階一點**：`/compress` 把舊對話壓縮，保留摘要省 token；`/bug` 直接報官方 issue（企業環境可重導向到內部工單）。

---

## 6. 三大原語的相互關係（一張圖）

```
        ┌──────────────────────────────┐
        │      你的自然語言問題           │
        └──────────────┬───────────────┘
                       │
                       ▼
              ┌──────────────────┐
              │  Gemini CLI 核心  │
              └────┬───────┬─────┘
                   │       │
        ┌──────────┘       └──────────┐
        ▼                              ▼
   AI 判斷「該叫工具？」           AI 判斷「該翻食譜？」
        │                              │
        ▼                              ▼
   ┌──────────┐                  ┌──────────┐
   │   MCP    │                  │  Skill   │
   │（外部能力）│                  │（程序知識）│
   └──────────┘                  └──────────┘

  使用者主動觸發：
        ▼
   ┌──────────┐
   │ Command  │  ← 你打 /xxx 才會跑
   └──────────┘
```

**搭配實例**：寫一個「自動審查 PR」流程

1. **Skill** `pr-review/SKILL.md` 定義流程：先看 diff → 檢查命名 → 跑測試 → 寫評論
2. **MCP** github 提供「讀 PR / 留評論」的能力
3. **Command** `/review-pr 123` 是你的觸發入口

三者協同：你打 `/review-pr 123` → command 把 PR 號塞進 prompt → AI 自動匹配到 `pr-review` skill → skill 指示它呼叫 github MCP 拉 diff → 完成審查。

---

## 7. 常見故障與處理

### 7.1 「AI 好像沒讀到我的規則」

```bash
# Step 1: 確認 GEMINI.md 內容真的存在
cat GEMINI.md | head -20

# Step 2: 進 CLI 確認載入
gemini
> /memory show
```

如果 `/memory show` 沒看到你的內容：

- 檢查 `.gemini/settings.json` 內 `contextFileName` 是否包含 `GEMINI.md`
- 檢查你是不是在錯的資料夾啟動 CLI（不是 repo root 就掃不到 project GEMINI.md）
- 跑 `/memory refresh` 強制重讀

### 7.2 「MCP server 掛掉了」

進 CLI 打 `/mcp`，看狀態：

- `connected` → 沒事
- `disconnected` → `npx` 套件可能裝失敗。手動跑一次 `.gemini/settings.json` 內的 `command + args` 看錯誤訊息
- `error: ENOENT` → `command` 路徑錯誤（例如沒裝 `node` / `python`）
- `error: missing env var` → 環境變數沒設（GitHub MCP 需要 `GITHUB_TOKEN`）

### 7.3 「checkpoint 太多想清」

```bash
# 快照存在 ~/.gemini/checkpoints/<project-hash>/
# 看一下大小
du -sh ~/.gemini/checkpoints/

# 太大就刪舊的（保留最近 7 天）
find ~/.gemini/checkpoints/ -mtime +7 -delete
```

### 7.4 「token 燒得太兇」

- 每次跑 `/compress` 壓縮舊對話
- 把不必要的 MCP 全設 `enabled: false`（每個 server 都會吃 token 描述自己）
- `GEMINI.md` 不要塞太多細節，用 `@file` 引用代替
- 切換到 `gemini-2.0-flash`（比 pro 便宜很多，初學者夠用）

### 7.5 「Skill 沒被自動觸發」

- 確認 SKILL.md 的 `description` frontmatter 有寫清楚「什麼時候該用」
- 自然語言問題要包含 description 內的關鍵字（例如 description 寫「security audit」，你問題要含「security」「audit」「安全審查」其中一個）
- 重啟 CLI 確認 skill 被掃到

---

## 8. 從 IDE → CLI 的心態調整清單

最後給你一張過渡 checklist：

- [ ] 接受「畫面上沒有按鈕，所有事都靠打字 + 規則檔」
- [ ] 把 `GEMINI.md` 當「給 AI 的合約」而不是文件——它每次都會讀
- [ ] 不要每次重講偏好，**用 `/memory add` 寫進長期記憶**
- [ ] 不要每次手動列計畫，**用 Custom Command 標準化開場**
- [ ] 不要憑記憶改檔，**用 `@file` 引用 + checkpointing 保命**
- [ ] 不要裝一堆 MCP「以防萬一」，**用一個關一個，token 是你的成本**
- [ ] 不要把所有規則塞進 `GEMINI.md`，**拆到 `rules/` 用 `@import` 引用**

---

## 9. 延伸閱讀

> 這份手冊綜合了下列來源整合重寫。深入學習推薦這條路徑：

**官方文件**

- [Gemini CLI GitHub repo](https://github.com/google-gemini/gemini-cli) — 原始碼與 release notes
- [Gemini CLI 官方文件站](https://geminicli.com/docs/) — 最完整的英文手冊
- [Custom Commands](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/custom-commands.md)
- [MCP Servers](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md)
- [Agent Skills](https://geminicli.com/docs/cli/skills/) — 2026 新原語

**中文資源（保哥 / Will / miniasp 維護）**

- [Gemini CLI 正體中文使用手冊](https://gemini-cli.gh.miniasp.com/) — 官方文件中譯，最快上手
- [企業級 Gemini CLI](https://gemini-cli.gh.miniasp.com/cli/enterprise.html) — 安全紀律必讀
- [YouTube EP05：快速上手 Gemini CLI](https://www.youtube.com/watch?v=0YVUkrqBJPg) — 開箱導覽

**進階學習**

- [Codelabs: Create Agent Skills for Gemini CLI](https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli)
- [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) — 官方 Skill 範例庫
- [Philipp Schmid Gemini CLI Cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet)
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — MCP 官方 server 清單

**安全參考（建議在裝 MCP 前讀）**

- [MCP Horror Stories: GitHub Prompt Injection (Docker Blog)](https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/)
- [Anthropic Git MCP CVE-2025-68143/68144/68145 (The Register)](https://www.theregister.com/2026/01/20/anthropic_prompt_injection_flaws/)

---

## 10. 下一步

讀完這份，建議照順序動手：

1. **跑 `/memory show`** 確認你的 `GEMINI.md` 真的被載入
2. **打開 [`.gemini/MCP.md`](../.gemini/MCP.md)**，啟用「初學者四件套」（filesystem + fetch + context7 + playwright）
3. **照 [`.gemini/SKILLS.md`](../.gemini/SKILLS.md)** 寫你的第一個 Skill（建議從 `explain-code` 開始）
4. **照 [`.gemini/commands/README.md`](../.gemini/commands/README.md)** 建你的第一個 Command（建議從 `/plan` 開始）
5. **回到 [`README.md`](../README.md)**，正式開始你的專案

祝 vibe coding 順利。
