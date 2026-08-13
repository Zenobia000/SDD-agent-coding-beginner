---
name: refactor
description: 在不改變可觀察行為的前提下重整程式碼結構：特徵測試護網、一次一個 transform、綠燈即經 /git-commit 提交。
disable-model-invocation: true
---

# Refactor

Change the structure. Do not change the behaviour. That line is the entire definition — a diff that alters what callers observe is not a refactor, whatever it is called.

**Observable** means what crosses a seam: return values, thrown errors, persisted data, outgoing requests. Private names, internal structure, call counts are fair game — unless something external depends on them (an SLA on latency, a parser on log format). When in doubt, treat it as behaviour.

## 0. Name the trigger

State, in one sentence, which of these applies:

- **Preparatory** — a coming change is hard; this restructuring makes it easy.
- **Rule of three** — the same thing now exists in a third place.
- **Comprehension** — it took real effort to understand; write the understanding back into the code. The bar: someone new to this codebase can follow it without asking.

No trigger → stop. "It could be cleaner" is not a trigger; clean has no finish line, triggers do. The trigger goes in the commit message — it is also the stop condition.

Given a path but no trigger, **scan first**. List candidates one per line, each as **finding → trigger → transform**: `calcTax duplicated in a third place → rule of three → Extract calculateTax`. No trigger, no line — the scan hunts triggered work, not beautification. Then stop: invoking the skill authorized the process; the user's pick authorizes the scope. Only picked candidates enter the loop.

Where the scan looks:

- **Comprehension**: long functions, long parameter lists, opaque names, logic that takes effort to follow, comment style that drifts from the project's documented conventions.
- **Comprehension, at the type level**: primitive obsession, parallel arrays, anonymous dicts passed around — value types and named types say what the code means. Expressiveness is the only motive here; a change chasing performance needs a measurement first, and that is a ticket, not a scan line.
- **Rule of three**: the same logic in a third place. When the duplication is conditional dispatch repeated across sites, a design pattern may be the transform's *destination* (Replace Conditional with Strategy) — never its starting point.

## 1. The net comes first

Before touching structure, there must be tests that pin the behaviour being moved, and they must be green.

None exist → write **characterization tests** first: tests that record what the code *does now*, including the parts that look wrong — someone may depend on them. Pin the seam's outputs, the boundary values (empty, zero, one, huge, null), and every branch that will move. Do not chase coverage; chase *goes red when I break it*.

**From this point until done, the test files are frozen.** A test edited mid-refactor is a net you cut yourself. If a test truly must change, that is a behaviour change — stop, finish or revert the refactor, do it separately.

## 2. One transform at a time

Extract function. Move function. Rename. Inline. Introduce value type. Split phase. Pick **one**, apply it, run the tests.

**Green** → commit, through one door:

1. Stage exactly the files this transform touched — never `git add -A`.
2. Apply the `/git-commit` rules — **mandatory**. If they are not already in this context, read its `SKILL.md` first (the Skill tool cannot load user-triggered skills). `/git-commit` owns the message format, the branch check, and the push; never write a commit that ignores it.
3. The subject names the transform: `Extract calculateTax`.

`/git-commit` is the repo's **commit primitive**, and invoking `/refactor` is the user's authorization for these per-transform commits. The transform *is* the staging boundary; everything outside its files stays unstaged.

**Red** → `git reset --hard HEAD` and retry smaller. HEAD is always the last green state, because every green transform was committed; the guard hook allows no other target. The reset leaves untracked files behind — check `git status --short` and delete each file this transform created, by explicit path. Never `git clean -fd`: it sweeps the user's files with yours. And never debug a half-applied refactor — that is two unknowns at once.

- Use the IDE's rename/extract where it exists. The tool does not typo; you do.
- Leaf to root: smallest independent transform first, each one making the next simpler.
- A bug found along the way gets an issue, not a fix in this diff. Mixed commits force a choice between keeping the bug and losing the refactor at revert time.

Comments and names are structure, not behaviour — rewriting them for clarity, or unifying their style, is a legal transform. It is still **one** transform: unify the comments of the code being touched, in its own commit; it is not a licence to sweep the repo. Follow the project's documented comment conventions (language, tone, density) where they exist.

Inlining is a refactor too. An abstraction with one implementation and no second in sight gets removed, not admired. Only-ever-more-abstract is how a codebase reaches a different kind of mud.

## 3. Stop when the trigger dies

Preparatory → the change is now easy: stop and go make it. Rule of three → the duplication is gone: stop. Comprehension → it reads: stop.

Close-out, all three literally:

1. Full suite green, and the test files byte-identical to step 1.
2. Re-read the diff asking of each hunk: does this change anything a caller observes?
3. The trigger sentence is in the commit or PR description.

## When not to

- Code about to be rewritten or deleted.
- No tests and no way to write them — that inability is the real problem; hand it to `/improve-codebase-architecture`.
- Against a deadline: the payoff is in the future, the deadline is not.
- The only reason is taste.

## Boundaries

This skill is the **middle scale**. The few lines just written are `/tdd`'s refactor step — no ceremony needed. A restructuring that spans modules or changes a design decision goes through `/improve-codebase-architecture` and the main flow — too big for a single frozen-net session. And the inverse invariant of `/tdd` is the reason this is a separate skill: there, behaviour changes and a test goes red first; here, behaviour holds and nothing goes red, ever.
