---
name: browser-evidence
description: 把既定案例清單跑成可交付的證據 — 截圖或原始回應、網路紀錄與被測版本 manifest。瀏覽器是預設通道，無 UI 案例走 api/cli，卡人一步由操作者接手；落在 docs/uat/，走 evidence 分支 PR 合回基底分支。
disable-model-invocation: true
---

# Browser Evidence

Drive a real browser through a given list of cases and leave behind an **exhibit**: numbered screenshots, a network log, and a record of what version was under test. The exhibit outlives the session and crosses to another person — an acceptance reviewer, a client, whoever fixes what it shows.

That is the line against `/run`. `/run` is *let me see it work*: a screenshot, glanced at, discarded. This is *let me prove it worked* — captured for someone who was not watching.

## Scope

Capture only. The case list arrives from outside — by default from `/uat-cases`, whose ledger holds the other half of the ID discipline; a list from any other source is equally welcome as long as it meets the contract below. The verdict is a human's.

So: record a `403`, and state in the 對照 line (step 4) how it compares to the written 期望結果 — both ends of that comparison are on paper, so the reader can check it. Whether the case passes acceptance stays the reader's call; every temptation to go further than the comparison is the skill exceeding itself.

**The exhibit, not the browser, is the identity.** The browser is the usual capture channel, never the boundary. A case with no UI at all — an API contract, a CLI job, a database state — runs through the `api`/`cli` channel under the same numbering, manifest and report discipline (the `evidence` helper in [`DRIVER.md`](DRIVER.md)). A case automatable except for one human step — an OTP, a CAPTCHA, an external mailbox — runs with that step handed to the operator (step 3). Only a case whose environment is genuinely out of reach — a physical device, a system with no automatable surface — is skipped, and every skip is reported, never silent.

## 0. Check the contract

Each case needs exactly two things:

- a **stable ID** (`TC-ONSITE-01`) — it becomes the evidence directory name
- an **ordered step list** — the order becomes the screenshot filename prefix

Either one missing leaves the evidence unnameable — stop and ask for it before launching anything.

The other fields a case may carry — 狀態, 負責人, 來源, 角色, 前置條件, 期望結果 — are welcome and **flow into the case report** verbatim. A field the list didn't provide is printed as 「未提供」, never silently dropped: a visible gap gets filled, an invisible one doesn't. Priorities stay ignored — a UAT list is run whole.

**Classify the channel while checking the contract.** For each case, decide from its steps which channel runs it — browser, `api`/`cli`, or unreachable. A case carrying an explicit 執行方式 field is respected; the field is optional, never demanded of the list. Say the classification out loud, then launch: all cases browser or api need no further gate — the operator is watching a headed browser and can stop it live. Any case headed for a skip, or one you cannot classify with confidence, stops the run for the user's ruling first — the gate sits only where there is something to rule on.

**IDs are frozen once issued** — a case whose content changed keeps its number, and a retired number is never reissued. Holding that line is the list generator's half of the discipline. This skill's half is the reconciliation in step 1, which only tells the truth while the numbers hold still.

## 1. Open the evidence branch

Evidence lives in `docs/uat/` and travels on an **ordinary branch**. Cut `evidence/<operator>-<YYYY-MM-DD>-<short-SHA>` from the **base branch** — the branch checked out right now, or the one the user names; the base is theirs to pick, never assumed to be `main`. The run ends as a PR back into that same base, so the exhibit lands where the next person is already working instead of on a side branch they never visit.

The branch key is also the run directory key, one to one: `docs/uat/<operator>-<YYYY-MM-DD>-<short-SHA>/<TC-ID>/NN-slug.png`（a non-browser step writes `NN-slug.json`/`.txt` through the same counter）, with `REPORT.md`, `manifest.json`, `network.json` and `console.json` beside the shots, and the case script plus the run index `REPORT.md` at the root of the run directory. The date reads for the human, the SHA pins the build, and the operator keeps two testers of the same build on the same day apart — two testers is two runs, two directories, by design.

**A run directory is never overwritten.** Each one is a complete exhibit of one build, so pinning a release means keeping its directory — not checking out an old commit to reconstruct what was captured. Within a run, re-capturing a case does overwrite that case's directory; across runs, nothing is ever touched again.

Storage therefore grows monotonically, by design. Retention — including when to move the directory onto Git LFS — is a policy decision and belongs in the project's `docs/test-blueprint.md` alongside the other scheduling policy, not a rule this skill invents.

**Reconcile before capturing.** Compare this run's ID list against the **most recent previous run directory** under `docs/uat/`, never against every directory — the whole history would come back as orphans. Report every ID that run captured and this list no longer claims: those are cases retired or renumbered upstream. Report them; deleting is the user's call.

**Migration note.** A project carrying the old orphan `evidence` branch keeps it as a read-only archive — cite old runs by branch name plus path. New runs all take this model; nothing is copied across.

## 2. Generate the driver

Read [`DRIVER.md`](DRIVER.md) before writing the first line — mandatory. It carries the launch flags, the banner, the numbering, and two pitfalls that have already cost a false defect report.

Python + Playwright, every time. The script sits outside the project's dependency tree, so a Node project keeps its `package.json` clean — and one fixed runtime keeps exhibits looking the same across projects, where a per-project choice lets the format drift.

The driver splits into two halves with different lifetimes. The **helpers** ship with this skill as [`drv.py`](drv.py): on a project's first run, copy it to `tests/e2e/lib/drv.py`; every later run imports the project's copy, so every tester on the project shares one set of helpers instead of regenerating them. The per-run **case script** imports those helpers, is generated fresh every time, and is committed with the evidence, because *reproducible* is part of *credible* — the reader can rerun it rather than take the pictures on faith. Two rules keep the split honest:

- **The case script is a snapshot; the helpers are a library.** Selectors and steps belong to the snapshot — they differ per sprint and are part of the exhibit. Launch flags, banner, numbering and collectors are identical every run and live in `tests/e2e/lib/`, maintained through normal code PRs; page objects that emerge from repeated flows sediment into the same place, via the code PR in step 6.
- **Every credential is read from an out-of-repo file** (`uat-creds.env`) **or the environment.** The file stays out of git. A literal in the script is permanent on a remote branch, and it is also printed into this conversation the moment it is generated. Open the script with a comment naming the keys it expects — otherwise whoever reruns it stalls on the first line.

## 3. Capture

Headed, slowed, and narrated: the operator watches it happen, and the narration is burned into the screenshots so the reviewer needs no separate key.

**Redact before capture, not after.** Before each shot, ask whether the frame holds real people — names, phones, addresses, prices. If it does, rerun that step against test data, or mask before shooting. This branch gets pushed, and a push is permanent.

**A red case does not stop the run.** Capture the failure as carefully as a pass — shots, network, console — then move to the next case. The list is run whole; stopping at the first failure delivers one defect and hides the rest.

**A human step does not break the chain.** When one step defeats automation — an OTP, a CAPTCHA, a mail to fetch from an external inbox — call `manual()`: the banner shows the instruction, the run waits for Enter, the operator performs the step in the same headed browser, the run resumes. The shot is still taken and the network still recorded; what changes is a 機器事實 line naming the step as operator-performed, and a row in the run index's 人工接手 table. A non-browser step captures with `evidence()` instead of a shot — same counter, so a case can mix channels without its numbering forking.

**Capture and the 觀察 pass run in parallel.** A case's skeleton `REPORT.md` landing on disk is the hand-off signal: from that moment its 觀察 and 對照 lines and its 測試結果 belong to the agent (step 4), while the script drives the next case. A run containing `manual()` steps is executed by the operator in their own terminal — `input()` needs an interactive stdin, and a background process's answers EOF — with the agent filling alongside; a run without them the agent launches in the background itself. Re-capturing a case overwrites its directory and takes the hand-off back; refill after. If parallel filling fails, filling after the run ends is legal: the gate sits at staging, not at the clock.

**Self-healing is fenced to location.** When a selector no longer finds its element, repair the locator and continue the run — a heal may change **how a step locates**, never **what it does or asserts**. A "heal" that lands on a different control turns the exhibit green while photographing the wrong thing; when the right element is genuinely gone, that is a red step to capture, not a locator to widen. Every heal leaves three traces: the healed case script committed with the run, a 機器事實 line on that step（`selector 由 X 改為 Y`）, and the heal table in the run index. No per-heal approval — the traces are the accountability.

Done when every ID on the list has a directory, every step of every case has a numbered artifact — a shot on a browser step, an `evidence` payload otherwise — and every case's report has its 觀察 and 對照 lines and its 測試結果 filled. A run that covered five of eight cases is reported as five of eight.

## 4. The report — capture made readable

A pile of PNGs and JSON is raw material; the reader was promised an exhibit. Two files per run:

- `<RUN>/<TC-ID>/REPORT.md` — one per case, the document a reviewer actually reads. The driver writes the skeleton (see [DRIVER.md](DRIVER.md)), so a report *exists* for every captured case by construction; the agent fills the 觀察 and 對照 lines and the header 測試結果 **as each skeleton lands** (the hand-off in step 3). All are written from reading the case's shots and `evidence` payloads, never from memory of the run — the exhibit is on disk, and memory is where "should" and "probably" creep in.
- `<RUN>/REPORT.md` — the run index: operator, which cases ran (five of eight is five of eight), the 未填 count（觀察、對照與測試結果）, a link per case report tagged with its channel and — once filled — its 測試結果, every skip, every redaction, orphan directories, the 人工接手 table — every operator-performed step — and the heal table — every selector repaired this run, old and new. **It lists, it never restates** — a copy of case content is a second document waiting to diverge.

The reader never leaves the `.md`. A browser step embeds its shot; a non-browser step embeds its captured payload as a fenced block the same way — excerpted when long, with the raw `NN-slug.json`/`.txt` always linked beside it.

In the case report, steps expand one by one, each step's screenshot embedded under it, followed by three lines:

- **機器事實** — what the capture files recorded: status codes, console errors, final URL.
- **觀察** — the literal words of the frame. The line between observation and verdict: **a sentence that still reads without the 期望結果 is an observation; one that only means something against it is a verdict.** 「覆核率統計顯示 100%」 stands on its own — write it. 「覆核率符合要求」 doesn't — verdicts live in `docs/uat-cases.md`'s 最近判定, registered by the human who read this report.

- **對照** — this step's 觀察 set against **the clause of the 期望結果 it bears on**, quoted — `符合`／`不符合`／`部分符合`／`無法對照`, with the exhibit and the quoted clause as grounds. A step the 期望結果 never speaks to writes 「無法對照 — 期望結果未涉及此步」; an expectation the run's evidence cannot observe writes 無法對照 plus one line naming what is missing — that value's job is to accuse the upstream field or the step list, never to shade into 符合. **A 對照 is a comparison statement, not a verdict**: it quotes both ends so the reader can check it, and what it may never say is whether the case passes acceptance.

One line in the header, directly below 期望結果:

- **測試結果** — the roll-up of the steps' 對照 values, by a fixed rule: comparable steps all 符合 → `符合`; all 不符合 → `不符合`; mixed → `部分符合`; nothing comparable → `無法對照`. One word, no grounds — the reader gets the outcome before the first screenshot, and the grounds stay in the steps.

Every sentence names its exhibit (`03-escalation.png`, `network.json`); "should", "probably" and "seems" have no place here — a statement without an exhibit behind it is an opinion, and opinions are the reviewer's department.

```markdown
## TC-COMPLIANCE-05 — SOP 未經 family review 不得 adopt
- **狀態**：active ／ **負責人**：未提供 ／ **角色**：知識審核者
- **來源**：Excel ch11／FR-REF-03、NFR-Aud-004
- **前置條件**：一份未經 family review 的 SOP draft
- **期望結果**：adopt 必須失敗；覆核率 100%
- **測試結果**：符合

### 步驟 1 — 直接對該 draft 執行 adopt
![](01-adopt.png)
- **機器事實**：`POST /api/sop/adopt → 403`（network.json）
- **觀察**：畫面顯示紅字「需完成 family review」，adopt 按鈕呈灰階（01-adopt.png）
- **對照**：符合 — `403` 與紅字（network.json、01-adopt.png）對期望結果「adopt 必須失敗」
```

## 5. Record the chain of custody

One `manifest.json` per case directory — per case, so that rerunning a single case leaves the others' records honest:

```json
{ "tc": "TC-ONSITE-01", "commit": "<SHA under test>", "env": "<base URL>",
  "ran_at": "<ISO 8601>", "channel": "<chromium｜api｜cli>", "operator": "<who drove>" }
```

`operator` is who drove the browser this run — an attribute of the execution. Who *owns* the case (負責人) is an attribute of the case and lives upstream in `docs/uat-cases.md`. Often the same person; by coincidence, never by design.

The `commit` is the whole point: the evidence branch's own commits say when the exhibit was made, never which build it tested — only the manifest does. It also makes *is this exhibit stale?* a question a machine can answer.

## 6. Hand off

Before staging, rerun `drv.verify_run()`: it recounts the blank 觀察／對照／測試結果 lines, rewrites the count and each case link's 測試結果 tag in the run index, and prints the count — **staging is legal only when it prints 0**. A nonzero count is unfinished work, not a footnote. Then stage the files this run produced — the run directory (the case script already lives inside it), by path, on the `evidence/…` branch. Then stop: **committing is the user's move** via `/git-commit`, and so are opening the PR back into the base branch and merging it. The PR is the last gate where a frame that should have been redacted can still be caught — merge is what makes the exhibit part of the base branch's history, and the user may also leave it unmerged; the branch stands as the exhibit either way.

Selector heals that belong in `tests/e2e/lib/` go to the base branch as a **separate code PR** — an evidence PR can sit unmerged or be declined, and the lib repair must not be hostage to that verdict. Cite the run key in that PR's body; the proof of why each selector changed is in the run's reports.

In the conversation, say **where to read and what went wrong**: the run directory path, five of eight if it was five of eight, every skip, every redaction, every heal, orphan directories — and nothing more. The content lives in the reports now; restating it here is a copy that evaporates with the session. Skips and redactions are said out loud *here*, not just in the index, because this pause is the last gate before an irreversible push.

## Where this sits

Downstream of `/implement` and `/code-review`: the manifest pins a commit, so there has to be a built, reviewed version to pin.

When a run happens — pre-release, periodic — is scheduling policy and lives in the project's `docs/test-blueprint.md` when one exists. This skill captures; it does not schedule.
