# Process 04 — Human Gate 與 AI Agent 角色

> 目的：定義人類在哪裡守關、AI 用什麼角色產出、產出如何排隊審查。
> 原則：AI Factory 大量產出，Human Gate 控制風險，Review Queue 防止 AI 變雜訊製造機。

---

## 六道 Human Gate

每道 Gate 只問一個關鍵問題。沒通過，不進下一步。

| Gate | 關鍵問題 | 把關角色 |
|------|----------|----------|
| Scope Gate | 範圍是否清楚？砍了哪些、保留哪些？ | PM |
| Flow Gate | 主流程是否跑得通？ | SA / PM |
| Data Gate | 資料來源與狀態是否清楚？source of truth 是誰？ | SA / DBA |
| Architecture Gate | 技術方案是否可維運？團隊撐得住嗎？ | Architect |
| Test Gate | 驗收條件是否明確？P0/P1/P2 分好了嗎？ | QA |
| Launch Gate | 上線風險是否可接受？Go / No-Go | Tech Lead / SRE |

高風險決策（Scope 取捨、架構拍板、資安接受、上線決策）必須在 Gate 由人類承擔，不可由 AI 代行（見 [articles/06](../articles/06-ai-era-human-gate-ai-factory.md) 的工作分級）。

---

## AI Agent 角色分工

大型系統不要讓一個 AI 什麼都做，角色化更穩。注意：所有 Agent 都是 assistant，不是 decision maker。

| Agent | 任務 | 輸出 |
|-------|------|------|
| Requirement Analyst | 展開需求與 Open Questions | User Story、需求卡 |
| Process Analyst | 梳理流程與例外 | Flow、State Machine |
| Architect Assistant | 產架構候選與風險 | 決策矩陣、ADR 草稿 |
| Data Analyst | 推導資料模型 | Entity、ERD、Data Dictionary |
| API Designer | 產 API 草稿 | OpenAPI、Request/Response |
| QA Assistant | 產測試案例 | GWT、Test Matrix |
| Security Reviewer | 檢查權限與風險 | Threat List、Control Checklist |
| Dev Assistant | 產程式骨架 | Code Skeleton、Unit Test |
| Documentation Curator | 整理正式文件 | Summary、Diff、Traceability |

這對應本 repo 的 [`.agents/SUBAGENTS.md`](../../../templates/antigravity_project_template/.agents/SUBAGENTS.md)：把工作拆給專職 subagent，比一個 agent 全包更可控。

---

## Review Queue

所有 AI 產出先進 Queue，人類審查後才成為正式 artifact：

```
AI Draft → Review Queue → Human Review → Approved Artifact
```

每個項目的欄位：

| 欄位 | 說明 |
|------|------|
| artifact_id | 文件或產出編號 |
| type | requirement / architecture / test / code |
| generated_by | 哪個 AI agent |
| risk_level | low / medium / high |
| reviewer | 誰審 |
| status | draft / approved / rejected |
| decision | 採用 / 不採用 / 修改後採用 |
| reason | 為什麼 |

`risk_level` 決定審查強度：low 抽查、medium 必審、high 必須人類決策並留 reason。

---

## 落地對照

| 本文件概念 | repo 對應 |
|------------|-----------|
| 六道 Gate | [`.agents/WORKFLOW.md`](../../../templates/antigravity_project_template/.agents/WORKFLOW.md) 十站 sprint 的檢查點 |
| Agent 分工 | [`.agents/SUBAGENTS.md`](../../../templates/antigravity_project_template/.agents/SUBAGENTS.md) |
| 草稿 / 正式分區 | [process/02](02-ai-collaboration-sop.md) 的目錄約定 |
| status 欄位 | [process/01](01-minimum-viable-documentation.md) 的文件狀態約定 |

---

## 收束

至此，從「沒有 AI 的年代如何開始」到「AI 時代如何治理」的完整脈絡與可執行流程都已就緒。回索引：[README](../README.md)。
