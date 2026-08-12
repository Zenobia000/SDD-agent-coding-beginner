# `.agents/` 架構說明

這個資料夾是一套**可移植的工程 harness**：把「怎麼做工程」寫成 Google Antigravity 能載入的檔案。它與 SmartTrip FX 產品實作無關，可以整包複製到其他 repo。

> 這份文件解釋「本 repo 如何實作」，不是 Antigravity 官方功能的完整清單。第一次學習請先走 [`../ANTIGRAVITY.md`](../ANTIGRAVITY.md)，再用 [`../BUILD.md`](../BUILD.md) 完成 SmartTrip FX。安裝與 `agy` 日常操作另見 [`../docs/INSTALL.md`](../docs/INSTALL.md) 與 [`../docs/CLI_GUIDE.md`](../docs/CLI_GUIDE.md)。

```text
.agents/
├── README.md                    # 本檔：harness 架構總覽與索引
├── AGENTS.template.md           # 搬到其他 repo 時使用的通用 AGENTS.md 模板
├── hooks.json                   # 具名 hook 註冊；top-level key 是 hook 名稱，不是事件名稱
├── mcp_config.json              # MCP server 宣告；本 repo 只放兩個 disabled 範例
├── hooks/                       # 機械閘門：工具呼叫前攔截（Python，非模型判斷）
│   ├── guard.py                 #   協定層：Antigravity hook JSON ⇄ (decision, reason)
│   └── guard_core.py            #   判定層：工具中立的風險規則，不知道自己跑在哪個 agent 上
├── rules/                       # 恆常紀律：frontmatter 的 trigger 決定載入時機
│   └── engineering-workflow.md  #   trigger: always_on
├── skills/                      # 程序知識：31 個「怎麼做某件事」的流程
│   └── <name>/SKILL.md [+ references/]
├── agents/                      # 隔離工人：4 個唯讀 subagent
│   └── <name>/agent.md
└── context/                     # 給後續 session 的筆記（非官方元件，Antigravity 不會自動載入）
    ├── codebase-map.md          #   repo 全貌
    ├── harness-guardrails.md    #   hooks.json 形狀與 guard 行為對照表
    ├── harness-skills.md        #   skills 分類、呼叫圖、subagent 責任
    └── known-non-bugs.md        #   容易誤判為 bug 的刻意設計
```

Antigravity 的 workspace root 接受四種名稱：`.agents/`、`.agent/`、`_agents/`、`_agent/`。本 repo 固定用 `.agents/`——`agy` 1.1.12 binary 內大量出現 `.agents/` 路徑字串（`strings -n 4 ~/.local/bin/agy | grep -oF '.agents/' | wc -l` 回 263），`.agent/`（單數）**查無字串**，不要依賴單數形式。

⚠️ **第一次在這個 repo 啟動 `agy` 會問要不要信任這個 workspace，一定要選信任。** 未信任的 workspace，`.agents/` 底下全部不載入而且**不報錯**。要確認信任狀態，讀 `~/.gemini/antigravity-cli/settings.json` 的 `trustedWorkspaces`。

---

## 1. 各層的分工

這些目錄不是平行的分類，而是**不同的執行責任**：

| 層 | 路徑 | 誰執行 | 控制性質 | 何時生效 |
|---|---|---|---|---|
| 事件閘門 | `hooks.json` + `hooks/` | Antigravity runtime 呼叫外部命令 | deterministic，可硬擋 | 每次工具呼叫前（`PreToolUse`） |
| 恆常紀律 | `rules/*.md` | 模型 | instruction，不是安全強制 | `trigger: always_on` → 每個 session |
| 程序知識 | `skills/<name>/SKILL.md` | 模型 | 按需載入的 instruction | `description` 命中情境或使用者點名 |
| 隔離工人 | `agents/<name>/agent.md` | 獨立 subagent | 隔離 context | 被流程委派時 |
| 外部連接 | `mcp_config.json` | MCP server 程序 | 增加可用 tool | server 未 `disabled` 時 |
| 封裝分發 | `plugins/`（本 repo 未建立） | `agy plugin` | 打包上述元件跨 repo 版本化 | 安裝並 enable 後 |

再加上根目錄的 [`../AGENTS.md`](../AGENTS.md)：目錄層級的長期 context，對所在目錄與所有子目錄永遠 active，官方規格明訂**不支援 frontmatter**。

關鍵設計：**不可逆的風險放在 hooks，可判斷的品質放在 skills**。文字規則只能提醒，Python hook 才能真的擋下 `rm -rf ~`。

> 🔴 **Antigravity 的 workspace 沒有 `settings.json`，也沒有 workspace 層級的 permission 宣告**（binary 內 `.agents/settings.json` 出現 0 次，已驗證的負面結論）。權限由使用者在 `/permissions` 自行設定，**`hooks.json` 是這個 repo 裡唯一能做 deterministic 硬性攔截的元件**。

📄 **`hooks.json` 的實際形狀、guard 的完整行為對照表（教材承諾）、可重跑的驗證樣本、兩層 guardrail 的分工** → [`context/harness-guardrails.md`](./context/harness-guardrails.md)

---

## 2. 所有 skill 的共同介面：專案契約

這是整套設計的樞紐。31 個 skill 沒有一個硬編碼「測試指令是 `pytest`」，它們一律去讀同一份**專案契約**：Quality commands（focused/full test、typecheck、lint、format、build）、Issue tracker、Git workflow、Domain docs 位置、Risk boundary。

契約是一組**欄位**，不是一個固定檔案。落點有三個，依優先序：

```text
① docs/agents/project.md    ← setup-project 產生；不隨 .agents/ 附帶，存在才用
② AGENTS.md〈專案契約〉節    ← AGENTS.template.md 自帶，小專案填這裡就夠
③ 從 repo 探索              ← 前兩者皆空時讀 CI 設定、manifest、既有 script
```

`.agents/` 內有多個檔案寫著「先讀 `docs/agents/project.md`」，那是①的路徑；`rules/engineering-workflow.md` 加了「（若存在）」作為全域降級，個別 skill 也各有 fallback（`to-spec` 安全推斷並明講預設、`wayfinder` 改用 `.scratch/`、`implement` 未知命令不能猜）。**沒有①的 repo 一樣能跑**，只是每個 skill 要自己探索一次。

因此：

- 換一個 repo，`.agents/` 整包不用改，只需重填契約欄位。
- 任何一層都拿不到的欄位標 `unknown`，不得捏造命令。
- 「未驗證」與「已通過」的界線由它定義——只有契約列出的命令跑過才算數。

這個 repo 目前走②（見 [`../AGENTS.md`](../AGENTS.md)〈專案契約〉節），刻意**不**預先建立 `docs/agents/project.md`——那會讓 `BUILD.md` 第 1 章的 `test -f` 驗收直接通過，練習失效。何時該外移到①是**機械判斷**：契約欄位需要獨立版本控管、或多個 agent/CI 要引用同一份事實時。與專案內容無關。

---

## 3. `skills/` 與 `agents/`

- **31 個 skill**，frontmatter 只有 `name` 與 `description` 兩欄且都必填。依「誰能啟動」分三類：11 個只給使用者叫的 orchestration、1 個給其他 skill 內嵌的 `grilling`、19 個模型與使用者都可用的 discipline。
  🔴 **這條線是軟約束**：Antigravity 的 skill frontmatter 沒有任何能結構性禁止模型自行啟動的欄位，那 11 個 skill 的限制只寫在正文第一句，模型可以違反。
- **4 個 subagent**（`code-explorer`、`standards-reviewer`、`spec-reviewer`、`security-reviewer`），每個是一個目錄，定義檔 `<name>/agent.md`。它們的唯讀性質同樣只是正文的文字約束——要硬性阻擋寫入，唯一可驗證的做法是 `hooks.json` 的 PreToolUse guard。
- **3 個多檔 skill**（`codebase-design`、`domain-modeling`、`tdd`）把「走到那個分支才需要」的內容放進 `references/`，示範 progressive disclosure。

📄 **完整的兩軸分類表、31 個 skill 的功能分層、實際引用圖（mermaid）、`references/` 的三種角色、4 個 subagent 的責任與已知落差** → [`context/harness-skills.md`](./context/harness-skills.md)

---

## 4. 讀取順序（一個 session 的實際生命週期）

```text
在 repo root 執行 agy
  ├─ 信任提示 ── 未信任 → .agents/ 全部不載入，而且不報錯
  ├─ 從 CWD 往上走到 repo root（含 .git 的目錄），逐層探索 .agents/
  ├─ AGENTS.md（目錄層級、無 frontmatter、永遠 active）              常駐
  ├─ .agents/rules/engineering-workflow.md（trigger: always_on）      常駐
  ├─ .agents/skills/*/SKILL.md ── 只注入 name + description           目錄
  ├─ .agents/agents/*/agent.md ── 註冊可委派的 subagent
  ├─ .agents/hooks.json ── 註冊具名 hook「smarttrip-guard」
  └─ .agents/mcp_config.json ── 連線未 disabled 的 MCP server
        │
使用者輸入 ─▶ 模型依 description 判斷要不要展開某個 skill
        ├─ 點名 implement ──▶ 展開 skills/implement/SKILL.md 全文
        │        └─ 流程指向 tdd ──▶ 展開 skills/tdd/SKILL.md
        │                └─ mock 有爭議 ──▶ 讀 tdd/references/mocking.md
        └─ 流程指向 code-review ─▶ 委派 standards-reviewer + spec-reviewer（獨立 context）
        │
任何工具呼叫 ─▶ PreToolUse hook 先跑 guard.py → deny / ask / {}
```

多來源同名時的載入優先序（高 → 低）：**Workspace Project**（`.agents/`）→ **Declared Configurations**（workspace 的 `skills.json` / `plugins.json`）→ **Global Discovery**（`~/.gemini/config/`）→ **Built-in** → **Global Declared**。所有 customization 依解析後路徑去重，同一輪對話同一檔案只注入一次。

`AGENTS.md`（薄、常駐）→ `rules/`（薄、常駐）→ `skills/`（厚、按需）→ `references/`（更厚、更按需）是同一個梯度：**常駐的東西必須短**。

> `context/` 不是官方元件，Antigravity 不會自動載入它。那是寫給維護者與後續 session 的筆記。

---

## 5. 移植到其他 repo

```bash
mkdir -p <target-repo>/.agents
cp -r .agents/{hooks.json,mcp_config.json,hooks,rules,skills,agents} <target-repo>/.agents/
cp .agents/AGENTS.template.md <target-repo>/AGENTS.md
cd <target-repo> && agy      # 第一次啟動要選「信任這個 workspace」
```

只要複製兩樣東西：根目錄的 `AGENTS.md` 與整個 `.agents/`。Antigravity 只讀這兩處；`hooks.json` 裡的相對路徑以 `.agents/` 為基準，整包搬過去就會繼續生效。

複製完就能用。填〈專案契約〉節是第一件事，可以手填，也可以用 `setup-project` 由它探索後外移成 `docs/agents/project.md`——**兩者等價，`setup-project` 不是前置條件**。

搬完建議跑一次 harness check：

```bash
python3 -m py_compile .agents/hooks/*.py
python3 -c "import json; json.load(open('.agents/hooks.json'))"
python3 -m json.tool .agents/mcp_config.json >/dev/null
```

整包沒有任何 SmartTrip FX 或 Python 專屬內容；`react-doctor` 與 `running-local-docker-stack` 用不到就留著，模型不會在無關情境啟動它們。

通用版 `AGENTS.md` 見 [`AGENTS.template.md`](./AGENTS.template.md)；本 repo 根目錄的 [`../AGENTS.md`](../AGENTS.md) 是它加上教材專屬約束後的版本。
