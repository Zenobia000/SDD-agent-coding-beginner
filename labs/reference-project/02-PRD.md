# PRD — SmartTrip FX

> [`BUILD.md`](../../BUILD.md) 第 2 步的參考答案。
> **對照重點：Constraints 裡沒有一句是「怕它出錯」的叮嚀。**

---

## 1. Role

行程生成與換匯量計算引擎。

## 2. Goal

使用者輸入目的地、日期、預算後，產出一份行程，並算出「建議攜帶的當地現金金額」
與「現在換匯划不划算」。

## 3. Inputs

| 輸入 | 型別 | 來源 | 沒有時 |
|---|---|---|---|
| `destination` | 列舉（MVP 只有 `kansai`） | 使用者 | 必填 |
| `start_date` / `end_date` | ISO 日期 | 使用者 | 必填 |
| `budget_twd` | 整數（新台幣元） | 使用者 | 必填 |
| `fx_history` | 過去 30 天匯率 | 匯率 API + 本地快取 | 燈號顯示「暫無資料」，**不影響換匯金額計算** |

## 4. Constraints

全部是業務規則。**沒有一句是叮嚀。**

- 只支援 `destination = kansai`，貨幣固定 JPY
- 金額一律用**整數存最小單位**（日圓存円、台幣存元），不使用浮點數
- 預備金係數 **1.1**，寫成具名常數，不散落在程式各處
- 建議換匯額 = `(sum(cash_only) + sum(unknown)) × 1.1`
  —— **`unknown` 保守計入現金側**
- 換匯燈號只比較「今日匯率 vs 過去 30 日均線」，**不做任何預測**
- 燈號畫面必須顯示「本資訊非投資理財建議」（法規要求）
- 行程總金額超出 `budget_twd` 的 ±20% 時，回傳警告欄位而非重新生成
- 單次生成對 LLM 最多重試 **2 次**，失敗回上一次結果
- 任一外部 API 失敗不得中斷其餘功能

> **對照**：這裡看不到「請仔細檢查金額」「請確保分類正確」。
> 那些無法驗證，而且是模型必須服從的雜訊——它們的位置在考卷，不在 spec。

## 5. Output format

```json
{
  "itinerary": [
    {
      "day": 1,
      "name": "伏見稻荷大社",
      "amount": 0,
      "currency": "JPY",
      "payment": "cash_only",
      "note": "參拜免費，御守與繪馬需現金"
    }
  ],
  "cash_recommendation": {
    "subtotal_jpy": 48200,
    "unknown_jpy": 3500,
    "reserve_ratio": 1.1,
    "total_jpy": 56870
  },
  "fx_signal": {
    "today": 0.2043,
    "ma30": 0.2071,
    "verdict": "BUY",
    "basis": "今日匯率低於 30 日均線 1.35%",
    "disclaimer": "本資訊非投資理財建議"
  },
  "budget_check": { "estimated_twd": 38400, "budget_twd": 40000, "status": "ok" },
  "degraded": []
}
```

`degraded` 列出這次哪些外部依賴失效（例：`["fx_api"]`），前端據此標示。

**約束層級**：用 schema 驗證，不是在 prompt 裡拜託它回 JSON。

## 6. Success criteria ★

直接拿去當考卷 → [`04-evals.md`](./04-evals.md)。

| # | 條件 | 裁判 |
|---|---|---|
| C1 | 輸出通過 schema 驗證 | schema |
| C2 | 每個項目的 `payment` 都在三個允許值內 | 程式 |
| C3 | `total_jpy` == `(subtotal + unknown) × 1.1`，無條件捨去到整数 | 程式 |
| C4 | `fx_signal.verdict` 與 today/ma30 的關係一致 | 程式 |
| C5 | 匯率 API 失效時，`cash_recommendation` 仍算得出來 | 程式 |
| C6 | 明顯只收現金的項目未被標成 `card_ok` | 程式（負例清單） |
| C7 | `estimated_twd` 超出預算 ±20% 時 `status` 為 `warn` | 程式 |
| C8 | 燈號輸出必含免責聲明字串 | 程式 |

> **八條裡有七條是程式判的。** 這是第 3 步那條線畫對了的直接結果——
> 可驗證的部分越多，你需要靠考卷賭運氣的地方越少。

## 7. Examples

**對格式，不是教推理。**

外部依賴失效時：
```json
{
  "itinerary": [ ... ],
  "cash_recommendation": { "total_jpy": 56870, ... },
  "fx_signal": null,
  "degraded": ["fx_api"]
}
```

---

## 自我檢查

| 問題 | 這份的答案 |
|---|---|
| 七欄位都非空？ | ✅ |
| Constraints 有 Model Rule 嗎？ | ❌ 沒有 |
| Success criteria 能直接當考卷？ | ✅ 八條，七條程式判 |
| 有沒有把法規寫進去？ | ✅ 免責聲明是 C8 |
| 外部依賴失效的行為定義了嗎？ | ✅ `degraded` 欄位 + C5 |
