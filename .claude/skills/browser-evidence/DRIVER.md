# Driver recipe

The Playwright mechanics behind [`browser-evidence`](SKILL.md): what each helper is for, and the pitfalls that have already produced a wrong answer. The helpers themselves live in [`drv.py`](drv.py) — copied to the project's `tests/e2e/lib/drv.py` on first run, imported by the per-run case script thereafter. This file explains; that file executes. Change behaviour there, not by restating code here.

## Run key first

```python
drv.RUN = "alex-2026-08-10-4b17006"   # <operator>-<date>-<short SHA> — mirrors the branch name
```

First line of every case script, from the build being captured. Every path the helpers write hangs off it, and `run_dir` refuses to write while it is unset — a path built from the case ID alone would land in whatever run came before, silently, corrupting an exhibit already committed.

## What each helper is (and why it is shaped that way)

- **`launch`** — headed, slowed, fixed window position. Every flag serves the human: the operator watches it run, eyes can follow, successive runs land on the same spot. Mobile layouts get a phone viewport instead (`480×950`) — the exhibit has to show what the user's device shows.
- **`banner`** — the burnt-in caption naming case and step, so the reviewer needs no separate key. `z-index` at the 32-bit ceiling sits above any modal; the fixed element id makes a second call replace the text instead of stacking bars; black-on-green monospace reads as obviously *not* the application under test. Call it before each step, let the page settle, then shoot.
- **`watch`** — network, console and dialogs on one page. Network records state-changing writes only: static assets and polling would bury the three lines that matter, and a `403`/`200` divergence across roles is how an authorization bypass surfaces. Widen to `GET` when the case is about data exposure in a response body. Console keeps errors and warnings — a JS error can leave the frame looking perfectly normal. Both are unrecoverable after the fact; a rerun may not reproduce the state. Dialogs auto-accept, because a native `confirm()` blocks the run until something answers it.
- **`step_shot`** — numbered screenshots, counter per case. One image can serve several cases (the same screen is step 1 of one and the precondition of another), so each sequence stays aligned with its own step numbers. `full_page=True` is a choice: it catches what scrolled out of view, and on a long list page it costs megabytes — use the viewport when the proof is on screen.
- **`fact` / `heal`** — the machine-facts channel. `heal` records a selector repair and writes its 機器事實 line in one move; the fence (location only, never action or assertion) is in [SKILL.md](SKILL.md) step 3.
- **`evidence`** — the non-browser step's `step_shot`: writes a numbered `NN-slug.json` (dict/list payload) or `.txt` (anything else) through the same per-case counter, so a case mixing browser and api steps keeps one unbroken sequence. Pass the raw request-plus-response, not a summary — the file is the exhibit.
- **`manual`** — hands one step to the operator: banner shows the instruction, `input()` blocks until Enter, then a 機器事實 line and a 人工接手 row record it. The operator acts in the same headed browser, so the shot and the network log around the step survive intact.
- **`flush_case`** — writes `network.json`, `console.json`, `manifest.json` (with the case's `channel`) and the report skeleton: fields as given (missing ones as 「未提供」), one heading per step with its shots and `evidence` payloads embedded (fenced block, excerpted past 1500 chars, raw file linked), the recorded 機器事實 lines — and the agent's half left blank: an **觀察** and a **對照** line per step, one header **測試結果** line. A report exists for every captured case by construction, not by memory. The skeleton landing on disk is also the hand-off: from that moment those blank lines belong to the agent, while the script drives on.
- **`flush_run`** — the run index: operator, covered-of-listed, the 未填 count, a link per case report tagged with its channel, the skip list, the 人工接手 table, and the heal table.
- **`verify_run`** — the staging gate's number: recounts blank 觀察／對照／測試結果 lines across the run's case reports, rewrites the count line and each case link's 測試結果 tag in the run index, and prints the count. Re-runnable, so the index stays honest after the report pass; only 0 clears staging.

> **Pitfall — the banner is page text.** Searching the DOM for a phrase can match the caption instead of the application, which once turned a passing case into a reported defect. Query the HTML for field names (`cost`, `unit_price`) rather than rendered words.

> **Pitfall — the screenshot counter is module state.** It resets with the process, so splitting one case across two scripts restarts its numbering at `01`. Keep a case inside one script.

## Login — real form, session reused

Fill the real login form once, then persist and replay:

```python
ctx.storage_state(path="brand_state.json")   # later runs: browser.new_context(storage_state=...)
```

Prefer stable ids (`#login-email`). Where the app gives none, index visible inputs positionally — and expect that to break when the form changes, because it will.

## API without UI

Forged signatures, internal tokens, cross-origin endpoints — and whole cases with no UI at all:

```python
api = p.request.new_context()
r = api.post(f"{BASE}/api/sop/adopt", data={...})
drv.evidence(["TC-API-01"], "adopt-403", {"req": {...}, "status": r.status, "body": r.json()})
```

`APIRequestContext` is outside the browser's CORS rules, so it reaches endpoints the page cannot. An api-channel case follows the same discipline as a browser one — numbered evidence per step via `evidence`, `flush_case(..., channel="api")` — it just has no shots. A CLI-channel case does the same with `subprocess` output and `channel="cli"`.
