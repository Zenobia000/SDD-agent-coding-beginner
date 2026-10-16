---
name: to-architecture
description: 在規格與拆票之間補上架構這一步：技術棧、資料模型、API 合約。每個取捨仍寫成獨立 ADR，架構文件只引用不重述。多 session 建置才需要，可選。
disable-model-invocation: true
---

# To Architecture

Turn a spec into the technical decisions the tickets will depend on: tech stack, data model, API contracts. Runs after `/to-spec`, before `/to-tickets` — architecture decisions directly change how work should be split, so settle them first.

**Optional step.** A one-session change, or a change inside an architecture that already exists, does not need this. Reach for it when the spec spans multiple sessions and the tech choices are genuinely open.

The issue tracker and docs layout were configured by `/setup-skills` — read `docs/agents/`. If missing, run `/setup-skills` first.

## Shape

One document at `docs/architecture.md` (or where `docs/agents/` says architecture lives):

```markdown
# Architecture — <what is being built>

> Scaffolding — durable decisions live in ADRs and tickets. Delete this file when the feature ships.

## Stack
| Layer | Choice | ADR |
| --- | --- | --- |
| <db / queue / framework…> | <choice> | [0007](docs/adr/0007-….md) |

## Data model
The core entities, who owns each, and the relations that matter.
Tables or a Mermaid ER diagram — whichever is shorter.

## API contracts
Endpoints and payload shapes the tickets will build against.
Only the contracts tickets need — not a full REST catalogue.

## Constraints
Measured targets only (latency budgets, quotas, compatibility floors).
No target measured or promised → this section is absent.
```

## Rules

- **One ADR per decision — the document links, never restates.** Every row in Stack that involved a real trade-off gets its own ADR via `/domain-modeling` (its three-part gate decides; a choice with no alternative considered gets no ADR and no apology).
- **This document is scaffolding, not truth.** Every durable decision must already live in an ADR or a ticket before it appears here — deleting this file must lose nothing. Nobody maintains a per-feature spec after merge; git history is the archive.
- **Decisions, not ceremony.** No C4 diagram levels, no NFR boilerplate, no security checklist. A section with nothing settled in it does not appear.
- **Do not invent.** The material is the spec and the conversation. An open tech choice goes back to `/grill-with-docs` or gets a `/prototype` detour — it does not get a plausible default.
- **Use the project's vocabulary.** Read `CONTEXT.md` first; the data model must use its terms.
- **Show the draft before writing.** Let the user edit, then write the file and the ADRs.

## Finish

Report the file path and the ADRs created. Say the next step: `/to-tickets` — tickets may now cite the contracts and entities by name, and the final ticket's done-when must include deleting this scaffolding file (never committed in private mode; deletion is local hygiene).

## Rationalization table

| Excuse | Reality |
| --- | --- |
| "I'll batch the trade-offs into the document, ADRs later" | Later is never. The document restating decisions is a second source of truth that starts lying the day an ADR changes. |
| "A C4 diagram makes it look complete" | Ceremony is not completeness. Diagrams earn their place by answering a question a ticket will ask. |
| "The spec didn't pick a database, Postgres is a safe default" | A guessed default is a decision nobody made. Unsettled choices go back upstream. |
