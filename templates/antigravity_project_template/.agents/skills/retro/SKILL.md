---
name: retro
description: 引導 sprint 回顧（4Ls format），歸檔到 tasks/retros/。**主動觸發時機**：使用者說「sprint 結束」「跑完了」「回顧」「learn 到什麼」「下個 sprint」，或 `tasks/sprint-current.md` 的 Now/Next 條目全 done。
---

# /retro — Sprint Retrospective

## 🚨 自動觸發訊號（AI 主動偵測）

依 `rules/07-proactive-skill-trigger.md`，AI 要監測對話、發現訊號主動建議。

### 強訊號（高機率該觸發）

- 「sprint 結束了」「sprint 跑完了」「結束了」
- 「來回顧」「來 retro」「做個 retro」
- 「這次學到什麼」「這次踩了什麼雷」
- 「下個 sprint」「下一輪」「接下來呢」
- `tasks/sprint-current.md` 的 Now/Next 區條目全打勾

### 中訊號（建議但詢問）

- 「今天做得不錯 / 不太順」
- Sprint goal 已達成、commit 也 push 了
- 即將切到新 user story 但沒做 retro

### 反訊號（這些不要觸發 retro）

- Sprint 還在進行中（建議 `/plan-sprint` 調整 backlog）
- 沒有任何 commit / 進度
- 使用者明確說「跳過 retro」

### 主動建議的話術範例

> 你 sprint 1 的 5 個 task 全部完成了 ✅，commit 也 push 了。建議跑 `/retro`。
>
> 它會問你 4 個問題（Liked / Learned / Lacked / Longed for），加上客觀資料（velocity / coverage / commit pattern），歸檔成 `tasks/retros/YYYY-MM-DD-sprint-1.md`。
>
> 連續 3 個 sprint 不做 retro，你會重複踩同一個雷而不自覺。10 分鐘的事，要做嗎？

---

## 何時觸發

- 使用者說「sprint 結束了」「來回顧」「這次學到什麼」
- 使用者打 `/retro`
- 每個 sprint 收尾（即使 sprint 失敗也要做）

## 不要觸發的情況

- Sprint 還在進行中（這時跑 `/plan-sprint` 調整 backlog）
- 沒有任何 commit / 任何進度（連 retro 都還不需要）

---

## 大廠對標

採 **4Ls retrospective format**（Mary Gorman 提出 / Agile 社群廣泛採用）：

- **Liked**（喜歡 / 做得好的）
- **Learned**（學到什麼）
- **Lacked**（缺了什麼 / 卡到哪）
- **Longed for**（希望未來有什麼）

優於 Start/Stop/Continue 的點：包含「**學到了什麼**」這個對 AI 時代 solo dev 最重要的維度。

---

## 執行步驟

### Step 1：讀取 sprint 資料

掃描：
- `tasks/sprint-current.md` — 計畫了什麼
- `git log --since="<sprint start>" --oneline` — 實際做了什麼
- `tasks/backlog.md` — 動了哪些優先序

### Step 2：問使用者 4Ls（不要自己腦補）

**逐項問**，每項給 60 秒思考：

```
這個 sprint 跑完了，做個 retro。

逐個問你 4 個問題：

1. **Liked 喜歡的 / 做得好的**：
   這個 sprint 有什麼事情你覺得做得不錯？
   （可以是工作流、AI 互動、技術選型、心理狀態⋯⋯任何維度）

2. **Learned 學到的**：
   這個 sprint 你學到 / 體會到什麼？
   （新技術、新心法、Antigravity 的某個用法、自己工作模式的觀察⋯⋯）

3. **Lacked 缺了什麼 / 卡到哪**：
   過程中有什麼讓你卡關 / 浪費時間 / 心累？
   （工具不熟、AI 誤解、spec 寫不清、方向反覆⋯⋯）

4. **Longed for 希望有什麼**：
   下個 sprint 你希望有什麼改善？
   （新 skill、新規則、新工具、新工作方式⋯⋯）

請依序回答。我會把 4 個答案匯整成 retro 檔案。
```

**等使用者依序回答**。AI 不替使用者腦補答案（這是個人化內容）。

### Step 3：客觀資料補充（AI 加值）

使用者答完後，補上客觀資料：

```
我從本 sprint 的客觀資料補充：

📊 **Velocity（速度）**
- 計畫 task: 5
- 完成 task: 4
- Carry over: 1（T-105 字數驗證）
- 完成率: 80%

📊 **Commit pattern**
- 總 commit: 12
- 平均每天: 4 個
- 平均 commit 間隔: 2 小時
- 最大 commit gap: 8 小時（5/27 深夜）→ 可能該休息

📊 **Test coverage**
- Sprint 開始: 0%
- Sprint 結束: 87%
- 達標 ✅（目標 80%）

📊 **Drift**
- 修了 3 個 drift（D-001 ~ D-003）
- 殘留 0 個 critical drift

📊 **時間分配（估算）**
- /spec-it: ~30 分鐘
- /tdd-cycle: ~6 小時
- /verify: ~15 分鐘
- /sync-it: ~10 分鐘
- /commit-msg: ~5 分鐘
- (其他): ~1 小時
```

### Step 4：產出 retro 檔案

寫入 `tasks/retros/YYYY-MM-DD-sprint-N.md`：

```markdown
# Sprint 1 Retrospective — 2026-05-27 ~ 2026-05-29

## Sprint Goal
讓 US-001 摘要主流程完整 demo（從輸入英文文章 → 看到中文摘要）

## 達成度
- Goal: ✅ 達成
- 計畫 task: 5 / 完成: 4 / Carry over: 1
- 完成率: 80%

---

## 4Ls

### ✅ Liked
- AI 跑 /tdd-cycle 時主動先問前置條件，避免我直接寫 code
- BDD scenarios 寫完後，AI 自動生對應 unit test 骨架很省事
- /verify 一鍵跑完 5 個維度，比手動跑舒服

### 🎓 Learned
- TDD 紅綠燈不是工作量加倍 — 是把「事後 debug 5 小時」前置成「事前寫測試 30 分鐘」
- ADR 寫一次後，再次討論「要不要用 X」AI 自動 reference 過去決策，省了重新思考
- Conventional commits 配 /commit-msg 後，git log 變得有用了

### 🔴 Lacked
- 字數驗證的 prompt 微調花了 40 分鐘（沒預期）→ 建議列入下次 risk
- API 失敗時的 retry 策略沒寫進 spec，AI 自由發揮 → 我得回頭改
- 沒做 sprint 中途的 mini retro，發現方向跑偏時已過 1 天

### 💭 Longed for
- 想要一個 `/risk-check` skill 在 sprint 中途快速掃 risk
- 想要 `/spec-it` 自動把「retry / timeout / fallback」三件事問清楚
- 想要 retro 時 AI 自動 highlight git log 中「同個檔案改超過 5 次」這種訊號

---

## 客觀資料

📊 Velocity: 4/5 task 完成
📊 Commits: 12（平均 4/天）
📊 Test coverage: 0% → 87%
📊 Drift: 3 fixed, 0 critical 殘留
📊 主要時間：/tdd-cycle 6 小時、/spec-it 30 分鐘

---

## Action Items（下個 sprint 要做的事）

1. [ ] 在 PRD-template.md 加入「failure & retry policy」必填欄
2. [ ] 評估寫一個 `/risk-check` skill（先看下個 sprint 是否再次遇到同類問題）
3. [ ] Sprint 中段（第 1.5 天）安排一次 mini-retro

---

## 給下個 Sprint 的繼承事項

- T-105 字數驗證 carry over（已修但測試還沒補完）
- API retry 策略需在新 ADR 中明確（候選：寫 ADR-0004-api-retry-policy）
```

### Step 5：更新 backlog 與 ADR 候選

依 Action Items 更新：
- `tasks/backlog.md` 加入新候選任務
- `tasks/known-issues.md` **review 一次**：哪些 issue 重評估時機到了？哪些該升級？哪些該刪？
- 若 retro 出現重大決策方向（如「下次都用 X 工具」）→ 提醒使用者寫 ADR

### Step 6：橋接到下個 Sprint（連動 `/plan-sprint`）

Retro 結束不該結束 — 自然過渡到下個 sprint：

```
🎯 Retro 完成（tasks/retros/2026-05-29-sprint-1.md 已寫入）。

下一步建議：

1. 你想立刻開新 sprint → 跑 `/plan-sprint`
   - 我會讀本次 Action Items + known-issues.md，幫你拆下個 sprint 的 task

2. 你想休息一陣再回來 → 沒問題
   - 下次回來時打 `/plan-sprint`，我會接續這份 retro 的 Action Items

3. 你想先讀本次 retro 沉澱一下 → 也很好
   - tasks/retros/2026-05-29-sprint-1.md 已寫好，慢慢看

要跑 `/plan-sprint` 嗎？
```

**鐵律**：Retro Action Items 必須在下個 sprint 的 `/plan-sprint` 被讀到。連續 2 個 sprint 沒執行的 Action Item → 升級成 backlog 條目（不能永遠停留在 retro 檔案內裝飾用）。

---

## 鐵律

1. **AI 不腦補 4Ls 答案** — 等使用者回答
2. **AI 主動補客觀資料** — 速度 / coverage / commit pattern
3. **每個 retro 必須產出 Action Items** — 不能只「感受良好」就結束
4. **失敗的 sprint 也要做 retro** — 失敗更要學
5. **retro 不檢討人 / 不批評過去自己** — 只看「下次怎麼做更好」

---

## 觸發範例

使用者：「sprint 跑完了，來 retro」

AI（你）：
> 跑 `/retro` — 4Ls 格式回顧。
>
> 先讓我掃 sprint 資料⋯⋯
>
> 📊 看到：12 個 commit、87% coverage、4/5 task 完成
>
> 接下來逐項問你 4 個問題（請慢慢答）：
>
> 1. **Liked** 這個 sprint 有什麼做得不錯？
>
> （等回答）
