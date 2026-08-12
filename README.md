# Antigravity：從官方元件到完整專案實戰

這是一門給初學者的 Google Antigravity 課程，固定分成兩冊、照同一條路走：

1. [`ANTIGRAVITY.md`](./ANTIGRAVITY.md)：約 2.5–3 小時，依 Google 官方元件理解 Antigravity。
2. [`BUILD.md`](./BUILD.md)：約 4–5 小時，把元件用進本課專屬的 **SmartTrip FX** 專案。

第一冊回答「每個元件負責什麼」；第二冊完成 project contract、需求訪談、spec、tickets、TDD、review 與 commit。官方速成不取代專案實戰，專案實戰也不要求學生靠猜理解 `.agents/`。

## 三分鐘開始

先準備 Git、Python 3.11+ 與 Antigravity CLI（`agy`）。完整安裝 SOP 與環境檢查在 [`docs/INSTALL.md`](./docs/INSTALL.md)，官方安裝命令是：

```bash
# macOS / Linux
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

```powershell
# Windows PowerShell
irm https://antigravity.google/cli/install.ps1 | iex
```

裝完先確認 `agy --version` 印得出版本，再照下面四行進入本課：

```bash
git clone https://github.com/Zenobia000/SDD-agent-coding-beginner.git
cd SDD-agent-coding-beginner
git switch antigravity
git switch -c workshop/antigravity-smarttrip
git config core.hooksPath .githooks
agy
```

**第三行不能省。** `main` 只是導覽頁，沒有任何教材；教材在 `antigravity` 分支上。
直接從 `main` 開 workshop 分支會拿到一個空的工作區。

`core.hooksPath` 是每個 clone 各自的設定，沒設就等於 `.githooks/` 完全沒作用。開始前先確認它真的生效：

```bash
git config core.hooksPath
```

必須印出 `.githooks`。印不出任何東西就代表上面那行沒跑到，回去補跑一次。

第一次執行 `agy` 會開瀏覽器完成登入；透過 SSH 連到遠端主機時改走 device code 流程，細節見 [`docs/INSTALL.md`](./docs/INSTALL.md)。**一定要在 repo 根目錄執行 `agy`** —— Antigravity 是從當前目錄往上走到 repo root 尋找 `AGENTS.md` 與 `.agents/`，在子目錄啟動會漏掉部分設定。

進入 `agy` 後先打開 [`ANTIGRAVITY.md`](./ANTIGRAVITY.md)，完成最後的元件選型，再接著做 [`BUILD.md`](./BUILD.md)。

## 第一冊會學到的官方元件

| 問題 | Antigravity 元件 | 本 repo 的實例 |
|---|---|---|
| 每次 session 都要知道什麼？ | `AGENTS.md`（目錄層級 rules，永遠 active、不支援 frontmatter） | [`AGENTS.md`](./AGENTS.md) |
| 哪些長期規範要能按需載入？ | Rules（frontmatter `trigger: always_on` / `model_decision`） | `.agents/rules/` |
| 重複流程怎麼變成可呼叫能力？ | Skills（`SKILL.md`，frontmatter 只有 `name` + `description`） | `.agents/skills/` |
| 大量探索怎麼隔離 context？ | Subagents | `.agents/agents/`（⚠️ 官方文件未載明檔案格式，本 repo 用法屬未驗證慣例） |
| 哪些規則不能只靠模型記得？ | Hooks | `.agents/hooks.json` + `.agents/hooks/` |
| 如何連接外部工具與資料？ | MCP | `.agents/mcp_config.json`（範例，預設 `disabled`） |
| 工具要不要每次都問過我？ | Permissions | `/permissions`；hook 的 `decision` 有五個值 `allow` / `deny` / `ask` / `force_ask` / `deny_unless_prior_grant`（見 [`ANTIGRAVITY.md`](./ANTIGRAVITY.md) 第 5 章） |
| 這一輪要用哪個模型、花多少推理？ | Model 選擇 | `agy models`、`/model`、`--effort low\|medium\|high` |
| 如何把整套元件發給其他專案？ | Plugins | 進階章辨識封裝邊界，用 `agy plugin` 管理 |

載入優先序（高 → 低）：Workspace（`.agents/`）→ `skills.json` / `plugins.json` 宣告 → Global（`~/.gemini/config/`）→ Built-in。Skills 與 `model_decision` 的 Rules 走 progressive disclosure，預設只注入 name 與 description。

## 第二冊會完成什麼

SmartTrip FX 讀取行程 JSON，驗證輸入、計算旅費現金與匯率燈號。學生會照貼 prompt，完成：

```text
project contract → 需求訪談 → spec → tickets
                 → 三個 TDD vertical slices
                 → code / security review → commit
```

核心產品只用 Python standard library，不接 live LLM、即時匯率 API、資料庫、登入、Web UI 或部署，讓學生專注在 Antigravity 的工程迴圈。

## 其他入口

| 路徑 | 用途 |
|---|---|
| [`.agents/`](./.agents/) | 可直接觀察與移植的工程 harness；[`架構說明`](./.agents/README.md) 是課後參考 |
| [`docs/INSTALL.md`](./docs/INSTALL.md) | `agy` 安裝 SOP、環境需求與認證流程 |
| [`docs/CLI_GUIDE.md`](./docs/CLI_GUIDE.md) | `agy` 日常操作與 `.agents/` 設定速查 |
| [`curriculum/README.md`](./curriculum/README.md) | 兩冊課程的講師節奏、巡場問題與維護規則 |
| [`docs/M0-M9_懶人包.md`](./docs/M0-M9_懶人包.md) | 原課程理論重點；不插入照貼照跑主線 |
| [`docs/exports/`](./docs/exports/) | 第二冊的 PDF 與 DOCX 離線版。⚠️ 內容為舊版，尚未依 Antigravity 版重新匯出，以 Markdown 主線為準 |

Antigravity 行為以 [官方文件](https://antigravity.google) 為事實來源；官方網站與本機 `agy` binary 實際行為不符時以 binary 為準，並在教材裡註明差異。社群文章只用來改善教法。文件最後核對日期：2026-08-11。
