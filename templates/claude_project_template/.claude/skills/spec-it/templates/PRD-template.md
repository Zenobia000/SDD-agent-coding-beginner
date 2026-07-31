# PRD — Product Requirements Document

> **Layer 1 spec（意圖層）**
> 大廠對標：Atlassian Product Spec、Amazon PR-FAQ（簡化版）
> 寫作時機：**任何功能動工前**，由 `/spec-it` skill 自動生成草稿，你補實。
> 寫作原則：**讀者是 6 個月後的自己 + AI**。能讓他們重建決策上下文，才算合格。

---

## 1. Problem Statement（問題陳述）

**用一段話回答**：
- 誰（who）有什麼痛點？
- 現在他們怎麼解？為什麼那個解法不夠好？
- 如果不做這個，會發生什麼？

> 範例：「上班族每天需要看 20 篇英文新聞但只有 30 分鐘。目前他們用 Google 翻譯逐篇貼，速度慢且失去結構。不做的話他們會放棄追新聞或只看標題。」

---

## 2. Goal & Non-Goal（目標 vs 非目標）

### Goals（這個 sprint 要做到的）
- G1：___
- G2：___
- G3：___

### Non-Goals（這個 sprint 明確不做的）
- NG1：不做 ___（理由：___）
- NG2：不做 ___（理由：___）

> Non-Goal 跟 Goal 一樣重要 — 它防止 AI 自作主張加功能。

---

## 3. Target User & Persona

| 維度 | 內容 |
|---|---|
| 主要使用者 | ___（年齡 / 角色 / 技術程度） |
| 使用情境 | ___（在什麼裝置、什麼時段、什麼狀態下用） |
| 知識前提 | ___（他們已經知道什麼？不需要解釋什麼？） |

---

## 4. User Stories（用 INVEST 寫）

複製多個 user story，每個用以下格式：

```
US-001
As a   [角色]
I want [行為 / 能力]
So that [得到的價值]

Acceptance Criteria（驗收條件）：
- [ ] 給定 ___，當 ___，則 ___
- [ ] 給定 ___，當 ___，則 ___

優先級：P0 / P1 / P2
估時：S / M / L（半天 / 一天 / 三天）
```

> **INVEST 原則**（Bill Wake）：Independent / Negotiable / Valuable / Estimable / Small / Testable。
> AC 寫不出來 → 表示這個 story 還太抽象，先拆。

---

## 5. Success Metrics（成功如何衡量？）

| 指標類型 | 名稱 | 目標值 | 量測方式 |
|---|---|---|---|
| **核心指標** | ___ | ___ | ___ |
| **品質指標** | 主流程成功率 | ≥ 95% | 手動測 20 次 / 自動測試 |
| **體驗指標** | 首屏時間 | < 2 秒 | DevTools Performance |

> Solo 專案不需要 OKR，但**至少要有一個可量測的成功定義**，否則你永遠在「再加一點功能」的迴圈裡。

---

## 6. Out of Scope（本次明確不碰）

- 不做使用者註冊 / 登入（用 localStorage）
- 不做後端資料庫（純前端）
- 不做付費機制

---

## 7. Open Questions（待決定的事）

- [ ] Q1：___？（決策時間：___）
- [ ] Q2：___？

---

## 8. Risks（風險）

| 風險 | 影響 | 機率 | 對策 |
|---|---|---|---|
| Gemini API 配額用完 | 中 | 低 | 加上 cache + 失敗降級 |
| 樣式在 Safari 跑掉 | 低 | 中 | 預留 30 分鐘 cross-browser 測試 |

---

## 9. Revision History

| 版本 | 日期 | 變更 | 作者 |
|---|---|---|---|
| v0.1 | YYYY-MM-DD | 初稿 | ___ |
| v0.2 | YYYY-MM-DD | 補 §4 user story | ___ |

---

## 寫作檢查清單

- [ ] 一段話能讓 6 個月後的自己想起「為何做這個」
- [ ] Goal / Non-Goal 都寫了（至少各 2 條）
- [ ] 每個 user story 有可勾選的 acceptance criteria
- [ ] 至少 1 個成功指標可量測
- [ ] 有列 Out of Scope（防 AI 加功能）
- [ ] 有列 Open Questions（誠實面對未知）
