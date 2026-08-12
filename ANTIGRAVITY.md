# Google Antigravity 官方元件速成手冊

這是本課第一冊，也是官方元件速成唯一要照著走的文件。你不需要先背 prompt，也不需要先做完整專案；全書用同一個案例 **SmartTrip FX**，帶你親手辨認 Antigravity 的官方元件、觀察載入方式，並知道什麼時候該用哪一個。核心練習全部是唯讀：你會執行查詢與安全的 hook 測試，但不會建立 App、不會新增外部連線、不會對外寫入、不會 commit，也不會 push。

**安裝不在這本書裡。** 還沒裝好 `agy` 的話，先做完 [`docs/INSTALL.md`](./docs/INSTALL.md) 再回來；日常操作與指令速查另有 [`docs/CLI_GUIDE.md`](./docs/CLI_GUIDE.md)。

## 完成後，你要能回答

1. `AGENTS.md` 與 `.agents/rules/*.md` 分別該放什麼，為什麼不能混成一大份 prompt。
2. Antigravity 怎麼探索 customization、五層優先序誰贏，以及為什麼「沒接受信任提示」會讓整個 `.agents/` 靜默失效。
3. Skill 的 frontmatter 為什麼只有兩欄，`description` 要怎麼寫才會被啟用。
4. 什麼工作留在主 agent，什麼工作交給 subagent。
5. 為什麼 Hooks 是 workspace 裡**唯一**能做硬性攔截的元件。
6. MCP 是 agent 的外部連接，不等於產品執行時的 API client。
7. 什麼時候才值得做 Plugin。
8. Artifacts 與 Browser 各解決什麼，哪些只有圖形介面才有。

## 全書共用案例

SmartTrip FX 是一個旅費工具。它可能需要：專案長期遵守「金額計算必須 deterministic」、一條可重複的需求訪談到實作流程、一位只讀的探索者先找出匯率程式與測試、一個永遠攔截 credential 與高風險命令的閘門、讓 agent 工作時查外部文件、把成熟設定分享給其他 repo。每一章用同一個案例回答一個問題，不要求你把產品做出來。

## 本書怎麼用

每章固定六格：**你要學會**（唯一目標）、**先看**（先讀哪個本地檔案）、**照貼照跑**（標「終端機」貼進 shell，標「agy」貼進 CLI 對話框）、**你應看到**（意思一致即可）、**通過**（可打勾的條件）、**卡住就貼**（整段貼給 agent）。

Antigravity 目前有三個官方說法來源，彼此**會互相矛盾**，所以本書一律標出處：**【已驗證】** 是本機 `agy` 1.1.12 的命令輸出、binary 字串或符號表直接證實；**【依文件】** 是只有 Google 文件這樣說、本機無法實測；**【⚠️ 未載明】** 是查不到 —— 本書不會替它編一個答案。

網站與 binary 衝突時一律以 binary 為準，並把差異寫出來。本機是一台**沒有圖形介面**的 Linux 主機，凡 IDE / 桌面應用程式的行為都只能是【依文件】。「照貼照跑：終端機」每一段都實跑過、無副作用；「照貼照跑：agy」會呼叫模型、消耗 AI credits，一章一次就夠。建議時間 2.5–3 小時。

---

## 第 0 章｜先看懂 Antigravity 在做什麼

### 你要學會

Antigravity 是 **agent-first** 的開發平台，不是補全外掛。它反覆進行一個 agent loop：讀 context、判斷下一步、呼叫工具、觀察結果，再決定是否繼續。你負責給目標、邊界與驗收；agent 負責在授權範圍內執行。

同一套 agent 能力有四個入口（【依文件】，來源是內建 skill `antigravity_guide`）：

| 介面 | 是什麼 | 本機能否驗證 |
|---|---|---|
| **Antigravity IDE** | 以 VS Code 為底的獨立 IDE：Editor 內補全 / Inline Command / Sidebar Agent | ❌ 需圖形介面 |
| **Agent Manager** | 派工與監看的中控台：Inbox、Workspaces、Knowledge、Browser、Settings | ❌ 需圖形介面 |
| **Browser** | agent 可操作的整合瀏覽器，用來實際點開頁面驗收 UI | ❌ 需圖形介面 |
| **`agy` CLI** | 終端機介面，讀同一份 `.agents/` 設定 | ✅ 本書全用它 |

分工只有一句話：**設定共用，介面不同。** IDE 與 CLI 都探索專案根目錄的 `AGENTS.md` 與 `.agents/`（【依文件】），所以你在本書寫的設定，換到有桌面的機器打開 IDE 一樣生效。IDE 多的是視覺化 diff、Browser 與 Artifacts 面板（第 8 章）；CLI 多的是可放進 CI 與 SSH 的非互動模式。

> ⚠️ **第一次在這個 repo 啟動 `agy` 會問要不要信任這個 workspace，一定要選信任。**
> 未信任的 workspace，`.agents/` 底下**全部不載入，而且不報錯**（機制見第 2 章）。

### 先看

`README.md`、`AGENTS.md`、`.agents/rules/engineering-workflow.md`

### 照貼照跑：終端機

```bash
git --version
agy --version
git rev-parse --show-toplevel
git status --short
```

前兩個要顯示版本（本書寫作時 `agy` 是 `1.1.12`）。第三個印出 repo 根目錄 —— 記住它，customization 探索就是走到這裡為止。全新 clone 的第四個通常沒有輸出；若有既存改動，保留它們，不要為了上課刪除或還原。接著執行 `agy` 啟動。

### 照貼照跑：agy

```text
先不要修改任何檔案，也不要 commit。
請根據實際 repo，用 5 行告訴我：
1. 這份教材的學習目標。
2. 你啟動時已經取得哪些 project context。
3. 你能使用哪幾類工具。
4. 哪些動作會被 .agents/hooks.json 檢查。
5. 現在最小的下一步。
每一行都附來源路徑；找不到就寫「尚未驗證」。
```

### 你應看到

目標是學會官方元件，不是立刻生成 SmartTrip FX；agent 能讀檔案、跑允許的查詢、看到 Git 狀態；`AGENTS.md` 提供長期 context、`.agents/hooks.json` 註冊工具閘門；它沒有開始改檔。

### 通過

- [ ] 能用一句話說出 agent loop：讀 context → 行動 → 看結果 → 繼續或停止。
- [ ] 能說出 IDE、Agent Manager、Browser 與 `agy` 讀同一份 `.agents/` 設定。
- [ ] agent 的回答有本地路徑，不是只靠記憶描述這個 repo。
- [ ] `git status --short` 沒有因這個練習多出新檔案。

### 卡住就貼

```text
停止推測。只讀 AGENTS.md、.agents/hooks.json 與
.agents/rules/engineering-workflow.md，重新回答；不要修改檔案。
```

官方延伸：[Antigravity Docs](https://antigravity.google/docs)、[CLI Reference](https://antigravity.google/docs/cli/reference)

---

## 第 1 章｜`AGENTS.md` 與 Rules：每次要記得什麼

### 你要學會

把內容放在正確的記憶層，不要把所有知識塞進 `AGENTS.md`。Antigravity 的長期 context 有兩種載體，差別在**有沒有 frontmatter**：

| 元件 | 位置 | frontmatter | 何時載入 |
|---|---|---|---|
| `AGENTS.md` / `GEMINI.md` | 任何目錄（含 repo 根目錄） | **不支援**【依文件】 | 對所在目錄與**所有子目錄永遠 active** |
| `.agents/rules/*.md` | **平放**的 `.md`，不是子目錄 | **支援**，可條件觸發 | 依 `trigger` 決定 |
| Skill | `.agents/skills/<name>/SKILL.md` | 支援（只有兩欄） | 相關時才載入（第 3 章） |

兩個檔名等價：binary 內 `AGENTS.md` 6 次、`GEMINI.md` 7 次（【已驗證】）。本 repo 統一用 `AGENTS.md`。

> Antigravity 只讀 `AGENTS.md` / `GEMINI.md` 與 `.agents/`。binary 內查無其他 AI CLI 的 context 檔名或設定目錄路徑字串（【已驗證的負面結論】）——**別的工具的設定搬過來不會被讀到**。

`agy` 建立新 rule 時寫出的樣板就是三欄（【已驗證】，binary 字串常數）：

```yaml
---
trigger: always_on
glob:
description:
---
```

`trigger` 的四個值信心不同：`always_on`（無條件載入）與 `model_decision`（模型讀 `description` 決定）是**【已驗證】**；`glob`（依檔案樣式）是**【依文件】**，有 `yaml:"glob"` tag 佐證；`manual`（使用者 `@` 提及）是**【依文件】**，而且**測不到同形式的證據**：把 binary 抽字串後比對「獨立出現的 trigger 值」，`always_on` 命中 2 行、`model_decision` 命中 1 行，`manual` 則沒有以同樣形式出現（它在 binary 裡的 99 次命中全是 `manual` 當英文單字或其他識別碼的一部分）—— 不要依賴這個值。單一 rule 檔上限 12,000 字元（【依文件】；內建規格與 binary 都查不到這個數字）。

**階層探索與去重**：agent 從工作目錄**往上走到 repo root**（含 `.git` 的目錄），沿路收集 `AGENTS.md`、`GEMINI.md` 與 `.agents/rules/*.md`（【依文件】）。所有 customization 依解析後的檔案路徑去重：同一輪對話裡同一檔案只注入一次，就算同時符合多個觸發條件也一樣。

**`AGENTS.md` 是 context，不是強制執行器。** 像「絕不能寫入 `.env`」這類要求不能只寫一句提醒。Antigravity 的 workspace **沒有** `settings.json`（第 2 章），能在版控裡做硬性攔截的只剩 `hooks.json`。

### 先看

`AGENTS.md`、`.agents/rules/engineering-workflow.md`、`.agents/AGENTS.template.md`

### 照貼照跑：終端機

```bash
sed -n '1,5p' .agents/rules/engineering-workflow.md
find . -name 'AGENTS.md' -not -path './.git/*'
ls -1 .agents/rules
```

第一段要看到 `trigger` / `glob` / `description`。第二段列出探索路徑上所有 `AGENTS.md`。第三段確認 rules 是**平放的 `.md`** —— 這點和 skills、agents 不同。

### 照貼照跑：agy

```text
只讀分析，不要修改檔案。
比較 AGENTS.md、.agents/rules/engineering-workflow.md、
.agents/skills/workflow/SKILL.md：
- 哪些內容每個 session 都需要？
- 哪些內容只有做特定任務才需要？
- 哪一條安全規則不能只靠文字提醒？
請用三列表格回答：內容、正確元件、理由。
```

### 你應看到

回覆規則與專案邊界屬於 `AGENTS.md` 或 `always_on` 的 rule；`workflow` 的路由程序只在需要選路時載入，屬於 Skill；敏感檔案與破壞性操作要靠 hook，而不是期待模型永遠記住。

### 通過

- [ ] 能解釋「無 frontmatter 的 `AGENTS.md` 永遠 active」與「有 `trigger` 的 rule 可條件載入」的差別。
- [ ] 知道 rules 平放、skills 與 agents 是子目錄。
- [ ] 不把文字 instructions 說成安全沙箱。
- [ ] 沒有把 `AGENTS.md` 塞成一份包山包海的巨型 prompt。

### 卡住就貼

```text
請只讀 AGENTS.md 與 .agents/rules/engineering-workflow.md 的 frontmatter，
把「永遠載入」「條件載入」「按需載入」分成三層，不要混成同一層，也不要修改檔案。
```

官方延伸：[Rules & Workflows](https://antigravity.google/docs/rules-workflows)

---

## 第 2 章｜Customization 探索與優先序

### 你要學會

Antigravity 不需要你註冊設定檔，它**自己去找**。搞懂它從哪找、誰蓋過誰，比記住任何單一欄位都重要。

**四種 workspace root 名稱**（【依文件】）：`.agents/`、`.agent/`、`_agents/`、`_agent/`。

> ⚠️ binary 內查無 `.agent/`（單數）字串（【已驗證的負面結論】）。文件說它向後相容但實證不足 —— **一律用 `.agents/`**。

**七種 customization**，`CUSTOMIZATION_TYPE_*` 的完整列舉（【已驗證】，binary 符號）：

| 類型 | 檔案 / 目錄 | 章節 |
|---|---|---|
| `RULE` | `AGENTS.md`、`.agents/rules/*.md` | 第 1 章 |
| `SKILL` | `.agents/skills/<name>/SKILL.md` | 第 3 章 |
| `AGENT` | `.agents/agents/<name>/agent.md` | 第 4 章 |
| `HOOKS` | `.agents/hooks.json` | 第 5 章 |
| `MCP` | `mcp_config.json` | 第 6 章 |
| `PLUGIN` | `.agents/plugins/<name>/plugin.json` | 第 7 章 |
| `WORKFLOW` | **【⚠️ 未載明】存放位置** | 見下 |

`WORKFLOW` 確實存在於 CLI（binary 有 `CUSTOMIZATION_TYPE_WORKFLOW`、`GetWorkflows`、`WorkflowSpec`，【已驗證】），但查無任何 `*/workflows` 的 workspace 路徑字串，內建規格也沒有 workflows 章節。**本書不會告訴你它放哪裡，因為官方沒說。** 另有 **Sidecars**（binary 內有 Sidecar 相關符號，官方 sitemap 有 `/docs/sidecars`），workspace 設定檔名與 schema【⚠️ 未載明】，本課用不到。

**五層載入優先序**，同名衝突時高的蓋掉低的（【依文件】）：① Workspace Project（從 CWD 往上走到 repo root 找到的 `.agents/`）→ ② Declared Configurations（workspace 的 `skills.json` / `plugins.json`）→ ③ Global Discovery（`~/.gemini/config/`）→ ④ Built-in Customizations（隨 `agy` 出貨的內建 skills）→ ⑤ Global Declared Configurations。**專案永遠贏過全域，全域永遠贏過內建。**

**Progressive disclosure**（【依文件】）：Skills 預設**只注入 name 與 description**，正文只在模型或使用者決定啟用時才讀進來；Rules 只有 `always_on` 無條件載入，`model_decision` 比照 skill 處理。這直接決定第 3 章的重點 —— `description` 寫壞，skill 就永遠不會被啟用。

### 兩個必須知道的陷阱

**一：`trustedWorkspaces` 是硬性 gate（【已驗證】）。** 不在 `~/.gemini/antigravity-cli/settings.json` 的 `trustedWorkspaces` 清單裡的 workspace，`.agents/` **完全不載入且不報錯**。實測在未信任的 repo 放合法 `hooks.json`，log 仍是 `loaded 0 named hooks from 0 hooks.json file(s)`。

**二：命名慣例在同一個目錄裡不一致（【已驗證】）。** `hooks.json` 的 key 是 **camelCase**（protojson，例如 `conversationId`）；`skills.json` / `plugins.json` 的 key 是 **snake_case**（例如 `include_only`）。

另外，**沒有 workspace 層級的 `settings.json`**（binary 內 `.agents/settings.json` 出現 **0 次**，【已驗證的負面結論】）。`.agents/` 只放 customization，不放 settings。這是相對於其他 agent 工具的能力落差：權限只能靠 `hooks.json` 的 PreToolUse guard 或使用者本機設定，不能寫成可版控的專案設定檔。

### 先看

`.agents/README.md`

### 照貼照跑：終端機

```bash
git rev-parse --show-toplevel
ls -1 .agents
ls -1 ~/.gemini/config/ 2>/dev/null || echo "(全域設定目錄尚未建立)"
python3 - <<'PY'
import json, pathlib
p = pathlib.Path.home() / ".gemini/antigravity-cli/settings.json"
print(json.load(p.open()).get("trustedWorkspaces", "(尚未信任任何 workspace)")
      if p.exists() else "(settings.json 尚未產生，先跑過一次 agy)")
PY
```

### 你應看到

第一段印出的 repo root 就是探索往上走的終點；`.agents` 底下有 `rules`、`skills`、`agents`、`hooks.json`、`mcp_config.json`；最後一段印出的清單**必須包含這個 repo 的絕對路徑**。沒有的話回第 0 章接受信任提示，否則後面所有章節都會「設定明明在、卻沒生效」。

### 通過

- [ ] 能背出五層優先序的前三層：workspace → declared → global。
- [ ] 能解釋 progressive disclosure 為什麼讓 `description` 變成 skill 最重要的一行。
- [ ] 知道 `hooks.json` 用 camelCase、`skills.json` 用 snake_case。
- [ ] 這個 repo 的路徑出現在 `trustedWorkspaces` 裡。

### 卡住就貼

```text
不要修改設定。請只根據 .agents/ 的實際內容回答：
這個 workspace 提供了哪幾種 customization？每一種是「永遠載入」還是「按需載入」？
最後指出一個「檔案存在但可能不生效」的原因。
```

官方延伸：[Skills](https://antigravity.google/docs/skills)、[Rules & Workflows](https://antigravity.google/docs/rules-workflows)

---

## 第 3 章｜Skills：把重複工作變成按需能力

### 你要學會

Skill 是一個**資料夾**，入口為 `SKILL.md`。因為 progressive disclosure，agent 只在相關時載入正文，比把完整流程塞進 `AGENTS.md` 省 context。

```text
.agents/skills/<skill_name>/
├── SKILL.md      # 必要
└── scripts/ examples/ resources/ references/   # 皆為選用子目錄
```

Skill 有**三層安放位置**，`agy` 的 `/skills` 介面自己會印出來（【本機實測 2026-08-12】）：

| 層 | 路徑 | 適用範圍 |
|---|---|---|
| **Workspace** | `<repo>/.agents/skills/<name>/SKILL.md` | 只在這個 repo；**進版控，team 共享**。本課用這一層 |
| **Global** | `~/.gemini/antigravity-cli/skills/<name>/SKILL.md` | 這台機器的所有專案 |
| **Shared** | `~/.gemini/skills/<name>/SKILL.md` | 這台機器，與其他吃 `~/.gemini/` 的 Google 工具共用 |

> ⚠️ 官方網站把 global 層寫成 `~/.gemini/config/skills/`，與 CLI 介面實際印出的
> `~/.gemini/antigravity-cli/skills/` **不一致**，而且網站完全沒提 Shared 這一層。
> 以 CLI 介面印的為準。

四個選用子目錄各自的用途：`scripts/` 放可執行的輔助腳本、`examples/` 放參考實作、`resources/` 放素材或模板、`references/` 放龐大的細部文件。

frontmatter **只有兩個欄位，兩個都必填**（【依文件】）：`name`（唯一識別，小寫加連字號）與 `description`（**agent 判斷要不要啟用的唯一依據**，必須同時寫清楚 **what** 與 **when**）。

```yaml
---
name: my-specialized-skill
description: >-
  說明這個 skill 做什麼、什麼時候該用。用第三人稱。
---
```

### 這裡有一個能力落差，不要假裝等價

Antigravity 的 **Skill** frontmatter 只有 `name` 與 `description`，**沒有任何能限制「誰可以啟動它」的欄位**。binary 裡確實有 `yaml:"disable-model-invocation"`（【已驗證】），但它屬於 **`WorkflowSpec` 而不是 `SkillSpec`** —— 而 workflow 的存放位置【⚠️ 未載明】。

結果：**Antigravity 的 workspace skill 沒有結構性的「只有使用者能呼叫」開關。** 本 repo 的處置是在 `SKILL.md` 正文第一段用文字約束（例如 `workflow` 開頭那句「這個 skill 只在使用者明確要求時執行」）。這是**軟約束**，不是保證。

至於能不能用 `/<skill-name>` 直接叫用：**【已驗證（間接）】** `agy --help` 的 `--disable-slash-commands` 原文是 `Disable slash command and skill expansion in print mode` —— binary 自己把「slash command」與「skill expansion」並列，這是支持斜線可以展開 skill 的正面證據。但 TUI 的實際互動無法在無圖形介面的機器實測，**斜線送不出去時一律改用純文字**：「使用 `tdd` skill」。本書兩種寫法都給。

### 寫出會被啟用的 description

`TDD 流程` 只有 what、沒有 when；`幫助開發` 太籠統，什麼都像等於什麼都不像。本 repo `tdd` 的寫法才是對的：「以 red-green-refactor 完成新功能或 bug regression。當使用者要求 test-first、提到 TDD/red-green、要新增可觀察行為，或 implement skill 需要逐片建立回饋迴圈時使用。」—— what + when + 具體觸發語。

其餘官方最佳實務（【依文件】）：`SKILL.md` 保持精簡，龐大文件放 `references/` 用相對連結指過去；複雜命令序列封裝成 `scripts/`；一定要寫「怎麼驗證這步成功了」；不要教 agent 通用程式知識。

### 先看

`.agents/skills/workflow/SKILL.md`、`.agents/skills/tdd/SKILL.md`

### 照貼照跑：終端機

```bash
ls -1 .agents/skills | wc -l
sed -n '1,4p' .agents/skills/workflow/SKILL.md
sed -n '1,4p' .agents/skills/tdd/SKILL.md
ls -1 .agents/skills/tdd
```

第一段應印出 `31`。第二、三段只看得到兩個欄位。第四段是 progressive disclosure 的實作：`tdd` 的細節被推到 `references/`，主檔只留決策。

### 照貼照跑：agy

```text
使用 workflow skill。我想替 SmartTrip FX 加入即時匯率，但還沒決定資料源、
失敗時的 fallback，也還沒決定核心流程能不能連網。先不要實作，
只推薦一條路並告訴我什麼條件會讓建議改變。
```

### 你應看到

回覆應只有三件事：建議的 skill / 路線、根據目前資訊的理由、會讓建議翻盤的條件。它很可能先建議需求訪談（`grill-with-docs`），而不是直接建立 API client。Skill 的重點不是能不能打斜線，而是「可重複的程序知識」。

### 通過

- [ ] 找得到 `SKILL.md` 與它的兩欄 frontmatter。
- [ ] 能說出為什麼 `description` 要同時寫 what 與 when。
- [ ] 知道 Antigravity 的 skill **沒有** `disable-model-invocation`，那是 workflow 的欄位。
- [ ] `workflow` 只推薦路線，沒有自行啟動另一條需要副作用的流程。
- [ ] 在互動模式 `agy` 裡打 `/skills`，標題顯示的數字 = 本 repo 的 workspace skill 數 + 2 個內建。
      【本機實測 2026-08-12】本 repo 是 31 + 2 = **`33 skills`**。
- [ ] 知道**同一件事用 `agy -p` 驗會失敗** —— print mode 不載入 workspace customization，
      只看得到 2 個內建 skill。驗收 harness 一律用互動模式，細節見
      [`docs/INSTALL.md` §5.2](./docs/INSTALL.md)。

### 卡住就貼

```text
請重新讀 .agents/skills/workflow/SKILL.md 的 frontmatter 與「輸出」段落。
只依它規定的三行格式回答，不要實作、不要寫檔。
```

官方延伸：[Skills](https://antigravity.google/docs/skills)

---

## 第 4 章｜Subagents：把大量探索隔離出去

### 你要學會

Subagent 有自己的 system prompt 與獨立 context。它適合會產生大量搜尋結果的探索、review 或研究；主 agent 最後只接收摘要，避免被中間雜訊塞滿。

**這是本書不確定性最高的一章**，下面每一條都標了信心。

**路徑：agent 是「目錄」，不是平放的檔案。** binary 內與 skills 並列的 workspace 樣板（【已驗證】）是 `{workspace}/.agents/agents/{agent_name}/`（注意結尾斜線）對 `{workspace}/.agents/skills/{skill_name}/SKILL.md`。

定義檔名是 **`agent.md`**（**高信心推論**：binary 有 `writing agent.md`、`formatting agent.md` 字串常數，且與 `SKILL.md` 出現在同一段 rodata；但 `agy agents` 零輸出，無法端到端實測）。也支援 **`agent.json`**（【已驗證】符號表有 `loadJSONAgent` / `saveJSONAgent`），完整 schema【⚠️ 未載明】。

frontmatter 一樣只有兩欄，正文就是這個 subagent 的 system prompt（【已驗證】，binary 建立新 agent 時寫出的樣板）：

```yaml
---
name: code-explorer
description: 什麼情況該派這個 agent
---
```

### ⚠️ 兩個必須知道的風險

1. **`agent.md` 可能被伺服器端 feature flag 擋掉。** binary 內有相鄰字串 `enable-markdown-agents`、`markdown agents are not allowed`（【已驗證】），flag 由伺服器下發。你的帳號是開是關【⚠️ 未載明】。真的載不進來時只剩 `agent.json`。
2. **`agy agents` 永遠印空字串。** 在已信任的真 repo 與測試 repo 都是 exit 0、零輸出（【已驗證】），同時 `agy models` 正常 —— 不是認證問題。**這個子命令不能拿來當驗收。**

### frontmatter 只有兩欄，沒有權限欄位

binary 全部 87 個 `yaml:"..."` struct tag 中查無 `tools`、`disallowedTools`、`permissionMode`、`color`、`allowed-tools`（【已驗證的負面結論】）。也就是說 **subagent 的「唯讀」無法宣告在檔案裡**，只能寫進正文。想限制本 session 的自主程度用 CLI 旗標 `agy --mode plan`，那是 session 層級、不是 agent 層級。

**能力落差：** 本 repo 四個 subagent 的唯讀性質只剩正文的文字約束。要硬性阻擋寫入，目前唯一可驗證的做法是第 5 章的 `hooks.json` PreToolUse guard。

相關工具與入口：`invoke_subagent`（派出 subagent）與 `browser_subagent`（瀏覽器專用）都在 binary 實測的 121 個 tool 清單內（【已驗證】）。`manage_subagents`（action = `list` / `kill` / `kill_all`）**只在 binary 字串中出現，不在那 121 個 tool 清單裡**，不要當成可直接呼叫的工具。CLI 用 `agy --agent <name>` 指定本 session 的 agent，TUI 內用 `/agents` 與 `/tasks` 查看。

### 先看

`.agents/agents/code-explorer/agent.md`、`.agents/agents/security-reviewer/agent.md`

### 照貼照跑：終端機

```bash
ls -1 .agents/agents
ls -1 .agents/agents/code-explorer
sed -n '1,4p' .agents/agents/code-explorer/agent.md
```

要看到四個**目錄**、每個目錄裡一個 `agent.md`、frontmatter 只有 `name` 與 `description`。

### 照貼照跑：agy

```text
請派 code-explorer subagent，只讀探索這個 repo：
找出 workflow skill 如何連到其他 skills，以及哪一個檔案負責阻擋高風險工具操作。
主對話只保留 8 行內摘要，每一項附 path:line。不要修改檔案。
```

### 你應看到

主 agent 明確派出 `code-explorer` 而不是把搜尋內容全灌回主對話；摘要指出 `.agents/skills/workflow/SKILL.md` 的路由關係與 `.agents/hooks/guard.py`（與判斷核心 `guard_core.py`）；沒有檔案被修改。

> 派不出來、或 agent 說找不到這個 subagent，很可能就是上面的 `enable-markdown-agents` 風險。這時**不要**假裝它成功了 —— 記下現象，改用主 agent 做同一件事，然後往下一章走。

### 通過

- [ ] 能說出 subagent 的價值是 context isolation，不是「名字比較專業」。
- [ ] 知道 agent 是**目錄**形式，frontmatter 只有 `name` + `description`。
- [ ] 知道 `agy agents` 零輸出不能當驗收，也知道 `agent.md` 有 feature flag 風險。
- [ ] `git status --short` 沒有因探索多出改動。

### 卡住就貼

```text
請明確委派給 workspace subagent `code-explorer`。
它只可讀取與搜尋；主 session 只接收有 path:line 的 8 行摘要。
如果找不到這個 subagent，直接說「找不到」，不要改用其他 agent 假裝完成。
```

官方延伸：[CLI Features & Subagents](https://antigravity.google/docs/cli/features)

---

## 第 5 章｜Hooks：把「每次都必須做」變成事件閘門

### 你要學會

Hook 在 agent loop 的特定事件自動執行外部命令。因為 workspace 沒有 `settings.json`，**`hooks.json` 是這個 repo 裡唯一能做 deterministic 硬性攔截的元件。**

最容易寫錯的一點：**top-level key 是 hook 名稱，不是事件名稱。**

```json
{
  "smarttrip-guard": {
    "enabled": true,
    "PreToolUse": [
      {
        "matcher": "run_command|shell_exec|send_command_input",
        "hooks": [
          { "type": "command", "command": "python3 ./hooks/guard.py", "timeout": 10 }
        ]
      }
    ]
  }
}
```

`"smarttrip-guard"` 是你自己取的**具名 hook**。不同來源（workspace、各個 plugin）的具名 hook 針對同一事件會合併、依序執行；整組要暫時停掉就設 `"enabled": false`。

| 事件 | 何時觸發 | matcher | 結構 |
|---|---|---|---|
| `PreToolUse` | 工具執行前 | 工具名 | **Grouped**：`matcher` + `hooks` 包一層 |
| `PostToolUse` | 工具完成後 | 工具名 | **Grouped** |
| `PreInvocation` | 呼叫模型前 | 忽略 | **Flat**：直接放 handler 陣列 |
| `PostInvocation` | 工具呼叫結束後 | 忽略 | **Flat** |
| `Stop` | 執行迴圈要終止時 | 忽略 | **Flat** |

`matcher` 是 regex：`"*"` 或 `""` 全部、`"run_command"` 精準、`"browser_.*"` 前綴。handler 欄位：`type`（預設 `"command"`，目前**只**支援這一種）、`command`（必填，Unix 走 `sh -c`、Windows 走 `cmd /c`，`~` 會展開）、`timeout`（預設 30 秒）。

> 🔴 **working directory 是 `hooks.json` 所在的目錄**，也就是 `.agents/` —— 不是 repo root，也不是腳本自己的目錄。所以本 repo 寫 `python3 ./hooks/guard.py`。這也是 `guard.py` 開頭要手動把自己的目錄補進 `sys.path` 的原因，否則 `import guard_core` 會在某些環境靜默失敗。

### PreToolUse 的輸入輸出契約

所有 JSON key 都是 **camelCase**（protojson）。stdin 長這樣 —— `toolCall`（含 `name` 與 `args`）加上每個事件都會帶的共通欄位：

```json
{ "toolCall": { "name": "run_command", "args": { "CommandLine": "npm test" } },
  "stepIdx": 19, "conversationId": "...", "workspacePaths": ["/path/to/workspace"],
  "transcriptPath": "...", "artifactDirectoryPath": "...", "modelName": "auto" }
```

stdout 的 `decision` 有**五個**值：`allow`（直接放行）、`deny`（立刻硬擋）、`ask`（問使用者，尊重「Always Allow」快取）、`force_ask`（一定要問，忽略快取）、`deny_unless_prior_grant`（除非已有授權否則擋）。前四個是【依文件】，第五個是**【已驗證】**（binary 出現 3 次）—— Google 隨 binary 出貨的內建規格只列了四個，是**它漏寫**。

選用欄位：`reason`（顯示給使用者）、`permissionOverrides`（臨時授權）、`overwrite`（**淺層**合併進 tool call 參數，可改寫實際執行的命令）。其他事件輸出：`PostToolUse` → `{}`；`PreInvocation` / `PostInvocation` → `{"injectSteps":[{"ephemeralMessage":"..."}]}`（後者另可加 `terminationBehavior`）。

`Stop` 的 `decision` 有**三個**值（【已驗證】，binary 的 schema tag 是 `enum=stop,enum=continue,enum=block`）：`stop` 放行終止、`continue` 與 `block` 都會擋下終止並重入迴圈。搭配 `reason` 說明原因。

> **本 repo 的 guard 沒有意見時輸出 `{}`，不是 `{"decision":"allow"}`。**
> ⚠️ 證據等級要說清楚：Google 內建規格把 `decision` 列為 **required**，binary 的 schema tag 也是
> `jsonschema:"required,enum=…"`，但**沒有載明**省略 `decision`（也就是輸出 `{}`）時 runtime 會怎麼做。
> 「`{}` = 不表態」是本書與本 repo 的**設計選擇 + 合理推論**，尚未端到端實測。
> 選它而不選 `allow` 的理由是失敗方向：猜錯只會多問一次；猜 `allow` 錯了會直接蓋過使用者的
> permission 設定，等於把整個授權機制關掉。

### 先看

`.agents/hooks.json`、`.agents/hooks/guard.py`、`.agents/hooks/guard_core.py`

### 照貼照跑：終端機

先確認 JSON 合法並印出具名 hook 的名字，再把假資料送進 hook（**不會真的建立 `.env`**）：

```bash
python3 -c "import json; d=json.load(open('.agents/hooks.json')); print('named hooks:', ', '.join(d))"
printf '%s\n' '{"toolCall":{"name":"file_change","args":{"AbsolutePathUri":"file:///tmp/x/.env","NewContent":"DEMO=value"}},"workspacePaths":["/tmp/x"]}' | python3 .agents/hooks/guard.py
printf '%s\n' '{"toolCall":{"name":"file_change","args":{"AbsolutePathUri":"file:///tmp/x/.env.example","NewContent":"DEMO=fake-value"}},"workspacePaths":["/tmp/x"]}' | python3 .agents/hooks/guard.py
printf '%s\n' '{"toolCall":{"name":"run_command","args":{"CommandLine":"rm -rf /"}},"workspacePaths":["/tmp/x"]}' | python3 .agents/hooks/guard.py
```

### 你應看到

```text
named hooks: smarttrip-guard
{"decision": "deny", "reason": "已擋下寫入 /tmp/x/.env。……"}
{}
{"decision": "deny", "reason": "已擋下可能刪除系統、家目錄或整個工作區的遞迴強制刪除。……"}
```

第三行是 `{}` —— 假值範例檔通過，而且 guard 正確地**不表態**，沒有濫發 `allow`。（guard 的輸出**不含結尾換行**，所以在終端機裡三段 JSON 會黏在同一行，這是正常的。）

### 通過

```bash
test "$(printf '%s\n' '{"toolCall":{"name":"file_change","args":{"AbsolutePathUri":"file:///tmp/x/.env","NewContent":"DEMO=value"}},"workspacePaths":["/tmp/x"]}' | python3 .agents/hooks/guard.py | python3 -c 'import json,sys; print(json.load(sys.stdin).get("decision",""))')" = "deny"
```

- [ ] 上面命令 exit 0。
- [ ] 沒有真的建立 `.env`（`ls /tmp/x` 應為 no such file）。
- [ ] 能說出 `hooks.json` 的 top-level key 是 hook 名稱，不是事件名稱。
- [ ] 能說出 hook 的 working directory 是 `.agents/`。

### 卡住就貼

```text
請只讀 .agents/hooks.json 與 .agents/hooks/guard.py，
找出 hook 期待的 stdin JSON 形狀、working directory，以及 deny 的輸出格式；
不要真的寫入任何檔案。
```

官方延伸：[Hooks](https://antigravity.google/docs/hooks)、[Permissions](https://antigravity.google/docs/permissions)

---

## 第 6 章｜MCP：讓 agent 連接外部工具與資料

### 你要學會

MCP（Model Context Protocol）讓 agent 連接外部服務、資料庫與工具。**MCP server 提供能力；Skill 教 agent 何時、如何組合這些能力。** 兩者可以一起用，但不是同一件事。

| 範圍 | 路徑 | 信心 |
|---|---|---|
| 全域 | `~/.gemini/config/mcp_config.json` | **【依文件】** 內建規格明列，本機確實存在 |
| Plugin | `plugins/<name>/mcp_config.json` | **【依文件】** 內建規格明列，plugin 啟用時生效 |
| Workspace | `.agents/mcp_config.json` | **【⚠️ 未載明】** 見下 |

> ⚠️ 內建規格的 MCP 章節**只列了全域與 plugin 兩處**。binary 有裸字串 `mcp_config.json` 與 `CUSTOMIZATION_TYPE_MCP`，但查無 `.agents/mcp_config.json` 完整路徑字串 —— 對照之下 `.agents/hooks.json` 是有的（【已驗證】）。本 repo 在 `.agents/mcp_config.json` 放了一份**全部 `disabled: true`** 的樣板當閱讀材料，不要當成「一定會載入」的保證。

```json
{
  "mcpServers": {
    "sqlite-helper": { "command": "python3", "args": ["-m", "your_mcp_server"],
                       "env": { "DB_READONLY": "true" } },
    "remote-service": { "serverUrl": "https://mcp.example.invalid/sse" }
  }
}
```

兩種 transport（【依文件】）：**Stdio**（本機執行檔，用 `command` / `args` / `env`）與 **SSE**（遠端，用 `serverUrl`）。其他可用欄位：`cwd`、`headers`、`authProviderType`、`oauth`、`disabled`、`disabledTools`。

> 從 Gemini CLI 遷移時，`url` / `httpUrl` 要改寫成 **`serverUrl`**，否則不會連上。TUI 裡用 `/mcp` 查看目前連上的 server 與工具。

| 情境 | 正確方向 |
|---|---|
| agent 工作時要查公司內部的匯率規範 | **MCP** |
| SmartTrip FX 成品在使用者執行程式時要取得即時匯率 | **產品本身的 API client** —— 不會因為你用 Antigravity 開發就變成 MCP |
| 團隊想固定「查規範 → 比對程式 → 產 review」的重複流程 | **MCP + Skill** |

### 先看

`.agents/mcp_config.json`

### 照貼照跑：終端機

```bash
python3 -m json.tool .agents/mcp_config.json
ls -1 ~/.gemini/config/mcp_config.json 2>/dev/null || echo "(全域 MCP 設定尚未建立)"
```

樣板裡兩個 server 都是 `"disabled": true`，這一章不會真的連上任何外部服務。

### 照貼照跑：agy

```text
先不要新增或啟用任何 MCP server。請判斷以下三件事各該用什麼：
1. agent 在開發時要查公司內部的匯率規範。
2. SmartTrip FX 成品在使用者執行程式時，要取得即時匯率。
3. 團隊想固定「查規範 → 比對程式 → 產 review」的重複流程。
只能從 MCP、產品 API client、Skill、MCP + Skill 中選，逐項說明理由。
```

### 你應看到

三個答案分別是 MCP、產品 API client、MCP + Skill。agent 不應該建議你現在就去註冊 server。

### 通過

- [ ] `python3 -m json.tool .agents/mcp_config.json` 成功解析。
- [ ] 能分辨「提供工具」與「教會工作流程」。
- [ ] 能分辨 agent 的 MCP 與產品執行時 integration。
- [ ] 知道遠端 server 的欄位叫 `serverUrl`，不是 `url`。
- [ ] 沒有為了完成本章新增 server 或把 token 寫進版控。

### 卡住就貼

```text
不要設定或連線。請先區分「Antigravity 開發環境需要的工具」與
「最終產品 runtime 需要的功能」，再判斷 MCP 是否適用。
```

官方延伸：[MCP](https://antigravity.google/docs/mcp)

---

## 第 7 章｜Plugins：把一整套元件打包分發

### 你要學會

當一組 Skills、Rules、Hooks 或 MCP 設定已在多個 repo 重複使用，才考慮封裝 Plugin。Plugin 是 **package / distribution layer**，不會帶來新的推理能力。

```text
.agents/plugins/<plugin_name>/
├── plugin.json                                  # 必要：manifest，也是「這是一個 plugin」的標記
└── mcp_config.json  hooks.json  rules/*.md  skills/<name>/SKILL.md   # 皆為選用
```

`plugin.json` 最小就一行 `{ "name": "team-developer-kit" }`。`name` 其實是**選用**的，省略時預設用目錄名；另可加 `"disabled": true` 讓 plugin 出貨時預設關閉。

啟用狀態記錄在 `config.json` 的 `plugins` map，key 是 plugin 的**目錄名**（【依文件】）：`{ "plugins": { "my-plugin": { "enabled": false } } }`。`config.json` 永遠贏過 `plugin.json` 的宣告，所以你的選擇在重裝或更新後仍然保留。被停用的 plugin 還會出現在清單裡（方便你開回來），但它帶的 customization 一個都不會載入。

`agy plugin` 的完整子命令（【已驗證】，`agy help plugin` 實測）：

```text
list                   List imported plugins
import [source]        Import plugins from gemini or claude   ← 官網未載明
install <target>       Install a plugin (supports plugin@marketplace)
uninstall <name>       Uninstall a plugin
enable <name>          Enable a plugin
disable <name>         Disable a plugin
validate [path]        Validate a plugin                      ← 官網未載明
link <mp> <target>     Generate link to a marketplace         ← 官網未載明
help                   Show this help
```

`import [source]` 收 `gemini` 或 `claude` 兩種來源，讀的是那些工具的 **plugin manifest 格式**（【已驗證】，binary 內有對應的 plugin 目錄字串），**不是**它們的 workspace customization 目錄。換句話說 `import` 只搬 plugin，不會幫你把別的工具的整套設定翻譯成 `.agents/`。本 repo 目前是直接放進專案的 `.agents/` harness，還不到必須封裝 Plugin 的階段。

### 先看

`.agents/README.md`

### 照貼照跑：終端機

```bash
agy plugin list
agy help plugin
```

`agy plugin list` 在乾淨環境印出 `No imported plugins.` —— 空清單是正確結果；`agy help plugin` 印出上面九個子命令。

### 照貼照跑：agy

```text
只做架構判斷，不要建立檔案：
如果這套 .agents 設定只在本 repo 使用、確定要讓第 2 個 repo
長期共用，以及要提供給 20 個團隊安裝，三個階段各應維持
workspace customization、暫時手動複製，還是封裝 Plugin？
請各給一個理由與升級條件。
```

### 你應看到

單一 repo 維持 workspace 的 `.agents/` 最簡單；第二個 repo 確定長期共用就開始封裝 Plugin，手動複製只適合短期驗證；多團隊安裝、版本化與更新用 Plugin 與 marketplace 管理分發。它不會因為「官方有功能」就建議全部啟用。

### 通過

- [ ] `agy plugin list` 能正常執行；空清單也算通過。
- [ ] 能說出 Plugin 是 package / distribution layer。
- [ ] 知道 `plugin.json` 的 `name` 是選用的，開關記在 `config.json`。
- [ ] 沒有為了完成本章安裝任何 plugin。

### 卡住就貼

```text
先用「是否跨 repo 發佈」「是否需要版本化更新」兩個問題判斷。
不要因為功能存在就建議啟用；請指出最小可用方案。
```

官方延伸：[Plugins](https://antigravity.google/docs/plugins)

---

## 第 8 章｜Artifacts 與 Browser

> **本章全部無法在本機驗證。** 這是一台沒有圖形介面的 Linux 主機（`DISPLAY` 與 `WAYLAND_DISPLAY` 皆未設定，也不是 WSL）。下面的內容來自 binary 字串與官方文件，**不是**本機實測結果。辨識它們即可，不必今天就跑起來。

### 你要學會

Antigravity 把「agent 做完事之後留下什麼」與「agent 怎麼親眼確認 UI 對不對」拆成兩組能力。

**Artifacts：agent 的工作產出物。** 與 agent 產出相關的 `ARTIFACT_TYPE_*` 有五個（【已驗證】，binary 符號）：`IMPLEMENTATION_PLAN`、`TASK`、`WALKTHROUGH`、`OTHER`、`UNSPECIFIED`。（binary 裡另有 `ARTIFACT_TYPE_MODEL_NAME`、`ARTIFACT_TYPE_TUNING_PIPELINE_TEMPLATE_URI` 等來自其他 proto 的同名前綴常數，與 agent artifact 無關。）兩份最重要的（【已驗證】，binary 內建 prompt 字串）：

- **`{artifactDirectoryPath}/implementation_plan.md`** —— Planning mode 產出的技術設計文件，給使用者審核批准。固定含 User Review Required、Open Questions、Proposed Changes、Verification Plan 四段。
- **`{artifactDirectoryPath}/walkthrough.md`** —— 完成後的總結：改了什麼、測了什麼、驗證結果。相關的後續工作要**更新既有的**，不要一直開新的。

`artifactDirectoryPath` **不是 IDE 專屬** —— 它就是第 5 章 hook stdin payload 裡的那個欄位。目錄名依介面而不同（【依文件】）：CLI 是 `.gemini/antigravity-cli/`、Antigravity 2.0 是 `.gemini/antigravity/`、IDE 是 `.gemini/antigravity-ide/`。**Artifact Review Mode** 控制 agent 什麼時候停下來要你看（【依文件】）：`always-proceed` / `agent-decides` / `asks-for-review`。

**Browser：讓 agent 親眼看畫面。** binary 實測的 121 個工具裡，瀏覽器相關的就佔 20 幾個（【已驗證】）：

```text
open_browser_url          list_browser_pages        read_browser_page
browser_click_element     browser_input             browser_press_key
browser_scroll            browser_select_option     browser_resize_window
capture_browser_screenshot           capture_browser_console_logs
execute_browser_javascript           browser_get_network_request
browser_subagent
```

價值在於**閉環驗收**：agent 改完前端可以自己打開頁面、點按鈕、截圖、讀 console log 與 network request，再回報結果，而不是只說「我改好了」。安全面由 **Browser Allowlist** 限制可導航的網域（【依文件】）。

**Agent Manager 的五個入口**（【依文件】，binary 內建的使用指南）：**Inbox**（通知與 agent 的緊急請求）、**Workspaces**（依專案分組對話與知識）、**Knowledge**（agent 的內部文件與專案慣例庫）、**Browser**（上面那組能力的整合檢視）、**Settings**（Secure Mode、Review Policy、Terminal Auto-Execution、Browser Tools 與 allowlist）。改完檔案後上方會出現 **Review Changes** 的 diff 檢視。CLI 與 IDE 的差別只有三處：`.agents/` customization 與 Artifacts 檔案兩邊完全相同；視覺化 diff review 與 Browser 只有 IDE 有；非互動 / CI（`agy -p`）只有 CLI 有。

### 先看

`.agents/hooks/guard.py` —— 看它的 docstring 怎麼描述 hook stdin 的欄位

### 照貼照跑：終端機

```bash
ls -1 .gemini/antigravity-cli 2>/dev/null || echo "(尚未產生 artifact；要跑過一次會做事的 agent 才會出現)"
grep -n 'artifactDirectoryPath' .agents/hooks/guard.py || echo "(本 repo 的 guard 沒用到這個欄位，但 hook payload 一定會帶)"
```

### 你應看到

兩段都印出括號裡的訊息，這是正常的 —— 你到目前為止都在做唯讀練習，沒有讓 agent 產生任何 artifact，本 repo 的 guard 也只用到 `toolCall` 與 `workspacePaths`。真正跑過一次會做事的 agent 之後，`.gemini/antigravity-cli/` 底下才會出現東西。

⚠️ **artifact 實際落在哪個子目錄名【⚠️ 未載明】。** 本書只證實了 hook payload 帶 `artifactDirectoryPath` 欄位、以及 CLI 用 `.gemini/antigravity-cli/` 這個目錄名；子目錄叫什麼要等你在有 GUI／有實際產出的環境自己看。

### 通過

- [ ] 能說出 `implementation_plan.md` 與 `walkthrough.md` 各在什麼時機產生。
- [ ] 知道 `artifactDirectoryPath` 會出現在 hook payload 裡，不是 IDE 專有的概念。
- [ ] 能說出 Browser 的價值是閉環驗收，而不是「多一個瀏覽器」。
- [ ] 知道本章沒有在這台機器驗證過，換到有桌面的機器要重新確認。

### 卡住就貼

```text
不要嘗試開啟瀏覽器或 GUI。請只根據 .agents/hooks/guard.py 的 docstring
與 Antigravity 的 hook 契約，說明 artifactDirectoryPath 是什麼、由誰產生。
```

官方延伸：[Browser Automation & Testing](https://antigravity.google/docs/ide/browser)、[Permissions](https://antigravity.google/docs/permissions)

---

## 第 9 章｜元件選擇表與 `agy` 指令總表

### 你要學會

官方元件不是九個獨立玩具，它們共同服務一條短迴圈：`探索 → 計畫 → 實作 → 驗證 → 提交`，並用證據回頭修正。

| 你現在缺什麼 | 先選什麼 |
|---|---|
| 每次都要知道的專案背景 | `AGENTS.md` |
| 只在某些檔案或某些情境才成立的紀律 | `.agents/rules/*.md`（`trigger: glob` 或 `model_decision`） |
| 可重複但只在特定任務使用的流程 | Skill |
| 大量搜尋、研究或 review 的隔離 context | Subagent |
| 每次事件都必須執行的 deterministic guardrail | Hook |
| agent 工作時需要外部工具或資料 | MCP |
| 一整套元件要版本化分發 | Plugin |
| 要讓 agent 親眼確認 UI | Browser（需圖形介面） |
| 把這輪工作交代清楚 | Artifact（`walkthrough.md`） |

最小元件能解決就停止，不要因為功能存在就要求自己全部啟用。

### `agy` 指令總表（【已驗證】，`agy --help` 與 `agy help` 實測）

**常用 flags**：`-c` / `--continue`（接續最近對話）、`--conversation <id>`（依 ID 恢復）、`--mode`（`accept-edits` 或 `plan`）、`--model`、`--effort`（`low`/`medium`/`high`）、`--agent <name>`、`--add-dir`（可重複）、`--sandbox`、`--log-file`（除錯 customization 載入很好用）。**非互動 / CI**：`-p` / `--print` / `--prompt`（跑一個 prompt 就結束）、`-i` / `--prompt-interactive`（跑完留在 session）、`--output-format`（`text`/`json`/`stream-json`）、`--json-schema`、`--print-timeout`（預設 `5m0s`）、`--disable-slash-commands`、`--new-project` / `--project`。

⚠️ `--dangerously-skip-permissions` 會自動核准所有工具請求，**不要在教學環境用**。沙箱底層是 Linux `nsjail` / macOS `sandbox-exec` / Windows `AppContainer`（【依文件】）。

**Subcommands**：`agy models`（列出模型）、`agy plugin` / `plugins`（第 7 章）、`agy changelog`、`agy install`（設定環境路徑與 shell）、`agy update`、`agy help <sub>`；`agy agent` / `agy agents` 名義上列出可用 agents，但**本機實測零輸出，不能當驗收**。

**Slash commands**（TUI 內，【依文件】）：`/resume`（`/switch`）、`/rewind`（`/undo`）、`/rename`、`/permissions`、`/model`、`/skills`、`/mcp`、`/agents`、`/tasks`、`/diff`、`/open`、`/usage`、`/keybindings`、`/statusline`、`/logout`。快捷鍵 `Ctrl+J` 跳到待批准項目、`Ctrl+K` 立即批准；離開用 `Ctrl+D Ctrl+D`、`/exit` 或 `/quit`（【內建規格】`antigravity_guide/references/cli.md` §1）。

⚠️ 這份清單是**官方文件的清單**，不是你那台機器的清單。內建規格 `cli.md` §2 明說權威來源是「進 TUI 跑 `/help`」——以畫面實際列出的為準。清單以外的斜線指令（例如其他 AI CLI 常見的 `/context`、`/clear`、`/compact`）在 Antigravity 一律**【⚠️ 官方文件未載明】**，本書不描述它們的行為。

**可用模型**（`agy models` 實測）：`gemini-3.6-flash-{high,medium,low}`、`gemini-3.5-flash-{high,medium,low}`、`gemini-3.1-pro-{high,low}`、`claude-sonnet-4-6`、`claude-opus-4-6-thinking`、`gpt-oss-120b-medium`。

### Session 與 context 維護

同一任務延續上一個 session 用 `agy -c`；從歷史對話挑一個恢復用 `agy --conversation <id>` 或 TUI 內 `/resume`；已切換成完全不同的任務就開新對話，不要在舊 context 裡硬撐；陌生、多檔、風險高先別改，用 `agy --mode plan`；想把某一步收回用 `/rewind`。

同一路徑修正兩次仍偏離時，先開新對話，用更精準的 scope、證據與通過條件重新開始，不要在污染的 context 裡無限補 prompt。

### 先看

`AGENTS.md`、`.agents/README.md`

### 照貼照跑：終端機

```bash
agy --help
agy models
```

### 照貼照跑：agy

```text
只做設計，不要修改檔案。以 SmartTrip FX 為例，產出一張 7 列表格：
AGENTS.md / Rules、Skill、Subagent、Hook、MCP、Plugin、Browser。
每列只能寫：這個案例是否需要、負責什麼、不需要時為什麼不加。
原則是使用最少元件，不准為了湊滿表格而啟用功能。
```

### 你應看到

專案邊界放 `AGENTS.md` / Rules；重複的需求到實作路線放 Skill；只讀 codebase 探索交給 Subagent；credential 與破壞性操作由 Hook 防護，而且要指出這是**唯一**的硬性手段；只有 agent 真要連外部工具時才需要 MCP；單一 repo 不急著做 Plugin；純 CLI 的 SmartTrip FX 沒有 UI，不需要 Browser。

### 最終通過

- [ ] 不看答案，也能為一個需求選出最小的官方元件。
- [ ] 能說出 context、workflow、isolation、enforcement、connection、distribution 六種責任。
- [ ] 知道何時開新對話、何時 `--continue`、何時用 `--mode plan`。
- [ ] 核心課程沒有修改產品碼、沒有新增 MCP server、沒有對外寫入、沒有新增秘密。

### 卡住就貼

```text
請用這個順序重新判斷：
長期 context → 按需 workflow → 隔離工作 → 強制閘門 → 外部連接 → 跨 repo 分發。
每一層只有在前一層無法解決時才新增元件，最後只給一個下一步。
```

官方延伸：[CLI Reference](https://antigravity.google/docs/cli/reference)、[CLI Best Practices](https://antigravity.google/docs/cli/best-practices)

---

## 一頁複習：遇到需求時先問六題

1. 這是每次都要知道的 context（`AGENTS.md`），還是特定任務才需要（Skill）？
2. 這是模型可以判斷的流程，還是每次都必須機械式執行（Hook）？
3. 這份工作會產生大量中間資訊，需要隔離 context（Subagent）嗎？
4. agent 需要連外部工具（MCP），還是最終 App 自己需要 runtime integration？
5. 這件事需要 agent 親眼看到畫面（Browser），還是文字驗收就夠？
6. 這套設定已經需要跨 repo 版本化分發（Plugin）了嗎？

能回答這六題，你就不是在堆設定，而是在設計 Antigravity 的工作環境。

## 官方來源索引

三個來源的優先序，本書從高到低使用：

1. **本機 `agy` binary 的實際行為**（1.1.12）—— `agy --help`、`agy models`、`agy help plugin`、binary 字串與符號表。
2. **隨 binary 出貨的內建規格** —— `~/.gemini/antigravity-cli/builtin/skills/agy-customizations/`（`SKILL.md` + `docs/{rules,skills,plugins,hooks,mcp_servers,json_configs}.md`）與 `.../builtin/skills/antigravity_guide/`（`references/{cli,ide,app,sdk}.md`）。
3. **antigravity.google 網站** —— 已發現多處與 binary 不符，只在前兩者沒寫時使用，並標明差異。

官方文件 sitemap（來自內建 skill `antigravity_guide`）：[文件首頁](https://antigravity.google/docs)、[Skills](https://antigravity.google/docs/skills)、[Rules & Workflows](https://antigravity.google/docs/rules-workflows)、[Hooks](https://antigravity.google/docs/hooks)、[Plugins](https://antigravity.google/docs/plugins)、[Sidecars](https://antigravity.google/docs/sidecars)、[MCP](https://antigravity.google/docs/mcp)、[Browser Automation & Testing](https://antigravity.google/docs/ide/browser)、[Permissions & Security](https://antigravity.google/docs/permissions)、[CLI Features & Subagents](https://antigravity.google/docs/cli/features)、[CLI Best Practices](https://antigravity.google/docs/cli/best-practices)、[CLI Reference](https://antigravity.google/docs/cli/reference)、[Changelog](https://antigravity.google/changelog)。

### 本書已知的三個官方矛盾

| 主題 | 網站說 | 內建規格說 | 本書採用 |
|---|---|---|---|
| hook `decision` 的值 | 五個 | 四個 | **五個**（binary 實證有 `deny_unless_prior_grant`） |
| Tool Execution Policy | 含 `strict` | 含 `strict` | binary 實證是 `always-proceed` / `request-review` / `proceed-in-sandbox` / `admin-control`，查無 `strict` |
| 全域 rules 位置 | `~/.gemini/GEMINI.md` | `~/.gemini/config/` | 兩者矛盾且本機無此檔 —— 本書只教 workspace 的 `.agents/rules/` |

最後核對日期：2026-08-11，對應 `agy` 1.1.12。若本書與官方文件衝突，先用本機 binary 複驗，再回報教材章節與官方 URL。

---

## 下一步｜進入本專案實戰

完成官方元件速成後，回到 [`BUILD.md`](./BUILD.md)，依序完成 SmartTrip FX 的 project contract、需求訪談、spec、tickets、TDD、review 與 commit。速成手冊教你「元件負責什麼」；專案實戰讓你證明「會把它們用在真工作裡」。

---

## 附錄 A：從其他 AI CLI 移植（歷史脈絡，非本課內容）

**本節只服務曾經使用其他 AI coding CLI 的讀者。第一次學 Antigravity 的學生可以整段跳過**——跳過不會漏掉任何本課需要的知識。

Antigravity 只讀根目錄的 `AGENTS.md` / `GEMINI.md` 與 `.agents/`；其他工具的 workspace 設定目錄在 binary 內查無路徑字串（【已驗證的負面結論】），搬過去不會被讀到，一定要重寫。對照如下：

| 你原本靠什麼 | Antigravity 的對應 | 落差 |
|---|---|---|
| 根目錄的專案 context 檔（`CLAUDE.md` 等） | `AGENTS.md` | 無，換檔名即可；同樣不支援 frontmatter |
| workspace 的 `settings.json` permissions | **沒有 workspace 對應物** | 🔴 只能靠 `hooks.json` 的 PreToolUse guard，或使用者自己在 `/permissions` 設 |
| skill frontmatter 的 `disable-model-invocation` | 那是 `WorkflowSpec` 的欄位，Skill 沒有 | 🔴 只剩正文的文字約束（第 3 章） |
| subagent 的 `tools` / `disallowedTools` / `permissionMode` | 不存在（87 個 yaml tag 中 0 命中） | 🔴 只剩正文的文字約束（第 4 章） |
| 平放的 subagent 定義檔 `<name>.md` | `.agents/agents/<name>/agent.md` | 檔案要改成**目錄**，frontmatter 刪剩 `name` + `description` |
| 獨立的 commands / prompts 層 | 併進 Skills | Antigravity **沒有獨立的 commands 層** |
| plugin | `agy plugin import gemini` / `import claude` | 只搬 plugin manifest，不會翻譯 workspace customization（第 7 章） |

hook 協定也完全不同，不要沿用舊格式：Antigravity 的 `hooks.json` **top-level key 是 hook 名稱不是事件名稱**、所有 JSON key 是 camelCase、working directory 是 `.agents/`、stdin 帶 `toolCall` 與 `workspacePaths`（第 5 章）。
