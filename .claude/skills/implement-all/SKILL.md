---
name: implement-all
description: 從議題追蹤器抓出可動工的票，依阻塞邊排程，每張票派一個子代理跑 /implement，彙整回報。只編排不動手，合併永遠留給使用者。
disable-model-invocation: true
argument-hint: 可選 — 限定票號或標籤
---

# Implement All

Clear the open tickets: schedule by blocking edges, run each ticket through the `/implement` skill in an isolated subagent, aggregate one report. This skill orchestrates; it never builds anything itself.

## 1. Load the ticket list

Read `docs/agents/issue-tracker.md` for the exact list command and how blocking edges are expressed. No such file → stop and ask the user to run `/setup-skills` first.

List open tickets, narrowed by the argument if one was given. Zero tickets → report that and stop.

## 2. Schedule by blocking edges

Build the run order from the tickets' declared blocking edges:

- A ticket whose blockers are all closed is **ready**.
- Ready tickets that touch disjoint files may run in parallel, each in its own git worktree on its own branch.
- Unsure whether two tickets overlap → run them sequentially. A wrong parallel guess costs a merge conflict; a wrong sequential guess costs minutes.

Present the schedule — waves, what runs in parallel, what waits — and **wait for the user's approval before dispatching anything**. This one checkpoint replaces N mid-run interruptions: subagents cannot ask the user questions.

## 3. Write the progress file

Long batches outlive the context window. In one field run the orchestrator was auto-compacted 11 times and the handoff summary carried state across exactly once. Conversation memory is not the ledger — a file on disk is.

Immediately after the user approves the schedule, and before dispatching anything, write `docs/agents/implement-all-progress.md`:

```
# implement-all progress — <argument, or "all">
Approved schedule: <waves, verbatim>

| ticket | wave | status | branch | blocker |
| <id> | 1 | pending | — | — |
```

- Update the ticket's row the moment its subagent returns — before dispatching the next one, not in a batch at the end.
- **After any compact or context loss, read this file before doing anything else.** It is the source of truth for what ran, what is running, and what is next; the conversation is not.
- The file is scaffolding: never commit it, and delete it after the final report. The report and the branches are the durable record.

## 4. Dispatch

One subagent per ticket, hard turn limit, each instructed to:

- Load the `/implement` skill via the Skill tool — mandatory first action — and run it on its ticket, on its own branch (parallel tickets: own worktree). Never invoke `/implement-all` — one orchestrator, no recursion.
- Treat the approved schedule as the seam confirmation `/implement` step 2 asks for. A ticket that names no seam is **blocked** — report it, never invent a seam mid-flight.
- Return a structured result and nothing else:

```
ticket: <id>
status: done | blocked
branch: <name>
commits: <n>
blocker: <one line, only when blocked>
```

A subagent that stalls or dies is recorded as `blocked`; its branch stays as-is for a human to pick up. Failed work is never cleaned away.

## 5. Report

One table: ticket, status, branch, blocker. Then:

- Blocked tickets: quote each blocker verbatim and ask the user how to proceed.
- Done tickets: branches are ready for review. **Never merge, never open PRs, never delete branches** — those are the user's buttons.
- Delete `docs/agents/implement-all-progress.md` — the batch is over, the report supersedes it.

## Rationalization table

| Excuse | Reality |
| --- | --- |
| "These two tickets look independent, parallelize" | Looking independent is not being independent. Unsure → sequential. |
| "The subagent is stuck, I'll finish its ticket myself" | An orchestrator that starts building loses the plot. Record blocked, move on. |
| "All green — I'll merge the branches to save the user a step" | Merge is the trust boundary. It is the user's button. |
| "The ticket names no seam, I'll pick a reasonable one" | Seams are agreed with humans before dispatch. That ticket is blocked. |
| "I remember the schedule, no need to write it down" | Eleven auto-compacts in one field run say otherwise. The file survives; you don't. |
