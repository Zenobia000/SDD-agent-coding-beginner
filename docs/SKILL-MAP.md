# 技能速查

> 對應 [`.claude/skills/`](../.claude/skills/) 的 36 個技能。
> 改了技能就要回來改這張表 —— 教材靠它指路。
> 漏改了 `bash scripts/check.sh` 會擋下來（它同時檢查 `compass/SKILL.md`）。

不確定用哪個 → **`/compass`**。

每一站的指令與逐字可貼的提示詞 → [`curriculum/COOKBOOK.md`](../curriculum/COOKBOOK.md)（**逃生口，卡住才翻**）。

---

## 一張圖看完

七站、每站的技能、以及每站的跳過條件：

[![路線圖：新題目 → 上線](./assets/route.svg)](./assets/route.svg)

**藍 = 你打字才會動；紫 = AI 也會自己用。第 5 站是唯一不能跳的。**

---

## 依站點查

| 站 | 技能 | 產出 | 什麼情況跳過 |
|---|---|---|---|
| （開始之前） | `/setup-skills` | `docs/agents/`、guard hooks | 每個 repo 跑一次。不是站，是雜務 |
| **1** 拆解問題 | `/grilling`（無 codebase）<br>`/grill-with-docs`（有 codebase）<br>`/domain-modeling`<br>`/to-spec` | spec、`CONTEXT.md`、ADR | 別人已經給你 spec |
| **2** 值不值得做 | `/feasibility` | ✅／⚠️／❌ 判決 | 沒有真實不確定性 |
| **3** 系統骨架 | `/to-architecture`<br>`/frontend-spec`<br>`/test-blueprint` | 技術棧、資料模型、API 合約、測試藍圖 | 一個 session 做得完，或在既有架構內 |
| **4** 拆解功能 | `/to-tickets` | 曳光彈票 + 阻塞邊 | 一張票就做完了 |
| **5** 建置 | `/implement`（內含 `/tdd`、`/code-review`） | 程式碼 | **不能跳** |
| **6** 驗收 | `/uat-cases`<br>`/browser-evidence` | 凍結編號的 TC 清單、證據 | 沒人要看證據 |
| **7** 上線交付 | `/wizard`<br>`/git-commit` → `/git-pr` → `/git-release` | 部署精靈、Runbook、release | 只有你自己用 |

> ⚠️ 第 7 站的部署沒有專用技能，是工具箱的已知缺口，用 `/wizard` 補。

---

## 依處境查

| 你現在的情況 | 打這個 |
|---|---|
| 不知道該用哪個 | `/compass` |
| 別人回報了 bug 或需求 | `/triage` → 匯入 `/implement` |
| 東西壞了但原因不明 | `/diagnosing-bugs` |
| 修完發現病根在架構 | `/improve-codebase-architecture` |
| 題目大到不知從何下手 | `/wayfinder` → 匯入 `/to-spec`（不能直接跳 `/implement`） |
| 一個設計問題在紙上定不下來 | `/prototype`（用完即丟） |
| 有個決定你答不出來，得問別人 | `/to-questionnaire` |
| 名詞開始一詞多義 | `/domain-modeling` |
| 想被質疑一個想法 | `/grilling` |
| agent 剛才那段話你沒聽懂 | `/wait-what` |
| Session 快滿了、或要換機器／交給別人 | `/handoff` |
| 要改 skill 或 `CLAUDE.md` | `/writing-for-agents` |
| 要在不改行為的前提下重整程式碼 | `/refactor` |
| 要畫圖 | `/diagram` |

---

## Session 邊界決策樹

完整版在 `.claude/skills/compass/PHASE-BOUNDARIES.md`。**由上往下，第一個 yes 就是答案。**

| # | 問題 | yes → |
|---|---|---|
| 1 | 能不能就留在這個 session？（下一階段需要這一階段當**原始資料**，或還有約 150k token 空間） | **繼續** |
| 2 | 這個 context 對接下來**完全無關**？ | **`/clear`** |
| 3 | 要換 harness／換目錄／交給別人／分岔側支線？ | **`/handoff`** |
| 4 | 任務夠明確，可以離開鍵盤讓它跑？ | **子代理** |
| 5 | 以上皆非 | **`/compact`**（帶指令，例如 `/compact 接下來要做 QA`） |

`/compact` 排最後不是因為它不好，是因為上面四個都更便宜或更精準。**從 `/compact` 開始的失敗模式**：新 session 對某個被摘要壓平的決定「很有自信地說錯」。

搞錯的代價是單向的 —— **清掉相關的 context，你會失去「為什麼」，看 diff 看不回來。**

---

## 技能分兩類

| | 誰能叫 | 例子 |
|---|---|---|
| **使用者觸發**（`disable-model-invocation: true`） | 只有你打字才會啟動 | `/to-spec`、`/to-tickets`、`/implement`、`/triage` |
| **模型觸發** | 你和 agent 都能叫，agent 判斷吻合會自己伸手 | `/tdd`、`/code-review`、`/grilling`、`/diagnosing-bugs` |

編排流程的是前者，裝紀律的是後者。

> ⚠️ **GitHub Copilot 不支援 `disable-model-invocation`。** 在 Copilot 上，編排型技能會被 agent 自行啟動。緩解方式是那些技能的 description 本來就寫成不帶觸發語的人話摘要，但那是降低機率，不是關掉開關。
>
> ⚠️ **Google Antigravity 同樣不支援。** 所以這條課程線實質是 Claude Code / Copilot 取向。

---

## 這門課沒用到的技能

不是不好，是這題用不到。知道它們存在，之後遇到再回來查：

| 技能 | 什麼時候會用到 |
|---|---|
| `/git-merge` | 合併分支且預期會有衝突 |
| `/implement-all` | 從追蹤器抓出所有可動工的票，派子代理平行跑 |
| `/management-frameworks` | 管理問題，不是工程問題 |
| `/svg-palette`、`/diagram` | 要畫圖給人看 |
| `/writing-hooks` | 要判斷某條規則該不該降成 hook |
| `/setup-skills` 以外的 repo 設定 | — |
