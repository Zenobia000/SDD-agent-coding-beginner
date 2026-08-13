---
name: to-tickets
description: 把計畫、規格或對話切成一張張曳光彈票，每張都標明自己的阻塞邊。
disable-model-invocation: true
---

# To Tickets

Split the work into tickets an agent can pick up cold, one per session.

The issue tracker was configured by `/setup-skills` — read `docs/agents/issue-tracker.md` for the exact create command and how blocking edges are expressed. If it is missing, run `/setup-skills` first.

## Tracer bullets, not layers

Every ticket is a **vertical slice**: something observably works when it is done. Never "add the database schema", "add the API layer", "add the UI" — three tickets, and nothing works until all three land, so nothing can be reviewed or reverted independently.

The first ticket is the **tracer bullet**: the thinnest path that runs end to end. It is allowed to be embarrassing — one hardcoded case, no error handling. Its job is to prove the seams line up. Everything after it widens that path.

## Sizing

One ticket = one fresh context window. If it needs more, split it. If three of them are one-liners, merge them.

The test for a good ticket: **could an agent that has never seen this conversation do it from the ticket alone?** If it needs the conversation, the ticket is underspecified.

## Blocking edges

Each ticket names what must be done before it. Real dependencies only — "B needs the type A defines" is an edge; "B feels like it comes after A" is not. Invented edges serialise work that could have run in parallel.

On a real tracker these become native blocking links, so any ticket with cleared blockers can be grabbed. On a local markdown tracker they are a `Blocked by:` line, worked blockers-first by hand.

## Ticket shape

```markdown
# <verb the outcome: "Persist sessions to Postgres">

## Done when
Observable conditions. Someone else must be able to check these without
reading the implementation.

## Context
The one paragraph of background needed to start. Link the spec, do not
restate it.

## Blocked by
#12, #14 — or "nothing".

## Notes
Traps, decided-against alternatives, the seam to test at.
```

## Rules

- **Do not triage these.** They are already agent-ready. `/triage` is for issues that arrived from outside.
- **Show the full set before publishing** — the sizing and the edges are much easier to judge as a list than one at a time.
- **Scaffolding docs die with the last ticket.** When the spec cites a document marked `Scaffolding` (architecture, frontend spec, mockups), the final ticket's done-when includes deleting it — its durable content already lives in ADRs and these tickets.

## Finish

Publish, report the URLs or paths and the blocking graph, and say: run `/implement` per ticket, **`/clear`ing context between each one** — each ticket is self-contained, so the last one's context is disposable.
