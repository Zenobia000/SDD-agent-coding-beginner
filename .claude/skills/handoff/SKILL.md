---
name: handoff
description: 把當前對話壓縮成一份交接文件，讓全新的 session 能接手這份工作。
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

# Handoff

Write a document that lets a fresh agent continue this work without re-deriving it. Save it to the OS temporary directory — **not** the workspace. It is a bridge, not an artifact.

`/handoff` **forks**: you do not continue in place. Open a new session and reference the file. `/compact` is the one that continues in place.

`/handoff` is narrow — what it buys is **portability**, a file that travels. Reach for it only when something is travelling: a **new harness** (Claude → Codex), a **new directory** or repo, a **colleague** taking over, or a side task forked **mid-phase** without derailing the current work. If nothing is travelling, one of the other boundary moves (continue, `/clear`, a subagent, `/compact`) is cheaper.

## What goes in

- **Where the work stands** — what is done, what is in flight, what has not been started
- **Decisions already made, and why** — this is the part that is expensive to re-derive and impossible to recover from a diff
- **What to do next**, concretely enough to act on
- **Known traps** — the thing that looked right and was not
- **Suggested skills** — which skills the next session should invoke, in order

## What stays out

**Anything already captured elsewhere.** Specs, ADRs, issues, commits, diffs, `CONTEXT.md` — reference them by path or URL. Duplicating them into the handoff creates a second copy that goes stale immediately and gets believed over the real one.

**Secrets.** Redact API keys, tokens, passwords, and personal data before writing.

**Narrative.** Nobody needs the conversation replayed. The next agent needs state and direction.

## Arguments

If the user passed arguments, treat them as the next session's focus and tailor the document to it — a handoff into a `/prototype` session needs the design question and the constraints, not the whole build plan.

## Finish

Print the absolute path, and the one line to paste into the new session.
