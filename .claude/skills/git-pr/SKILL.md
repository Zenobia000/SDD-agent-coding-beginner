---
name: git-pr
description: 檢視分支的所有 commit 撰寫並開出 PR；PR 合併後同步 main、清理本地與遠端分支。
disable-model-invocation: true
argument-hint: 開 PR；或 PR 已合併後輸入 cleanup 做清理
allowed-tools: Bash(git log:*), Bash(git diff:*), Bash(git push:*), Bash(git switch:*), Bash(git pull:*), Bash(git branch:*), Bash(git fetch:*), Bash(git rebase:*), Bash(gh pr view:*), Bash(gh pr create:*)
---

# Git PR

The head and tail of a branch's lifecycle: **opening the PR** and **cleaning up after merge**. Decide which phase from the argument or the current state — if the current branch's PR is already MERGED, go to cleanup.

## A. Open the PR

### 1. Gather material

```bash
git log --oneline <base>..HEAD   # the PR's content is these commits, not your memory
git status                       # uncommitted changes → stop, ask the user to deal with them first
```

`<base>` is the branch this PR will merge into — usually `main`, but ask when the user named a different one. **Every commit that range prints must be yours.** A branch cut from `dev` while the PR targets an older `release/x` drags in whatever landed on `dev` between them, and that cargo is charged to your PR: it inflates the diff, and the repo's secret scanner blocks on other people's commits with findings you cannot fix. Foreign commits in the range → resolve it before opening, either by pointing the PR at the branch you actually cut from, or:

```bash
git rebase --onto <base> <fork-point> <branch>   # replant your commits on the real base
```

Report which you did and why. The check costs one command; discovering it from a red PR costs the round trip.

### 2. Write it

- **Title (English)**: first letter capitalized, no trailing period, 70 characters max. Cover the whole branch's intent, not a restatement of the last commit.
- **Body (Traditional Chinese)**, sections in this order. Drop a section only when it truly has nothing to say — never pad one:

```markdown
## 摘要
一段話：這個 PR 做了什麼、動到哪些面。

## 問題
為什麼需要這個改動：症狀 → 根因。有量測就上表格，沒有就寫清楚觀察到什麼。
順手記下這個改法「不會」解決什麼，免得日後被誤引用。

## 變更內容
### `path/to/file`
- 該檔改了什麼、為什麼 — 依檔案或模組分組，不是 commit 的流水帳

## 設計決定
- 每條一行：決定 + 為什麼。只寫真的做過取捨的，不寫理所當然的。

## 測試
| 項目 | 結果 |
| --- | --- |
| 具體可執行的驗證步驟 | ✅ 附證據（數字、輸出），不是「功能正常」 |

**未驗證**：明列沒測到的範圍。沒說出口的缺口，比缺口本身更貴。
```

- Situational sections (遷移、部署提醒…) go between 設計決定 and 測試 when the change genuinely needs them.

### 3. Open

```bash
git push -u origin <branch>
gh pr create --title "..." --body "..."
```

Report the PR URL. **Do not merge** — merging is the user's button to press.

## B. Cleanup after merge

### 1. Verify, don't trust

```bash
gh pr view <branch> --json state,mergedAt
```

**`state` is not `MERGED` → stop the cleanup** and report the actual state. "The PR passed" is input to verify, not a fact.

### 2. Sync and delete

```bash
git switch main
git pull --ff-only origin main
git branch -d <branch>
git push origin --delete <branch> # only if the remote branch still exists; gh may have deleted it on merge
git fetch --prune
```

A squash merge rewrites the branch's commits into one new SHA on `main` — the branch's own SHAs never appear there. Two steps can react to that, each with a defined answer:

- **`git pull --ff-only` refused** → something other than this PR moved `main`. Stop and report. The flag is what makes that visible: a plain `git pull` buries the surprise in a merge commit and lands the same change on `main` twice.
- **`git branch -d` refused** → happens once `origin/<branch>` is gone (auto-delete on merge, or an earlier prune). While that ref survives, `-d` counts the branch as merged to its upstream and deletes it with a warning — expect that, not a refusal. On a real refusal, get the **evidence** before deleting: `git diff origin/main <branch>` empty means every change landed under a new SHA, and `-D` is then the correct command. Non-empty is the real warning — work on this branch never reached `main`. Stop and report.

Also check `git branch -v` for other branches marked `[gone]`. List them and ask whether to clean them too — **list and ask, never delete outright**.

## Rationalization table

| Excuse | Reality |
| --- | --- |
| "The user said the PR passed, just delete" | Claims get verified with `gh pr view`. Checking costs three seconds; deleting wrong costs half an hour. |
| "`-d` refused, switch to `-D`" | `-D` needs the evidence first: `git diff origin/main <branch>` empty. Without it, `-d` refusing means commits never reached main, and `-D` mutes the warning. |
| "`--ff-only` refused, drop the flag and pull again" | The refusal *is* the finding. Dropping the flag merges whatever moved `main` and duplicates this change in its history. |
| "I'll write the PR body from memory" | The material is `git log <base>..HEAD`. The branch in your memory and the actual branch are not the same branch. |
| "Extra commits in the range aren't mine — I'll note them in the body and open anyway" | A note does not take them out of the diff or out of the scanner's range. Repoint the base or `rebase --onto` first. |
