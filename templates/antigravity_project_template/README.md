# Antigravity 初學者專案模板

> 給 Vibe Coding 工作坊學員：把這整個資料夾複製到你的專案位置，用 Antigravity 桌面版或 `agy` CLI 打開，AI 就會自動讀懂規則開始幫你做事。

---

## 📁 這個資料夾裡有什麼

```
my-project/
├── README.md                      ← 你正在看
├── AGENTS.md                      ← ⭐ Antigravity 一定會讀的「總指揮文件」（業界統一規範）
├── docs/
│   ├── PRD.md                     ← 從 AI Studio 帶過來的需求規格（填空）
│   └── HANDBOOK.md                ← Antigravity CLI 完整操作手冊（從 IDE 轉 CLI 必讀）
└── .agents/
    ├── settings.json              ← Antigravity CLI 設定（model / checkpoint / MCP）
    ├── MCP.md                     ← MCP 外掛工具入門（github / fetch / context7 等）
    ├── SKILLS.md                  ← Skill + Slash Command 教學（2026 統一原語）
    ├── rules/                     ← AI 寫 code 時必須遵守的規則
    │   ├── 01-keep-it-simple.md   ← 別寫複雜的東西
    │   ├── 02-coding-style.md     ← code 長什麼樣
    │   └── 03-when-stuck.md       ← AI 卡住時該怎麼辦
    ├── prompts/                   ← 你可以直接複製貼上的常用 prompt
    │   ├── start-project.md       ← 開新專案的第一句話
    │   ├── add-feature.md         ← 加功能
    │   ├── fix-bug.md             ← 修 bug
    │   └── deploy.md              ← 想上線時
    └── skills/                    ← 自訂 skill / slash command（只附 2 個模型本能彌補不了的）
        ├── check-key.md           ← /check-key（部署前安全檢查）
        └── explain-code/          ← /explain-code（架構師視角講解）
            └── SKILL.md
```

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
| 觸發自訂 skill        | 打 `/check-key`、`/explain-code`（本模板附 2 個；更多範例見 `.agents/SKILLS.md`） |
| 從 Gemini CLI 搬過來    | 打 `agy plugin import gemini`（一次性遷移） |

---

## 💡 卡住時看哪裡

| 狀況            | 看哪份 prompt                              |
| ------------- | --------------------------------------- |
| 想從桌面版轉到 CLI、看整套協作環境 | **`docs/HANDBOOK.md`** ← 推薦先讀 |
| 不知道怎麼開始       | `.agents/prompts/start-project.md`      |
| 想加新功能         | `.agents/prompts/add-feature.md`（手動複製貼全文模板） |
| 想要 AI 動手前先列計畫 | 直接跟 AI 講「先列計畫等我確認」（AGENTS.md 第 3 章五步流程已要求；SOTA 模型自動會做） |
| 跑起來有錯 / bug   | `.agents/prompts/fix-bug.md`            |
| AI 一直亂寫 / 越改越糟 | `.agents/rules/03-when-stuck.md`        |
| AI 改錯一堆檔案、想回到改之前 | 打 `/restore` 選快照回滾（比 git reset 安全） |
| 想把專案放網路上給朋友看  | `.agents/prompts/deploy.md`             |
| AI 好像「忘了規則」   | 跑 `/memory show` 檢查 AGENTS.md 是否載入；改完 AGENTS.md 跑 `/memory refresh` |
| 想讓 AI 多會新技能（外部能力） | `.agents/MCP.md`（github、fetch、playwright…） |
| 想包「AI 自動觸發的流程」或自訂指令 | `.agents/SKILLS.md` |

---

## ⚠️ 三個不要

1. ❌ **不要自己改 code** — 改不好還會壞掉。改「需求描述」讓 AI 重做。
2. ❌ **不要一次給太多需求** — 一次加一個小功能，跑得起來再加下一個。
3. ❌ **不要刪 `.agents/` 資料夾** — 它是 AI 的「規則書」，刪了 AI 就會亂寫。

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
