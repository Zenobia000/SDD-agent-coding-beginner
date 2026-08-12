---
trigger: always_on
glob:
description: 本 repo 的常駐工程紀律：先固定範圍與成功訊號、事實與推論分開、垂直切片推進、新行為走 TDD、只回報實際跑過的驗證、不自行 commit / push / 部署。
---

<!-- 移植註記（給教材維護者，不是給 agent 的指令）
- 這三個 frontmatter 欄位（`trigger` / `glob` / `description`）是 `agy` 1.1.12 binary 建立新 rule 時
  寫出的樣板（binary 字串常數，已驗證）。`trigger` 的 `always_on` 與 `model_decision` 兩個值皆有 binary 佐證；
  官網另列 `glob` 與 `manual`，其中 `manual` 在 binary 中查無，教材不要依賴。
- `trigger: always_on` 表示無條件載入，`glob` 因此留空。
- ⚠️ Google 隨 binary 出貨的 `docs/rules.md` 只寫了目錄式的 `AGENTS.md` / `GEMINI.md`，
  沒有記載 `.agents/rules/*.md` 的欄位語法；本檔的 frontmatter 依 binary 樣板撰寫，尚未端到端實測。
- ⚠️ workspace 必須先被信任才會載入 `.agents/`：`~/.gemini/antigravity-cli/settings.json` 的
  `trustedWorkspaces` 不含本 repo 路徑時，本規則會靜默失效。第一次開啟 workspace 要接受信任提示。
- 官網對單一 rule 檔的字元上限是 12,000；本檔遠低於此。
-->

# 實戰工程工作流

這套規則只定義工程紀律，不替使用者決定產品需求。使用者當下的明確指令永遠優先；不要讓其他專案文件擴大或改寫使用者指定的範圍。

## 每次開始

1. 先讀 `docs/agents/project.md`（若存在），取得本專案的驗證指令、issue tracker 與文件位置。
2. 只讀和任務直接相關的 `CONTEXT.md`、ADR、規格與程式碼。不要為了「了解全貌」把整個 repo 灌進 context。
3. 把事實與推論分開。事實附檔案行號、命令輸出或來源；缺證據就說尚未驗證。
4. 先固定本輪範圍、成功訊號與比較基準，再修改檔案。

## 執行原則

- 可以從環境查到的事實就自己查；只有真正的產品或取捨決策才問使用者，而且一次問一題並附建議答案。
- 功能以可獨立驗證的垂直切片前進。每一片都要縮短回饋時間，不要先做完所有層再一起驗證。
- 修 bug 先建立能抓到同一個症狀的紅燈命令，再推測根因。
- 新行為優先用 TDD；重構必須由既有綠燈保護，且不能把行為改動混進同一輪。
- 只報告自己實際跑過的驗證。未跑的檢查明講原因，不能寫成「已通過」。
- 並行前先畫 dependencies、read/write sets 與 side effects；共享 working tree 的 subagent 只做唯讀工作，並行寫入使用獨立 worktrees。
- commit message 必須來自 staged diff 並遵循 repo 歷史；不同意圖先拆 commit，不用一段訊息掩蓋混合變更。
- 不主動 commit、push、開 PR、部署、建立或修改外部 issue；只有使用者明確要求或核准後才做。

## 技能分層

`.agents/skills/` 底下的 skill 分兩層。**這是本 repo 的約定，不是工具強制的。**

- **流程型**：`grill-with-docs`、`to-spec`、`to-tickets`、`implement`、`workflow`、`handoff`、`triage`。
  只在使用者明確要求時啟動；不要自己決定開跑，也不要從一個流程型 skill 偷偷跳到另一個流程型 skill。
- **紀律型**：`tdd`、`diagnosing-bugs`、`codebase-design`、`code-review`、`commit-message` 等。
  只提供可重用紀律，符合情境時可自行載入。流程型 skill 可以呼叫紀律型 skill，反向不行。

不知道該走哪條路時，請使用者指名使用 `workflow` skill 取得一條建議，不要自行套一整套儀式。

⚠️ **兩個已知能力落差，不要當成已強制**

- Antigravity 的 skill frontmatter 只支援 `name` 與 `description`，沒有「禁止模型自行啟動」的欄位。
  上面「只在使用者明確要求時啟動」是文字約束，不是結構性保證。
- 使用者能否用 `/<skill-name>` 直接叫用 workspace skill，官方文件未載明。
  教材與 skill 之間一律用「請使用 `<skill-name>` skill」的自然語言指稱，不要寫成斜線命令。
