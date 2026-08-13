---
name: code-review
description: 沿兩條軸審查自某個定點以來的 diff — Standards（有沒有遵守這個 repo 的規範？）與 Spec（有沒有做到票要求的事？）。當使用者要審查一個分支、一個 PR 或進行中的工作時使用，也對應 "code review"、"review this branch"、「審一下」等說法。
---

# Code Review

Two-axis review of the diff between `HEAD` and a fixed point.

- **Standards** — does the code conform to this repo's conventions?
- **Spec** — does it faithfully implement the originating ticket or spec?

Run both as **parallel sub-agents** so neither pollutes the other's context, then report side by side. Sub-agents must not invoke `/code-review` themselves — one level of review, no recursion.

## 1. Pin the fixed point

Whatever the user gave: a SHA, a branch, a tag, `main`, `HEAD~5`. If they gave nothing, ask. Reviewing against a merge-base you assumed is reviewing a different diff than they meant.

`git diff <point>...HEAD` — the diff, not the file tree.

## 2. Standards axis

The repo's own documented standards win over everything below. Read `CLAUDE.md` / `AGENTS.md`, any `docs/` conventions, and — more reliable than either — the surrounding code.

Baseline smells, always checked, always reported as **judgement calls, never violations**:

- **Mysterious name** — the name does not say what it does
- **Duplicated code** — same logic in three places, about to drift
- **Feature envy** — a function more interested in another object's data than its own
- **Data clumps** — the same three parameters travelling everywhere together
- **Primitive obsession** — a domain concept carried as a bare string
- **Repeated switches** — the same branch on the same type, scattered
- **Shotgun surgery** — one change forcing edits across many files
- **Divergent change** — one file edited for unrelated reasons
- **Speculative generality** — abstraction for a case that does not exist
- **Message chains** — `a.b().c().d()`
- **Middle man** — a class that only delegates
- **Refused bequest** — a subclass that ignores most of what it inherits

A documented repo standard overrides any of these. Consistency beats a rule from a book.

## 3. Spec axis

Read the originating ticket or spec. Check the diff against it:

- Every *Done when* condition, literally — met, or not
- **Scope creep** — shipped things the spec did not ask for
- **Silent gaps** — spec items with no code
- **Reinterpretation** — built something adjacent to what was asked

## 4. Report

Side by side, most severe first. Each finding: file and line, one sentence on the defect, and the concrete failure — inputs or state, and what breaks.

Separate **must fix** from **judgement call**. A review where everything is urgent gets ignored wholesale.

Say plainly when an axis found nothing. Manufactured findings to look thorough cost more than they are worth.
