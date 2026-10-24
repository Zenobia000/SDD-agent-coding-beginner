# 規格驅動 × AI 開發實戰營

> 2 天、14 小時，以 Claude Code 為核心。D1 理解 AI 時代的軟體工程、學會駕馭 coding agent；
> D2 用一個請假系統，從需求、規格、測試先行一路做到一個可驗收的功能。
> 桑尼資料科學出品。

## 兩天在做什麼

| | 主線 | 單元 | 學員帶走 |
|---|---|---|---|
| **D1** 理解與探索 | WHY → WHAT → HOW | 1–3 典範轉移、AI 協作、軟體工程與規格治理；4–7 Claude Code、Context Engineering、能力 Demo、Archify | 知道怎麼要求 AI、去哪裡檢查它、何時該停下來釐清規格 |
| **D2** 專案實作 | DO | 8–14 需求 → PRD → SRS／SAD／SDS → 測試案例 → TDD 垂直切片 → 除錯與需求變更 → 交付 | 一個可執行、可測試的請假功能，加上每條需求對到哪個測試 |

D2 的基本完成標準是**表單請假的垂直切片**；主管核准、額度檢查、一句話 AI 解析與注入防護是進階挑戰。
落後的組可以切到講師準備的 checkpoint 分支接著做，細節見 [`handbook/03-day2.md`](./handbook/03-day2.md)。

> ⚠️ 講義對應的是上課 repo 改版後的結構，目前在 leavebot-bootcamp 的 `refactor/form-slice-course` 分支，彩排完成後合併進 main。

## 這個 repo 放什麼

```text
handbook/      學員講義：課前準備、兩天課程、提示詞卡與問題排解
class_plan/    講師備課：投影片逐頁內容、Demo 腳本、上課 repo 改版規格
starter-kit/   企業啟動包：AI-Native 企業策略報告、高層簡報、部門拆解與工具
```

**看講義**：直接在 GitHub 上讀 `handbook/` 的 markdown。

**看高層簡報**：下載 [`starter-kit/deck/`](./starter-kit/deck/) 整個資料夾，雙擊 `index.html` 用瀏覽器打開。方向鍵翻頁，`ESC` 看總覽，`P` 開演講者模式（含每頁講稿備註），`B` 關掉動畫。

## 要上課的人

| 你要 | 去哪 |
|---|---|
| 開課前一週把環境裝好 | [`handbook/00-setup.md`](./handbook/00-setup.md) |
| 看兩天在做什麼 | [`handbook/01-overview.md`](./handbook/01-overview.md) |
| 上課用的專案 | [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp)：每組 fork 一份（取消勾選「只複製 main」） |
| 講師備課 | [`class_plan/`](./class_plan/README.md)：課程設計、投影片逐頁內容、備課清單 |

## 結訓之後

| 你要 | 去哪 |
|---|---|
| 帶回公司說服團隊 | [`starter-kit/`](./starter-kit/README.md) |
| 開一個有完整 AI 工具鏈的新專案 | [`agent-skills-starter`](https://github.com/Zenobia000/agent-skills-starter)：按 Use this template |
