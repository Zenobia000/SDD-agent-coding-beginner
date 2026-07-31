---
name: worktree-strategy
description: Plan, create, coordinate, integrate, and clean up Git worktrees for isolated concurrent work. Use when multiple implementations need independent working trees, when preserving a dirty primary tree, or when experiments and reviews must not share branch state.
---

# Worktree Strategy

Use one branch per worktree and one clear integration owner. A worktree isolates files and index state; it does not isolate external services, caches, ports, databases, or credentials.

## 1. Preflight

1. Inspect `git status`, repository/common-dir, current worktrees, remotes, default branch, and candidate base commit.
2. Preserve dirty changes in their current worktree. Never move, stash, reset, or clean them unless the user explicitly chooses that action.
3. Define each workstream's branch, path, base, file/write scope, verification, ports, database/schema, and integration order.
4. Confirm branch and target path do not already exist. Use an explicit sibling or configured worktree directory, never a broad or ambiguous path.

## 2. Create

Prefer the host agent's native worktree feature when it provides lifecycle tracking. Otherwise use an explicit command such as:

```bash
git fetch origin
git worktree add ../<repo>-<slug> -b <type>/<slug> <base-ref>
```

Fetch only when current remote state matters and network access is authorized. Do not copy `.env`, credentials, dependency directories, or build outputs. Share package caches only when the package manager supports concurrent access safely.

Assign unique ports, Compose project names, temporary directories, and test databases to concurrent worktrees.

## 3. Work and integrate

- Commit only each worktree's bounded changes on its own branch.
- Revalidate after rebasing or merging an updated base.
- Integrate through PRs, merge, or cherry-pick according to repository policy; one owner resolves cross-workstream design conflicts.
- Merge blockers before dependents. Run combined typecheck/tests/build in the integration branch, because isolated green results do not prove the combination is green.
- Never check out one branch in multiple worktrees or mutate another worktree's files from the current one.

## 4. Clean up safely

Remove a worktree only after confirming its changes are committed/pushed or intentionally disposable and the branch is integrated or preserved. Show `git status` for the target, then use `git worktree remove <exact-path>` and `git worktree prune` when appropriate.

Never use force removal or delete the directory directly without explicit approval. Report retained branches/worktrees and recovery references after cleanup.
