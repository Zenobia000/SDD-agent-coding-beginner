# 03 — 逐層收斂取代完整 top-down

> 重點：成熟團隊不幻想一開始定義完整系統，而是用一種務實的流程一圈一圈收斂。
> 像雕刻：先切大輪廓，再修細節，不是一刀就成型。

---

## 收斂流程

```
模糊需求
  ↓
核心場景
  ↓
主流程
  ↓
系統邊界
  ↓
資料模型
  ↓
API / 模組切分
  ↓
例外情境
  ↓
測試案例
  ↓
文件補齊
```

這不是一次做完，而是分多輪逐步逼近。每一輪都讓「要做什麼」更清楚一點。AI 時代把這個收斂流程升級成「AI 發散、人類收斂」的五輪工作流（見 [process/02](../process/02-ai-collaboration-sop.md)）。

---

## 四種起手式

收斂的第一步是選一個入口。常見有四種，沒有對錯，只有適不適合。

| 起手式 | 從哪裡開始 | 最適合 | 風險 / 限制 |
|--------|------------|--------|-------------|
| Business Flow | 畫業務流程（誰做什麼、順序如何） | 流程驅動的系統（審批、訂單、工單） | 容易忽略資料關係與例外 |
| User Story | `As a 角色, I want 動作, so that 價值` | 敏捷團隊、功能導向產品 | 故事拆太碎會看不見全貌 |
| Data Model | 先抓核心名詞與關係（ERD） | 企業後台（ERP / MES / CRM / 報表） | 太早設表會綁死，難改 |
| Architecture | 先畫系統元件與依賴 | 整合型系統、跨多個外部服務 | 只畫方塊不畫互動等於沒定義 |

### Business Flow 範例

```
使用者提出申請 → 主管審核 → 系統檢查資料
  → 產生單號 → 通知相關人員 → 寫入 ERP → 完成結案
```

先知道「事情怎麼發生」，再決定「系統怎麼實作」。很多系統爛掉，就是直接設表、開 API，卻沒搞懂業務流程。

### Data Model 範例

抓出 `Customer / Order / OrderItem / Product / Inventory / Invoice / Payment / Shipment`，然後逼問關係：一個 Customer 幾張 Order？Payment 可以分期嗎？Shipment 可以部分出貨嗎？企業系統的靈魂就是資料關係。

### Architecture 起手式的陷阱

只畫三個方塊不夠：

```
Frontend → Backend API → Database
                  ↘ ERP / Third-party
```

這只說明「系統大概長怎樣」，沒說明「系統怎麼跑」。成熟的做法會補一句責任邊界，例如「Backend Service 負責權限、商業規則、資料轉換與 API 整合」，並補上 Sequence Diagram、API Contract、Permission Matrix。

---

## 對應到 Vibe Engineering

這四種起手式最終都收斂到本 repo 的三層 Spec：

- Business Flow / User Story → **L1 PRD**（誰、為什麼、做什麼）
- Architecture / Data Model → **L2 API contract + 資料模型**
- 例外情境 / 測試案例 → **L3 BDD scenarios**

`/spec-it` skill（[`.agents/skills/spec-it`](../../../templates/antigravity_project_template/.agents/skills/spec-it/)）就是把這個收斂過程一次產出三層。

---

## 銜接

收斂流程說明「怎麼一步步把系統定義清楚」。但真正讓專案翻車的，往往不是收斂得不夠快，而是**收斂過程沒有治理**。

→ [04 — 不完整不可怕，沒治理才可怕](04-incompleteness-vs-governance.md)
