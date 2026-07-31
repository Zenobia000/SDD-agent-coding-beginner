---
name: create-pull-request
description: Prepare and create a pull request from the current branch using the repository's actual template, default branch, commit history, diff, and verification evidence. Use when the user explicitly asks to open, create, or draft a PR.
---

# Create Pull Request

Treat PR creation as an external write. Run only after an explicit request.

## 1. Establish the comparison

1. Confirm the current branch is not the remote default branch.
2. Resolve the base from the user's instruction, repository config, or remote default branch; never hardcode `main`, `master`, or `preview`.
3. Check for an existing PR for the branch before creating another.
4. Inspect in parallel where supported:
   - `git status --short`
   - `git log <base>..HEAD --oneline`
   - `git diff <base>...HEAD --stat`
   - `git diff <base>...HEAD`
   - upstream tracking state
   - `.github/pull_request_template.md` or configured alternatives

Uncommitted changes are not part of the PR diff. Stop and explain when they materially change the description or required verification.

## 2. Draft from evidence

- Infer title style from repository PRs or commit history. Fall back to Conventional Commits.
- Keep the title concise and outcome-focused; include an issue ID only when one exists.
- Fill every applicable template section from the entire branch diff, not only the latest commit.
- Explain what changed, why, important design decisions, verification commands/results, risks, rollout, and screenshots when relevant.
- Do not claim a check ran unless its output was observed. Mark unrun checks explicitly.

Preview title, body, base, and head before the external write.

## 3. Push and create

If the branch has no upstream, push with `git push -u origin <branch>` after confirmation. Create the PR with the repository's hosting CLI, preferring a temporary `--body-file` over shell interpolation. Use draft mode when requested or when required checks are still intentionally incomplete.

Return the PR URL, base/head, and any remaining checks. Never merge the PR unless separately requested.
