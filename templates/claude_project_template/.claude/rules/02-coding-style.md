# 規則 2：Code 風格

> 給 Claude Code：寫 code 時遵守以下規範。

---

## 命名

- 變數、函式：用**英文小駝峰**（或語言慣例），但**有意義的全名**
  - ✅ `newsContent`、`summarizeNews()`
  - ❌ `nc`、`fn1`、`data`、`temp`
- 常數：全大寫加底線
  - ✅ `const MAX_LENGTH = 2000`
- **命名對齊 spec 的領域語言**：PRD 叫 "summary"，code 就別叫 "result"

## 註解

- 註解說明**「為什麼」**不是「做什麼」（code 本身已說明 what）
- 複雜邏輯 / 非顯而易見的決策前，寫一句說明背後取捨
- **對齊 spec**：關鍵實作標出對應哪個 user story / AC（例：`// 實作 US-001 AC-2：空輸入回傳友善錯誤`）
- 不要寫廢話註解（`// 設定變數` 之類的）

## 結構

- **依專案結構分層、單一職責**：不要把所有東西塞進一個檔
- 模組邊界對齊 spec 的領域劃分（`db-schema` / `api-contract` 怎麼切，code 就怎麼切）
- import 順序：標準庫 → 第三方 → 專案內部

## 錯誤處理

- 每個 I/O（fetch / DB / 檔案讀寫）都要處理失敗路徑
- **不要靜默吞錯**：log 或拋出有意義的錯誤，不要空 `catch {}`
- 錯誤路徑要能對應到測試——TDD 的失敗案例（empty input / timeout / 403）就是錯誤處理的 spec

範例：
```javascript
try {
  const result = await fetchSummary(content);
  return result;
} catch (err) {
  // 對應 test_summarize_with_api_error：失敗時拋出帶 context 的錯誤
  throw new SummarizeError(`摘要失敗：${err.message}`, { cause: err });
}
```

## Secret 處理（硬約束，違反 = 任務失敗）

- ❌ **絕不**把 API Key / token / 密碼寫死在 code
- ✅ 一律從環境變數讀（`process.env.X` / `os.environ["X"]`），`.env` 進 `.gitignore`
- ✅ 前端需要呼叫 LLM / 第三方 API → **走後端 proxy**，金鑰只存後端，不進前端 bundle
- ✅ commit 前必跑 `/sec-scan` 掃描（見 `skills/sec-scan.md`）

## 面向使用者的文案

- 如專案有 UI：使用者看得到的文字（按鈕、提示、錯誤訊息）用**繁體中文**
- 程式內部（log、變數名、commit message type、測試名）用**英文慣例**
