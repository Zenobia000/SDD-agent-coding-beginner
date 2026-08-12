# Repo 全貌：ai-vibe-coding-beginner

> 用途：後續 session 快速取得結構認知，不必重新掃全 repo。
> 本檔於 **2026-08-12** 依 `find` / `wc -l` / `grep` 實跑結果重建。
> 本分支是 Google Antigravity 原生版：workspace customization 只有 `AGENTS.md` 與 `.agents/`。

## 一句話定位

這是**教 Google Antigravity 的教材 repo**，不是應用程式：**零產品原始碼**。SmartTrip FX 是學生要從零長出來的專案，repo 內刻意不放 reference answer。`.agents/` 本身就是給學生觀察的活教具 —— 它既是工程 harness，也是第一冊的教材實例。

## 0. 頂層佈局

```text
ai-vibe-coding-beginner/
├── README.md               85 行   唯一導覽入口
├── ANTIGRAVITY.md         893 行   第一冊：官方元件速成（ch0–ch9 + 附錄 A）
├── BUILD.md               657 行   第二冊：SmartTrip FX 實戰（ch0–ch7）
├── AGENTS.md              123 行   目錄層級長期 context + 本 repo 專案契約
├── .agents/               52 檔    工程 harness（見第 2 節）
├── .githooks/              3 檔    第二層 guardrail（pre-commit / pre-push / README）
├── curriculum/README.md   202 行   講師手冊
├── docs/
│   ├── INSTALL.md          422 行   `agy` 安裝 SOP、環境需求、認證、解除安裝
│   ├── CLI_GUIDE.md        161 行   `agy` 日常操作與 `.agents/` 速查
│   ├── M0-M9_懶人包.md    1119 行   前一門 LLM/RAG 課的理論筆記，刻意不進主線
│   └── exports/              2 檔   ⚠️ 舊版 PDF/DOCX，尚未依 Antigravity 版重新匯出
├── LICENSE  .gitignore  .gitattributes
└── -M0-M9.pptx            330MB   舊課投影片（未追蹤於主線導覽）
```

## 1. 主線教材

學生路線固定：`README.md` → `ANTIGRAVITY.md` → `BUILD.md`（此順序在 `AGENTS.md:10` 與 `curriculum/README.md`〈教材 UX 規則〉被寫成硬性規則）。行數與角色見上面的頂層佈局；`docs/INSTALL.md` 是**課前作業**（安裝已從第一冊獨立出來，課堂不排安裝時間），`docs/CLI_GUIDE.md` 是隨查速查、不是要照走的章節。

### 第一冊教法（ch0–ch9 + 附錄 A，建議 2.5–3 小時）

ch0 agent loop / ch1 `AGENTS.md` 與 Rules / ch2 Customization 探索與五層優先序 / ch3 Skills / ch4 Subagents / ch5 Hooks / ch6 MCP / ch7 Plugins / ch8 Artifacts 與 Browser / ch9 元件選擇表與 `agy` 指令總表 / 附錄 A 從其他 AI CLI 移植（第一次學的人可整段跳過）。

每章固定六格：**你要學會**、**先看**、**照貼照跑**、**你應看到**、**通過**、**卡住就貼**。「照貼照跑」分兩種標籤：**終端機**（唯讀、無副作用、全部實跑過）與 **agy**（會呼叫模型、消耗 AI credits，一章一次就夠）。

全書標三種出處：**【已驗證】**（`agy` 1.1.12 命令輸出 / binary 字串 / 符號表）、**【依文件】**（只有 Google 文件這樣說）、**【⚠️ 未載明】**（查不到，不編答案）。ch8 全章無法在無圖形介面的機器驗證，已在章首標明。

### 第二冊規格與驗收

- **需求規格** `BUILD.md:227-245`；**驗收訊號** `BUILD.md:507-521` —— `python3 -m unittest discover -s tests -v` 全綠、`python3 -m compileall -q smarttrip_fx`、CLI 輸出必含
  `現金項目: ¥5,500 / 不確定項目: ¥1,800 / 建議換匯: ¥9,000 / 匯率燈號: GOOD`
  （反算：7300 × 1.1 = 8030 → 進位 9000；-2.75% → GOOD）
- **八章流程**：`:58` ch0 讀對規則 → `:143` ch1 `setup-project` → `:216` ch2 `grill-with-docs` → `:297` ch3 `to-spec` → `:367` ch4 `to-tickets` → `:424` ch5 `implement` ×3 → `:536` ch6 `code-review` + `security-review` → `:629` ch7 帶走方法
- **交付物**：`docs/agents/project.md`、`docs/specs/smarttrip-fx.md`、`.scratch/smarttrip-fx/issues/01-03`、`smarttrip_fx/`、`tests/`、`examples/kansai-3-days.json`、一個 Conventional Commit
- **Skill 呼叫方式** `BUILD.md:147-162`：斜線 `/setup-project` 有 binary 的間接證據（`agy --help` 的 `--disable-slash-commands` 原文寫 `Disable slash command and skill expansion in print mode`），但 TUI 行為在無 GUI 的機器無法實測，所以教材一律同時給純文字 fallback（「請使用 `<name>` skill」）。

## 2. `.agents/` harness

52 個檔案（不含 `__pycache__`）。架構總覽在 `.agents/README.md`；細節拆在 `.agents/context/harness-guardrails.md`（hooks 與 guard 行為）與 `.agents/context/harness-skills.md`（skills 分類、呼叫圖、subagents）。

### Skills：31 個

frontmatter 只有 `name` 與 `description` 兩欄，兩欄都必填 —— Antigravity 的 skill 沒有其他欄位。

- **user-invoked 11 個**（正文第一句約束「這個 skill 只在使用者明確要求時執行」）：`workflow`、`setup-project`、`wayfinder`、`grill-with-docs`、`to-spec`、`to-tickets`、`implement`、`triage`、`improve-codebase-architecture`、`create-pull-request`、`handoff`。**這 11 個是唯一寫了這句話的 skill**（`grep -l` 實測），其餘 20 個沒有，也不需要。
- **內部紀律 1 個**（正文約束為給其他 skill 內嵌）：`grilling`
- **兩者皆可 19 個**：其餘全部。完整清單與功能分層見 `harness-skills.md` 第 1 節。

`test` 與 `build-check` 是正常 skill，不是獨立元件 —— **Antigravity 沒有 commands 層**。兩者零判斷、零副作用，命令一律從專案契約讀，讀不到就回報 `unknown`。

多檔 skill 只有 3 個，附檔一律放 `references/`（官方建議目錄名）：`codebase-design`、`domain-modeling`、`tdd`。

### Subagents：4 個，`<name>/agent.md`

`code-explorer`（回報上限 20 行，被 `improve-codebase-architecture/SKILL.md:15` 呼叫）、`standards-reviewer` 與 `spec-reviewer`（雙軸互不可見，被 `code-review/SKILL.md:36` 平行呼叫）、`security-reviewer`（只在敏感面啟動，不併入雙軸）。frontmatter 只有 `name` + `description`。職責細節見 `harness-skills.md` 第 4 節。

`code-review/SKILL.md:43` 與 `security-review/SKILL.md:7` 都寫了 fallback：subagent 定義載不進來時改為分次獨立審查，且第二軸開始前不得讀第一軸結論。

### Rules：1 個

`.agents/rules/engineering-workflow.md`（57 行），frontmatter `trigger: always_on` + 空的 `glob` + `description`，因此**每個 session 都吃**。三個欄位取自 `agy` 1.1.12 建立新 rule 時寫出的樣板。

### Orchestration 鏈

`grill-with-docs → to-spec → to-tickets → implement → code-review`，中途分別內嵌 `grilling` / `domain-modeling`、`codebase-design`、`parallel-work` + `worktree-strategy`、`tdd` + `commit-message`，最後由 `code-review` 派出 `standards-reviewer` + `spec-reviewer`（敏感面才加 `security-reviewer`）。完整引用圖見 `harness-skills.md` 第 2 節。

⚠️ 這四段主線只寫在 `workflow/SKILL.md:18` 這個 router 與 `AGENTS.md:100`（〈Skills 的角色〉節）。個別 skill 的正文**不互相串接**（`to-spec` 不提 `to-tickets`、`to-tickets` 不提 `implement`），這是刻意的，讓每一段能單獨使用。

`implement` 收尾三步固定在 `implement/SKILL.md`：跑專案契約的 quality commands → `code-review`（沿用同一個 fixed point）→ 敏感變更加 `security-review`。

**共同入口**：orchestration skill 都先讀 `docs/agents/project.md`。31 個 skill 沒有一個硬編碼測試指令，一律去讀專案契約（三落點見 `.agents/README.md` 第 2 節）。

### 入口型 skill

`workflow`（router，只輸出三行：建議路徑／證據／翻盤條件，明令不自動啟動其他 user-invoked skill）、`wayfinder`（跨 session decision map，只解決策不實作，清晰後交回 `to-spec`）、`triage`（只處理外部進來的 issue/PR）、`handoff`（寫到 OS 暫存目錄，不進 repo）、`setup-project`（唯一產出 `docs/agents/project.md`）。

## 3. Guardrail 兩層

**第一層 — Antigravity hooks**（`.agents/hooks.json`）：單一具名 hook `smarttrip-guard`，只註冊 `PreToolUse`，兩個 matcher（`run_command|shell_exec|send_command_input`、`file_change|write_blob|edit_notebook|delete_directory`）都指向 `python3 ./hooks/guard.py`，timeout 10 秒。腳本分兩層：`guard.py`（157 行，協定翻譯）+ `guard_core.py`（256 行，工具中立的風險判定）。分層理由：hook 協定的欄位名會隨 host 改變，「什麼叫不可逆操作」不會。協定是讀 stdin camelCase JSON、**一律 exit 0**、靠 stdout 的 `decision` 表態，解析失敗即 fail-open。

⚠️ 官方規格把 `decision` 列為 required 且**未載明**省略時的行為，「`{}` = 不表態」是本 repo 的設計選擇與合理推論，尚未端到端實測 —— 不要把它寫成事實。

行為對照表維護在 `harness-guardrails.md` 第 2 節 —— **那是教材承諾，改 hook 就必須同步改表**，並用同檔第 4 節那三行可重跑的 stdin 樣本複驗。

**第二層 — git hooks**（`.githooks/`）：`pre-commit`（42 行）擋 staged 的真 `.env` / `*.pem` / `id_rsa*` / `secrets/` 與新增行的 secret；`pre-push`（24 行）對 `main` / `master` 用 `merge-base --is-ancestor` 要求快轉。啟用需每個 clone 手動 `git config core.hooksPath .githooks`（`README.md:30`），且 `README.md:37` 要求學生回讀確認。

**分層**：`.agents/hooks/` 管 Antigravity 的工具呼叫；`.githooks/` 管**人與任何 agent** 的 git 操作。換掉 AI 工具時第一層要重寫，第二層完全不用動。

## 4. 刻意設計，不是缺陷

探索時容易誤判為 bug 的 14 條（skill / subagent 的約束只是文字、workspace 沒有 `settings.json`、`docs/agents/project.md` 刻意不預建、教材命令不用 `rg` 等）整理在 [`known-non-bugs.md`](./known-non-bugs.md)。**動手改任何 `.agents/` 檔案前先看那份。**

## 5. 已知待修

| # | 位置 | 問題 | 為什麼還沒修 |
|---|---|---|---|
| 1 | `LICENSE:3,31-33` | copyright holder 與段落標題仍寫舊工具名，且描述的 `.claude/` 路徑在本分支不存在 | 授權檔改動需使用者裁決 |
| 2 | `.githooks/pre-commit:26-27`、`.githooks/README.md:3` | 註解指向已不存在的 `.claude/hooks/guard-write.py`，正確對照組是 `.agents/hooks/guard_core.py` 的 `SECRET_PATTERNS` | `.githooks/` 被列為本輪不得改動 |
| 3 | `docs/exports/` | PDF / DOCX 仍是舊版內容 | 需要重新匯出流程 |
