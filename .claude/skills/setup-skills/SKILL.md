---
name: setup-skills
description: 為這個 repo 設定工程技能所需的組態 — 議題追蹤器、領域文件位置與 git 護欄 hook。初始化跑一次；重跑可換追蹤器或補裝、更新護欄。
disable-model-invocation: true
---

# Setup Skills

Write the per-repo configuration the other skills assume. Prompt-driven, not a script: explore, present, confirm, then write.

Produces:

- `docs/agents/issue-tracker.md` — where issues live
- `docs/agents/domain.md` — where `CONTEXT.md` and ADRs live, and the collaboration mode
- An `## Agent skills` section in `CLAUDE.md` pointing at both
- Copies of `guard-git.sh` and `guard-secrets.sh` in `.claude/hooks/`, registered in `.claude/settings.json`
- In private mode: entries in `.git/info/exclude`

## 1. Explore

Read what exists. Assume nothing.

- `git remote -v` — GitHub? GitLab? No remote?
- `CLAUDE.md` / `AGENTS.md` at root — does either exist? Does either already have an `## Agent skills` section?
- `CONTEXT.md`, `docs/adr/` — is a domain layer already here?
- `docs/agents/` — has this skill already run?
- `.scratch/` — sign of a local-markdown issue convention
- `.claude/settings.json` and `.claude/hooks/` — hooks already registered? Which events and matchers? Are the guard copies present, and do they still match their source (Section E)?
- Monorepo signals: `pnpm-workspace.yaml`, a `workspaces` field, populated `packages/*`

## 2. Present and ask

Summarise what is present and what is missing. Take the sections in order — one section, one answer, then the next. Lead each with the recommended answer so it can be accepted in a word. Skip a section outright when exploration already settled it.

**Section A — Issue tracker.** Where issues live for this repo. `to-tickets`, `to-spec`, and `triage` read from and write to it; they need to know whether to run `gh issue create`, write a file under `.scratch/`, or follow something you describe.

Propose from the remote: GitHub remote → GitHub Issues (`gh` CLI). GitLab remote → GitLab Issues (`glab` CLI). No remote → local markdown under `.scratch/<feature>/issues/`. Anything else → ask for one paragraph of description and record it as prose.

**Section B — Domain docs.** Default to **single-context**: one `CONTEXT.md` and one `docs/adr/` at the repo root. Write it without asking. Offer **multi-context** — a root `CONTEXT-MAP.md` pointing at per-package `CONTEXT.md` files — only when exploration found monorepo signals.

**Section C — Collaboration mode.** Ask: **does everyone committing to this repo use these skills?** Solo repos answer themselves — skip the question and record `shared`.

- **shared** (solo repo, or the whole team runs the skills): everything the skills write is committed. Current behaviour; nothing extra to set up.
- **private** (mixed-tooling team — teammates never opted into these skills): add `CONTEXT.md`, `docs/agents/`, `docs/decision-log.md`, `docs/architecture.md`, `docs/frontend-spec.md`, and `docs/mockup/` to **`.git/info/exclude`** — per-clone, never committed, invisible to teammates. Two things stay shared regardless: `docs/adr/` (decisions belong next to the code they constrain) and tracker issues (they live where the team already looks).

**Section D — Comment language.** What language code comments are written in. Skills that write or restyle comments (`refactor` among them) follow the project's *documented* conventions — this section does the documenting. Propose from what the existing comments already do; when the repo is silent, propose Traditional Chinese. The answer is **team truth**: comments ship with the code, so like `docs/adr/` it stays in the committed file in every mode — step 4 has the private-mode placement.

Record the reasoning in `domain.md` so future sessions apply it: a document only your tooling reads has no rot-detection loop. And a private file must not become a shadow copy of team truth — a fact teammates should read gets promoted into the committed `CLAUDE.md`/`AGENTS.md` or an ADR, never fixed by committing the private file.

**Section E — Guard hooks.** Two PreToolUse hooks on `Bash`, copied in from the luca-skills repo: `guard-git.sh` (blocks `git add -A`/`git add .`, force push, `git reset --hard` beyond HEAD, `--no-verify`, and PR merges — merging is the user's button) and `guard-secrets.sh` (blocks `git commit` while a credential literal sits in the staged diff). Prose rules hold roughly 70% compliance; these red lines ride on exit code 2 instead. Propose both, one nod per hook.

- **Source**: resolve the luca-skills repo from this skill folder's link target (`(Get-Item <skill-dir> -Force).Target` — the repo root is two levels up); the files are `<repo>/hooks/guard-git.sh` and `<repo>/hooks/guard-secrets.sh`. Unresolvable → ask where the repo lives.
- **Copy byte-for-byte into `.claude/hooks/`**, never reference the repo by path: a copy that ages still runs the old guard, while a pointer to a moved repo guards nothing and says nothing. Their tests stay in luca-skills — the copy is verbatim, so a green source is a green copy.
- **Drift**: copies present but differing from source → show the diff, propose refreshing.
- **Register** each under `PreToolUse`, matcher `Bash`, in `.claude/settings.json` as `bash .claude/hooks/<name>.sh`. Merge into whatever hooks structure exists — existing entries stay untouched.

## 3. Confirm

Show a draft of every file to be written and the block to be added to `CLAUDE.md`. Let it be edited before anything lands on disk.

## 4. Write

Pick the file to edit: `CLAUDE.md` if it exists, else `AGENTS.md`, else ask which to create. Never create one when the other already exists.

**In private mode, the `## Agent skills` block goes into `CLAUDE.local.md` instead** — a committed file must not point at paths teammates' clones don't have. One line still goes into the committed `CLAUDE.md`/`AGENTS.md`: the comment-language convention. It documents the code, not the tooling, so it belongs where the code's readers look.

If an `## Agent skills` block is already there, update it in place. Do not touch the surrounding sections.

```markdown
## Agent skills

### Issue tracker

[one line]. See `docs/agents/issue-tracker.md`.

### Domain docs

[one line — "single-context" or "multi-context", and "shared" or "private"]. See `docs/agents/domain.md`.

### Comment language

[one line — e.g. "程式註解一律使用繁體中文"].
```

`docs/agents/domain.md` must record the collaboration mode and, in private mode, which paths are excluded — downstream skills read it to know whether their output is committed or personal.

`docs/agents/issue-tracker.md` must record, concretely: the exact command to create an issue, the exact command to list open issues, how a blocking relationship is expressed, and where issue bodies live. Vague prose here makes every downstream skill guess.

## 5. Done

Say which skills now read these files, and that `docs/agents/*.md` can be hand-edited later — re-running this skill is for switching trackers or refreshing the guard-hook copies.
