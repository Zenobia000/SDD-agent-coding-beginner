# 裝積木踩到的坑 — rate-digest

> 對照重點：**你有沒有記錄踩到什麼**。這份未來會變成你的 `known-issues.md`。

---

## 考卷有沒有退步

| 階段 | 通過率 |
|---|---|
| S4 收工 | 10 / 10 |
| 裝完 db | 8 / 10 ← **掉了** |
| 修完 | 10 / 10 |
| 裝完 etl | 10 / 10 |

**中間掉分是正常的。** 重點是修回來，而且知道為什麼掉。

---

## 坑 1：裝 db 之後 #7、#8 掛了

**症狀**：冷啟動與資料不足那兩題失敗。

**根因**：積木的 schema 把 `delta_1d` 設成 `NOT NULL`，
但 PRD 明寫「首次執行時 `delta_1d` 為 null」。

**修法**：
```sql
-- migrations/002_fix_delta_nullable.sql
ALTER TABLE rates RENAME TO rates_old;
CREATE TABLE rates (
  run_date   TEXT NOT NULL,
  currency   TEXT NOT NULL,
  rate       INTEGER NOT NULL,      -- 存最小單位，不用浮點數
  delta_1d   INTEGER,               -- ← 可空：首次執行沒有昨日
  source     TEXT NOT NULL,
  created_at TEXT NOT NULL,
  UNIQUE(run_date, currency)
);
INSERT INTO rates SELECT * FROM rates_old;
DROP TABLE rates_old;
```

**學到的**：積木的預設是「關鍵欄位一律 NOT NULL」——
這個預設是對的，但**你的 spec 說了算**。
積木是起點，不是規定。

---

## 坑 2：金額用整數存，但我一開始沒改對

積木說「金額用整數存最小單位，不用浮點數」。
匯率 31.2450 → 存成 `312450`（放大 10000 倍）。

**我第一次改的時候只改了寫入，沒改讀出**，
結果摘要顯示「今日美元 312450.0000」。

**修法**：把轉換集中到一個地方
```python
SCALE = 10_000
def to_storage(rate: float) -> int:  return math.floor(rate * SCALE)
def from_storage(v: int) -> float:   return v / SCALE
```

**學到的**：**單位轉換一定要集中在一個地方**。
散在各處遲早會有一邊忘了轉。

---

## 坑 3：etl 的 Validate 一開始擋太兇

第一次跑，Validate 的「筆數變動 > 50% 要人確認」直接擋下 ——
因為前一天沒資料，0 → 3 筆是無限大的變動。

**修法**：
```python
# 前一批為空時跳過筆數比對
if prev_count > 0 and abs(count - prev_count) / prev_count > 0.5:
    return Fail("筆數變動超過 50%")
```

**學到的**：**冷啟動是所有驗證邏輯的共同盲點**。
寫任何「跟上次比」的檢查時，先想「沒有上次的時候呢」。

---

## 兩塊積木的接點

最後長這樣：

```python
# src/pipeline.py
def run(run_date: date) -> Result:
    raw       = extract(SOURCES)          # etl 積木
    normed    = transform(raw)            # etl 積木
    verdict   = validate(normed, prev=db.latest())   # etl 積木 ★
    if not verdict.ok:
        return Result.failed(verdict.reason)         # ← 不進 Load
    db.upsert(normed)                     # db 積木
    return Result.ok(normed)
```

**那一行 `if not verdict.ok: return` 就是接點。**
它是「自動產生髒資料機」和「可信管線」的唯一差別。

---

## 回填到 known-issues.md

| 問題 | 狀態 |
|---|---|
| 冷啟動時筆數驗證會誤擋 | ✅ 已修（跳過 prev_count = 0） |
| 單位轉換散落各處 | ✅ 已修（集中到 to_storage / from_storage） |
| migration 沒有 rollback script | ⚠️ 未修 —— 記進 `docs/OPS.md` 的「不可回滾操作」 |
