# Gemini CLI 初學者專案模板

> 給 Vibe Coding 工作坊學員：把這整個資料夾複製到你的專案位置，在終端機 `cd` 進去後執行 `gemini`，AI 就會自動讀懂規則開始幫你做事。

---

## 📁 這個資料夾裡有什麼

```
my-project/
├── README.md                      ← 你正在看
├── GEMINI.md                      ← ⭐ Gemini CLI 一定會讀的「總指揮文件」
├── docs/
│   └── PRD.md                     ← 從 AI Studio 帶過來的需求規格（填空）
└── .gemini/
    ├── settings.json              ← Gemini CLI 設定（MCP、sandbox、checkpoint）
    ├── MCP.md                     ← MCP 外掛工具入門（github / fetch / context7 等）
    ├── rules/                     ← AI 寫 code 時必須遵守的規則
    │   ├── 01-keep-it-simple.md   ← 別寫複雜的東西
    │   ├── 02-coding-style.md     ← code 長什麼樣
    │   └── 03-when-stuck.md       ← AI 卡住時該怎麼辦
    ├── prompts/                   ← 你可以直接複製貼上的常用 prompt
    │   ├── start-project.md       ← 開新專案的第一句話
    │   ├── add-feature.md         ← 加功能
    │   ├── fix-bug.md             ← 修 bug
    │   └── deploy.md              ← 想上線時
    ├── commands/                  ← 自訂 slash command（可選）
    │   └── README.md              ← 怎麼自己加 /xxx 指令
    └── memory/                    ← Gemini 長期記憶說明
        └── README.md              ← /memory show 怎麼用
```

---

## 🚀 三步驟開始用

### 步驟 1：複製整個資料夾
把 `gemini_cli_project_template/` 複製到你想放專案的地方，重新命名（例如：`news-summarizer/`）。

### 步驟 2：填好 PRD 與 API Key
1. 打開 `docs/PRD.md`，把 `___` 通通填上你的需求（你在 AI Studio 已經做過這一步，直接複製過來就好）
2. 在終端機設定 Gemini API Key：
   ```bash
   export GEMINI_API_KEY="你的金鑰"
   ```
   或寫到 `~/.zshrc` / `~/.bashrc` 永久生效。
3. 申請金鑰：[aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### 步驟 3：在終端機啟動 Gemini CLI
```bash
cd 你的專案資料夾
gemini
```
進入互動式對話後，把 `.gemini/prompts/start-project.md` 裡那段話貼進去，按 Enter。

接下來 AI 就會接手。**你只要一直用「自然語言」跟它說話就好，不要自己改 code。**

---

## 💡 CLI 專屬技巧（Antigravity 沒有的）

| 動作                | CLI 怎麼做                                   |
| ----------------- | ----------------------------------------- |
| 引用某個檔案給 AI 看      | 在對話中打 `@docs/PRD.md`                      |
| 跑 shell 指令        | 在對話中打 `!ls` 或 `!npm install`               |
| 看 AI 現在記住什麼       | 打 `/memory show`                          |
| 叫 AI 記住某件事        | 打 `/memory add 我習慣用 pnpm 不是 npm`          |
| 清空對話重新開始          | 打 `/clear`                                |
| 看可用的 slash 指令     | 打 `/help`                                 |

---

## 💡 卡住時看哪裡

| 狀況            | 看哪份 prompt                              |
| ------------- | --------------------------------------- |
| 想從 IDE 轉到 CLI、看整套協作環境 | **`docs/HANDBOOK.md`** ← 推薦先讀 |
| 不知道怎麼開始       | `.gemini/prompts/start-project.md`      |
| 想加新功能         | `.gemini/prompts/add-feature.md`        |
| 跑起來有錯 / bug   | `.gemini/prompts/fix-bug.md`            |
| AI 一直亂寫 / 越改越糟 | `.gemini/rules/03-when-stuck.md`        |
| 想把專案放網路上給朋友看  | `.gemini/prompts/deploy.md`             |
| AI 好像「忘了規則」   | 跑 `/memory show` 檢查 GEMINI.md 是否載入       |
| 想讓 AI 多會新技能（外部能力） | `.gemini/MCP.md`（github、fetch、playwright…） |
| 想包「AI 自動觸發的流程」 | `.gemini/SKILLS.md`（2026 新原語） |
| 想做自己的 `/xxx` 指令 | `.gemini/commands/README.md` |

---

## ⚠️ 三個不要

1. ❌ **不要自己改 code** — 改不好還會壞掉。改「需求描述」讓 AI 重做。
2. ❌ **不要一次給太多需求** — 一次加一個小功能，跑得起來再加下一個。
3. ❌ **不要刪 `.gemini/` 資料夾** — 它是 AI 的「規則書」，刪了 AI 就會亂寫。
