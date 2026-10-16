---
name: feasibility
description: 在規格與拆票之間補上可行性這一關：技術風險、競品對照、成功指標、量級成本，收在明確判決上（✅／⚠️／❌），以 comment 掛回 spec issue。規格帶真實不確定性才需要，可選。
disable-model-invocation: true
---

# Feasibility

Assess a published spec before work gets split into tickets: can it be built, is it worth building, what does success look like, what will it roughly cost. Runs after `/to-spec`, before `/to-tickets` — a spec that fails here should not be ticketed.

**Optional step.** A small internal change with no open technical risk does not need this. Reach for it when the spec carries real uncertainty — new tech, external dependencies, a market with alternatives.

The issue tracker was configured by `/setup-skills` — read `docs/agents/issue-tracker.md`. If it is missing, run `/setup-skills` first.

## Input

The published spec issue plus the current conversation. Fetch the spec from the tracker — never ask the user to paste it, and never re-derive it from memory. Read `CONTEXT.md` first; the assessment must use the project's vocabulary.

## The four questions

Answer all four. Reference the spec by section — never restate it; the report and the spec live on the same issue.

1. **Can it be built?** The technical risks: architecture-level unknowns, external dependencies and their limits (quotas, latency, licensing), the one or two things most likely to sink the build. Not a design — that is `/to-architecture`.
2. **Is it worth building?** Search the web for existing alternatives — products, open-source projects, the manual process people use today. Compare honestly, including where the alternative is stronger. No direct competitor found → say "no direct competitor found" and list the closest substitutes. Never invent an opponent to win against.
3. **What does success look like?** 2–4 measurable indicators with target values, and the milestone at which each gets measured. An indicator nobody will actually measure does not belong here.
4. **What will it cost?** Order of magnitude only — person-weeks, person-months, or person-years, derived from the spec's scope. No team rosters, no week-by-week plans; that is `/to-tickets` territory.

## Verdict

The report must end on exactly one of:

- **✅ Feasible** — proceed to `/to-tickets`.
- **⚠️ Conditionally feasible** — proceed only after the listed conditions clear. Every condition must be a **verifiable action** ("obtain the API quota raise", "PoC shows p95 latency < 100ms"), each naming who can clear it and whether work may start before it does. An adjective is not a condition — "needs further research" and "depends on resources" do not qualify. If no verifiable condition can be written, the verdict is ❌.
- **❌ Not feasible** — back to the spec. State which of the four questions killed it and what change would reopen the door.

"It has pros and cons" is not a verdict. A report that ends without committing to one of the three is the failure mode this skill exists to prevent.

## Rules

- **Do not invent.** Every claim traces to the spec, the conversation, or a search result. A gap the material cannot answer goes into the verdict as a ⚠️ condition or a ❌ reason — not a plausible guess.
- **The report is a snapshot, not an ADR.** Competitor state, estimates, and indicators all expire. But a durable decision hatched during assessment ("buy X, do not build — building was judged infeasible") must be recorded on its own: load the `/domain-modeling` skill via the Skill tool — mandatory — and let its three-part gate decide whether it becomes an ADR. The report links the ADR, never restates it.
- **Show the draft before posting.** Let the user edit — the verdict included. Then post.

## Finish

Post the report as a comment on the spec issue per `docs/agents/issue-tracker.md` and report the URL. Say the next step by verdict: ✅ → `/to-tickets`; ⚠️ → clear the conditions (a `/prototype` detour often clears a technical one); ❌ → back to `/grill-with-docs` to rework the spec.

## Rationalization table

| Excuse | Reality |
| --- | --- |
| "Both options have merit, I'll present the trade-offs" | A verdict-free assessment is a form the user fills in themselves. Committing to ✅/⚠️/❌ is the entire job. |
| "⚠️ with 'needs more investigation' keeps it safe" | An unverifiable condition is ❌ wearing a costume. Name the action that clears it, or judge it infeasible. |
| "No competitor showed up, but surely someone does this — I'll describe a typical one" | An invented competitor produces an invented advantage. "No direct competitor found" is a finding, not a failure. |
| "While I'm at it, an 8-week team plan would be helpful" | Schedules come from tickets. A plan derived from zero tickets is fiction with dates on it. |
