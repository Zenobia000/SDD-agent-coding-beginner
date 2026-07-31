# PRD — rate-digest

> 對照重點：**七個欄位的結構**，以及「Constraints 裡沒有一句 Model Rule」。

---

## 1. Role

匯率資料抓取與摘要引擎。

## 2. Goal

每個工作日 09:00 前，從三個指定來源取得當日匯率，產出一份含現價、
日變動、月均差的文字摘要。

## 3. Inputs

| 輸入 | 型別 | 來源 |
|---|---|---|
| `sources` | 三個固定 URL | 設定檔（寫死，不接受外部指定） |
| `currencies` | `["USD", "JPY", "EUR"]` | 設定檔 |
| `history` | 過去 30 天的匯率 | 本地 SQLite |
| `run_date` | ISO 日期 | 執行時的系統日期（可注入，供測試用） |

## 4. Constraints

**全部都是 Business Rule。沒有一句是「怕它出錯」的叮嚀。**

- 只接受設定檔中的三個來源，**不接受執行期傳入的 URL**
- 匯率一律保留小數點後 4 位，**無條件捨去**（不四捨五入）
- 任一來源失敗時，其餘照常輸出，並在 `missing_sources` 欄位列出缺哪個
- 三個來源**全部**失敗時，**不寫入資料庫**，保留上一版並回傳失敗
- 單次執行對每個來源最多重試 **3 次**，間隔 2 秒
- 抓取逾時 **10 秒**

> **對照重點**：這裡看不到「請仔細檢查」「請確保數字正確」「請不要遺漏」。
> 那些是 Model Rule，會變成模型必須服從的雜訊，且無法驗證。

## 5. Output format

```json
{
  "run_date": "2026-07-31",
  "generated_at": "2026-07-31T08:52:14Z",
  "rates": [
    {
      "currency": "USD",
      "rate": 31.2450,
      "delta_1d": -0.0320,
      "delta_month_avg": 0.1180,
      "source": "bank-a"
    }
  ],
  "missing_sources": [],
  "summary": "今日美元 31.2450，較昨日下跌 0.0320..."
}
```

**約束層級**：用 schema 驗證（第 3 層），不是在 prompt 裡拜託它回 JSON。

## 6. Success criteria ★

**直接拿去當考卷。** 見 [`eval-set.md`](./eval-set.md)。

| # | 條件 | 裁判 |
|---|---|---|
| C1 | 輸出通過 schema 驗證，`rates` 陣列非空 | 程式 |
| C2 | 每個 `rate` 與該來源網頁顯示值誤差 < 0.01 | 程式 |
| C3 | 任一來源失敗時，`missing_sources` 列出它，其餘 rate 照常 | 程式 |
| C4 | 三來源全失敗時**不寫入 DB**，回傳失敗 | 程式 |
| C5 | `generated_at` 早於當日 09:00 | 程式 |
| C6 | 每個 `rate` 的三個數值欄位都非空 | 程式 |

## 7. Examples

**只是對格式，不是教推理。**

正常情況 → 上方 Output format 的範例。

一個來源掛掉：
```json
{
  "rates": [ { "currency": "USD", "rate": 31.2450, "source": "bank-b" } ],
  "missing_sources": ["bank-a"],
  "summary": "今日美元 31.2450...（註：bank-a 來源今日無法取得）"
}
```

---

## 自我檢查

| 問題 | 這份的答案 |
|---|---|
| 七欄位都非空？ | ✅ |
| Constraints 裡有 Model Rule 嗎？ | ❌ 沒有（這是對的） |
| Success criteria 能直接當考卷？ | ✅ 六條全是程式判準 |
| Examples 是對格式還是教推理？ | ✅ 對格式 |
