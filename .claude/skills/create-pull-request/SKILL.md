---
name: create-pull-request
description: 用 repository 實際的 template、default branch、commit history、diff 與驗證證據準備並建立 pull request。當使用者明確要求開啟、建立或草稿 PR 時使用。
disable-model-invocation: true
argument-hint: "base branch、draft/ready 或其他 PR 要求"
---

# 建立 Pull Request

把 PR 建立視為外部寫入。只在明確要求後執行。

## 1. 建立比較基準

1. 確認目前分支不是 remote 的 default branch。
2. 從使用者指示、repository 設定或 remote default branch 推斷 base；絕不硬編碼 `main`、`master` 或 `preview`。
3. 檢查該分支是否已有 PR，再建立新的。
4. 平行檢查（如支援）：
   - `git status --short`
   - `git log <base>..HEAD --oneline`
   - `git diff <base>...HEAD --stat`
   - `git diff <base>...HEAD`
   - upstream tracking state
   - `.github/pull_request_template.md` 或設定的替代項

未提交的變更不是 PR diff 的一部分。當它們實質改變說明或必要驗證時停止並解釋。

## 2. 從證據草稿

- 從 repository PRs 或 commit history 推斷標題風格。降級到 Conventional Commits。
- 標題保持簡潔且結果導向；只在 issue ID 存在時才加入。
- 用整個分支 diff（不只最新 commit）填充每個適用的 template section。
- 說明改了什麼、為何改、重要設計決策、驗證命令/結果、風險、推出計畫與相關截圖。
- 不在沒有觀測輸出時聲稱檢查已執行。明確標記未執行的檢查。

在外部寫入前預覽標題、body、base 與 head。

## 3. 推送並建立

若分支沒有 upstream，在確認後用 `git push -u origin <branch>` 推送。用 repository 的 hosting CLI 建立 PR，優先使用暫時 `--body-file` 而非 shell 插值。在要求或必要檢查仍刻意未完成時使用草稿模式。

回報 PR URL、base/head 與任何剩餘檢查。除非另外要求，否則不合併 PR。
