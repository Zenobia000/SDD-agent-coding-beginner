# USAGE.md — 本模板完整使用說明

> 本模板提供**兩種使用模式**。先在這份文件決定你要走哪條路，再進入細節文件。

---

## 0. 5 秒決策：A or B？

回答以下 3 題，看你符合哪邊較多：

| 問題 | A 模式（Vibe Coding 五步） | B 模式（SDD Sprint 十站） |
|---|---|---|
| 你寫過 code 嗎？ | 完全沒寫過 / 只用過 Scratch | 寫過至少一個小專案、知道 function 是什麼 |
| 這次目標是？ | 玩一下 / hackathon / 一個 demo 給朋友看 | 認真做一個專案 / 學業界做法 / 準備接 PM 工作 |
| 預期投入時間？ | 半天 ~ 一天 | 至少一週、會持續迭代 |

**多數答 A → 用 Mode A**。**多數答 B → 用 Mode B**。**完全不確定 → 先用 A，能力上來再升 B**。

> 兩個模式不是「初級 vs 高級」 — 是「不同目的的工具」。Mode A 適合快速看到結果、Mode B 適合練習業界做法。

---

## 1. Mode A — Vibe Coding 五步（適合純新手）

### 1.1 適合場景

- 第一次做專案、純新手
- 想在 4 小時內看到「螢幕上有個能動的東西」
- Hackathon、課堂作業、給朋友 demo

### 1.2 五步流程

每次需求都跑這 5 步：

```
1. 重述需求    → AI 用 5 行內告訴你「我理解你要的是 ___」
2. 列出計畫    → AI 列出要改 / 新增的檔案，等你說 OK
3. 寫 code     → AI 寫完告訴你「這段在做 ___，因為 ___」
4. 帶你測試    → AI 告訴你怎麼跑、預期看到什麼
5. 等回報      → 你回報結果，再決定下一步
```

詳細規則在 `AGENTS.md §3.1`。

### 1.3 第一次跑：30 分鐘 walkthrough

**步驟 1：填好 `docs/PRD.md`**（10 分鐘）

打開 `docs/PRD.md`，把 `___` 填上你的需求。**不會填 → 跳到 Mode B 用 `/spec-it` 讓 AI 幫你問**。

**步驟 2：啟動 Antigravity**（2 分鐘）

```bash
cd 你的專案資料夾
agy
```

或開 Antigravity 桌面版開啟資料夾。

**步驟 3：丟入第一句 prompt**（1 分鐘）

複製 `.agents/prompts/start-project.md` 整段內容、貼到對話框、按 Enter。

**步驟 4：跑五步迴圈**（剩下 17 分鐘）

AI 會依五步流程動作。你的工作：

| AI 在做 | 你要做 |
|---|---|
| 重述需求 | 看對不對，不對就糾正 |
| 列計畫 | 確認方向，OK 就說「OK，動手」 |
| 寫 code | **不要自己改 code**，等 AI 寫完 |
| 帶你測試 | 照 AI 的步驟跑，看到預期就回報「OK」 |
| 等回報 | 說下一步要什麼，或說「先這樣就好」 |

### 1.4 常用對話模式

| 你想 | 怎麼說 |
|---|---|
| 加新功能 | 「我想加 ___ 功能」 |
| 修 bug | 「我跑出來 ___，預期 ___，差在哪？」 |
| 解釋 code | 「@app.js 這段在做什麼？」 |
| 回滾 | 打 `/restore` 選快照（不要直接改 code 還原） |
| AI 忘了規則 | 打 `/memory show` 看載入內容、`/memory refresh` 重讀 |

### 1.5 卡關時看哪

| 狀況 | 看哪份 |
|---|---|
| 不知道怎麼開始 | `.agents/prompts/start-project.md` |
| AI 一直亂寫 | `.agents/rules/03-when-stuck.md` |
| AI 改錯一堆檔案 | 打 `/restore` |
| 想上線給朋友看 | `.agents/prompts/deploy.md` |

### 1.6 Mode A 三不要

1. ❌ **不要自己改 code** — 改不好還會壞掉。改「需求描述」讓 AI 重做。
2. ❌ **不要一次給太多需求** — 一次加一個小功能，跑得起來再加下一個。
3. ❌ **不要刪 `.agents/` 資料夾** — 它是 AI 的「規則書」。

---

## 2. Mode B — SDD Sprint 十站（適合有程式基礎）

### 2.1 適合場景

- 已經寫過至少一個專案，知道 function / class / API 是什麼
- 想學「業界怎麼用 AI 做專案」
- 準備接 PM / 後端 / 全端職位、需要練 spec / TDD / git workflow
- 專案會持續迭代（至少 1 週）

### 2.2 十站流程總圖

完整流程圖見 `.agents/WORKFLOW.md`：

```
意圖澄清 → 架構決策 → Backlog → Spec 設計 → TDD 開發
/spec-it    /adr      /plan-sprint  /spec-it    /tdd-cycle

驗證 → 文件同步 → Commit → 部署 → Retro
/verify  /sync-it    /commit-msg  (deploy.md)  /retro
```

### 2.3 Sprint 1 完整 walkthrough（範例：英文新聞摘要工具）

> 以下是學員第一個 sprint 的完整對話流程。實際打字內容用 `>` 標示。

#### Day 1 上午（90 分鐘）— 意圖 + 架構 + Backlog

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

#### Day 1 下午 ~ Day 2（10 小時）— TDD 開發

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

每個 task 跑完整 cycle，AI 會告訴你「T-102 完成，跑 /verify？」。

#### Day 3 上午（60 分鐘）— 驗證 + 同步 + Commit

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

#### Day 3 下午（30 分鐘）— Retro

**Step 9：跑 `/retro` sprint 回顧**

```
> /retro
> sprint 跑完了
```

AI 依 4Ls（Liked / Learned / Lacked / Longed for）逐項問你，補上客觀資料（velocity / coverage / commit pattern），寫入 `tasks/retros/YYYY-MM-DD-sprint-1.md`。

### 2.4 一輪完整時程示意

| Sprint 長度 | 建議分配 |
|---|---|
| **半天**（4h） | `/spec-it` 20 min → `/plan-sprint` 10 min → `/tdd-cycle` 2.5h → `/verify` + `/sync-it` 20 min → `/commit-msg` 10 min → `/retro` 20 min |
| **一天**（8h） | `/spec-it` + `/adr` 1h → `/plan-sprint` 30 min → `/tdd-cycle` 5h → `/verify` + `/sync-it` 30 min → `/commit-msg` + 部署 30 min → `/retro` 30 min |
| **三天**（24h） | Day 1：意圖 + 架構 + Backlog（3h）+ TDD（5h）/ Day 2：TDD 持續（8h）/ Day 3：剩餘 TDD（4h）+ `/verify` + `/sync-it`（1h）+ `/commit-msg` + 部署（1h）+ `/retro`（1h）|

### 2.5 八個 skill 觸發時機速查

| Skill | 何時打 | 不要打 |
|---|---|---|
| `/spec-it` | 新功能動工前 / 既有功能要重新對齊 | 純樣式調整 / 修 typo |
| `/adr` | 重大技術選型（DB / 框架 / auth） | 局部小決定（用哪個 lib function） |
| `/plan-sprint` | Sprint 開始 / 重整 backlog | Sprint 進行中（會打亂節奏） |
| `/tdd-cycle` | 寫每個功能 / 修 bug（先寫重現測試） | 純 refactor / 純樣式 |
| `/verify` | Commit 前 / sprint 結尾 / 上線前 | 還在 RED-GREEN 過程中 |
| `/sync-it` | Commit 前 / 改完 API 或 schema | 純樣式或註解修改 |
| `/commit-msg` | 全綠 + 無 drift 後、commit 前 | 還有紅燈時 |
| `/retro` | Sprint 結束 | Sprint 還在進行中 |

---

## 3. A → B 升級路徑

### 3.1 什麼時候你該從 A 升 B？

出現以下任一情境 → 該升 B：

- [ ] 你做完一個 Mode A 專案，想做下一個更大的
- [ ] 你發現「我需求改了 5 次、code 改了 20 次」 → 缺 spec
- [ ] 你發現「AI 改的 code 我看不懂」 → 缺 TDD（測試會逼你跟 AI 對齊「正確長怎樣」）
- [ ] 你發現「我忘記為什麼當初選 X」 → 缺 ADR
- [ ] 你發現「文件跟 code 對不上」 → 缺 `/sync-it`
- [ ] 你準備接技術職位 / 進階課程 / 要跟人協作

### 3.2 升級的 3 步驟

不需要砍掉重練。在現有 Mode A 專案上漸進升級：

**Step 1（10 分鐘）：補 PRD**

打 `/spec-it`，AI 會反過來問你 5 題，幫你把現有專案的需求結構化寫進 `docs/PRD.md`。

**Step 2（30 分鐘）：補測試**

打 `/tdd-cycle`，AI 會用「為現有 code 補測試」模式：
- 先列出主要 function
- 對每個 function 寫測試
- 跑測試確認 code 行為符合預期
- 補 user story 對應的 BDD scenario

**Step 3（10 分鐘）：補 ADR + 開始走十站流程**

回想當初做了哪些技術選擇，打 `/adr` 補 ADR-0001、ADR-0002⋯⋯下個 sprint 開始走 Mode B 完整流程。

### 3.3 升級後的差異感

| 維度 | Mode A 感受 | Mode B 感受 |
|---|---|---|
| 動工前 | 直接寫，邊做邊想 | 先寫 spec、AC、BDD，30 分鐘 |
| 寫 code 時 | AI 自由發揮 | TDD 引導，每個行為都有測試 |
| 改完當下 | 「應該沒事吧」 | `/verify` + `/sync-it` 告訴你具體狀況 |
| Commit 時 | 「先 push」 | Conventional Commits 結構化訊息 |
| Sprint 結束 | 「下次再說」 | `/retro` 4Ls 歸檔 |
| 6 個月後回來 | 完全不記得當初為什麼這樣寫 | 看 ADR + PRD + retro 重建脈絡 |

---

## 4. 常見陷阱

### 陷阱 1：用 Mode A 做超出能力的事

**症狀**：第一次寫程式就想做「全端 + 後端資料庫 + Auth + 部署」

**對策**：Mode A 第一個專案請限定**單頁前端 + localStorage + 不超過 200 行**。等做完一個再升級。

### 陷阱 2：用 Mode B 但跳過 spec

**症狀**：「`/tdd-cycle` 寫 code 比較快，先寫，spec 之後補」

**結果**：AI 沒方向自由發揮 → 寫出來不是你要的 → 改 10 次 → 比一開始寫 spec 還慢

**對策**：強制 `/spec-it` → `/tdd-cycle` 順序。沒 spec 不寫 code（見 `rules/04-spec-first.md`）。

### 陷阱 3：覺得 SDD 太繁瑣放棄

**症狀**：「我只是想做小工具，要寫 PRD + ADR + BDD 太累」

**對策**：兩條路 ——
- 真的只是小工具 → 用 Mode A，不要硬上 B
- 你只是還不熟流程 → 跑完一個 Mode B sprint 你會發現「30 分鐘 spec 省下 3 小時返工」

### 陷阱 4：所有 task 都標 P0

**症狀**：`tasks/backlog.md` 全部 P0、沒有 P1 / P2

**對策**：強制每 sprint **最多 3 個 P0**。其餘往 P1 / P2 / Later 推。**選擇 = 決策 = 思考**。

### 陷阱 5：retro 變成「感覺良好大會」

**症狀**：retro 只列「做得好」、沒列「卡到哪」

**對策**：4Ls 四項都必填。寫不出 Lacked / Longed for → 表示你沒在反思。

### 陷阱 6：文件寫了從不更新

**症狀**：PRD 是第一天寫的、後來 code 改了很多但 PRD 沒動

**對策**：強制每個 commit 前跑 `/sync-it`。文件腐爛 = 專案腐爛。

---

## 5. FAQ

**Q：我打 `/spec-it` 但 AI 沒進入「問 5 個問題」模式？**
A：1) 看 `.agents/skills/spec-it/SKILL.md` 是否在那邊；2) 打 `/memory show` 看 skills 有沒有載入；3) 打 `/memory refresh`；4) 重啟 `agy`。

**Q：Mode A 跟 Mode B 可以混用嗎？**
A：可以。你可以在 Mode A 專案臨時打 `/spec-it` 補一份 PRD；也可以在 Mode B 專案某個小調整直接寫 code 不跑 `/tdd-cycle`。**混用的判斷標準**：行為改變 → 走 B；純樣式 / 註解 → 用 A 即可。

**Q：我沒寫過 git，要直接學 Conventional Commits 嗎？**
A：不需要。`/commit-msg` 會幫你生 message。你只要 `git add .` 然後打 `/commit-msg`，AI 寫好 message 你確認後它幫你 commit。

**Q：BDD 跟 TDD 差在哪？我兩個都要寫嗎？**
A：BDD（`.feature` 檔）寫**使用者語言的情境**（「點按鈕後看到摘要」）；TDD（`test_*.py`）寫**程式碼層的測試**（「`summarize()` 用 500 字輸入回傳 SummaryResult」）。Mode B 兩個都寫，因為層級不同：BDD 給人看、TDD 給程式看。

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
A：**不用**。當 PRD 已經把技術寫死成「外部約束」（例：講師要求、學員只有 Google 帳號），那就不是「決策」、是「條件」，PRD 已經捕捉到。ADR 是用來記錄**多選項在競爭、你做了選擇**的情況（「Gemini vs OpenAI vs Claude，我選 Gemini 因為 ___」）。
判斷 3 題：1) 影響超出單一 user story？ 2) 有 2+ 個合理選項？ 3) 3 個月後想換會痛？三題都 Yes 才寫。Solo dev 半天~一週專案，0-3 個 ADR 就夠用。

**Q：我新手，不會判斷何時該打哪個 skill 怎麼辦？**
A：**你不需要判斷**。本模板的 `rules/07-proactive-skill-trigger.md` 規定 AI 要主動偵測訊號、主動建議。
範例：你說「我想做摘要工具」 → AI 會自動說「動工前建議跑 `/spec-it`」。
你只要選「要 / 不要 / 之後再說」，不需要記 8 個 skill 名稱。**第一次跑某個 skill 時，AI 會附 30 字白話介紹**。

**Q：AI 一直建議我跑 skill，太煩怎麼辦？**
A：兩個方法 ——
1. **每次 session 內**：說「不要建議任何 skill，我自己來」，整個 session 安靜。
2. **永久設定**：編輯 `.agents/settings.json` 加 `"skillTriggerMode": "passive"`，AI 只在你打 `/xxx` 時觸發、不主動建議。
進階學員推薦 `passive`，純新手用預設 `proactive-friendly`。

---

## 6. 下一步建議

| 你現在的狀態 | 下一步 |
|---|---|
| 完全新手、還沒填 PRD | 讀 `docs/PRD.md` 填空 → 跑 Mode A |
| 已填完 PRD、第一次跑 | 貼 `.agents/prompts/start-project.md` → 跑 Mode A 五步 |
| Mode A 跑完一輪、想升級 | 跑 `/spec-it` 補完整 PRD → 進入 Mode B |
| 直接想用 Mode B | 跑 `/spec-it` 開新功能 → 看 `.agents/WORKFLOW.md` |
| 想精讀大廠規範 | 逐份讀 `docs/templates/` 7 份範本（內附對標來源） |

---

## 7. 三句口訣

1. **新手選 A**、**進階選 B**、**不確定先 A 再升 B**
2. **A 模式三不要**：不自己改 code、不一次給太多需求、不刪 `.agents/`
3. **B 模式三要**：先 spec、後測試、文件跟著 code 走
