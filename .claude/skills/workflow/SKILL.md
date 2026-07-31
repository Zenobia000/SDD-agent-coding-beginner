---
name: workflow
description: 根據目前專案狀態，選出最適合的工程 skill 或完整路徑。
disable-model-invocation: true
argument-hint: "目前的目標或卡點"
---

# Workflow Router

先檢查實際 repo 狀態與 `docs/agents/project.md`，再只推薦一條路。這些 skills 是可組合工具，不是每次都要走完的關卡。

## 主流程：idea → ship-ready

1. 需求仍有分支或術語不一致：`/grill-with-docs`。
2. 紙上無法回答狀態模型、互動或 UI 選擇：使用 `prototype` 做一次性實驗，再回到討論。
3. 單一 session 能完成：直接 `/implement`。
4. 多 session 或多人工作：`/to-spec` → `/to-tickets` → 用 `parallel-work` 找出 frontier。只有互不相依的 tickets 才並行；會寫 code 時用 `worktree-strategy` 隔離，每張 ticket 開新 session 執行 `/implement`。
5. `/implement` 內部在已同意的 seam 使用 `tdd`，最後執行 `code-review`；高風險變更加 `security-review`。

在 `/to-tickets` 前保留同一個 context，讓訪談、spec 與切票共享理解。每張 implementation ticket 使用乾淨的新 context，只依 ticket、domain glossary 與 ADR 工作。

## 其他入口

- 難解 bug、flake、效能退化：`diagnosing-bugs`。
- 大到看不清完整路線：`/wayfinder`；它只解決決策，路線清楚後回到 `/to-spec`。
- 外部 bug report 或需求堆積：`/triage`；`/to-tickets` 自己產生的票不再 triage。
- 架構摩擦、很難測或一改多處：`/improve-codebase-architecture`。
- merge/rebase 衝突：`resolving-merge-conflicts`。
- 兩個以上獨立調查、review、tests 或實作：`parallel-work`；同時寫 repository 時再套用 `worktree-strategy`。
- 開始分支：`branch-name`。準備提交：`commit-message`。明確要求建立 PR：`/create-pull-request`。
- 產生跨版本 changelog 或 release body：`release-notes`。
- React diff 健康檢查：`react-doctor`。本機 Compose stack：`running-local-docker-stack`。
- 需要換 session 且保留脈絡：`/handoff`。
- 第一次使用或 `docs/agents/project.md` 不存在：`/setup-project`。

## 輸出

用三行回答：

1. 建議執行的 skill 或路徑。
2. 目前證據為何符合這條路。
3. 哪個條件會讓建議改變。

不要自動啟動使用者專用 skill；讓使用者決定是否執行建議命令。外部寫入（commit、push、PR、release、issue）仍需明確要求。
