---
name: tdd
description: 測試驅動開發，紅—綠—重構。當要以測試先行的方式建置功能或修 bug、當使用者提到 "TDD"、"red-green"、「紅綠」，或要求寫出能撐過重構的測試時使用。
---

# Test-Driven Development

Red → green → repeat, one behaviour at a time.

## The loop

1. **Red** — write one failing test for the next behaviour. Run it. See it fail, and see it fail *for the reason you expect*. A test that passes before the code exists is testing nothing.
2. **Green** — the least code that passes it. Ugly is allowed here.
3. **Refactor** — clean up with the test holding the behaviour still. Optional; skip it when there is nothing to clean.

Never write all the tests up front. Batching them produces tests of *imagined* behaviour: they pin the shape you guessed at, and go numb to the shape you actually built. Each cycle should be informed by what the previous one taught you.

The first cycle is a **tracer bullet** — one test proving a single path works end to end, before building outward.

## What a good test is

**Tested through the public interface.** Code should be able to change entirely without the tests moving. A test that breaks on a rename is a test of implementation.

**Named as a specification.** `user can check out with a valid cart` — reading the test names should tell you what the system does.

**Expected values from an independent source.** A known-good literal, a worked example, the spec. Never recomputed the way the code computes it — that test passes by construction and is **tautological**: it will pass just as happily when the code is wrong.

**One behaviour per test.** A test asserting five things fails without telling you which one broke.

## Seams

A **seam** is the boundary where behaviour is observable without reaching inside. Tests live at seams.

Pick the seam before the first test. Too deep and every refactor breaks the suite; too shallow and failures stop being diagnostic. The right seam is usually the interface another part of the system already calls.

The loop does not change at a module boundary. A test at the seam between two modules — real collaborators on both sides — is an integration test, written red-first like any other; the layer is a property of where the seam sits, not a different ritual.

Which seams deserve tests is a project decision, not a per-test guess. Take the list from the project's `docs/test-blueprint.md` when one exists — it names the seams and the promise each serves. Otherwise the boundary `/implement` declared; failing both, the heuristic above.

## Mocking

Default to **not** mocking. A test with four mocks is testing the mocks.

Mock only what you do not own and cannot make fast or deterministic: third-party network calls, the clock, randomness, the filesystem when it is genuinely slow. Your own modules are not on that list — if they are hard to use in a test, that is a design finding, not a mocking problem.

In-memory fakes beat mocks. A fake repository backed by a map exercises real logic; a mocked one asserts you called a method.

## Anti-patterns

- **Testing internals** — private functions, internal state. Rename-fragile, refactor-hostile.
- **Tautological tests** — expected value computed by the code under test.
- **Assertion-free tests** — "it runs without throwing" is not a specification.
- **Shared mutable fixtures** — order-dependent suites that pass alone and fail together.
- **Coverage as the goal** — coverage measures which lines ran, not which behaviours are pinned.

## Bugs

A bug fix starts with a test that reproduces it and goes red. Fix, watch it go green, keep the test. A fix without that test is a fix that comes back.
