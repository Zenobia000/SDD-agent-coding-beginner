#!/usr/bin/env bash
# PreToolUse hook (matcher: Bash). Blocks 'git commit' while a credential literal
# sits in the staged diff. Contract: exit 2 = block the tool call; stderr = why.
#
# Why a hook: /browser-evidence already forbids this in prose ("every credential is
# read from an out-of-repo file or the environment") and it was violated anyway —
# a live password reached a public branch, and force-push does not un-publish it.
# One violation is an incident, so the rule cannot stay probabilistic.

command -v jq >/dev/null 2>&1 || exit 0
cmd=$(jq -r '.tool_input.command // empty' 2>/dev/null)
[ -z "$cmd" ] && exit 0

# Only 'git commit' at command position — the moment content becomes permanent.
P='(^|&&|\|\||[;|]|\$\()[[:space:]]*'
printf '%s\n' "$cmd" | grep -qE "${P}git[[:space:]]+commit([[:space:]]|;|\)|$)" || exit 0

git rev-parse --git-dir >/dev/null 2>&1 || exit 0

# Added lines only. A literal already in history is someone else's finding;
# this gate owns what this commit introduces.
#
# This gate's own files are excluded: defining the rule means writing the
# shapes it catches, so scanning them blocks every edit to the gate itself.
# The exclusion is by path, not by an in-line marker — a marker the model can
# type is a gate the model can open. .claude/hooks/guard-secrets.sh is where
# setup-skills installs the copy in other projects; same file, same reason.
added=$(git diff --cached -U0 -- . \
          ':(exclude)hooks/guard-secrets.sh' \
          ':(exclude)hooks/test-guard-secrets.sh' \
          ':(exclude).claude/hooks/guard-secrets.sh' 2>/dev/null \
        | grep -E '^\+' | grep -vE '^\+\+\+')
[ -z "$added" ] && exit 0

# Two shapes, both requiring a quoted value with real content:
#   assignment  TEST_PW = "UatTest#2026"      (name unquoted, '=' )
#   json        "password": "UatTest#2026"    (name quoted, ':' — keeps prose out)
NAME='(PASS(WORD|WD)?|SECRET|TOKEN|API_?KEY|CREDENTIAL|[A-Za-z0-9]_PW)'
hits=$(printf '%s\n' "$added" \
  | grep -iE "[A-Za-z0-9_]*${NAME}[A-Za-z0-9_]*[[:space:]]*=[[:space:]]*[\"'][^\"']{4,}[\"']|\"[A-Za-z0-9_]*${NAME}[A-Za-z0-9_]*\"[[:space:]]*:[[:space:]]*\"[^\"]{4,}\"" \
  | grep -vE '\$\{|\{\{|<[A-Za-z_-]+>|os\.environ|getenv|process\.env|ENV\[|REDACTED|\*\*\*|xxxx|your[-_]|example\.com' \
  | head -5)

[ -z "$hits" ] && exit 0

{
  echo "Blocked: a credential literal is in the staged diff."
  printf '%s\n' "$hits" | sed 's/^/    /'
  echo ""
  echo "Read it from the environment or an out-of-repo file instead — os.environ[\"NAME\"], a gitignored .env, or a value generated per run. A literal on a pushed branch stays reachable even after a force-push rewrites the commit, so the fix afterwards is rotation, not deletion."
  echo "Already rotated, or this is a placeholder the pattern misread? Say so and the user unstages or overrides it — muting this gate is their call."
} >&2
exit 2
