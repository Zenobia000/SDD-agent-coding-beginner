#!/usr/bin/env bash
# Stop hook: while the invariant surface has uncommitted changes, check.sh must be
# green before the agent may finish. Contract: exit 2 = keep working; stderr = why.

input=$(cat)

# Loop protection: if a previous Stop-hook block is already being handled, let go.
printf '%s' "$input" | jq -e '.stop_hook_active == true' >/dev/null 2>&1 && exit 0

cd "$(dirname "$0")/.." || exit 0

# Only act when the files the invariants govern have changed.
git status --porcelain -- skills .claude-plugin README.md package.json 2>/dev/null | grep -q . || exit 0

if ! out=$(bash scripts/check.sh 2>&1); then
  {
    echo "scripts/check.sh is red with uncommitted skill changes. Fix the violations before finishing:"
    printf '%s\n' "$out" | tail -30
  } >&2
  exit 2
fi

exit 0
