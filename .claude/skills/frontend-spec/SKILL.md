---
name: frontend-spec
description: 為有 UI 的規格產出前端規格書與 Pencil 設計稿：路由表、每頁 design brief、四態畫面（Loading/Empty/Error/Success）的 .pen mockup。在 /to-spec 之後、/to-tickets 之前跑，可選。
disable-model-invocation: true
---

# Frontend Spec

Turn a spec's UI surface into a frontend spec plus Pencil mockups. Runs after `/to-spec` (and `/to-architecture` if it ran), before `/to-tickets` — tickets that can cite `dashboard.pen`'s Empty frame are verifiable; "make a nice dashboard" is not.

**Optional step.** No UI in the spec → skip entirely.

**Not `/prototype`.** Prototype answers "does this interaction work" with throwaway code that gets deleted. This skill produces durable deliverables: the spec document and `.pen` files that tickets build against. Never let a prototype graduate into a mockup — redraw the answer here.

## Shape

One document at `docs/frontend-spec.md`, mockups under `docs/mockup/`:

```markdown
# Frontend spec — <what is being built>

> Scaffolding — durable decisions live in ADRs and tickets. Delete this file when the feature ships.

## Routes
| Page | Path | Auth | One-line purpose |
| --- | --- | --- | --- |

## Style tokens
Chosen style archetype, colors, type, density — set once via Pencil
variables, shared by every screen. Never restyled per page.

## Pages
### <page> → `docs/mockup/<page>.pen`
- **Story**: as <role>, I want <action>, so that <goal>.
- **Dominant region**: the one question this page answers, and its one
  primary action.
- **States**: Loading / Empty / Error / Success — each is a frame in the
  .pen file. A page missing a state frame is not done.
```

## Pencil workflow — per .pen file, in order

`.pen` files are encrypted: only `pencil` MCP tools may touch them — never Read/Grep/Edit.

1. `get_editor_state(include_schema: true)` — no schema, no other Pencil calls.
2. `get_guidelines()` — pick the guide matching the product type and one style archetype; write its tokens as shared variables.
3. `batch_design(...)` — one screen per file, filename from the route table. Reusable components live in `components.pen`; other screens reference them, never redraw.
4. `snapshot_layout(...)` + `get_screenshot(...)` — verify structure and look at the screenshot before calling a screen done. Desktop and mobile frames both; hierarchy must survive every breakpoint.

## Rules

- **The .pen file is the source of truth for layout.** The document carries briefs and acceptance state lists; pixels live in Pencil. Never hand-write HTML/CSS as a stand-in for a mockup.
- **The document is scaffolding, not truth.** Every durable decision must already live in an ADR or a ticket before it appears here — deleting the document must lose nothing. Nobody maintains a per-feature spec after merge; git history is the archive.
- **All four states, every page.** Silent failure is not a design. An Empty state nobody drew becomes an Error state nobody handled.
- **No standards sections.** Coding conventions, browser support, API-client choices belong to the target repo's CLAUDE.md — not here.
- **Do not invent flows.** A page or interaction not settled in the spec goes back to `/grill-with-docs`, or through a `/prototype` detour if it needs a runnable answer.
- **Show the draft before writing.** Document first, then mockups; let the user redirect before pixels get expensive.

## Finish

Report the document path and the `.pen` files produced, each verified by screenshot. Say the next step: `/to-tickets` — tickets cite pages and state frames by name, and the final ticket's done-when must include deleting the scaffolding document (never committed in private mode; deletion is local hygiene). The `.pen` mockups follow the same lifecycle.

## Rationalization table

| Excuse | Reality |
| --- | --- |
| "The prototype already looks right, I'll reuse its code as the mockup" | Prototype code carries every shortcut it was born with. Keep the answer, redraw the design. |
| "Success state is obvious, I'll skip Empty/Error frames" | The undrawn states are where users actually live. Four frames or the page is not specced. |
| "I'll restyle this one page, it's special" | One shared token set. A special page today is an inconsistent app in a month. |
| "Screenshot looks fine in my head, no need to render it" | Layouts overlap in ways schemas don't show. Look at the screenshot before you call it done. |
