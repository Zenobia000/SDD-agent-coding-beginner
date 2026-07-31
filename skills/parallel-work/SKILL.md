---
name: parallel-work
description: Split a task into safe concurrent workstreams and aggregate their outputs without dependency, context, or file-write collisions. Use when two or more investigations, reviews, tests, or implementations could run in parallel, or when deciding whether parallelism is actually beneficial.
---

# Parallel Work

Parallelize only independent work. More workers on a dependency chain create coordination overhead, not speed.

## 1. Draw the dependency graph

For every candidate workstream record:

- input artifacts and facts it needs;
- decision or deliverable it produces;
- files/state it may read and write;
- side effects, external systems, ports, databases, and git operations;
- tasks that block it and tasks it unblocks.

The frontier contains tasks whose blockers are complete. Run frontier tasks concurrently only when their write sets and side effects do not conflict.

## 2. Choose the isolation level

- Same working tree: read-only exploration, independent reviews, or commands that only create separate temporary artifacts.
- Separate worktrees: concurrent implementations, migrations, generated files, formatters, or any tasks that may touch overlapping repository state. Use `worktree-strategy`.
- Sequential: one task consumes another's result, both edit the same conceptual decision, share a mutable database/port/index, or require the same human decision.

Do not parallelize `git add`, commits, rebases, merges, package-lock generation, schema migrations against one database, or fixes whose correct design is still undecided.

## 3. Give each worker a bounded contract

Provide only task-local context:

```text
Objective:
Inputs and fixed point:
Allowed read/write scope:
Required output artifact:
Verification command:
Stop conditions and forbidden side effects:
```

Avoid leaking the expected conclusion to independent reviewers. Ask for evidence, paths, commands, uncertainties, and one recommended next action.

## 4. Fan in deliberately

Wait for every required result, then validate artifacts rather than trusting summaries. Reconcile contradictions against primary evidence. Check combined diffs for overlapping assumptions, run integration checks once, and report failed/cancelled workstreams.

Parallel speedup is bounded by the longest dependency chain. Prefer two high-value independent tasks over many tiny agents whose coordination costs exceed their work.
