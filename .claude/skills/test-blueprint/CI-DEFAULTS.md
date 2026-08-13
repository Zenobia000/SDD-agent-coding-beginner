# CI defaults

Starting positions for step 2's tier layout, distilled from how seven high-star projects run CI (Kubernetes, Rust, Chromium, Node.js, PostgreSQL, LLVM, React). Every one is overridable per project — the proposal states the override and its reason.

## Tiers

Placement is a cost × risk decision; no surveyed project runs everything per PR.

- **presubmit** — every PR: full static layer, unit tests, integration tests affected by the change. Budget is real: Chromium requires CQ builders to keep a sub-40-minute median before admission.
- **merge** — before merge, against the latest base: the full suite. A merge queue (bors/Tide style) when volume justifies one; below that volume, branch protection on the same checks.
- **periodic** — on a schedule: expensive E2E, cross-platform matrices, ecosystem regression sweeps.

## Gates

Static checks and unit tests are hard required checks. Keep the required set small — every added check taxes throughput and adds a false-block risk; everything else runs advisory.

**The unimplemented gate is graded: new promises block, existing ones report.** A promise with no test claiming it is the failure CI cannot otherwise see — it never goes red, because nothing runs. Gating all of them on day one blocks every existing project immediately, and a gate that blocks everything gets switched off and never switched back on. Gating only new ones freezes the debt where it stands without hunting the backlog, and keeps the required set small the way the paragraph above demands. The boundary is an explicit exemption list in the blueprint, shrinking only — a debt line that can grow is not a boundary.

## Flake policy

Default: **no auto-retry** — a red is investigated, not re-rolled. This is the Kubernetes position, and it is the right one while the suite is small: it forces flakes to be fixed while they are still cheap. Past roughly a thousand tests, revisit — at that scale Chromium and Node institutionalize retry plus a quarantine list. The split holds either way: executing the quarantine list is a script's job; adding to or removing from it is a judgment.

## Coverage

Traceability coverage — every promise has a test, the blueprint's traceability table — is the definition of done. Line coverage is a dashboard, never a merge gate: all seven surveyed projects refuse coverage-number gates, because a high line count with no assertions passes it.

## Evidence

Every failure leaves an investigable trail: logs and traces uploaded, artifacts kept. The looser the retry policy, the heavier the evidence must be — retries hide signal, and evidence is what buys it back.
