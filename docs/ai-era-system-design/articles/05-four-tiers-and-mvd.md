# 05 — 四級系統與最小可行文件集

> 重點：「簡單架構圖就開工」對不對，取決於你在做哪一級系統。
> POC、MVP、Product、Enterprise 對文件與治理的要求差很多。
> 把 POC 當正式系統上線，是最常見的災難。

---

## 四級系統

| 等級 | 要證明什麼 | 簡單架構圖夠嗎 |
|------|------------|----------------|
| POC | 技術可行 | 夠 |
| MVP Demo | 有沒有價值 | 勉強夠，要補主流程與資料 |
| Product | 可持續使用 | 不夠 |
| Enterprise | 可治理、可維運、可擴充 | 絕對不夠 |

金流、醫療、製造、ERP、長期維運系統，全部落在「不夠」這一側。所以重點不是「能不能先開發」，而是**先搞清楚自己在做哪一級**。這四級不能混在一起。

---

## 最小可行文件集（MVD）

不需要一開始全部完整，但每一份至少要有第一版。回到沒有 AI 的年代，一個產品專案最少需要這 7 份：

| # | 文件 | 用途 | 沒有會怎樣 |
|---|------|------|------------|
| 1 | Problem Statement | 定義為什麼做 | 做出沒人要的東西 |
| 2 | User / Business Flow | 定義流程 | 系統流程混亂 |
| 3 | Scope / Non-scope | 定義邊界 | 需求無限膨脹 |
| 4 | Architecture Diagram | 定義系統組成 | 工程師各做各的 |
| 5 | Data Model / ERD | 定義資料關係 | DB 後期難改 |
| 6 | API Contract | 定義介面 | 前後端整合爆炸 |
| 7 | Test Scenario | 定義驗收 | 上線前才發現不符 |

> Minimum Viable Documentation 的精神：不是文件越多越好，而是每個關鍵維度都有第一版，且能持續演化。

完整的 SOP 與模板，以及它如何對應本 repo 的三層 Spec，見 [process/01](../process/01-minimum-viable-documentation.md)。

---

## 沒有 AI 時，文件不完整怎麼補救

這四個手法在 AI 之前就有效，AI 時代依然有效，只是 AI 能大幅加速。

### 1. 用會議補需求

固定 Review：這週新增哪些需求、哪些規則還不清楚、哪些 API 要改、哪些決策已確認，最後形成 Decision Log。

### 2. 用 Prototype 逼出需求

使用者常常講不清楚，但看到畫面就很會講。Wireframe、Mockup、可點擊原型甚至 Excel 假畫面的目的不是設計漂亮 UI，而是逼使用者回應「這是不是你要的、這欄位要不要、這按鈕誰可以按」。

> Prototype 是拿來吵架的，吵完需求就清楚了。

### 3. 用資料表反推規則

看到一張訂單表就能反推流程：

```
order_id, customer_id, status, total_amount,
created_at, approved_by, shipped_at, cancelled_at
```

問題自然浮出：`status` 有哪些狀態？`approved_by` 何時出現？`cancelled_at` 出現後還能修改嗎？`total_amount` 是人工輸入還是系統計算？

### 4. 用測試案例當活文件

需求文件寫不清楚時，測試案例反而清楚（BDD 精神）：

```
Given 訂單已出貨
When 使用者點擊取消訂單
Then 系統顯示「已出貨訂單不可取消」
```

這對應本 repo 的 L3 BDD scenarios 與 `/tdd-cycle`。文件會過期，但被執行的測試案例不會說謊。

---

## 銜接

到這裡，傳統工程的脈絡講完了。AI 沒有打掉這套流程，而是把它升級。下一篇是整個文件集的核心轉折。

→ [06 — AI 時代：Human Gate + AI Factory](06-ai-era-human-gate-ai-factory.md)
