---
name: compass
description: 問這個情況該用哪個技能、走哪條流程。工具箱的路由器。
disable-model-invocation: true
---

# Compass

You don't remember every skill, so ask.

A **flow** is a path through the skills. Most work runs along one **main flow**; three **on-ramps** merge onto it. Everything else is standalone or a vocabulary layer running underneath.

## Precondition

**`/setup-skills`** — run once per repo before any engineering flow. It records where issues live and where domain docs go. Skills that publish to a tracker are wrong without it.

## Main flow: idea → ship

1. **`/grill-with-docs`** — sharpen the idea by interview, leaving a paper trail in `CONTEXT.md` and ADRs. No codebase to write into? Run `/grilling` on its own.
2. **Branch — does a question need a runnable answer?** State model, business logic, a UI you have to see. Detour: **`/handoff`** out → fresh session → **`/prototype`** → **`/handoff`** back.
3. **Branch — is this more than one session of build?**
   - **Yes** → **`/to-spec`**, then **`/to-tickets`**. Each ticket declares its blocking edges. Run **`/implement`** once per ticket, **`/clear`ing context between each one** — each ticket is self-contained, so the last one's context is disposable.
   - **No** → **`/implement`** right here.

`/implement` drives `/tdd` internally and closes with `/code-review` before committing. Reach for `/tdd` alone to build one concrete behaviour test-first; `/code-review` alone to review any branch against a fixed point.

### Context hygiene

Steps 1–3 stay in **one unbroken context window** — no compact, no clear, until `/to-tickets` is done. The limit is the **smart zone**: the window (~150k tokens) where the model still reasons sharply. If a session approaches it early, don't push on degraded — `/compact` at the nearest phase boundary and carry on.

At every **phase boundary** — the gap between two chunks of work — there are five options: Continue, `/clear`, `/handoff`, subagent, `/compact`. Read [PHASE-BOUNDARIES.md](PHASE-BOUNDARIES.md) for the ordered tree: the five questions, why **Continue** is ruled out first (primary-source cost), and why `/compact` is the default at the bottom, not the first reach. Make the decision **at** a boundary; mid-phase, continue or split the rest into subagents.

## On-ramps

- **Incoming bugs and requests piling up** → **`/triage`**. Only for issues you did *not* create. Tickets from `/to-tickets` are already agent-ready — do not triage them. Output merges at `/implement`.
- **Something is broken** → **`/diagnosing-bugs`**. For the ones that resist a first glance: intermittent flakes, regressions between two known-good states. When the finding is "there was no seam to lock this down", it merges at `/improve-codebase-architecture`.
- **A fog too big for one session** → **`/wayfinder`**. Charts a map of decision tickets and resolves them one at a time, producing **decisions, not deliverables**. When the fog clears it merges at **`/to-spec`** — never straight into `/implement`, which throws the map's linked detail away.

## Codebase health

- **`/improve-codebase-architecture`** — survey for deepening opportunities. Picking one *generates an idea*, which re-enters the main flow at `/grill-with-docs`.

## Git flow

The branch lifecycle, one skill per stage — each acts only on what you decided, never guesses:

- **`/git-commit`** — commit what *you* staged and push; empty staging stops and asks.
- **`/git-pr`** — open the PR (English title, Traditional Chinese body), and clean up branches after the merge is verified.
- **`/git-release`** — bump version files, distill the changelog in Traditional Chinese, tag, and publish the release page.

## Standalone

Off the main flow entirely.

- **`/wizard`** — when a procedure needs the **human's** hands (provisioning, credentials, CI secrets, a one-off migration), generate an interactive bash wizard that walks them through it. Steps the agent can do itself never go in a wizard.
- **`/wait-what`** — the agent's last message didn't land. Stop and make it re-pitch: context first, plain technical language, the project's vocabulary.
- **`/to-questionnaire`** — a decision you can't answer alone becomes a questionnaire for the one person who can. It grills the *send* (who, and what you need back), never the subject.
- **`/writing-for-agents`** — the reference for writing any document an agent consumes: skills, `CLAUDE.md`/`AGENTS.md`, pointed-at docs. Load it before writing or editing one.

## Vocabulary underneath

Reach for these when the **words**, not the process, are the problem.

- **`/domain-modeling`** — the project's domain language. Challenge a fuzzy term, split an overloaded one, record a hard-to-reverse decision as an ADR.
- **`/grilling`** — the interview primitive `/grill-with-docs` and `/wayfinder` both run.
