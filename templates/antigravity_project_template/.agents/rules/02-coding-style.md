# 規則 2：Code 風格

> 給 Antigravity Agent：寫 code 時遵守以下規範。

---

## 命名

- 變數、函式：用**英文小駝峰**，但**有意義的全名**
  - ✅ `newsContent`、`summarizeNews()`
  - ❌ `nc`、`fn1`、`data`、`temp`
- 常數：全大寫加底線
  - ✅ `const API_KEY = "..."`、`const MAX_LENGTH = 2000`

## 註解

- **每個函式上方一行中文註解**說明它在做什麼
- 複雜邏輯（超過 5 行）前面寫一句中文說明
- 不要寫廢話註解（`// 設定變數` 之類的）

範例：
```javascript
// 把使用者貼的新聞傳給 Gemini，回傳三點摘要
async function summarizeNews(content) {
  // ...
}
```

## 結構

- HTML / CSS / JS 全寫在 `index.html` 裡（用 `<style>` 和 `<script>` 標籤）
- JS 區塊順序：常數 → 工具函式 → 主邏輯 → 事件綁定
- 同類功能放一起，不要散落

## 錯誤處理

- **每個 `fetch` 都要有 `try/catch`**
- 錯誤訊息**用繁體中文**顯示在畫面上（不要只 `console.log`）
- API Key 沒填時要明確提示「請先在 code 開頭填入你的 API Key」

範例：
```javascript
try {
  const result = await fetch(...);
  // ...
} catch (err) {
  resultArea.textContent = "出錯了：" + err.message + "（請檢查網路或 API Key）";
}
```

## API Key 處理

- 一定放在檔案最上方：
  ```javascript
  // ⚠️ 把下面的字串換成你自己的 Gemini API Key
  // 申請網址：https://aistudio.google.com/apikey
  const API_KEY = "請貼上你的金鑰";
  ```
- 如果 `API_KEY === "請貼上你的金鑰"`，按按鈕時要 `alert("請先在 code 開頭填入 API Key")`

## 給使用者的訊息

- 所有 `alert()`、畫面上的文字、按鈕標籤 → **繁體中文**
- 不要用「Submit」、「Loading...」這種英文，用「送出」、「處理中…」
