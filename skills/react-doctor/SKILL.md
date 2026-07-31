---
name: react-doctor
description: Run and triage React project diagnostics without assuming a specific repository, package manager, or tool version. Use after React changes, before commit/PR, or when asked to inspect React correctness, accessibility, performance, security, or architecture regressions.
---

# React Doctor

Use the project's pinned diagnostic tooling when present; do not silently download or execute changing remote prompts.

## Workflow

1. Confirm the repository is a React project and locate its workspace/package manager, scripts, lockfile, React version, lint/type/test commands, and any existing React Doctor configuration.
2. Establish a fixed comparison base from the current branch's merge-base.
3. Prefer, in order:
   - a repository script that already runs React diagnostics;
   - a locally installed `react-doctor` binary;
   - a one-off package runner only after the user approves network execution.
4. Before using a non-pinned or unfamiliar CLI, run its current `--help` and construct the command from supported flags. Do not assume a cached command syntax is still valid.
5. Run changed-file/diff diagnostics first. Run a full scan only for baseline cleanup or when the user requests it.
6. Record the baseline output or score, group findings by rule and root cause, then separate:
   - regressions introduced by the current diff;
   - pre-existing findings;
   - false positives or rules needing configuration.
7. Fix only in-scope regressions unless the user requested cleanup. After each cluster, rerun the narrow scan; finish with the repository's typecheck, lint, tests, and build as applicable.

Report exact commands, before/after results, unresolved findings, and whether any network-fetched tool was used. Never commit or open a PR unless separately requested.
