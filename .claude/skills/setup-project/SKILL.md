---
name: setup-project
description: 為目前 repo 建立一次性的實戰工程設定：驗證指令、issue tracker、domain docs 與高風險操作界線。
disable-model-invocation: true
---

# Setup Project

只建立或更新 `docs/agents/project.md`。不要因 setup 改動產品程式碼、根目錄規則或外部 issue tracker。

## 1. 探索

從檔案與可用命令找答案，不要先問使用者：

- 套件管理器、runtime、workspace/monorepo 結構。
- focused test、full test、typecheck、lint、format、build 的真實命令。
- CI 實際跑哪些命令；本機指令應與 CI 對齊。
- git remote 指向 GitHub、GitLab 或其他系統；若沒有 remote，預設 local markdown。
- default/base branch、branch naming、最近 commit subjects、PR template 與 release note 慣例。
- `CONTEXT.md`、`CONTEXT-MAP.md`、ADR、spec 與 issue 文件現有位置。
- production、付款、寄信、資料刪除、不可逆 migration 等高風險操作。

不要安裝依賴。候選命令可用 `--help`、列出設定或執行最小 read-only 檢查確認；無法安全確認就標 `unknown`。

## 2. 一次問一個決策

只問探索無法回答且會改變工作流的決策。每題先給推薦答案：

1. issue tracker 用 GitHub、GitLab、既有系統或 `.scratch/<feature>/issues/`。
2. 若存在真正 monorepo 訊號，domain docs 採單一 context 還是 context map；一般 repo 不詢問，預設單一 context。
3. 哪些外部動作即使使用者要求實作，也必須在執行前再次確認。

## 3. 預覽後寫入

先展示草稿並讓使用者修正，再寫 `docs/agents/project.md`：

```markdown
# Project Contract

## Quality commands
- Focused test: `<command>`
- Full test: `<command>`
- Typecheck: `<command>`
- Lint: `<command>`
- Format check: `<command>`
- Build: `<command>`

## Issue tracker
- Type: `github | gitlab | local | custom`
- Location: `<repo/url/path>`
- Read: `<command or procedure>`
- Create/update: `<command or procedure>`
- Ready label: `<label or none>`

## Git workflow
- Default/base branch: `<branch>`
- Branch style: `<observed format or conventional fallback>`
- Commit style: `<observed format or Conventional Commits fallback>`
- PR template: `<path or none>`
- Release notes: `<observed source and format or none>`

## Domain docs
- Layout: `single-context | multi-context`
- Glossary: `<path or create lazily>`
- ADRs: `<path or create lazily>`
- Specs: `<path or tracker>`

## Risk boundary
- Require confirmation: `<operations>`
- Never automate: `<operations>`

## Verified on
`YYYY-MM-DD` — only facts verified from files or command output are listed above.
```

保留使用者已編輯的內容。設定缺少時，其他 skills 應先探索並使用安全預設，不得捏造命令。
