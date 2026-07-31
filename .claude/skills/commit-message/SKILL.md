---
name: commit-message
description: Draft or validate a Git commit message from the staged diff and repository history. Use when preparing a commit, splitting mixed changes, checking Conventional Commit style, or explaining why a change belongs in one atomic commit.
---

# Commit Message

Describe the staged change truthfully. Do not use the conversation as the source of truth when the index says something different.

## Workflow

1. Read `git status --short`, `git diff --cached --stat`, and `git diff --cached`. If nothing is staged, stop or clearly label the result as a draft for unstaged changes.
2. Inspect recent commit subjects and any contributing guide to learn the repository's established language, capitalization, scopes, issue references, and body style.
3. Check atomicity. If the staged diff contains independent intents, recommend a split before drafting; one message must not hide multiple unrelated changes.
4. Use the repository's style. With no clear precedent, fall back to:

   ```text
   <type>(<optional-scope>)<!>: <imperative outcome>
   ```

5. Choose the type from intent: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `chore`, or `revert`.
6. Keep the subject specific, imperative, and normally at most 72 characters. Say what observable outcome changed; do not write “updates” or list filenames.
7. Add a body only when it preserves useful context: motivation, non-obvious trade-off, migration/compatibility impact, or why an obvious alternative was rejected. Do not narrate the diff.
8. Add issue references and `BREAKING CHANGE:` footers only when supported by evidence.

Return the proposed subject and optional body separately. Never stage files, commit, amend, or push unless the user explicitly requests that action.

## Examples

```text
fix(auth): reject expired refresh tokens

Keep refresh-token validation at the session seam so every caller receives
the same expiry behavior.
```

```text
refactor(skills): separate orchestration from engineering disciplines
```
