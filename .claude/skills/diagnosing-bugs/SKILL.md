---
name: diagnosing-bugs
description: 對付硬 bug、間歇性失敗與效能回歸的紀律迴圈 — 重現、最小化、立假說、下探針、修好、補回歸測試。當東西壞了而原因不明顯時使用，也對應 "flaky"、"regression"、「時好時壞」、「找不到原因」等說法。
---

# Diagnosing Bugs

For the bugs that resist a first glance: the intermittent flake, the regression that crept in between two known-good states, the failure that only happens in one environment.

## The one rule

**No theorising until you have a tight feedback loop.** One command that goes red on *this* bug, right now, in under a few seconds.

Everything before that loop exists is guessing, and guessing on a hard bug produces a fix that changes the symptom rather than the cause. If getting to a fast red is hard, that *is* the first task — not a detour from it.

## 0. Triage

Classify the failure before chasing it — three buckets, three different treatments:

- **Real regression** — the product broke. The seven steps below.
- **Flake** — fails intermittently against unchanged code. Still a bug; the hunt is for the hidden condition (step 1's discipline). A green retry hides the signal the red just gave you — the retry count is data, not a fix.
- **Infrastructure** — runner died, network hiccup, disk full. Not a bug-fixing problem: fix or report the environment, and say which. The seven steps do not apply.

Triage also names which side broke: a failing *test* over correct product behaviour is a bug in the test, and the fix lands there.

## 1. Reproduce

Get it failing on demand. Intermittent means "reproduces under conditions you have not identified yet" — hunt the condition: ordering, concurrency, time, cached state, environment.

A bug you cannot reproduce cannot be verified as fixed. Stop and say so rather than shipping a speculative change.

## 2. Minimise

Cut everything that is not needed to still see the failure. Inputs, steps, config, code paths. Each cut either keeps the bug — good, cut more — or kills it, which just told you something.

Minimising usually finds the bug outright. That is the point.

## 3. Bisect, when there was a known-good state

`git bisect` against the minimal repro. This is the cheapest available answer whenever a "it used to work" exists, and it is skipped far too often in favour of reading code.

## 4. Hypothesise

Write the hypothesis down as a falsifiable statement: "the token is compared before the refresh completes, so a request in that window sees the old value."

**One hypothesis at a time.** Changing two things and seeing green tells you nothing about which one mattered.

## 5. Instrument

Prove or kill the hypothesis with evidence — a log, a breakpoint, an assertion. Not by reading the code harder. Reading finds what you expect to find; a printed value does not.

Killed hypothesis → back to 4, with what you learned. Do not smuggle a dead theory into the next one.

**Redact before you paste.** Probe output lands in the conversation, and the conversation is not a safe place for live credentials. Replace tokens, keys, passwords, and connection strings with `<REDACTED>` before quoting any captured output — the shape of a value proves a hypothesis just as well as the value itself.

## 6. Fix

Fix the **cause**, not the symptom. A `try/catch` around a crash, a retry around a race, a null guard on a value that should never be null — those hide the bug and hand the next person a harder one.

If the real cause is out of scope to fix, say that explicitly and mitigate deliberately, in writing.

## 7. Regression test

A test that fails before the fix and passes after. Confirm both directions — revert the fix and watch it go red. A regression test that was never seen red is not known to test anything.

## Post-mortem

Two sentences: what the cause was, and why it was not caught.

When the answer is "there was no seam where this could have been caught", the finding is architectural — hand off to `/improve-codebase-architecture` rather than filing it as fixed and moving on.
