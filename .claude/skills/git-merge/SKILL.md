---
name: git-merge
description: 把指定分支合併進當前分支；發生衝突時停下來分析與建議，解法是使用者的決定。
disable-model-invocation: true
allowed-tools: Bash(git merge:*), Bash(git status:*), Bash(git log:*), Bash(git diff:*), Bash(git fetch:*)
---

# Git Merge

Merge a target branch (e.g. `main`) into the current branch. A clean merge just completes; a conflicted one switches into analysis mode — **this skill analyzes conflicts, it does not resolve them**.

## 1. Preflight

```bash
git status                  # working tree must be clean, else stop and report
git fetch origin
git log --oneline HEAD..<target>   # see what is about to come in
```

Dirty working tree → stop. Uncommitted changes mixed into a merge become impossible to attribute afterwards.

## 2. Merge

```bash
git merge <target>
```

- **Clean merge** → report the range of commits merged in. Done.
- **`git status` shows Unmerged paths** → **committing is forbidden**. Go to step 3.

## 3. Conflict analysis (not resolution)

1. **List every conflicted file.**
2. For each file, read the `<<<<<<<`, `=======`, `>>>>>>>` markers, and for each conflict block:
   - **Summarize both sides' intent** — not pasted code, but what each side was trying to do. Example: "`main` added a parameter to this function; the current branch rewrote its internal logic."
   - **Suggest a direction** — are the two intents compatible? If yes, describe how to combine them; if mutually exclusive, state the trade-off.
3. Present the analysis and **wait for the user's ruling**. Only after their instruction do you edit the conflicted files and complete the merge.

## Rationalization table

| Excuse | Reality |
| --- | --- |
| "This conflict is tiny, I'll just resolve it" | Size is a property of the code; the ruling belongs to the user. |
| "The two sides touch different lines — the machine flagged it, that's all" | Then report exactly that: "intents compatible, suggest keeping both" — and still wait. |
| "This is a mess, let me `git merge --abort` and retry" | Abort throws away a merge the user initiated. Whether to give up is their question. |
| "Halfway resolved, I'll just commit to wrap up" | Every second Unmerged paths exist, committing is forbidden. Fully resolved and user-confirmed, then commit. |
