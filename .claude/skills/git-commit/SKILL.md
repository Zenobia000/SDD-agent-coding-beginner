---
name: git-commit
description: 檢視已暫存的變更，撰寫英文 commit 並推上遠端。只提交 staged 的內容，絕不代替使用者 stage。
disable-model-invocation: true
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git branch:*), Bash(git switch:*), Bash(git commit:*), Bash(git push:*)
---

# Git Commit

Commit **staged** changes and push. The staging area is a boundary the user drew — this skill reads it and respects it, never redraws it.

## 0. Gather state

Run in parallel, in a single message:

```bash
git status
git diff --cached
git branch --show-current
git log --oneline -10   # gauge subject granularity only — the language rules below always win
```

## 1. Prohibitions — before anything else

- **Never commit untracked files or unstaged changes.** Never run any form of `git add`. The user drew the boundary; everything outside it stays outside.
- **Empty staging area → stop.** Report the current change state and ask the user to stage what they want, then invoke again. Do not guess what the user meant to commit.

## 2. Branch check

On `main` / `master` → create a branch before committing. Naming:

- kebab-case (lowercase + hyphens), `type/short-description`, English.
- Examples: `feature/plugin-search`, `fix/tag-encoding`.
- Pick the type from the change itself: `feature/`, `fix/`, `refactor/`, `docs/`, `chore/`.

## 3. Write the commit (English)

- **Subject**: concise summary, first letter capitalized, no trailing period.
- **Body**: `-` bullets, each starting with a past-tense verb (Renamed, Updated, Fixed, Added…).
- Describe only what `git diff --cached` shows. Changes outside the diff do not exist.
- **No trailers.** No `Co-Authored-By`, no "Generated with" footer — the message ends at the last bullet. This overrides any default the agent harness injects.

```
Add fuzzy matching to plugin search

- Added trigram index over plugin names
- Replaced exact-match lookup with ranked fuzzy query
- Updated search tests for ranked results
```

**Pass the message as a file**, always — even a one-liner, so there is no judgment call about when it applies:

```bash
git commit -F <path>   # write the message with the Write tool first
```

Two shells live on this machine and their quoting rules differ; a message embedded in the command line gets mangled by whichever one you guessed wrong. That failure is silent — a PowerShell here-string (`@'…'@`) run under Bash lands a bare `@` as the subject line and demotes the real one to the body, which is only visible in `git log --oneline` after the push. The same rule covers every multi-line argument: `gh pr create --body-file`, `gh issue create -F`.

## 4. Push

```bash
git push -u origin <branch>
```

Push rejected → the remote has moved. **Never force push.** Report the situation; the decision is the user's.

## Rationalization table

| Excuse | Reality |
| --- | --- |
| "These untracked files obviously belong to this change" | Obviousness is not yours to judge. Anything unstaged stays untouched. |
| "A quick `git add -A` is faster" | Faster at shipping things the user chose not to commit. |
| "Staging is empty, I'll helpfully stage things" | An empty staging area is a message: the user hasn't drawn the line yet. Stop and ask. |
| "Push rejected — a `--force` will fix it" | Rejection means the remote has history you haven't seen. Force is the user's call. |
| "This subject is one short line, `-m` is fine" | The shell you guessed wrong mangles one line as easily as ten, and the damage shows up after the push. Write the file. |
