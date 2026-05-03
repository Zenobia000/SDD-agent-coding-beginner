# Antigravity 初學者專案模板

> 給 Vibe Coding 工作坊學員：把這整個資料夾複製到你的專案位置，用 Antigravity 打開，AI 就會自動讀懂規則開始幫你做事。

---

## 📁 這個資料夾裡有什麼

```
my-project/
├── README.md                      ← 你正在看
├── AGENTS.md                      ← ⭐ Antigravity 一定會讀的「總指揮文件」
├── docs/
│   └── PRD.md                     ← 從 AI Studio 帶過來的需求規格（填空）
└── .antigravity/
    ├── rules/                     ← AI 寫 code 時必須遵守的規則
    │   ├── 01-keep-it-simple.md   ← 別寫複雜的東西
    │   ├── 02-coding-style.md     ← code 長什麼樣
    │   └── 03-when-stuck.md       ← AI 卡住時該怎麼辦
    └── prompts/                   ← 你可以直接複製貼上的常用 prompt
        ├── start-project.md       ← 開新專案的第一句話
        ├── add-feature.md         ← 加功能
        ├── fix-bug.md             ← 修 bug
        └── deploy.md              ← 想上線時
```

---

## 🚀 三步驟開始用

### 步驟 1：複製整個資料夾
把 `antigravity_project_template/` 複製到你想放專案的地方，重新命名（例如：`news-summarizer/`）。

### 步驟 2：填好 PRD
打開 `docs/PRD.md`，把 `___` 通通填上你的需求（你在 AI Studio 已經做過這一步，直接複製過來就好）。

### 步驟 3：用 Antigravity 打開資料夾，貼第一句話
打開 Antigravity → 開啟這個資料夾 → 在對話框貼上 `.antigravity/prompts/start-project.md` 裡面那段話 → 按送出。

接下來 AI 就會接手。**你只要一直用「自然語言」跟它說話就好，不要自己改 code。**

---

## 💡 卡住時看哪裡

| 狀況 | 看哪份 prompt |
|---|---|
| 不知道怎麼開始 | `.antigravity/prompts/start-project.md` |
| 想加新功能 | `.antigravity/prompts/add-feature.md` |
| 跑起來有錯 / bug | `.antigravity/prompts/fix-bug.md` |
| AI 一直亂寫 / 越改越糟 | `.antigravity/rules/03-when-stuck.md` |
| 想把專案放網路上給朋友看 | `.antigravity/prompts/deploy.md` |

---

## ⚠️ 三個不要

1. ❌ **不要自己改 code** — 改不好還會壞掉。改「需求描述」讓 AI 重做。
2. ❌ **不要一次給太多需求** — 一次加一個小功能，跑得起來再加下一個。
3. ❌ **不要刪 `.antigravity/` 資料夾** — 它是 AI 的「規則書」，刪了 AI 就會亂寫。
