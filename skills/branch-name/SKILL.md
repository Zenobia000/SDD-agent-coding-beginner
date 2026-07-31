---
name: branch-name
description: Create or rename a Git branch using the repository's established naming convention, with a safe conventional fallback. Use when starting isolated work, naming a feature/fix branch, or preparing a branch for a pull request or worktree.
---

# Branch Name

Derive the name from the work, not from an organization-specific tracker.

## Workflow

1. Inspect `git status`, the current branch, the remote default branch, and recent branch names if available.
2. Preserve a documented repository convention. If none exists, use:

   ```text
   <type>/<optional-issue-id>-<short-outcome>
   ```

3. Choose `feat`, `fix`, `refactor`, `docs`, `test`, `perf`, `build`, `ci`, or `chore` based on the user-visible intent.
4. Include an issue identifier only when the user or repository provides one. Never invent it.
5. Write a 2–6 word lowercase kebab-case outcome. Describe what changes, not the implementation technique.
6. Check that the branch does not already exist locally or remotely.
7. Create it only when the user asked to create/rename a branch; otherwise return the proposed name.

Prefer `git switch -c <name> <base>` for creation. Do not switch away from uncommitted work until confirming that the changes belong on the new branch.

## Examples

```text
feat/add-export-filters
fix/gh-248-retry-timeouts
refactor/simplify-auth-boundary
docs/document-local-setup
```
