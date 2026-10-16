---
name: triage
description: 把外來議題推過一台由分診角色組成的狀態機，直到每一張都代理可接手或關閉。
disable-model-invocation: true
---

# Triage

Take issues that arrived from outside and push each to a terminal state.

**Only for issues you did not create.** Bug reports, feature requests, anything raw. Tickets from `/to-tickets` are already agent-ready — triaging them is wasted motion and invites re-litigating settled decisions.

Read `docs/agents/issue-tracker.md` for the label and list commands. If it is missing, run `/setup-skills` first.

## The roles

| Role | Meaning | Next |
| --- | --- | --- |
| `needs-triage` | Untouched. The queue. | anywhere |
| `needs-info` | Cannot proceed without an answer from the reporter. | back to `needs-triage` on reply |
| `ready-for-agent` | Specified well enough for an agent to build cold. | `/implement` |
| `ready-for-human` | Real, but needs a decision or judgement an agent should not make. | a human |
| `wontfix` | Closed with a reason. | terminal |

Exactly one role at a time. Two roles on one issue means the state machine is lying.

## Process

Work the `needs-triage` queue one issue at a time.

**Read it, then search.** Duplicates and already-fixed reports are the cheapest wins available. Search the tracker and the recent log before spending any thought on the issue itself.

**Reproduce, if it claims a bug.** A bug report that cannot be reproduced is `needs-info` — never guess at a repro and promote it. What lands in `ready-for-agent` must include the steps.

**Decide the role.** The question for `ready-for-agent` is the same as for a ticket: **could an agent that has never seen this issue build it from the issue alone?** If not, it is `needs-info` (missing facts) or `ready-for-human` (missing a decision).

**Rewrite before promoting.** Do not promote a raw report. `ready-for-agent` means it has been rewritten into ticket shape — outcome, done-when conditions, context, traps. Promoting without rewriting just moves the ambiguity downstream.

**Say why on `wontfix`.** One line, in the issue. A closed issue with no reason gets reopened.

## Rules

- **Never write code here.** Triage decides; it does not build.
- **Respond in the session's language.** Issue comments follow the language the issue was written in.
- **Do not invent facts.** A missing detail is `needs-info`. Filling it in from imagination produces a confidently wrong ticket.
- **Batch the report.** Work the queue, then report all the moves at once with the reason for each.
