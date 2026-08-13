# Blueprint document template

The shape of `docs/test-blueprint.md` in the target project. Content in Traditional Chinese; identifiers and tier names in English. Every table row exists because step 2 derived it — an empty section stays present with a one-line reason rather than disappearing.

```markdown
# 測試藍圖

> 由 /test-blueprint 產生與修訂。手改條目視為藍圖失真 — 要改，走修訂提案。
> 本次核准：<日期>／來源：<spec 檔、story 清單>

## 層佈局

| 層 | 測什麼 | 誰落地 | CI 時段 |
| --- | --- | --- | --- |
| 靜態 | lint／format／型別 | scripts/check-*.sh（本藍圖產出） | presubmit |
| 單元 | 模組對其設計 | /tdd | presubmit |
| 整合 | 縫清單所列邊界 | /tdd | 受影響→presubmit；全套→merge |
| 驗收 | docs/uat-cases.md 全清單 | /uat-cases → /browser-evidence | 發佈前 |

## 縫清單

| 縫 | 服務的承諾 | 現況 |
| --- | --- | --- |
| OrderService ↔ PaymentGateway | spec §4.2 付款一致性 | 未測 |

## 追溯表

| 承諾 | 標題 | 層 | 時段 | 測試／案例 |
| --- | --- | --- | --- | --- |
| PR-AUTH-01 | 會員登入 | 驗收 | 發佈前 | TC-AUTH-01 |

## 缺口清單

- PR-RPT-01 匯出報表 — 無任何層覆蓋

## 未實作豁免清單

存量債的界線。列在這裡的承諾缺測試只軟報，不擋 merge；未列的一律硬擋。

**只減不增。** 移除一條走修訂提案；新增一條沒有合法途徑 — 新承諾缺測試就是擋下來的那一刻該補的東西。

| 承諾 | 缺的層 | 列入日期 |
| --- | --- | --- |
| PR-RPT-01 | 全部 | 2026-08-09 |

## CI 政策

- 時段：presubmit＝靜態全套＋單元＋受影響整合；merge＝完整套件；periodic＝（本專案無昂貴項，暫缺）
- flake：禁自動重試（預設）
- 覆蓋率：追溯覆蓋為完成定義；行覆蓋僅儀表，不設門檻
- 未實作門：新增硬擋、存量軟報，界線為上方豁免清單
- 現況報告：`docs/test-status.md`，CI 於 merge 後生成
- 證據保留：<留最近 N 次＋每次發佈一份，或「暫不設限」>；單 run 超過約 50MB 或 `docs/uat/` 累計超過約 1GB 時，改上 Git LFS
- 偏離預設：<無，或逐條列偏離＋理由>
```

承諾欄用凍結編號，不用 spec 章節號。章節號會隨改版漂走，整欄同時失真；凍結編號撐得過規格被重寫。編號沿用專案既有的需求編號體系（FR-／NFR-／SC-）；範例中的 `PR-` 是專案沒有體系時 `/to-spec` 發的預設，不是規範。
