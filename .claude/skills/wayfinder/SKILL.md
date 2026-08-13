---
name: wayfinder
description: 把龐大而迷霧重重的工程畫成一張決策票地圖，一次解一張，直到通往終點的路清晰為止。
disable-model-invocation: true
---

# Wayfinder

For the effort too big to hold in one session: a greenfield project, a migration, a feature build where the route from here to the destination is not visible yet.

It produces **decisions, not deliverables**. Nothing gets built here.

The most expensive flow in this repo. `/grill-with-docs` handles the idea you can hold in one session — reach for wayfinder only for the one you cannot. On a well-scoped feature it is pure overhead.

Read `docs/agents/issue-tracker.md` for the create and link commands. If it is missing, run `/setup-skills` first.

## 1. Name the destination

One paragraph: what is true when this is done. Not how — what.

If the destination cannot be written down, that is the first thing to resolve, and nothing else can be mapped until it is.

## 2. Cut the fog into decision tickets

Create a parent issue — the **map**. Under it, one child issue per **decision ticket**: a *question* whose resolution is a decision.

A decision ticket, not an implementation ticket:

- ✅ "Do sessions live in Postgres or Redis?"
- ✅ "Is the import synchronous, or a job queue?"
- ❌ "Build the session store" — that is a `/to-tickets` output, later

Each ticket carries: the question, why it matters, what it blocks, and the options as currently understood. Blocking edges between tickets are the shape of the fog — an unresolved ticket that blocks four others is where to look first.

The map is not complete at the start and does not need to be. Resolving one ticket routinely spawns two more; that is the fog receding, not a planning failure.

## 3. Resolve one at a time

Pick the ticket that unblocks the most. Load the `/grilling` skill via the Skill tool — mandatory, every ticket, even if it was loaded for a previous one — and run it on that question alone, in the session's language.

Where the answer needs to be runnable, `/handoff` out to a `/prototype` session and bring the answer back.

Write the resolution **into the ticket** — the decision, the rejected options, and why — and close it. Then load the `/domain-modeling` skill via the Skill tool and apply its three-part ADR gate; a resolution that passes gets an ADR at `Status: Proposed`, since nothing is built yet. A resolution that lives only in a conversation is a resolution that will be re-litigated.

**Clear context between tickets.** The map is the memory; that is what it is for.

## 4. Stop when the way is clear

Not when every ticket is closed. When you can see the route from here to the destination, stop mapping.

## 5. Hand off — do not build

Merge onto the main flow at **`/to-spec`**, which collapses the map's linked decisions into one buildable plan, then `/to-tickets`, then `/implement`.

Going straight from the map to `/implement` skips that collapse and throws the linked detail away. Do it only if the effort turned out genuinely small — which means wayfinder was the wrong tool and that is worth noting.
