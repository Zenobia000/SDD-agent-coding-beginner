# Sprint 1 Retrospective — 2026-05-27 ~ 2026-05-29

> 這是範例 retro，給學員看「一個有用的 retro 長怎樣」。
> 真實 sprint 結尾跑 `/retro` skill，AI 會引導你寫一份新的。

---

## Sprint Goal

讓 US-001 摘要主流程完整 demo（從輸入英文文章 → 看到中文摘要）

## 達成度

- Goal: ✅ 達成（demo 跑得起來）
- 計畫 task: 5 / 完成: 4 / Carry over: 1
- 完成率: 80%

---

## 4Ls

### ✅ Liked（喜歡的 / 做得好的）

- **AI 跑 /tdd-cycle 時主動先問前置條件**，避免我直接寫 code 跑掉
- **BDD scenarios 寫完後，AI 自動生對應 unit test 骨架**很省事
- **`/verify` 一鍵跑完 5 個維度**，比手動跑舒服很多
- **每天結束前打 `/sync-it` 確認沒漂移**變成自然習慣
- **Conventional commits 配 `/commit-msg`**，git log 變得有用了

### 🎓 Learned（學到的）

- **TDD 紅綠燈不是工作量加倍** — 是把「事後 debug 5 小時」前置成「事前寫測試 30 分鐘」
- **ADR 寫一次後**，再次討論「要不要用 X」AI 自動 reference 過去決策，省了重新思考
- **AGENTS.md 寫角色 + 必讀文件 + 絕對禁止** 這三段最有用，其他章節 AI 自動會做
- **Spec 不寫不會死，但寫了之後 AI 的產出質量直接翻倍**

### 🔴 Lacked（缺了什麼 / 卡到哪）

- **字數驗證的 prompt 微調花了 40 分鐘**（沒預期）→ 建議列入下次 risk
- **API 失敗時的 retry 策略沒寫進 spec**，AI 自由發揮 → 我得回頭改
- **沒做 sprint 中途的 mini retro**，發現方向跑偏時已過 1 天
- **第一天太想一次寫完，沒走 /spec-it** → 後續花更多時間補

### 💭 Longed for（希望未來有什麼）

- 想要一個 `/risk-check` skill 在 sprint 中途快速掃 risk
- 想要 `/spec-it` 自動把「retry / timeout / fallback」三件事問清楚
- 想要 retro 時 AI 自動 highlight git log 中「同個檔案改超過 5 次」這種訊號
- 想要 sprint 中段（第 1.5 天）有自動提醒「該不該調整 backlog」

---

## 客觀資料

📊 **Velocity**
- 計畫 task: 5
- 完成 task: 4
- Carry over: 1（T-105 字數驗證）
- 完成率: 80%

📊 **Commits**
- 總 commit: 12
- 平均每天: 4 個
- 最大 commit gap: 8 小時（5/27 深夜）→ 可能該休息

📊 **Test coverage**
- Sprint 開始: 0%
- Sprint 結束: 87%
- 達標 ✅（目標 80%）

📊 **Drift**
- 修了 3 個 drift（D-001 ~ D-003）
- 殘留 0 個 critical drift

📊 **時間分配（估算）**
- `/tdd-cycle`: ~6 小時
- `/spec-it`: ~30 分鐘
- `/verify`: ~15 分鐘
- `/sync-it`: ~10 分鐘
- `/commit-msg`: ~5 分鐘
- (其他/思考/中斷): ~1 小時

---

## Action Items（下個 sprint 要做的事）

1. [ ] 在 `docs/templates/PRD-template.md` 加入「Failure & Retry Policy」必填欄
2. [ ] 評估寫一個 `/risk-check` skill（先看下個 sprint 是否再次遇到同類問題）
3. [ ] Sprint 中段（第 1.5 天）安排一次 mini-retro
4. [ ] 寫 ADR-0004-api-retry-policy（決定全專案的 retry 策略）

---

## 給下個 Sprint 的繼承事項

- **T-105 字數驗證 carry over**（已修但測試還沒補完）
- **API retry 策略需在新 ADR 中明確**（候選：ADR-0004-api-retry-policy）
- **新的 risk**: Gemini prompt 微調比預期久，下次估時要 +30%

---

## 一句話收尾

> **這個 sprint 我證明了：花 30 分鐘寫 spec，省下了 3 小時的「再改改」。**
