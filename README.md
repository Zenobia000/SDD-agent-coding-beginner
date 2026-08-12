# Claude Code：從官方元件到完整專案實戰

這是一門給初學者的 Claude Code 課程，固定分成兩冊、照同一條路走：

1. [`CLAUDE-CODE.md`](./CLAUDE-CODE.md)：約 2.5–3 小時，依 Anthropic 官方元件理解 Claude Code。
2. [`BUILD.md`](./BUILD.md)：約 4–5 小時，把元件用進本課專屬的 **SmartTrip FX** 專案。

第一冊回答「每個元件負責什麼」；第二冊完成 project contract、需求訪談、spec、tickets、TDD、review 與 commit。官方速成不取代專案實戰，專案實戰也不要求學生靠猜理解 `.claude/`。

## 三分鐘開始

先準備 Git、Python 3.11+ 與最新版 Claude Code；安裝方式以 [Anthropic 官方安裝文件](https://code.claude.com/docs/en/setup) 為準。

```bash
git clone https://github.com/Zenobia000/SDD-agent-coding-beginner.git
cd SDD-agent-coding-beginner
git switch claude
git switch -c workshop/claude-code-smarttrip
git config core.hooksPath .githooks
claude
```

**第三行不能省。** `main` 只是導覽頁，沒有任何教材；教材在 `claude` 分支上。
直接從 `main` 開 workshop 分支會拿到一個空的工作區。

`core.hooksPath` 是每個 clone 各自的設定，沒設就等於 `.githooks/` 完全沒作用。開始前先確認它真的生效：

```bash
git config core.hooksPath
```

必須印出 `.githooks`。印不出任何東西就代表上面那行沒跑到，回去補跑一次。

進入 Claude Code 後先打開 [`CLAUDE-CODE.md`](./CLAUDE-CODE.md)，完成最後的元件選型，再接著做 [`BUILD.md`](./BUILD.md)。

## 第一冊會學到的官方元件

| 問題 | Claude Code 元件 | 本 repo 的實例 |
|---|---|---|
| 每次 session 都要知道什麼？ | `CLAUDE.md`、Rules、Auto memory | `CLAUDE.md`、`.claude/rules/` |
| 哪些工具可以直接用或必須確認？ | Settings、Permissions | `.claude/settings.json` |
| 重複流程怎麼變成可呼叫能力？ | Skills | `.claude/skills/` |
| 大量探索怎麼隔離 context？ | Subagents | `.claude/agents/` |
| 哪些規則不能只靠模型記得？ | Hooks | `.claude/hooks/` |
| Claude 如何連接外部工具與資料？ | MCP | 核心課只辨識，不新增 server |
| 如何把整套元件發給其他專案？ | Plugins | 進階章辨識封裝邊界 |
| 何時需要多個獨立 Claude session？ | Agent teams | 實驗性功能，只做選型比較 |
| 大型 typed codebase 怎麼精準導覽？ | Code intelligence / LSP | 進階章辨識，不強迫安裝 |
| Session 輸出怎麼視覺化分享？ | Artifacts | 進階章辨識，不在核心課發布 |

## 第二冊會完成什麼

SmartTrip FX 讀取行程 JSON，驗證輸入、計算旅費現金與匯率燈號。學生會照貼 prompt，完成：

```text
project contract → 需求訪談 → spec → tickets
                 → 三個 TDD vertical slices
                 → code / security review → commit
```

核心產品只用 Python standard library，不接 live LLM、即時匯率 API、資料庫、登入、Web UI 或部署，讓學生專注在 Claude Code 的工程迴圈。

## 其他入口

| 路徑 | 用途 |
|---|---|
| [`.claude/`](./.claude/) | 可直接觀察與移植的工程 harness；[`架構說明`](./.claude/README.md) 是課後參考 |
| [`curriculum/README.md`](./curriculum/README.md) | 兩冊課程的講師節奏、巡場問題與維護規則 |
| [`docs/M0-M9_懶人包.md`](./docs/M0-M9_懶人包.md) | 原課程理論重點；不插入照貼照跑主線 |
| [`docs/exports/`](./docs/exports/) | 第二冊的 PDF 與 DOCX 離線版；由 Markdown 產生，更新後需重新匯出 |

Claude Code 行為以 [官方文件](https://code.claude.com/docs/en/overview) 為事實來源；社群文章只用來改善教法。文件最後核對日期：2026-07-31。
