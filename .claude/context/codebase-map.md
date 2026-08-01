# Repo 全貌：ai-vibe-coding-beginner

> 由 code-explorer subagents 平行探索後彙整，關鍵宣稱已逐條回查原始碼驗證。
> 用途：後續 session 快速取得結構認知，不必重新掃全 repo。

## 一句話定位

這是**教 Claude Code 的教材 repo**，不是應用程式：61 個檔案、**零產品原始碼**。SmartTrip FX 是學生要從零長出來的專案，repo 內刻意不放 reference answer。`.claude/` 本身就是給學生觀察的活教具 —— 它既是工程 harness，也是第一冊的教材實例。

## 1. 主線教材

學生路線固定：`README.md` → `CLAUDE-CODE.md` → `BUILD.md`（此順序在 `curriculum/README.md:156` 被寫成硬性 UX 規則）。

| 檔案 | 行數 | 讀者 | 角色 |
|---|---:|---|---|
| `README.md` | 60 | 學生 | 唯一導覽入口，連出的 6 個目標全部存在 |
| `CLAUDE-CODE.md` | 716 | 學生 | 第一冊：官方元件速成，**全書唯讀**（:5） |
| `BUILD.md` | 567 | 學生 | 第二冊：SmartTrip FX 實戰 |
| `curriculum/README.md` | 165 | 講師 | 時間表、巡場、檢查題；無替代路線 |
| `docs/M0-M9_懶人包.md` | 1119 | 課外 | 前一門 LLM/RAG 課的理論筆記，零連結、刻意不進主線 |

### 第一冊教法

ch0 agent loop、ch1 CLAUDE.md/Rules/Auto memory、ch2 Settings/Permissions/Plan mode、ch3 Skills、ch4 Subagents、ch5 Hooks、ch6 MCP、ch7 Plugins/Agent teams/Commands/Output styles、ch8 元件選擇表（:606-619）。每章固定六格版型（:31-38）。

全書只實際執行四處本機唯讀命令：`python3 -m json.tool`(:204)、`sed` 讀 frontmatter(:276)、hook stdin 自測(:399-406)、`claude mcp list`(:455)。只啟動一個 Skill（`/workflow`:285）與一個 Subagent（`code-explorer`:338）。MCP 章刻意不建 `.mcp.json`(:450)，Plugins/Agent teams 只做選型比較(:526,537)。

### 第二冊規格與驗收

- **需求規格**：`BUILD.md:168-191` —— 輸入 JSON schema、payment 三值、現金小計 = cash_only + unknown、+10% 後無條件進位到 1000、±2% 匯率燈號、錯誤走 stderr + exit code 2。
- **驗收訊號**（可 pass/fail）：`:440-454` —— `python3 -m unittest discover -s tests -v` 全綠、`python3 -m compileall -q smarttrip_fx`、CLI 輸出必含
  `現金項目: ¥5,500 / 不確定項目: ¥1,800 / 建議換匯: ¥9,000 / 匯率燈號: GOOD`
  （反算：7300 × 1.1 = 8030 → 進位 9000；-2.75% → GOOD，與教材一致）
- **七章流程**：`:43` ch0 讀規則 → `:102` ch1 `/setup-project` → `:157` ch2 `/grill-with-docs` → `:235` ch3 `/to-spec` → `:303` ch4 `/to-tickets` → `:359` ch5 `/implement` ×3 → `:465` ch6 `/code-review` + `/security-review` → `:542` ch7 帶走方法
- **交付物**：`docs/agents/project.md`、`docs/specs/smarttrip-fx.md`、`.scratch/smarttrip-fx/issues/01-03`、`smarttrip_fx/`、`tests/`、`examples/kansai-3-days.json`、一個 Conventional Commit

## 2. `.claude/` harness

### Skills：29 個，依 frontmatter 分三類

- **user-invoked**（`disable-model-invocation: true`）**11 個**：`workflow`、`setup-project`、`wayfinder`、`grill-with-docs`、`to-spec`、`to-tickets`、`implement`、`triage`、`improve-codebase-architecture`、`create-pull-request`、`handoff`
- **model-only**（`user-invocable: false`）**1 個**：`grilling`
- **兩者皆可**（無欄位）**17 個**：`tdd`、`code-review`、`security-review`、`codebase-design`、`diagnosing-bugs`、`domain-modeling`、`parallel-work`、`worktree-strategy`、`prototype`、`research`、`branch-name`、`commit-message`、`release-notes`、`react-doctor`、`resolving-merge-conflicts`、`running-local-docker-stack`、`adhd-dev-mode`

### Subagents：4 個，frontmatter 一致

全部 `tools: Read, Glob, Grep, Bash` + `disallowedTools: Write, Edit, NotebookEdit` + `model: inherit` + `permissionMode: plan` —— 結構性唯讀，不是靠 prompt 約束。

| agent | 呼叫者 | 特點 |
|---|---|---|
| `code-explorer` | `improve-codebase-architecture/SKILL.md:16` | 回報上限 20 行 |
| `standards-reviewer` | `code-review/SKILL.md:39` | 唯一有 `skills: [codebase-design]`，agent→skill 反向連結 |
| `spec-reviewer` | `code-review/SKILL.md:40` | 無 spec 就不啟動；禁止用 code 反推需求 |
| `security-reviewer` | `security-review/SKILL.md:8`、`code-review/SKILL.md:42` | 只在敏感面啟動，不併入雙軸 |

### Orchestration 鏈

```
/grill-with-docs → /to-spec → /to-tickets → /implement → code-review
   ↓ grilling       ↓ codebase-  ↓ parallel-   ↓ tdd        ├ standards-reviewer
   ↓ domain-modeling  design      work +       ↓ commit-     ├ spec-reviewer
   決策摘要          .scratch/     worktree-     message      └ security-reviewer
   (不寫檔)          <feature>/    strategy                     (僅敏感面)
                     spec.md      .scratch/<feature>/issues/<NN>-<slug>.md
```

`/implement` 收尾三步固定在 `implement/SKILL.md:27-31`：跑 project.md 的 quality commands → `code-review`（沿用步驟 1 的 fixed point）→ 敏感變更加 `security-review`。

**共同入口**：四個 orchestration skill 都先讀 `docs/agents/project.md`（`grill-with-docs:12`、`to-spec:14`、`to-tickets:12`、`implement:14`）。29 個 skill 沒有一個硬編碼測試指令，一律去讀這份專案契約（`.claude/README.md:70`）。

### 入口型 skill

- `/workflow`（`workflow/SKILL.md:36-44`）：router，只輸出三行（建議路徑／證據／翻盤條件），明令不自動啟動其他 user-invoked skill
- `/wayfinder`：跨 session 的 decision map，只解決策不實作，清晰後交回 `/to-spec`
- `/triage`：只處理外部進來的 issue/PR；`/to-tickets` 產出的票不再 triage
- `/handoff`：寫到 OS 暫存目錄，不進 repo
- `/setup-project`：唯一產出 `docs/agents/project.md`

### Commands：skills 的單檔變體，不是第五層

`.claude/commands/<name>.md` 與 `.claude/skills/<name>/SKILL.md` 建立的是同一個 `/<name>`，差別只在單檔 vs 目錄。本 repo 只在**零判斷、零副作用、不需要附檔**的情境用單檔形式，目前兩個：`test`、`build-check` —— 都是 Quality command 的直接 shortcut，命令一律從專案契約讀，不假設框架。凡是需要判斷的一律留在 `skills/`（`.claude/README.md:69-71`）。

### Rules 載入方式

`.claude/rules/engineering-workflow.md` 無 frontmatter，根 `CLAUDE.md` 內無 `@` import，`settings.json` 也無 rules 欄位 —— 由 Claude Code 的 `.claude/rules/` 目錄機制自動載入，且未設 `paths`，因此**每個 session 都吃**（`.claude/README.md:35`）。

## 3. Guardrail 兩層

**第一層 — Claude Code hooks**（`.claude/settings.json:24-48`）
只註冊 PreToolUse 一個 event，兩個 matcher：`Bash` → `guard-bash.py`、`Edit|Write` → `guard-write.py`，各 timeout 5s。無 PostToolUse / SessionStart / Stop。
另有 `permissions.allow` 9 條唯讀白名單(:5-15) 與 `permissions.deny` 5 條(:16-22，擋 Read `.env`/`*.pem`/`id_rsa*`/`secrets/**`)。

協定：讀 stdin JSON、**一律 exit 0**，靠 stdout 的 `hookSpecificOutput.permissionDecision`（deny/ask）表態；JSON 解析失敗即 fail-open。

行為對照表維護在 `.claude/README.md:56-59` —— **那是教材承諾，改 hook 就必須同步改表**。

**第二層 — git hooks**（`.githooks/`）
`pre-commit` 擋 staged 的真 `.env` 與新增行的 secret；`pre-push` 對 main/master 用 `merge-base --is-ancestor` 要求快轉。
啟用需每個 clone 手動 `git config core.hooksPath .githooks`（`README.md:18`）。

**分層**：`.claude/hooks/` 管 Claude 的工具呼叫；`.githooks/` 管**人與任何 agent** 的 git 操作（`.claude/README.md:64`）。

## 4. 刻意設計，不是缺陷

探索時容易誤判為 bug，先記在這裡避免重複踩：

- **`.scratch/` 被 gitignore**（`.gitignore:33-34`）：註解明寫「Claude workflow 暫存；正式 spec 放 docs/specs/」。tickets 本來就不是 commit 交付物，`BUILD.md:514` 的 `git add -A` 只收產品碼是正確行為。
- **`docs/agents/project.md` 不在 repo**：由 `/setup-project` 於課堂產生，各 skill 有 fallback。
- **`.mcp.json`、`plugins/`、`output-styles/` 皆不存在**：對齊 `CLAUDE.md`「最小元件能解決就停止」。`commands/` 只有兩個零判斷的 shortcut，不承載流程。
- **`docs/exports/` 未被 gitignore**：`.docx`/`.pdf` 已 tracked，符合教材契約。
- **`.gitattributes:2` 全庫 LF**：讓 `.githooks/*` 在 WSL 下 shebang 不壞。
