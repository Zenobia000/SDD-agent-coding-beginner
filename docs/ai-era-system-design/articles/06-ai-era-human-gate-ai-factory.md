# 06 — AI 時代：Human Gate + AI Factory

> 重點：AI 沒有打掉傳統工程治理，而是把它升級。
> 模型很簡單：**AI 是工廠，人類是 Gate。**
> AI 大量產草稿、案例、檢查、骨架；人類負責決策、取捨、承擔責任。

---

## 核心模型

```
AI Factory（快速產出）
  ↓
Human Gate（判斷採用）
  ↓
Official Artifact（正式文件 / 程式 / 決策）
```

危險的反模式是：

```
AI 產出 → 直接相信 → 開發照做
```

AI 速度快，但若沒有 Human Gate，它會變成雜訊製造機。詳細的角色分工與 Review Queue 見 [process/04](../process/04-human-gate-and-agent-roles.md)。

---

## AI 不該產「更多文件」，該產「可追溯鏈」

大型系統最重要的是 Traceability：

```
需求 → 流程 → API → 資料表 → 測試案例 → 部署與監控
```

每個東西都要追得回去。AI 特別適合維護這種重複、繁瑣、容易漏的鏈（Traceability Matrix），因為人類討厭做這件事。讓 AI 進入表格、Schema、狀態機、ADR，而不是一直「說」。模板見 [process/03](../process/03-schemas-and-traceability.md)。

---

## 五大原則

| # | 原則 | 含義 |
|---|------|------|
| 1 | AI 先發散，人類再收斂 | AI 列出可能性，人類決定哪個成立 |
| 2 | AI 產草稿，人類定版本 | draft ≠ decision |
| 3 | AI 補細節，人類控邊界 | AI 補 100 個測試案例，人類決定哪些是 P0/P1/P2 |
| 4 | AI 做一致性檢查，不做權責決策 | AI 可發現 PRD 與 API 不一致，但不能決定改哪個 |
| 5 | 文件不是越多越好，而是越可追溯越好 | 文件價值 = 決策清晰度 × 可追溯性 |

---

## 工作分級：什麼交給 AI，什麼留給人

判準很簡單：**凡是需要承擔責任的，不交給 AI；凡是重複、展開、檢查、整理的，交給 AI。**

### 低風險 — AI 可直接做，人類抽查

文件格式整理、命名建議、測試資料生成、README 草稿、code comment 草稿。

### 中風險 — AI 做草稿，人類 Review

API Spec、DB Schema、測試案例、架構比較、部署腳本。

### 高風險 — AI 只輔助，必須人類決策

| 工作 | 為什麼不能交給 AI |
|------|-------------------|
| Scope 取捨 | 牽涉資源與政治 |
| 架構最終選擇 | 牽涉組織能力 |
| 資安風險接受 | 牽涉責任歸屬 |
| 上線 Go / No-Go | 出事人類負責 |
| 客戶承諾 | AI 不知道商務脈絡 |
| 技術選型拍板 | 要問「我們團隊真的能維運嗎」 |

技術選型尤其要小心：不要問 AI「幫我選最好的技術」，要問「在以下約束下，列出 3 個可行方案並用決策矩陣比較」。最後那句「我們團隊真的能維運這個選擇嗎」，AI 不能替你回答。

---

## 升級後的主流程

傳統主流程不變，AI 嵌在每一段，但每一段都要有 `AI 產出 → 人類審查 → 正式採用`：

```
需求分析   ├ AI 展開 User Story / Open Questions   └ 人類決定 Scope
架構設計   ├ AI 產架構候選 / 風險清單              └ Architect 拍板 ADR
開發       ├ AI 產骨架 / 測試 / 文件               └ Engineer 審查整合
測試       ├ AI 產測試案例 / 邊界條件              └ QA 確認驗收標準
部署       ├ AI 產 IaC / Runbook 草稿             └ DevOps 審核安全
維運       ├ AI 協助 Log 分析 / Incident Summary  └ SRE 做根因決策
```

這正是本 repo [`.agents/WORKFLOW.md`](../../../.claude/skills/next/SKILL.md) 十站式 sprint 的精神：AI 加速每一站，人類守每一道 Gate。

---

## 一句話總結

> 大型系統主流程仍走傳統工程治理。AI 放在每一階段的發散、補洞、產生候選、檢查一致性與生成重複資產。
> 人類不再手寫所有文件，而是設計 Gate、Schema、Review Queue，把 AI 產出收斂成正式決策。
>
> AI 產能提升後，真正稀缺的不是內容，而是判斷力、決策權與治理結構。

---

## 接下來

把原則落地成可執行的流程與模板：

- [process/01 — 最小可行文件集 SOP](../process/01-minimum-viable-documentation.md)
- [process/02 — AI 協作五輪工作流](../process/02-ai-collaboration-sop.md)
- [process/03 — 結構化產出模板與可追溯性](../process/03-schemas-and-traceability.md)
- [process/04 — Human Gate 與 AI Agent 角色](../process/04-human-gate-and-agent-roles.md)
