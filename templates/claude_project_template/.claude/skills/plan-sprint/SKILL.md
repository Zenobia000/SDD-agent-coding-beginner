---
name: plan-sprint
description: 把 PRD 拆解成可執行的 sprint backlog。**主動觸發時機**：使用者剛跑完 `/spec-it`（PRD 寫好了）、說「sprint 開始」「這禮拜要做什麼」「先做哪個」「拆任務」「優先排序」，或當前 sprint-current.md 條目全打勾。
---

# /plan-sprint — Sprint Backlog 拆解

## 🚨 自動觸發訊號（AI 主動偵測）

依 `rules/07-proactive-skill-trigger.md`，AI 要監測對話、發現訊號主動建議。

### 強訊號（高機率該觸發）

- 「sprint 開始」「sprint 怎麼安排」
- 「這禮拜要做什麼」「今天要做什麼」「先做哪個」
- 「拆任務」「拆 backlog」「優先排序」
- 「PRD 寫好了，下一步」（剛跑完 `/spec-it` 的延續訊號）
- 當前 `tasks/sprint-current.md` 的 Now/Next 條目都打勾

### 中訊號（建議但詢問）

- 「先做 ___ 還是 ___」（多任務優先序問題）
- 對話進入「規劃接下來」階段
- 使用者列出 3+ 件要做的事但沒分優先級

### 反訊號（這些不要觸發 plan-sprint）

- 沒有 PRD → 先建議 `/spec-it`
- Sprint 進行中、Now 區還有未完成 task → 不要打斷
- 單一 task 的子拆解（這屬 `/tdd-cycle` 的範圍）

### 主動建議的話術範例

> 你剛跑完 `/spec-it`、PRD 有 4 個 user story 了。動工前建議跑 `/plan-sprint` 拆任務。
>
> 它會把每個 user story 拆成「半天可完成」的小 task，寫到 `tasks/sprint-current.md` 的 Now/Next/Later 區。這樣你不會「同時動 3 件事都做不完」。
>
> 要拆嗎？

---

## 何時觸發

- 使用者剛跑完 `/spec-it`，PRD 有了，要拆任務
- 使用者說「sprint 開始」「拆任務」「這禮拜要做什麼」
- 使用者打 `/plan-sprint`
- 每個 sprint 結尾，整理下個 sprint 的 backlog

## 不要觸發的情況

- 沒有 PRD → 先跑 `/spec-it`
- 任務已經拆完且還在執行中

---

## 大廠對標

採 **Atlassian Jira / Linear 的 backlog 格式** + **INVEST 原則拆解粒度**：

- 每個任務 = INVEST 原則的 user story
- Size 用 XS / S / M / L / XL（不用 story point — solo dev 不需要 velocity tracking）
- 狀態用 Now / Next / Later / Blocked / Done（Linear-style）

---

## 執行步驟

### Step 1：讀取 PRD + 現有 backlog + 已知 issue

```
docs/PRD.md
tasks/backlog.md
tasks/sprint-current.md
tasks/known-issues.md      ← 新增
tasks/retros/*.md          ← 讀最新一份的 Action Items
```

抓出：
- PRD 中所有 user story（US-XXX）
- 已 backlog 但尚未完成的條目
- 上個 sprint 的 retros 提到的 follow-up
- **`known-issues.md` 中候選排程的 issue**（特別注意「重評估時機 = 下個 sprint」的條目）

### Step 1.5：known-issues review（防 issue 永遠不被排程）

逐條 review `tasks/known-issues.md`：

| 條件 | 行動 |
|---|---|
| 「重評估時機」= 本 sprint | 列入本 sprint 候選 task |
| Warning 持續 2 sprint 沒修 | 升級成 Critical、強制排入本 sprint |
| Info 持續 3 sprint 沒修 | 建議使用者刪除（顯然不重要） |
| 其他 | 留在 known-issues |

範例話術：

> 我看到 `known-issues.md` 有 3 條 issue：
> - ISSUE-002（Gemini retry）已過 2 sprint 沒修 → 我建議升級成 Critical 排入本 sprint
> - ISSUE-005（Safari 字體）重評估時機是本 sprint → 你要排嗎？
> - ISSUE-001（命名混亂）持續 3 sprint 沒修 → 建議刪除，你同意嗎？

### Step 2：跟使用者對齊 sprint 目標

```
這個 sprint 你想達成什麼？（一句話）

我看到以下候選 user stories：
- US-001 [P0, M] 摘要主流程
- US-002 [P1, L] 批次摘要
- US-003 [P2, S] 歷史記錄
- US-004 [P1, M] 多語言輸出

建議 sprint 範圍（半天 / 一天 / 三天）：
[依使用者答案推薦]
```

### Step 3：把 user story 拆成 task

每個 user story 拆成 3-5 個 task，每個 task：
- 半天以內能完成（≤ M size）
- 可獨立 commit
- 可獨立 demo

範例拆法（US-001 摘要主流程 → 5 個 task）：

```
US-001 摘要主流程 [M]
├── T-101 [S] 建立輸入框 UI + 按鈕
├── T-102 [S] 寫 Summarizer class 骨架 + 測試
├── T-103 [M] 接 Gemini API + 處理 success
├── T-104 [S] 處理失敗 case（API 錯 / network 斷）
└── T-105 [S] 加字數驗證（80-120 字）
```

### Step 4：寫入 backlog（採 Linear-style）

更新 `tasks/sprint-current.md`：

```markdown
# Sprint Current — 2026-05-27 ~ 2026-05-29

## Goal
讓 US-001 摘要主流程完整 demo（從輸入英文文章 → 看到中文摘要）

## Now（這 2 小時要做）
- [ ] T-101 [S] 建立輸入框 UI + 按鈕

## Next（這個 sprint 內要做）
- [ ] T-102 [S] 寫 Summarizer class 骨架 + 測試
- [ ] T-103 [M] 接 Gemini API + 處理 success
- [ ] T-104 [S] 處理失敗 case
- [ ] T-105 [S] 加字數驗證

## Later（下個 sprint 候選）
- [ ] T-201 US-002 批次摘要

## Blocked
- (無)

## Done（本 sprint 已完成）
- (無)

## Notes
- US-001 對應 docs/PRD.md §4 US-001
- 對應 BDD scenario：tests/features/summarize.feature
```

### Step 5：寫入長期 backlog

更新 `tasks/backlog.md`（所有未來任務的總清單）：

```markdown
# Backlog

## P0 — Critical
- [ ] US-001 摘要主流程 [Sprint 1]
- [ ] US-004 多語言輸出 [Sprint 2]

## P1 — Important
- [ ] US-002 批次摘要 [Sprint 2-3]

## P2 — Nice to have
- [ ] US-003 歷史記錄 [Later]

## Ideas（未進 PRD）
- 主題標籤
- 個人化摘要長度
```

### Step 6：產生 Sprint Briefing

```markdown
# Sprint 1 Briefing — 2026-05-27 ~ 2026-05-29

## 目標
✓ 完成 US-001 摘要主流程

## 範圍
- 5 個 task（T-101 ~ T-105）
- 預估 1.5 天（含測試）

## 不做的（明確）
- 不做 UI 美化（先功能跑通）
- 不做歷史記錄
- 不做批次

## 風險
- Gemini API 配額：先測 50 次內可完成
- 字數驗證可能需要 prompt 微調 → 預留 30 分鐘

## 第一步
打 `/tdd-cycle` 開始 T-102（寫 Summarizer 測試）。
```

---

## INVEST 自檢（每個 task 都該過）

| 字母 | 自問 |
|---|---|
| **I** | 這個 task 能獨立完成嗎？不依賴另一個未完成 task？ |
| **N** | 還有彈性嗎？實作細節可以再討論？ |
| **V** | 完成這個 task 有可感知的進展嗎？（不是「設定環境」這種隱形工作） |
| **E** | 你能說出大概要花多久嗎？ |
| **S** | 半天以內能完成嗎？（超過拆） |
| **T** | 有明確的「完成」定義嗎？（測試通過 / demo OK） |

---

## 鐵律

1. **每個 task 半天以內**（超過拆）
2. **每個 task 可獨立 commit**（不要「我這個 commit 動了 10 個 task」）
3. **Now 區只放當前正在做的 1-2 個**（避免 context switch）
4. **Blocked 條目要寫原因 + 解鎖條件**
5. **Sprint 範圍鎖定後不加新 task**（除非 critical bug，否則進 Later）

---

## 觸發範例

使用者：「PRD 寫好了，這禮拜要做什麼？」

AI（你）：
> 跑 `/plan-sprint` 拆任務。
>
> 讀完 `docs/PRD.md`，看到 4 個 user story（US-001 ~ US-004）。
>
> 動手前問你：
>
> 1. **這個 sprint 目標一句話：** ___？
> 2. **預期長度：** 半天 / 一天 / 三天？
> 3. **必做的 user story：** US-001 一定要做嗎？
>
> 回答後我拆 task + 寫 `tasks/sprint-current.md`。
