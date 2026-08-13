---
name: domain-modeling
description: 建立並磨利一個專案的領域語言 — 挑戰模糊術語、拆開超載的詞、把難以回頭的決策寫成 ADR。當問題出在命名、當同一個詞在不同地方意思不同、或當一個決策需要白紙黑字的紀錄時使用。
---

# Domain Modeling

The active discipline of keeping the project's words precise. Merely *reading* `CONTEXT.md` for vocabulary is not this skill — that is a one-line lookup. This skill is for when the words themselves need work.

## The three artifacts

**`CONTEXT.md`** — the glossary, **and nothing else**. No implementation details, decisions, or todos — anything else here gets read as current reality by every downstream agent. One entry per domain term:

```markdown
**Session**:
A single authenticated period for one user, bounded by login and expiry. Holds no
request state.
_Avoid_: connection, login (a login is the event that starts a Session)
```

The `_Avoid_` line is the load-bearing part. A glossary that only says what a word means does not stop the wrong word being used.

**`docs/adr/NNNN-<slug>.md`** — one decision per file. **A decision earns an ADR only when all three are true:**

1. **Hard to reverse** — undoing it means touching code not yet written.
2. **Surprising without context** — a future reader would ask "why on earth is it done this way?"
3. **A real trade-off** — an alternative was genuinely considered and rejected.

Any of the three missing → no ADR file. An ADR per preference is noise that buries the three that matter.

Title states the decision, not the topic: `0007-sessions-expire-after-30-days`, never `0007-session-handling`. Body covers what was decided, what was rejected, and why. One status line at the top: `Status: Proposed` until the change implementing it flips it to `Accepted` — unbuilt work must not read as settled. No template ceremony beyond that.

**`docs/decision-log.md`** — one line per decision that fails the gate but deserves a trace: date, decision, one clause of why. Single file, append-only, no template. Deliberately not in `CONTEXT.md`: the glossary is in-force truth; the log is history.

## Sharpening a term

**Test for overload.** Grep the term across the codebase and docs. If it names three different things, it is doing three jobs — split it. "Account" that means the billing entity, the login identity, and the org is three terms wearing one word.

**Test for emptiness.** Ask what the term *excludes*. A term that excludes nothing is decoration. "Manager", "handler", "service", "data" usually fail this.

**Stress with scenarios.** Push edge cases at the definition until it breaks: what happens on a refund? A partial one? Two at once? The definition that survives is the one to write down.

**Prefer the word the users already say.** Inventing vocabulary buys precision at the cost of every future conversation.

## Rules

- Update `CONTEXT.md` **inline, during the work** — not in a cleanup pass afterwards. A glossary written at the end is a glossary written from memory.
- One ADR per decision. Never batch.
- Create files lazily. A session that settles nothing durable writes nothing.
- Renaming a term means renaming it in the code too, in the same change. A glossary the code disagrees with is worse than no glossary.
- Record flagged ambiguities you could not resolve at the bottom of `CONTEXT.md`, with what would settle them. An open question written down beats a false definition.
