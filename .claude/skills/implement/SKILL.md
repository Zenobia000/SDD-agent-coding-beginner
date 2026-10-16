---
name: implement
description: 依規格或一組票建置，在議定的接縫上驅動 TDD，收尾跑一次程式碼審查。
disable-model-invocation: true
---

# Implement

Build one ticket, or one small spec, to a committed state.

**One ticket per context window.** If several tickets are in play, do one and stop. Carrying a finished ticket's context into the next one is how the second one drifts.

## 1. Orient

Read the ticket and whatever it links. Read `CONTEXT.md` for vocabulary — names in the code should match the glossary. Read any ADR covering the area; a decision recorded there is settled, not up for reconsideration.

Find the existing pattern before inventing one. Code that reads like the code around it is worth more than code that is locally better and locally unique.

## 2. Agree the seams

Say, before writing anything: what the public boundary is, what will be tested through it, and what will not be tested at all. A **seam** is where behaviour is observable without reaching inside.

If nothing here has a testable seam, that is the finding — say so and propose one, rather than testing internals to hit a number.

Wait for confirmation on the seams. Everything downstream depends on this being right, and it is cheap to fix now.

## 3. Build

Load the `/tdd` skill via the Skill tool — mandatory, before the first test is written, not "if needed". Skipping it silently is the most common way this step fails.

Drive `/tdd` at those seams: one failing test, just enough code, next. Vertical slices, never all the tests up front.

Not every line needs a test first. Wiring, config, and layout do not. The behaviour the ticket is about does.

Between slices: typecheck, and run **that** test file. Not the whole suite — the loop has to stay fast enough to stay in.

## 4. Close

- Full test suite, once. Green.
- Typecheck and lint, clean.
- Load the `/code-review` skill via the Skill tool — mandatory, not optional — and review against the ticket. Fix what it finds; push back in writing on what you disagree with.
- Re-read the ticket's *Done when* list and check each condition literally.
- Any ADR this ticket implements that is still `Status: Proposed` → flip it to `Accepted` in the same commit. An ADR for work that has landed is no longer a proposal.

## 5. Commit

Commit to the current branch. Message says what changed and why, and references the ticket.

Report: what was built, what the review found, what was left undone and why. **Anything skipped gets said out loud.** A silent omission reads as complete and is the most expensive kind of error to find later.
