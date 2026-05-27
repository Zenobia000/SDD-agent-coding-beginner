# User Story — INVEST Format

> **Layer 1 spec（意圖層）— PRD 的子單位**
> 大廠對標：Atlassian Story Format（Bill Wake INVEST 原則）
> 寫作時機：拆 backlog 時，每張卡片就是一個 user story。

---

## 標準格式

```
[US-XXX] [一句話標題]

As a       [角色 / persona]
I want     [行為 / 能力]
So that    [得到的價值 / 痛點被解掉]

Acceptance Criteria（驗收條件，用 Given-When-Then）：
- [ ] Given [前置條件], When [動作], Then [結果]
- [ ] Given [前置條件], When [動作], Then [結果]

Priority: P0 / P1 / P2
Size:     XS / S / M / L / XL
Status:   Todo / In-Progress / Review / Done
```

---

## INVEST 原則

每張 story 寫完後，逐條檢查：

| 字母 | 原則 | 自問 |
|---|---|---|
| **I** | Independent | 不需要等別張 story 就能開做嗎？ |
| **N** | Negotiable | 還有討論空間嗎？（不是聖旨） |
| **V** | Valuable | 對使用者有可感知的價值嗎？ |
| **E** | Estimable | 你能說出大概要花多久嗎？ |
| **S** | Small | 一個 sprint 內能完成嗎？（Solo: 1-3 天） |
| **T** | Testable | 你能寫出明確的驗收條件嗎？ |

**任一條不過 → 拆 / 重寫**。

---

## Size 換算（Solo 一人版）

| Size | 估時 | 適合什麼 |
|---|---|---|
| XS | < 2 小時 | 改文字、調樣式、加按鈕 |
| S | 半天 | 一個小元件、一個 API 端點 |
| M | 1 天 | 一個完整 feature 含測試 |
| L | 2-3 天 | 跨模組功能，需要先設計 |
| XL | > 3 天 | **過大，必須拆**（拆到 M 以下） |

---

## 範例

```
[US-001] 使用者貼上英文新聞，點按鈕得到 100 字中文摘要

As a       想快速看英文新聞的上班族
I want     貼一篇英文文章後點一下，就拿到 100 字中文摘要
So that    我能在 30 分鐘內掃完 20 篇新聞而不是 3 篇

Acceptance Criteria：
- [ ] Given 我貼了一篇 500 字的英文文章, When 我點「摘要」, Then 3 秒內顯示中文摘要
- [ ] Given 摘要產出, When 我數字數, Then 字數在 80-120 字之間
- [ ] Given 我貼了不是英文的內容, When 我點「摘要」, Then 顯示「請貼英文文章」錯誤訊息
- [ ] Given API 失敗, When 錯誤發生, Then 畫面顯示「請稍後再試」並保留輸入

Priority: P0
Size:     M
Status:   Todo
```

---

## 寫作 anti-pattern（要避免）

❌ **太大不可估**：「做出新聞摘要系統」
✅ 拆成：US-001 貼+摘要 / US-002 多檔批次 / US-003 歷史記錄

❌ **只描述介面**：「加一個藍色按鈕」
✅ 改寫成：「使用者能點按鈕觸發摘要（其中按鈕長藍色）」

❌ **AC 不可驗證**：「使用者要覺得好用」
✅ 改寫成：「90% 受測者能在不看說明的情況下完成第一次摘要」

❌ **AC 太籠統**：「系統能正確運作」
✅ 拆成具體 Given-When-Then 條目
