---
name: to-spec
description: 把當前對話收斂成一份規格，並發佈到議題追蹤器。
disable-model-invocation: true
---

# To Spec

Collapse what the current conversation settled into a written spec, then publish it.

**No interview.** This skill synthesises what was already decided. If questions remain open, the conversation was not finished — go back to `/grill-with-docs`. A spec that papers over an unresolved branch buys nothing.

The issue tracker was configured by `/setup-skills` — read `docs/agents/issue-tracker.md`. If it is missing, run `/setup-skills` first.

## Shape

```markdown
# <what is being built>

## Why
The problem, in the user's terms. One paragraph.

## Scope
What this covers.

## Promises
Every testable commitment this spec makes, one line each, carrying a frozen
ID: `<ID> — <the behaviour promised>`. Everything downstream — test
cases, test markers, the blueprint's traceability table — keys on these.

## Out of scope
What it deliberately does not, and why. Load-bearing — this is the section
that stops the build drifting.

## Decisions
Each decision from the conversation, with the alternative that was rejected.
Link to an ADR where one exists rather than restating it.

## Open questions
What is still unresolved, and what would settle it. Empty is fine. Hiding
one here is not.
```

## Promise IDs

A **promise** is a commitment this spec makes that something downstream can test.

**The ID format is the project's, not this skill's.** A project with a requirement numbering scheme already in use (`FR-REF-03`, `NFR-Aud-004`, `SC-16`) keeps it — issuing a parallel scheme beside a working one creates a second source of truth for the same fact, and every downstream reference then has two names to disagree over. Only a project with no scheme gets one issued here: `PR-<AREA>-NN`, area from the project's domain language, reusing the areas `/uat-cases` already issued against when a case list exists. What this skill owns is the discipline, whatever the prefix:

**Issued once, frozen forever, never reissued.** A promise whose wording changed keeps its number. A promise that is dropped keeps its line, flipped to `retired` with a one-line reason — the retired line standing in the spec is what makes "never reissue" checkable by grep instead of by archaeology. Same discipline `/uat-cases` holds for `TC-` numbers, and for the same reason: a renumbered promise silently breaks every test marker, case and traceability row pointing at it.

Read the IDs already issued before issuing more. The published specs are the ledger; `docs/agents/issue-tracker.md` says where they live.

Specs written before IDs existed get numbered **on demand** — a promise takes a number when something downstream first needs to cite it, never in one sweep. Bulk numbering freezes hundreds of IDs the moment it writes them, and most are never cited.

## Rules

- **Use the project's vocabulary.** Read `CONTEXT.md` first. A spec that invents its own words forces a translation step on every reader.
- **A promise that cannot be enumerated is not a promise.** 「登入要好用」 cannot be traced or tested; 「會員以正確憑證登入後導向儀表板」 can. A Scope line that resists being written as a numbered promise means the conversation left it vague — that belongs under Open questions, not under a number.
- **Behaviour, not implementation.** The spec says what must be true. How to build it is `/to-tickets` and `/implement`.
- **Do not invent.** Anything not settled in the conversation goes under Open questions. Filling a gap with a plausible guess is how a spec quietly becomes wrong.
- **Show the draft before publishing.** Let the user edit, then publish.

## Finish

Publish per `docs/agents/issue-tracker.md` and report the URL or path. Say the next step: `/to-tickets` to split it, or `/implement` if it turned out to be one session of work.
