---
name: writing-hooks
description: 撰寫與審查 Claude Code hook 的判準 — 什麼規則該降到 hook、hook 該不該說話、怎麼防它靜默腐爛、跨平台怎麼寫。當要新增 hook、決定一條規則放 CLAUDE.md 還是 hook、hook「應該要擋」卻沒擋、對話被重複的機器訊息污染、或 hook 在別台機器上靜默失效時使用。
---

# Writing Hooks

Reference for hooks that stay alive. `/writing-for-agents` covers documents the model reads; this covers the machine enforcement around it. Evidence for every rule here — three rot modes observed in a real project, with numbers — lives in [PATHOLOGY.md](PATHOLOGY.md); read it when you need to justify a rule, not to apply one.

## Tier placement: what deserves a hook

CLAUDE.md rules are probabilistic — read, not guaranteed, and compliance decays as context grows. Place each rule by the cost of a violation:

| Rule kind | Belongs in | Why |
| --- | --- | --- |
| Taste, style, preference (naming, comment density) | CLAUDE.md / rules | A violation is ugly, not broken; machine enforcement costs more than it saves |
| Process order (test first, changelog before commit) | Docs + human review | Review catches it; exceptions are common, hard blocks would paralyze work |
| Irreversible or architecture-polluting actions (writing into a retired dir, bypassing the single entry point) | **Hook, exit 2** | Someone spends a day tracing it back; that rule cannot be probabilistic |
| Secrets, destructive commands, production operations | **Hook, exit 2** | One violation is an incident |

**The 10th-violation test**: if this rule is broken ten times, what does cleanup #10 cost? "Manual archaeology" → hook. "Fixed in passing during review" → keep it prose; every hook you add is one more thing that can rot.

## Silence discipline: where output goes

The three destinations look identical in shell and cost wildly differently:

| Destination | Cost | Use |
| --- | --- | --- |
| `>> logfile` | Zero — never enters the conversation | **Default.** Everything diagnostic |
| `>&2` (stderr) | Fed back to the model on a block | Only alongside `exit 2`, to say **what to do instead** — it is your one chance to correct the model, and a bare "not allowed" makes it invent something worse |
| stdout | Injected into conversation context on some events | Almost never |

A hook has two legitimate forms: a **decider** (can exit 2 — silent until it decides) and an **observer** (writes logs — silent always). A hook that always exits 0 and still talks is pure liability: it taxes every tool call to say nothing. Status broadcasts ("hook fired", "done") are worse than waste — they make dead functionality look alive.

`tee` is stdout in disguise: it writes the file **and** stdout by definition. Write logs with `>>`; this repo's check.sh rejects `tee` in hooks (invariant [8]).

## Staying alive: every hook ships with its test

The three rot modes ([PATHOLOGY.md](PATHOLOGY.md)) share one root cause: nothing verified the hook still worked. So the rule, enforced here by invariant [8]:

- Every `hooks/<name>.sh` has a `hooks/test-<name>.sh`, run by `scripts/check.sh` on every PR.
- The test feeds **real payloads** through the hook and asserts its **decisions** (allow/block), never just that it ran — running is the default, deciding is the function.
- The hook locates its repo relative to `$0`, so the test can copy it into a throwaway fixture repo and control every condition (dirty/clean, red/green) with no injection points in production code. `hooks/test-check-on-stop.sh` is the model.

A rule you cannot write a check for is a rule you should not encode as a hook — an unverified hook is worse than none, because it creates the illusion that someone is watching the door.

## Cross-platform: this repo runs on Git Bash

Windows Git Bash returns non-zero from many harmless operations (path conversion, missing `/proc`, `date` quirks). Three rules keep hooks alive there:

1. **Handle errors manually, line by line** — under `set -e` a hook dies mid-script with no error, no log, no trace, which is the hardest failure to diagnose. (Detecting platforms: env vars `WSL_DISTRO_NAME` / `MSYSTEM` before `uname`, which reports WSL as plain `Linux`.)
2. **Fail open, loudly**: the only non-zero exit is the deliberate `exit 2` block. A missing dependency (`jq`, a config file) logs "off duty today" and exits 0 — a broken guardrail must not stop the user's work, but it must leave a trace.
3. **Give fallbacks to everything**, even `date`: `$(date '+%F %T' 2>/dev/null || echo '????')`, and `>> "$LOG" 2>/dev/null || true`.

## Structure: the four-layer skeleton

Order guards from cheapest to most expensive, exiting 0 early: dependency present → tool name matches → path in jurisdiction → only then read content and judge. Full annotated skeleton, the Write/Edit field gotcha (`.content` vs `.new_string`), and observability patterns (`jq -nc`, truncation with original length) are in [PATHOLOGY.md](PATHOLOGY.md).
