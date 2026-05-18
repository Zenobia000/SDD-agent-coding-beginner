# AGENTS.md — 跨 Agent 共用規則

> 這份是給「所有 coding agent」看的共用規則（Gemini CLI、Codex、Cursor 等）。
> Gemini CLI 專屬行為請看 [`GEMINI.md`](./GEMINI.md)。
>
> 如果你之後也用 Claude Code，可以 `ln -s AGENTS.md CLAUDE.md` 直接重用。

---

## 1. Project Mission

把使用者**沒寫過程式**的點子，最快變成「螢幕上能動的東西」。

- 不追求架構完美
- 不追求未來擴充
- 追求「下一個 5 分鐘」能看到進展

---

## 2. Repository Structure

```
my-project/
├── README.md                # 給人看的入口
├── GEMINI.md                # Gemini CLI 專屬規則（單一真相來源）
├── AGENTS.md                # 你正在看 — 跨 Agent 共用規則
├── docs/
│   └── PRD.md               # 需求規格
├── .gemini/
│   ├── settings.json        # Gemini CLI 設定
│   ├── rules/               # 寫 code 的硬規則
│   ├── prompts/             # 常用 prompt
│   ├── commands/            # 自訂 slash command
│   └── memory/              # 長期記憶說明
└── index.html               # 你的主程式（單檔優先）
```

---

## 3. Development Workflow

```bash
# 啟動 Gemini CLI（在專案根目錄）
gemini

# 看本機檔案
ls

# 直接打開瀏覽器測試
open index.html              # macOS
xdg-open index.html          # Linux
```

---

## 4. Coding Standards

詳見 `.gemini/rules/02-coding-style.md`。重點：

- 變數命名用「有意義的英文小駝峰」
- 常數全大寫加底線
- 每個函式上方一行中文註解
- 錯誤訊息用繁體中文顯示在畫面上

---

## 5. Testing Rules

這是 MVP 階段，**不寫單元測試**。驗證方式：

1. 瀏覽器打開 `index.html`
2. 按照 `docs/PRD.md` 的「期望輸出」操作一次
3. 確認沒有 console 紅字

---

## 6. Security Rules

- ❌ API Key 不可寫死後 commit — 用 `const API_KEY = "請貼上你的金鑰"` 佔位符
- ❌ 不可把 `.env` commit 上去
- ❌ 不可在 git 上做不可逆操作（`reset --hard`、`push --force`）
- ✅ 上線前如果要公開，改成 `prompt("請輸入你的 API Key")` 讓使用者自己貼

---

## 7. Agent Behavior Rules

1. **先讀文件再改 code** — 必讀順序見 `GEMINI.md` 第 2 節
2. **大改動前先 plan** — 列出要改哪些檔案，等使用者 OK 再動手
3. **每次回覆給 4 段結尾** — Summary / Changed Files / How to Test / Next Step
4. **卡關走 SOP** — 觸發條件見 `.gemini/rules/03-when-stuck.md`

---

## 8. Definition of Done

一個任務算完成 = 同時滿足：

- [ ] 使用者在瀏覽器看到結果
- [ ] 已告訴他怎麼測試
- [ ] 沒有 console error
- [ ] PRD 的「期望輸出格式」有達成
