# BDD Scenarios Template

> **Layer 3 spec（行為層）— 系統行為的可執行規格**
> 大廠對標：**Gherkin language**（Cucumber / Behave / SpecFlow 通用語法）
> 寫作時機：每個 user story 至少 1 個 scenario。**先寫情境、後寫實作**。
> 副檔名：`.feature`（讓 IDE 自動 syntax highlight）

---

## 為什麼用 BDD？

**TDD 解決「程式對不對」，BDD 解決「我們做的是正確的東西嗎」。**

Gherkin scenario 是 **使用者語言 + 工程師可執行** 的雙重格式：
- 產品 / 設計師看得懂（自然語言）
- AI / 測試框架可直接執行（語法穩定）

對 Solo dev：BDD 是「給 6 個月後的自己看的需求文件」，比註解更可信。

---

## Gherkin 標準語法

```gherkin
Feature: <功能名稱>
  As a <角色>
  I want <能力>
  So that <價值>

  Background:
    Given <每個 scenario 共用的前置>

  Scenario: <情境名稱>
    Given <前置條件>
    And <額外前置>
    When <觸發動作>
    Then <預期結果>
    And <額外驗證>

  Scenario Outline: <參數化情境>
    Given <前置 with <param>>
    When <動作>
    Then <結果 with <expected>>

    Examples:
      | param | expected |
      | a     | 1        |
      | b     | 2        |
```

**5 個關鍵字的角色：**

| Keyword | 用法 | 範例 |
|---|---|---|
| `Given` | 前置狀態 | `Given 我有一篇 500 字英文文章` |
| `When` | 觸發行為 | `When 我點擊「摘要」按鈕` |
| `Then` | 預期結果 | `Then 3 秒內顯示中文摘要` |
| `And` | 接續上個關鍵字 | `And 字數在 80-120 之間` |
| `But` | 接續但反向 | `But 不應該顯示原文` |

---

## 完整範例

```gherkin
# tests/features/summarize.feature

Feature: 英文新聞摘要
  As a 想快速看新聞的上班族
  I want 貼一篇英文文章後得到 100 字中文摘要
  So that 我能在 30 分鐘內掃完 20 篇新聞

  Background:
    Given 我已開啟摘要工具頁面
    And 我已輸入有效的 Gemini API Key

  Scenario: 主流程 — 成功摘要 500 字英文
    Given 我貼上一篇 500 字的英文新聞
    When 我點擊「摘要」按鈕
    Then 3 秒內顯示中文摘要
    And 摘要字數在 80-120 字之間
    And 摘要保留原文的主要事件、人物、時間

  Scenario: 邊界 — 文章太短
    Given 我貼上一篇 50 字的英文文章
    When 我點擊「摘要」按鈕
    Then 顯示錯誤訊息「文章太短，請貼 100 字以上」
    And 不應該呼叫 Gemini API

  Scenario: 邊界 — 文章太長
    Given 我貼上一篇 15000 字的英文文章
    When 我點擊「摘要」按鈕
    Then 顯示錯誤訊息「文章太長，請貼 10000 字以內」

  Scenario: 邊界 — 非英文內容
    Given 我貼上一篇中文文章
    When 我點擊「摘要」按鈕
    Then 顯示錯誤訊息「請貼英文文章」

  Scenario: 失敗 — API Key 無效
    Given 我輸入無效的 API Key
    When 我嘗試摘要任何文章
    Then 顯示錯誤訊息「API Key 無效，請檢查」
    And 不會洩漏 API Key 的具體內容

  Scenario: 失敗 — API 服務中斷
    Given Gemini API 回傳 503
    When 我點擊「摘要」按鈕
    Then 顯示錯誤訊息「服務暫時無法使用，請稍後再試」
    And 我輸入的原文保留在輸入框

  Scenario Outline: 多種語言輸出
    Given 我選擇輸出語言為 <language>
    And 我貼上一篇 500 字英文新聞
    When 我點擊「摘要」按鈕
    Then 摘要應該是 <language> 語言

    Examples:
      | language |
      | 繁體中文   |
      | 簡體中文   |
      | 日文      |
```

---

## Scenario 設計原則（採 Cucumber 官方建議）

### 1. 一個 Scenario 一個 behaviour

❌ **混和多種行為**：
```gherkin
Scenario: 摘要 + 翻譯 + 儲存
```

✅ **拆成 3 個 scenario**：
```gherkin
Scenario: 摘要成功
Scenario: 翻譯成功
Scenario: 儲存成功
```

### 2. 用業務語言、不用技術語言

❌ **技術語言**：
```gherkin
When I send a POST request to /api/summarize with content="..."
Then the HTTP response status should be 200
```

✅ **業務語言**：
```gherkin
When 我點擊「摘要」按鈕
Then 我看到中文摘要顯示
```

API 層的測試另外用 contract test 寫，不混在 BDD 裡。

### 3. Given-When-Then 各只用一次（多用 And）

❌
```gherkin
Given 我有 A
Given 我有 B
When 我做 C
When 我做 D
```

✅
```gherkin
Given 我有 A
And 我有 B
When 我做 C
And 我做 D
```

### 4. 每個 feature file 對應一個 user story

```
tests/features/
├── summarize.feature        ← US-001 摘要功能
├── batch-summarize.feature  ← US-002 批次摘要
├── history.feature          ← US-003 歷史記錄
```

---

## Tag 系統（採 Cucumber 慣例）

```gherkin
@smoke @critical
Scenario: 主流程
  ...

@edge-case @slow
Scenario: 邊界
  ...

@wip
Scenario: 還沒做完的
  ...
```

執行時：

```bash
# 只跑 smoke test
behave --tags=@smoke

# 跳過 work-in-progress
behave --tags=~@wip
```

---

## 寫作檢查清單

- [ ] 每個 Feature 都有 As-I-So-that 三行
- [ ] 每個 user story 至少 1 個主流程 scenario
- [ ] 主流程之外至少 2 個邊界 scenario（短 / 長 / 異常輸入）
- [ ] 至少 1 個失敗 scenario（API 掛 / 網路斷）
- [ ] 用業務語言、不出現 HTTP / SQL 字眼
- [ ] 每個 Scenario 只測試一個行為
- [ ] 對應的 user story ID 寫在 feature file 開頭註解
- [ ] 對應的 API endpoint 寫在 feature file 開頭註解
