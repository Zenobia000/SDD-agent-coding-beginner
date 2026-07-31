---
name: grill-with-docs
description: 以一次一題的深度訪談釐清工程需求，並在決策形成時同步維護 domain glossary 與必要 ADR。
disable-model-invocation: true
argument-hint: "要釐清的功能、設計或決策"
---

# Grill With Docs

執行 `grilling` 的訪談紀律，並在涉及領域語言或難以逆轉的技術決策時套用 `domain-modeling`。

先讀 `docs/agents/project.md`、相關 glossary、ADR 與程式碼。可從環境查到的事實自行查，不要問使用者。

訪談期間：

- 一次只問一題，每題附推薦答案與會翻盤的條件。
- 沿決策樹逐一解依賴，不跳到實作。
- 術語一旦收斂，立即更新 glossary；符合 ADR 三條件的決策先詢問是否記錄。
- 發現對話與 code 不一致時，展示雙方證據並請使用者決定哪一個代表正確領域行為。
- 每幾題重述一次已決定、未決定與 out of scope，避免對話漂移。

直到使用者明確確認已達成共同理解才停止；停止時只總結決策、未決問題與建議下一個 skill，不寫產品 code。
