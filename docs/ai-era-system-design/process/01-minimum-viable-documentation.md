# Process 01 — 最小可行文件集 SOP

> 目的：給一個可直接套用的文件清單，讓任何新專案在啟動時都有「最小但完整」的定義。
> 原則：不是文件越多越好，而是每個關鍵維度都有第一版，且能持續演化。

---

## 7 份文件清單

| # | 文件 | 用途 | 沒有會怎樣 | 對應 Vibe Engineering |
|---|------|------|------------|----------------------|
| 1 | Problem Statement | 定義為什麼做 | 做出沒人要的東西 | 種子簡報 / L1 PRD 開頭 |
| 2 | User / Business Flow | 定義流程 | 系統流程混亂 | L1 PRD 的 User Flow |
| 3 | Scope / Non-scope | 定義邊界 | 需求無限膨脹 | L1 PRD 的 Scope 段 |
| 4 | Architecture Diagram | 定義系統組成 | 工程師各做各的 | ADR + 架構草圖 |
| 5 | Data Model / ERD | 定義資料關係 | DB 後期難改 | L2 資料模型 |
| 6 | API Contract | 定義介面 | 前後端整合爆炸 | L2 `docs/api-contract.md` |
| 7 | Test Scenario | 定義驗收 | 上線前才發現不符 | L3 BDD scenarios |

---

## 與三層 Spec 的對應

本 repo 的 `/spec-it` skill（[`.agents/skills/spec-it`](../../../templates/antigravity_project_template/.agents/skills/spec-it/)）一次產出三層，正好覆蓋這 7 份的多數：

```
L1 PRD          → #1 Problem Statement + #2 Flow + #3 Scope
L2 API contract → #5 Data Model + #6 API Contract
L3 BDD          → #7 Test Scenario
（#4 Architecture 由 ADR skill 補上）
```

實作建議：用 `/spec-it` 產出 L1–L3 草稿，再用 `/adr` 補架構決策，即可一次湊齊 MVD。

---

## 啟動 SOP（建議順序）

1. **寫種子簡報**：用六個起始問題（見 [articles/01](../articles/01-pre-ai-how-systems-began.md)）填出 Problem Statement 與 Scope。
2. **選一個起手式**：Business Flow / User Story / Data Model / Architecture 擇一切入（見 [articles/03](../articles/03-converge-not-topdown.md)）。
3. **跑 `/spec-it`**：產出 L1–L3 草稿，標記 `status: draft`。
4. **人類收斂**：對每段做「保留 / 刪除 / 待確認」，未確認項進 Open Questions。
5. **跑 `/adr`**：把架構與技術選型決策寫成 ADR。
6. **進 Gate**：通過 Scope Gate 與 Flow Gate 後才開始開發（見 [process/04](04-human-gate-and-agent-roles.md)）。

---

## 文件狀態約定

每份文件 frontmatter 都帶狀態，避免「AI 草稿被誤用成正式決策」：

```yaml
status: draft | reviewed | approved | deprecated
owner:
reviewer:
last_updated:
source: [human | ai | meeting | customer]
decision_level: suggestion | working_agreement | official_decision
```

只有 `status: approved` 且 `decision_level: official_decision` 的文件，才能當開發依據。

---

## 相關

- 五輪工作流如何產出與收斂這些文件 → [process/02](02-ai-collaboration-sop.md)
- Schema 與可追溯性模板 → [process/03](03-schemas-and-traceability.md)
