---
name: workflow
description: 依目前 repo 狀態與專案契約判斷下一步該用哪個工程 skill 或哪條完整路徑，只給一條建議並說明會翻盤的條件。只在使用者明確詢問下一步該做什麼或要求路線建議時使用，不要在其他情況自行啟動。
---
# Workflow Router

這個 skill 只在使用者明確要求時執行。不要在使用者沒要求時自行啟動它。

先檢查實際 repo 狀態與 `docs/agents/project.md`，再只推薦一條路。這些 skills 是可組合工具，不是每次都要走完的關卡。

本檔一律用 `` `skill-name` `` 指稱 skill，不要寫成 `/skill-name`。使用者那端兩種寫法都可能可用（`agy --help` 的 `--disable-slash-commands` 把「slash command」與「skill expansion」寫在一起，是斜線能展開 skill 的間接證據），但各介面實際行為未經實測，所以請使用者啟動時建議他明講「使用 `<skill-name>` skill」，那個寫法永遠有效。

## 主流程：idea → ship-ready

1. 需求仍有分支或術語不一致：`grill-with-docs`。
2. 紙上無法回答狀態模型、互動或 UI 選擇：使用 `prototype` 做一次性實驗，再回到討論。
3. 單一 session 能完成：直接 `implement`。
4. 多 session 或多人工作：`to-spec` → `to-tickets` → 用 `parallel-work` 找出 frontier。只有互不相依的 tickets 才並行；會寫 code 時用 `worktree-strategy` 隔離，每張 ticket 開新 session 執行 `implement`。
5. `implement` 內部在已同意的 seam 使用 `tdd`，最後執行 `code-review`；高風險變更加 `security-review`。

在 `to-tickets` 前保留同一個 context，讓訪談、spec 與切票共享理解。每張 implementation ticket 使用乾淨的新 context，只依 ticket、domain glossary 與 ADR 工作。

## 其他入口

- 難解 bug、flake、效能退化：`diagnosing-bugs`。
- 大到看不清完整路線：`wayfinder`；它只解決決策，路線清楚後回到 `to-spec`。
- 外部 bug report 或需求堆積：`triage`；`to-tickets` 自己產生的票不再 triage。
- 架構摩擦、很難測或一改多處：`improve-codebase-architecture`。
- merge/rebase 衝突：`resolving-merge-conflicts`。
- 兩個以上獨立調查、review、tests 或實作：`parallel-work`；同時寫 repository 時再套用 `worktree-strategy`。
- 開始分支：`branch-name`。準備提交：`commit-message`。明確要求建立 PR：`create-pull-request`。
- 產生跨版本 changelog 或 release body：`release-notes`。
- React diff 健康檢查：`react-doctor`。本機 Compose stack：`running-local-docker-stack`。
- 需要換 session 且保留脈絡：`handoff`。
- 第一次使用或 `docs/agents/project.md` 不存在：`setup-project`。

## 輸出

用三行回答：

1. 建議執行的 skill 或路徑。
2. 目前證據為何符合這條路。
3. 哪個條件會讓建議改變。

本 skill 只推薦路線，不代替使用者啟動下一個 skill。凡是正文寫著「只在使用者明確要求時執行」的 skill，都要等使用者自己說要跑才啟動。外部寫入（commit、push、PR、release、issue）仍需明確要求。
