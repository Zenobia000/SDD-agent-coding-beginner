---
name: to-spec
description: 把目前對話與已確認的 codebase 事實合成可實作規格，經確認後發布到專案設定的 tracker 或本地文件。
disable-model-invocation: true
argument-hint: "可選：規格名稱或來源"
---

# To Spec

這是合成，不是新一輪訪談。只使用目前對話、已讀規格、domain glossary、ADR 與實際 code 證據；未知內容標成 open question，不能補寫成決定。

## 流程

1. 讀 `docs/agents/project.md`。若不存在，依 repo 安全推斷輸出位置並明講預設；不要自動執行 `/setup-project`。
2. 補讀與需求直接相關的現況，讓規格描述目標差距而不是理想化新系統。
3. 使用 `codebase-design` 找出最高層、最少數量的公開測試 seam。只有新增 seam 時才需要使用者確認；既有且明確的 seam 直接採用並列證據。
4. 產生草稿，檢查每條 acceptance criterion 都能得到 pass/fail。
5. 預覽摘要、seams、out of scope 與 open questions。使用者確認後才發布或寫檔。

## 規格格式

```markdown
# <Title>

## Problem
從使用者角度描述目前成本與失敗狀態。

## Outcome
描述完成後可觀察到的行為，不描述實作步驟。

## User stories
1. As a <actor>, I want <behavior>, so that <benefit>.

## Acceptance criteria
- [ ] Given <state>, when <action>, then <observable result>.

## Implementation decisions
- 已確認的模組、interface、資料/API contract 與重要取捨；不要放易過期的檔案行號或完整 code。

## Testing decisions
- 測試 seams、層級、既有先例與必要 fixtures。

## Out of scope
- 明確不做的行為。

## Open questions
- 尚未決定且會改變實作的項目；沒有就寫 None。
```

本地 tracker 預設寫到 `.scratch/<feature>/spec.md`。外部 tracker 依 `docs/agents/project.md` 執行；建立前再次顯示標題與目的地。
