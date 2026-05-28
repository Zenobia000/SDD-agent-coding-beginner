# USAGE.md — 本模板完整使用說明

> 本模板用 **Spec-Driven Development（SDD）** 工作流：spec 先於 code、測試先於實作、文件與 code 同步。
> 適合**有基本程式概念**（知道 function / API / 測試是什麼）、要做正規可維護專案的開發者。

---

## 0. 這套模板假設你

- 寫過至少一個小專案，知道 function / class / API / 測試是什麼
- 想用「業界做法」做專案：有 spec、有測試、有文件、有 git 紀律
- 專案會持續迭代（不是一次性 demo）

> 純新手 / 只想快速做個 demo？這套 SDD 流程對你會太重。先去 `class_plan/` 的工作坊教案學 Vibe Coding 基礎，能力上來再回來用這個模板。

---

## 1. SDD Sprint 十站

### 1.1 十站流程總圖

**完整 Mermaid 流程圖 + 每站產出 + 大廠對標** → [`.agents/WORKFLOW.md`](./.agents/WORKFLOW.md)

一句話順序：**意圖（`/spec-it` / `/adr` / `/plan-sprint`）→ 設計（`/spec-it` L2+L3）→ 實作（`/tdd-cycle` / `/verify` / `/sync-it`）→ 上線（`/commit-msg` / 部署 / `/retro`）**。

### 1.2 四條鐵則

- **沒 PRD 不開工**：新需求一律先 `/spec-it`（見 `rules/04-spec-first.md`）
- **沒測試不算完成**：實作走 `/tdd-cycle` 紅綠燈（見 `rules/05-tdd-required.md`）
- **沒 `/verify` 不 commit**：過五維度驗證才 commit
- **沒 `/sync-it` 不收工**：code 改了文件要跟上（見 `rules/06-doc-as-code.md`）

> **不必全用**：Solo dev 最小集是 `/spec-it` + `/tdd-cycle` + `/commit-msg`。`/adr`（多選項決策）、`/sync-it`（有獨立文件）、`/retro`（sprint 收尾）依需要啟用。

---

## 2. Sprint 1 完整 walkthrough（範例：英文新聞摘要工具）

> 以下是第一個 sprint 的完整對話流程。實際打字內容用 `>` 標示。

### Day 1 上午（90 分鐘）— 意圖 + 架構 + Backlog

**Step 1：跑 `/spec-it` 澄清需求 + 生 spec**（40 分鐘）

```
> /spec-it
> 我想做一個英文新聞摘要工具
```

AI 會問 5 個澄清問題：解什麼問題 / 成功長怎樣 / 不做什麼 / 既有 PRD / 預期 sprint 長度。

你回答後，AI 生：
- `docs/PRD.md`（PRD + 4 個 user story + AC）
- `docs/api-contract.md`（如有 API）
- `tests/features/summarize.feature`（BDD scenarios）
- `tests/unit/test_summarizer.py`（測試骨架）
- `tasks/backlog.md`（新增條目）

**Step 2：跑 `/adr` 記架構決策**（20 分鐘）

```
> /adr
> 要用 Gemini API 還是 OpenAI？
```

AI 問 3 題確認是 ADR 等級決策，生 `adr/ADR-0001-llm-provider.md` 草稿（Status: Proposed），你 review 後標 Accepted。

**Step 3：跑 `/plan-sprint` 拆 backlog**（30 分鐘）

```
> /plan-sprint
> 這個 sprint 想完成 US-001 摘要主流程
```

AI 把 US-001 拆成 5 個 task（T-101 ~ T-105），寫入 `tasks/sprint-current.md`：

```
Now：T-101 建立輸入框 UI
Next：T-102 ~ T-105
Later：T-201 批次摘要（下 sprint）
```

### Day 1 下午 ~ Day 2（10 小時）— TDD 開發

**Step 4：跑 `/tdd-cycle` 寫每個 task**

```
> /tdd-cycle
> 實作 T-102 Summarizer class
```

AI 依 Red-Green-Refactor 三步驟：

```
🔴 RED：寫第一個失敗測試 test_summarize_with_valid_500_word_article
       跑 pytest → 紅燈 ✅（預期）

🟢 GREEN：寫最少實作讓測試過
        跑 pytest → 綠燈 ✅

🔵 REFACTOR：重構成真實版（接 Gemini API）
            跑 pytest → 綠燈 ✅

繼續下一個測試 test_summarize_with_empty_string...
```

每個 task 跑完整 cycle，AI 會告訴你「T-102 完成，跑 `/verify`？」。

### Day 3 上午（60 分鐘）— 驗證 + 同步 + Commit

**Step 5：跑 `/verify` 五維度驗證**

```
> /verify
```

AI 跑 Format / Lint / Type / Test + Coverage / Security 五項，產出報告。紅燈 → 修；全綠 → 進下一步。

**Step 6：跑 `/sync-it` 文件對齊**

```
> /sync-it
```

AI 比對 code 與 `docs/PRD.md` / `docs/api-contract.md`，列出 drift。你裁決要改哪邊（通常改 code 對齊 spec）。

**Step 7：跑 `/commit-msg` 生 commit**

```
> /commit-msg
```

AI 掃 staged changes，依 Conventional Commits 1.0 + WHY/WHAT/IMPACT 格式生 message，你確認後 commit。

**Step 8：部署（如需要）**

```
> 我想把這個放到 GitHub Pages
```

依 `.agents/prompts/deploy.md`。

### Day 3 下午（30 分鐘）— Retro

**Step 9：跑 `/retro` sprint 回顧**

```
> /retro
> sprint 跑完了
```

AI 依 4Ls（Liked / Learned / Lacked / Longed for）逐項問你，補上客觀資料（velocity / coverage / commit pattern），寫入 `tasks/retros/YYYY-MM-DD-sprint-1.md`。

---

## 3. 一輪完整時程示意

| Sprint 長度 | 建議分配 |
|---|---|
| **半天**（4h） | `/spec-it` 20 min → `/plan-sprint` 10 min → `/tdd-cycle` 2.5h → `/verify` + `/sync-it` 20 min → `/commit-msg` 10 min → `/retro` 20 min |
| **一天**（8h） | `/spec-it` + `/adr` 1h → `/plan-sprint` 30 min → `/tdd-cycle` 5h → `/verify` + `/sync-it` 30 min → `/commit-msg` + 部署 30 min → `/retro` 30 min |
| **三天**（24h） | Day 1：意圖 + 架構 + Backlog（3h）+ TDD（5h）/ Day 2：TDD 持續（8h）/ Day 3：剩餘 TDD（4h）+ `/verify` + `/sync-it`（1h）+ `/commit-msg` + 部署（1h）+ `/retro`（1h）|

---

## 4. 八個 skill 觸發時機

每個 skill 的「何時打 / 不要打」、Pre/Post 條件、與其他 skill 的依賴 → [`.agents/SKILL-MAP.md` §1 §2 §11](./.agents/SKILL-MAP.md)（單一 SoT，本檔不重述）。

---

## 5. 常見陷阱

### 陷阱 1：跳過 spec 直接寫 code

**症狀**：「`/tdd-cycle` 寫 code 比較快，先寫，spec 之後補」

**結果**：AI 沒方向自由發揮 → 寫出來不是你要的 → 改 10 次 → 比一開始寫 spec 還慢

**對策**：強制 `/spec-it` → `/tdd-cycle` 順序。沒 spec 不寫 code（見 `rules/04-spec-first.md`）。

### 陷阱 2：覺得 SDD 太繁瑣想偷工

**症狀**：「我只是改個小東西，要寫 PRD + ADR + BDD 太累」

**對策**：依規模縮放，不是放棄紀律 ——
- 純樣式 / 註解 / typo：直接改，不用跑全套
- 任何**行為改變**：至少 `/spec-it`（精簡）+ `/tdd-cycle`。30 分鐘 spec 省下 3 小時返工。

### 陷阱 3：所有 task 都標 P0

**症狀**：`tasks/backlog.md` 全部 P0、沒有 P1 / P2

**對策**：強制每 sprint **最多 3 個 P0**。其餘往 P1 / P2 / Later 推。**選擇 = 決策 = 思考**。

### 陷阱 4：retro 變成「感覺良好大會」

**症狀**：retro 只列「做得好」、沒列「卡到哪」

**對策**：4Ls 四項都必填。寫不出 Lacked / Longed for → 表示你沒在反思。

### 陷阱 5：文件寫了從不更新

**症狀**：PRD 是第一天寫的、後來 code 改了很多但 PRD 沒動

**對策**：強制每個 commit 前跑 `/sync-it`。文件腐爛 = 專案腐爛。

---

## 6. FAQ

**Q：我打 `/spec-it` 但 AI 沒進入「問 5 個問題」模式？**
A：1) 看 `.agents/skills/spec-it/SKILL.md` 是否在那邊；2) 打 `/memory show` 看 skills 有沒有載入；3) 打 `/memory refresh`；4) 重啟 `agy`。

**Q：小調整也要跑全套 SDD 嗎？**
A：不用。判斷標準：**行為改變 → 走 SDD（至少 `/spec-it` 精簡 + `/tdd-cycle`）；純樣式 / 註解 / typo → 直接改**。SDD 是為了「會持續迭代、要維護」的東西，不是綁住每個 typo。

**Q：我沒寫過 git，要直接學 Conventional Commits 嗎？**
A：不需要硬背。`/commit-msg` 會幫你生 message。你只要 `git add .` 然後打 `/commit-msg`，AI 寫好 message 你確認後它幫你 commit。

**Q：BDD 跟 TDD 差在哪？我兩個都要寫嗎？**
A：BDD（`.feature` 檔）寫**使用者語言的情境**（「點按鈕後看到摘要」）；TDD（`test_*.py`）寫**程式碼層的測試**（「`summarize()` 用 500 字輸入回傳 SummaryResult」）。兩個都寫，因為層級不同：BDD 給人看、TDD 給程式看。

**Q：tasks/sprint-current.md 我手動編輯還是讓 AI 改？**
A：兩種都行。`/plan-sprint` 會幫你寫；過程中你想加 task 直接編輯 markdown；sprint 結束打 `/retro` 也會更新。

**Q：ADR 我寫一個後再也沒回頭看，這樣有用嗎？**
A：有。**ADR 的價值在「未來 AI 進新 session 自動讀到」**，不是給你看的。3 個月後 AI 會自動 reference 過去的 ADR，避免推翻過去決策。

**Q：我每個 sprint 都跑 retro 但永遠寫一樣的東西？**
A：表示你的工作模式沒在演化。Action Items 沒被執行 → 下個 sprint 重貼。建議**強制每個 retro 至少完成 1 個 Action Item**才能跑下個 sprint。

**Q：模板裡的 8 個 SDD skill 我能砍掉幾個嗎？**
A：可以。**Solo dev 不必全用**。最小集：`/spec-it` + `/tdd-cycle` + `/commit-msg`。其餘是「該專案需要時再啟用」。例：個人小工具不需要 `/adr`、單檔專案不需要 `/sync-it`。

**Q：我發現某個 skill 寫得不適合我的領域，能改嗎？**
A：可以。`.agents/skills/<name>/SKILL.md` 是純 markdown，直接編輯。改完打 `/memory refresh` 重載。

**Q：PRD 已經寫了「使用 Gemini API」，還要寫 ADR 嗎？**
A：**不用**。當 PRD 已經把技術寫死成「外部約束」（例：講師要求、只有 Google 帳號），那就不是「決策」、是「條件」，PRD 已經捕捉到。ADR 是用來記錄**多選項在競爭、你做了選擇**的情況（「Gemini vs OpenAI vs Claude，我選 Gemini 因為 ___」）。
判斷 3 題：1) 影響超出單一 user story？ 2) 有 2+ 個合理選項？ 3) 3 個月後想換會痛？三題都 Yes 才寫。Solo dev 半天~一週專案，0-3 個 ADR 就夠用。

**Q：我不會判斷何時該打哪個 skill 怎麼辦？**
A：**你不需要判斷**。本模板的 `rules/07-proactive-skill-trigger.md` 規定 AI 要主動偵測訊號、主動建議。
範例：你說「我想做摘要工具」 → AI 會自動說「動工前建議跑 `/spec-it`」。
你只要選「要 / 不要 / 之後再說」，不需要記 8 個 skill 名稱。**第一次跑某個 skill 時，AI 會附 30 字白話介紹**。

**Q：`prompts/` 和 `skills/` 有什麼差別？**
A：
- **`skills/`** 是「可觸發的程序工具」— 可手動 `/xxx` 或 AI 自動建議。例：`/spec-it` 有 step-by-step 執行流程、會產出多個檔案。SDD 主力。
- **`prompts/`** 是「對話開場白模板」— 複製貼上就行。部署 / 安裝 / 開場等場景用。例：`prompts/start-project.md` 是「我要開新專案，請帶我跑 SDD 第一站」的固定話術。

完整連動關係見 `.agents/SKILL-MAP.md`。

**Q：怎麼知道某個 skill 完成後接著該跑什麼？**
A：看 `.agents/SKILL-MAP.md` §2 Pre/Post 矩陣與 §4 六種典型路徑。簡化版：
- `/spec-it` 完 → `/plan-sprint`
- `/plan-sprint` 完 → `/tdd-cycle`
- `/tdd-cycle` 完 → `/verify`
- `/verify` 綠 → `/sync-it`
- `/sync-it` 無 drift → `/commit-msg`
- `/commit-msg` 完 → 下個 `/tdd-cycle` 或 `/retro`
- `/retro` 完 → `/plan-sprint`（下個 sprint）

AI 在每個 skill 結束時會主動建議下一步，你不必背。

**Q：AI 一直建議我跑 skill，太煩怎麼辦？**
A：兩個方法 ——
1. **每次 session 內**：說「不要建議任何 skill，我自己來」，整個 session 安靜。
2. **永久設定**：編輯 `.agents/settings.json` 加 `"skillTriggerMode": "passive"`，AI 只在你打 `/xxx` 時觸發、不主動建議。

---

## 7. 下一步建議

| 你現在的狀態 | 下一步 |
|---|---|
| 還沒有 PRD | 跑 `/spec-it`，AI 問你 5 題幫你結構化成 PRD |
| 已填完 PRD、第一次跑 | 貼 `.agents/prompts/start-project.md` → 進入 SDD 第一站 |
| 有現成 code、想補上 SDD 紀律 | 跑 `/spec-it` 補 PRD → `/tdd-cycle` 為現有 code 補測試 → `/adr` 補關鍵決策 |
| 想精讀大廠規範 | 逐份讀 `.agents/skills/spec-it/templates/`（6 份）+ `.agents/skills/adr/templates/adr-template.md` — 共 7 份範本內附對標來源 |

---

## 8. 三句口訣

1. **先 spec、後測試、文件跟著 code 走**
2. **行為改變走全套，純樣式直接改**
3. **不必全用 8 個 skill — 最小集是 `/spec-it` + `/tdd-cycle` + `/commit-msg`**
