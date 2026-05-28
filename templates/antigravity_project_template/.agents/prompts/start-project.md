# Prompt：開新專案的第一句話

> 把整段複製貼到 Antigravity 對話框，按送出。

---

```
請先讀以下文件，再開始工作：

1. AGENTS.md（你的工作守則）
2. .agents/WORKFLOW.md（SDD Sprint 十站總圖）
3. docs/PRD.md（我的需求規格，可能還沒填完）

讀完後，請跑 SDD 第一站 /spec-it：

1. 問我 5 個澄清問題（解什麼問題 / 成功長怎樣 / 不做什麼 / 既有 PRD / sprint 長度）
2. 依我的回答生 PRD + user story + AC（寫進 docs/PRD.md）
3. 如有 API，生 api-contract；生 BDD scenarios + 測試骨架
4. 把任務寫進 tasks/backlog.md

不要跳過 spec 直接寫 code（rules/04-spec-first）。請開始問第 1 題。
```

---

## 為什麼這樣寫

| 這句話 | 在做什麼 |
|---|---|
| 「請先讀 AGENTS.md / WORKFLOW.md」 | 強迫 AI 對齊工作守則與 SDD 十站流程 |
| 「跑 /spec-it」 | SDD 第一站：把模糊意圖結構化成 spec，後面 TDD 才有對齊基準 |
| 「問我 5 個澄清問題」 | 揪出需求誤會 + 逼你想清楚範圍（不做什麼跟做什麼一樣重要）|
| 「不要跳過 spec 直接寫 code」 | rules/04 鐵則：沒 spec 的 code 是「以為要、其實不要」的最大來源 |

---

## 接下來要說的話

當 AI 問完 5 題、生出 PRD + 測試骨架後：

- ✅ spec 對 → 「OK，跑 `/plan-sprint` 拆 backlog」
- ⚠️ spec 有誤 → 「US-002 不對，我要的是 ___，請改 spec」

進入實作時：

- 跑 `/tdd-cycle` 逐個 task 寫（紅綠燈循環）
- 完整下一步順序見 `.agents/SKILL-MAP.md` 或 `USAGE.md` §2 walkthrough
