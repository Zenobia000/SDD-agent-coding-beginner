# Antigravity 初學者專案模板

> 給 Vibe Coding 工作坊學員：把這整個資料夾複製到你的專案位置，用 Antigravity 桌面版或 `agy` CLI 打開，AI 就會自動讀懂規則開始幫你做事。

---

## 📁 這個資料夾裡有什麼

```
my-project/
├── README.md                      ← 你正在看（入口）
├── USAGE.md                       ← ⭐ 完整使用說明（A/B 模式 walkthrough + FAQ）
├── AGENTS.md                      ← ⭐ Antigravity 一定會讀的「總指揮文件」（跨工具新興共通格式）
├── ai_ready_repo_blueprint.md     ← 整套 template 為什麼這樣設計
├── terminal_configuration.md      ← Terminal 工作站哲學（RUN/WATCH/CHECK）
├── docs/
│   ├── PRD.md                     ← 從 AI Studio 帶過來的需求規格（填空）
│   └── HANDBOOK.md                ← Antigravity CLI 完整操作手冊（從 IDE 轉 CLI 必讀）
├── tasks/                         ← ⭐ Solo Sprint backlog 系統
│   ├── backlog.md                     (整個專案的未來任務總清單)
│   ├── sprint-current.md              (當前 sprint 執行清單)
│   ├── known-issues.md                (已知但暫不修的問題)
│   └── retros/                        (sprint retrospective 歸檔)
└── .agents/
    ├── WORKFLOW.md                ← ⭐ Solo Vibe Engineering Sprint 工作流總圖（10 站 + 對應 skill）
    ├── SKILL-MAP.md               ← ⭐ 10 個 skill 完整連動地圖（Pre/Post / 依賴 / 6 種路徑 / 斷層分析）
    ├── settings.json              ← Antigravity CLI 設定（model / checkpoint / MCP）
    ├── MCP.md                     ← 三大擴充原語 ①：MCP 外掛工具
    ├── SKILLS.md                  ← 三大擴充原語 ②：Skill + Slash Command
    ├── SUBAGENTS.md               ← 三大擴充原語 ③：Subagents 平行任務分派
    ├── rules/                     ← AI 寫 code 時必須遵守的規則
    │   ├── 01-keep-it-simple.md   ← 別寫複雜的東西
    │   ├── 02-coding-style.md     ← code 長什麼樣
    │   ├── 03-when-stuck.md       ← AI 卡住時該怎麼辦
    │   ├── 04-spec-first.md       ← ⭐ 沒 spec 不寫 code
    │   ├── 05-tdd-required.md     ← ⭐ 先寫測試
    │   └── 06-doc-as-code.md      ← ⭐ 文件與 code 一起改
    ├── prompts/                   ← 常用對話開場白
    │   ├── start-project.md
    │   ├── add-feature.md
    │   ├── fix-bug.md
    │   └── deploy.md
    └── skills/                    ← ⭐ Slash command 工具箱
        ├── check-key.md               (/check-key 部署前安檢)
        ├── explain-code/SKILL.md      (/explain-code 架構師視角)
        ├── spec-it/
        │   ├── SKILL.md               ⭐ /spec-it    生 PRD + API + BDD
        │   └── templates/             ⭐ 6 份大廠對標 spec 範本（PRD / user-story / api-contract / db-schema / bdd / test-cases）
        ├── adr/
        │   ├── SKILL.md               ⭐ /adr        架構決策記錄
        │   └── templates/adr-template.md  (MADR v3.0)
        ├── plan-sprint/SKILL.md       ⭐ /plan-sprint backlog 拆解
        ├── tdd-cycle/SKILL.md         ⭐ /tdd-cycle  紅綠燈循環
        ├── verify/SKILL.md            ⭐ /verify     5 維度品質驗證
        ├── sync-it/SKILL.md           ⭐ /sync-it    code↔文件 drift
        ├── commit-msg/SKILL.md        ⭐ /commit-msg Conventional Commits
        └── retro/SKILL.md             ⭐ /retro      sprint 4Ls 回顧
```

---

## 🎯 這套模板怎麼用：Vibe Engineering Sprint

本模板走 **Vibe Engineering** 單一工作流：**用工程紀律放大 AI coding**（自動化測試 / 事前規劃 / 版本控制 / CI 品質閘 / 文件同步），而非靠一份規格文件驅動。落到鐵則就三句：spec 先於 code、測試先於實作、文件與 code 同步。

| 階段 | skill | 產出 |
|---|---|---|
| 意圖 | `/spec-it` `/adr` `/plan-sprint` | PRD + ADR + backlog |
| 設計 | `/spec-it`（L2+L3） | API contract + BDD + 測試骨架 |
| 實作 | `/tdd-cycle` `/verify` `/sync-it` | 紅綠燈循環 + 五維驗證 + 文件對齊 |
| 上線 | `/commit-msg` 部署 `/retro` | Conventional Commits + 部署 + 回顧 |

**適合**：有基本程式概念（知道 function / API / 測試）、要做正規可維護專案。
**純新手** → 先看 `class_plan/` 工作坊教案學 Vibe Coding 基礎，能力上來再回來。

📖 **完整使用說明、Sprint walkthrough、FAQ → 看 [`USAGE.md`](./USAGE.md)**
📊 **十站流程總圖 → 看 [`.agents/WORKFLOW.md`](./.agents/WORKFLOW.md)**

---

## 🚀 三步驟開始用

### 步驟 1：複製整個資料夾
把 `antigravity_project_template/` 複製到你想放專案的地方，重新命名（例如：`news-summarizer/`）。

### 步驟 2：填好 PRD 與 API Key
1. 打開 `docs/PRD.md`，把 `___` 通通填上你的需求（你在 AI Studio 已經做過這一步，直接複製過來就好）
2. 在終端機設定 Gemini API Key：
   ```bash
   export GEMINI_API_KEY="你的金鑰"
   ```
   或寫到 `~/.zshrc` / `~/.bashrc` 永久生效。
3. 申請金鑰：[aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### 步驟 3：用 Antigravity 開啟資料夾

**方案 A：用 CLI（推薦給想學自動化的人）**

先裝 Antigravity CLI（一次性）：

```bash
# macOS / Linux
curl -fsSL https://antigravity.google/cli/install.sh | bash

# Windows PowerShell
irm https://antigravity.google/cli/install.ps1 | iex
```

然後：

```bash
cd 你的專案資料夾
agy
```

第一次啟動會走三個確認：**配色 → 條款 → 資料夾信任**（只信任你自己的工作區，其他選 No）。

進入互動式對話後，把 `.agents/prompts/start-project.md` 裡那段話貼進去，按 Enter。

**方案 B：用 Antigravity 桌面版（推薦給不熟終端機的人）**

打開 Antigravity 桌面版 → 開啟這個資料夾 → 在對話框貼上 `.agents/prompts/start-project.md` 裡那段話 → 按送出。

不論哪個方案，接下來 AI 就會接手。**你只要一直用「自然語言」跟它說話就好，不要自己改 code。**

---

## 💡 CLI 專屬技巧（桌面版沒有的）

| 動作                | CLI 怎麼做                                   |
| ----------------- | ----------------------------------------- |
| 引用某個檔案給 AI 看      | 在對話中打 `@docs/PRD.md`                      |
| 跑 shell 指令        | 在對話中打 `!ls` 或 `!npm install`               |
| 看 AI 現在記住什麼       | 打 `/memory show`                          |
| 叫 AI 記住某件事        | 打 `/memory add 我習慣用 pnpm 不是 npm`          |
| 清空對話重新開始          | 打 `/clear`                                |
| 看內建 slash 指令       | 打 `/help`                                 |
| 觸發 Vibe Engineering skill        | `/spec-it` `/adr` `/plan-sprint` `/tdd-cycle` `/verify` `/sync-it` `/commit-msg` `/retro` + `/check-key` `/explain-code`（連動見 `.agents/SKILL-MAP.md`） |
| 從 Gemini CLI 搬過來    | 打 `agy plugin import gemini`（一次性遷移） |

---

## 💡 卡住時看哪裡

| 狀況            | 看哪份 prompt                              |
| ------------- | --------------------------------------- |
| 想從桌面版轉到 CLI、看整套協作環境 | **`docs/HANDBOOK.md`** ← 推薦先讀 |
| 不知道怎麼開始       | `.agents/prompts/start-project.md`      |
| 想加新功能         | `.agents/prompts/add-feature.md`（手動複製貼全文模板） |
| 想要 AI 動手前先列計畫 | 跑 `/plan-sprint` 拆 backlog；小調整也可直接講「先列計畫等我確認」 |
| 跑起來有錯 / bug   | `.agents/prompts/fix-bug.md`            |
| AI 一直亂寫 / 越改越糟 | `.agents/rules/03-when-stuck.md`        |
| AI 改錯一堆檔案、想回到改之前 | 打 `/restore` 選快照回滾（比 git reset 安全） |
| 想把專案放網路上給朋友看  | `.agents/prompts/deploy.md`             |
| AI 好像「忘了規則」   | 跑 `/memory show` 檢查 AGENTS.md 是否載入；改完 AGENTS.md 跑 `/memory refresh` |
| 想讓 AI 多會新技能（外部能力） | `.agents/MCP.md`（github、fetch、playwright…） |
| 想包「AI 自動觸發的流程」或自訂指令 | `.agents/SKILLS.md` |
| 大型任務跑很久 / 想平行加速 | `.agents/SUBAGENTS.md`（Antigravity 2026 殺手特性） |
| 想跑 Vibe Engineering 完整 Sprint（spec + TDD + 文件同步） | `.agents/WORKFLOW.md` + 8 個 Vibe Engineering skill |
| 不知道 spec 怎麼寫 | `.agents/skills/spec-it/templates/` (6 份) + `.agents/skills/adr/templates/` (ADR) — 共 7 份大廠對標範本，與 skill 共置 |
| 想看「從一句痛點到可跑 app」完整流程 | [`../VIBE_ENGINEERING_RUNBOOK.md`](../VIBE_ENGINEERING_RUNBOOK.md) — SmartTrip FX 端到端 walkthrough（AI Studio meta-prompt → agy Vibe Engineering Sprint） |
| 進度比較慢、要 MVP 填空版 | [`../MVP_RUNBOOK.md`](../MVP_RUNBOOK.md) — STRIKE 三格急救組合 |
| 不知道任務怎麼拆 | 打 `/plan-sprint` |
| 想 commit 但不知道訊息怎麼寫 | 打 `/commit-msg` |
| Sprint 結束想回顧 | 打 `/retro` |

---

## ⚠️ Vibe Engineering 四鐵則

1. **沒 PRD 不開工** — 新需求先 `/spec-it`（`rules/04-spec-first.md`）
2. **沒測試不算完成** — 實作走 `/tdd-cycle` 紅綠燈（`rules/05-tdd-required.md`）
3. **沒 `/verify` 不 commit** — 過五維度驗證才 commit
4. **沒 `/sync-it` 不收工** — 文件跟著 code 走，不容許 drift（`rules/06-doc-as-code.md`）

詳細 → [`USAGE.md` §1.2 四條鐵則](./USAGE.md)。

---

## 📚 我以前用 Gemini CLI，怎麼搬過來？

```bash
# 1. 裝 Antigravity CLI
curl -fsSL https://antigravity.google/cli/install.sh | bash

# 2. 一鍵搬遷舊有設定（MCP servers / commands / memory / 配色）
agy plugin import gemini

# 3. 第一次 agy 啟動會自動偵測 ~/.gemini/ 並問你要不要 import
agy
```

舊有 `~/.gemini/` 不會被刪，可先審查再決定要不要清。**個人版 Gemini CLI 在 2026-06-18 停止服務**（企業版 Gemini Code Assist Standard/Enterprise 不受影響）。
