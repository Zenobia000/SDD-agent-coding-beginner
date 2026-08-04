# CLAUDE.md

本 repo 的最高目標有兩個，缺一不可：

1. 讓第一次接觸 Claude Code 的學生，照 [`CLAUDE-CODE.md`](./CLAUDE-CODE.md) 理解官方元件的責任與選用時機。
2. 讓學生照 [`BUILD.md`](./BUILD.md) 完成本課專屬、可執行、可測試、可 review 的 SmartTrip FX。

## 教材契約

- 固定學生路線：`README.md` → `CLAUDE-CODE.md` → `BUILD.md`。
- 第一冊依 Claude Code 官方元件組織，以唯讀練習為主；不能取代第二冊專案實戰。
- 第二冊固定題目 SmartTrip FX、固定 Python 3.11+ standard library CLI、固定驗收結果。
- SmartTrip FX 的 AI / code 邊界：AI 或人產行程 JSON；程式負責驗證、金額計算與匯率燈號。
- 核心產品不接 live LLM、即時匯率 API、資料庫、登入、Web UI 或部署。
- 不建立 `labs/`、reference answer 或預建成品；範例、問答與檢查直接放在對應手冊。
- `.claude/` 是可觀察的實戰 harness，不要求為了教學湊齊 MCP、Plugin 或 Agent team。
- `docs/M0-M9_懶人包.md` 保留原課程理論，但不插入照貼照跑主線。
- 根目錄只放兩冊主線、`CLAUDE.md` 與授權/設定檔。課外參考放 `docs/`，衍生檔放 `docs/exports/`。

修改第一冊時先核對 Anthropic 最新官方文件。社群文章可以改善教法，但不能覆蓋官方元件名稱、路徑、scope、命令或穩定性標示。修改第二冊時不得刪除 project contract、需求訪談、spec、tickets、TDD、review、security review 與 commit 的完整學習迴圈。

## 專案契約

> 這是**教材 repo 本身**的契約，對應 `.claude/CLAUDE.template.md` 三落點機制的第②落點。
> 學生的 SmartTrip FX 契約由 `BUILD.md` 第 1 章產出到 `docs/agents/project.md`；
> 兩者是不同專案的契約，不共用檔案。**不要在本 repo 預先建立 `docs/agents/project.md`**，
> 那會讓第 1 章的 `test -f` 驗收直接通過，練習失效。

**Quality commands**

- Focused test: `unknown` — 本 repo 產出物是 Markdown 與 harness 設定，無測試框架
- Full test: `unknown`
- Typecheck / Lint / Format check: `unknown` — 未設定，不要假裝已驗證
- Harness check（實際可跑，改動 `.claude/` 或 `.githooks/` 後執行）:
  - `python3 -m py_compile .claude/hooks/guard-bash.py .claude/hooks/guard-write.py`
  - `python3 -c "import json; json.load(open('.claude/settings.json'))"`
  - `bash -n .githooks/pre-commit .githooks/pre-push`

**Issue tracker**

- Type: `local`
- Location: `.scratch/<feature>/issues/`（`.gitignore` 已忽略 `.scratch/`，不進版控）

**Git workflow**

- Default branch: `main`
- Branch style: `<type>/<short-description>`
- Commit style: Conventional Commits，body 分 WHY / WHAT / IMPACT
- PR template: 無

**Domain docs**

- Glossary、ADRs: 尚未建立，第一個內容確定時才產生，不預先 scaffold
- Specs: `.scratch/<feature>/spec.md`（不進版控）。
  **`docs/specs/` 是學生領地**——`BUILD.md` 第 3 章要學生把 SmartTrip FX 規格寫進 `docs/specs/smarttrip-fx.md`。
  harness 自身的工程規格不得放進去，否則學生 clone 後會在自己的工作目錄看到無關文件。

**Risk boundary**

- 需再次確認: 刪除資料、force push、部署、寫入外部系統、註冊 MCP server
- 永不自動化: 繞過 `.claude/hooks/` 或 `.githooks/`

**Verified on**

`2026-08-04` — 以上只列出從檔案或命令輸出驗證過的事實；標 `unknown` 者為真的不存在。

## 元件責任不能混用

- `CLAUDE.md` 與 Rules：長期 context；不是安全強制。
- Settings 與 Permissions：設定與工具授權範圍。
- Skills：按需載入的程序知識與重複 workflow。
- Subagents：隔離 context 的委派工作。
- Hooks：事件驅動、可測試的 guardrail 或 automation。
- MCP：Claude Code 的外部工具與資料連接；不等於產品 runtime API。
- Plugins：Skills、Subagents、Hooks、MCP 等元件的封裝與分發。
- Agent teams：多個可互相溝通的獨立 session；目前屬實驗性功能。

最小元件能解決就停止，不因為功能存在而要求學生全部啟用。

## 工程核心

開始任何改動前，先固定：

1. 這輪的 scope 與 out of scope。
2. 可以 pass / fail 的成功訊號。
3. fixed point 與停止條件。

從 repo、文件或命令能查到的事實自行查。只有會改變教材、產品行為或風險的決策才問使用者，而且一次問一題、先給推薦答案。

以可獨立驗證的 vertical slice 前進。新產品行為使用 TDD：保留紅燈證據、寫最小實作、轉綠後才重構。教材命令必須能在 macOS、Linux 或 Windows WSL 的 repo 根目錄執行。只回報實際跑過的檢查，未跑或無法驗證的項目必須明說。

## Skills 的角色

`.claude/skills/` 同時是官方 Skill 的教材實例與可移植工程工具箱；它不是每位學生必須逐一執行的清單。

SmartTrip FX 的完整 idea-to-code 路線：

```text
/grill-with-docs → /to-spec → /to-tickets → /implement
```

不知道下一步時用 `/workflow` 取得一條建議。不要在使用者沒要求時，自行啟動另一條 user-invoked workflow 或產生外部副作用。

## 回覆方式

- 使用繁體中文，技術術語保留英文。
- 結論先行，只保留一條主要建議。
- 區分已確認、主要假設與未知；不要把推測寫成根因。
- 教學回答優先給「照貼內容、預期形狀、通過條件」。
- 每次回覆結尾給一個可執行的下一步。

## 安全底線

`.claude/hooks/` 會攔截敏感檔案、疑似 credential 與高風險 shell 操作；`.githooks/` 保護 commit 與 push。不要繞過 hook，也不要自行 commit、push、開 PR、部署、註冊 MCP server 或寫入外部系統，除非使用者明確要求。

修改教材時保留工作目錄中與本輪無關的既存內容，不自行刪除、還原或納入提交。同一路徑連續失敗三次就停止微調，回報共同失敗模式並重新檢查最初假設。
