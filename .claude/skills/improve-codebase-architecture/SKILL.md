---
name: improve-codebase-architecture
description: 勘查程式庫的深化機會，排序後呈上，再對你挑中的那一個進行拷問。
disable-model-invocation: true
---

# Improve Codebase Architecture

Upkeep, not feature work. Run it when there is a spare moment and the goal is to keep the codebase good to operate in — for agents and for you.

This skill **surveys**. It finds candidates and hands the chosen one into the main flow. It does not refactor.

## The thing being looked for

A **deep module**: a lot of behaviour behind a small interface. The opposite — a shallow module — costs more to use than it saves, because its interface is nearly as complicated as the thing it hides.

The signals, in rough order of how much they cost:

- **Shallow modules** — a wrapper whose interface restates its implementation
- **Leaky interfaces** — callers that must know the internals to use it correctly (call order, initialise-then-use, awareness of a private cache)
- **Information leakage** — one design decision spread across several modules, so changing it means changing all of them
- **Pass-through layers** — a function that only forwards to another, adding a name and nothing else
- **Temporal decomposition** — modules split by *when* things happen rather than *what* they know, which spreads one concept across each stage
- **Missing seams** — behaviour with no boundary to test at (this is what `/diagnosing-bugs` hands over when a bug had nowhere to be caught)
- **Conjoined change** — files that always appear in the same commit, but live apart

`git log` earns its keep here: files that change together, and files that change constantly, are where the real coupling is — independent of what the structure claims.

## Process

**Survey.** Read broadly. Note evidence, not impressions — a claim needs a file and a line.

**Rank by leverage.** Each candidate gets: what is wrong, the evidence, what it costs today, and roughly what fixing it costs. Rank by cost-today ÷ fix-cost, not by how ugly it is.

Ugly and cheap to live with loses to clean-looking and expensive every time.

**Present and stop.** Show the ranked list. The user picks. Picking one **generates an idea** — hand it to `/grill-with-docs` to design, then the main flow builds it.

## Rules

- **Do not refactor here.** Surveying and changing in one pass produces a diff nobody can review.
- **No speculative generality.** "This will be hard to extend later" is not a finding unless there is a real, named, near-term extension.
- **Say when it is fine.** A survey that always finds work is a survey that is padding.
