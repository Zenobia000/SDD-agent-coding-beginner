# Process 03 — 結構化產出模板與可追溯性

> 目的：給 AI 一組固定的輸出結構，讓它產的不是散文，而是可審查、可收斂、可追溯的結構化資料。
> 原則：讓 AI 進入 Schema 與表格，人類才好檢查。

---

## 1. 需求 Schema（User Story）

```yaml
id: US-001
title: 訂單狀態查詢
as_a: 業務主管
i_want: 查看部門的客戶訂單狀態
so_that: 減少人工詢問 ERP 與客服往返
priority: P0
assumptions:
  - 使用者帳號來自公司 AD
  - 訂單狀態以 ERP 為 source of truth
acceptance_criteria:
  - Given 使用者已登入 When 查詢有效訂單 Then 顯示訂單狀態
  - Given 使用者無權限 When 查詢訂單 Then 顯示權限不足
status: draft
owner: PM
reviewer: SA
```

`acceptance_criteria` 直接對應 L3 BDD scenarios 與 `/tdd-cycle` 的測試。

---

## 2. ADR Schema（架構決策）

對接本 repo 的 [`.agents/skills/adr`](../../../.claude/skills/spec/)（MADR 風格）：

```yaml
adr_id: ADR-0001
title: 後端採用 Modular Monolith
context:
  - 團隊規模 < 8 人
  - 模組邊界仍可能變動
  - 無專職 SRE 團隊
decision: Phase 1 採用 Modular Monolith，不採用 Microservices
options:
  - name: Modular Monolith
    pros: [部署簡單, 模組邊界可調, 維運成本低]
    cons: [未來拆分需規劃]
  - name: Microservices
    pros: [獨立部署, 擴展彈性]
    cons: [維運複雜, 需成熟 DevOps]
decision_reason: 當前階段重視交付速度與維運穩定
consequences:
  - 需定義清楚模組邊界
  - 未來依 bounded context 拆分
status: approved
owner: Architect
```

> AI 可以起草 ADR，但 `decision` 一定要人類確認。

---

## 3. 技術選型決策矩陣

不要問 AI「選最好的」，讓它產這張表，人類拍板：

| 方案 | 適用條件 | 優點 | 風險 | 組織適配度 | 建議 |
|------|----------|------|------|-----------|------|
| Modular Monolith + PostgreSQL | 初期產品、團隊小 | 快、簡單、好維運 | 未來需拆分 | 高 | 優先 |
| Microservices + Kafka | 多團隊、高吞吐事件 | 解耦、擴展性好 | 維運成本高 | 中低 | 延後 |
| Serverless | 流量不穩、事件驅動 | 部署快、彈性 | Vendor lock-in | 中 | 特定模組 |

選型要看：團隊能力、維運能力、公司標準、整合需求、資料規模、可靠性（SLA/RTO/RPO）、成本、安全、可替換性。

---

## 4. 假設清單

AI 每次產出都附假設，人類逐條標記：

```markdown
## Assumptions
- [confirmed] 使用者帳號來自公司 AD
- [pending]   ERP API 支援即時查詢
- [rejected]  MVP 需支援訂單修改
- [confirmed] 訂單狀態由 ERP 作為 source of truth
```

---

## 5. Traceability Matrix

可追溯鏈是大型系統最重要的資產。AI 最適合維護這張容易漏的表：

| Requirement | Flow | API | DB | Test Case |
|-------------|------|-----|----|-----------|
| US-001 訂單查詢 | FLOW-001 | `GET /orders/{id}` | orders, audit_logs | TC-001, TC-002 |
| US-002 匯出報表 | FLOW-002 | `POST /reports/export` | report_jobs | TC-010 |
| US-003 權限控管 | FLOW-003 | `GET /permissions` | users, roles | TC-020 |

每個需求都能往下追到 API、資料表、測試案例，反向也能從一個欄位追回它服務的需求。

---

## 相關

- 這些產出如何在五輪中被產生與收斂 → [process/02](02-ai-collaboration-sop.md)
- 它們在哪一道 Gate 被檢查 → [process/04](04-human-gate-and-agent-roles.md)
