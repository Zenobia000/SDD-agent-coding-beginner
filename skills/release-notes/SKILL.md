---
name: release-notes
description: Generate repository-agnostic release notes from a tag range, branch comparison, milestone, or release PR. Use when drafting changelogs or publishing release notes while filtering mechanical commits and preserving only user-relevant changes.
---

# Release Notes

Draft from primary repository evidence. Publish only when explicitly requested.

## 1. Resolve the range

Determine the target version and comparison range from the user's reference, tags, release branch, PR, or repository convention. Never assume semantic versioning, date versioning, branch names, or hosting provider.

Capture:

- commits and merge commits in the range;
- linked PRs/issues when available;
- the prior release's format and tone;
- migration, security, deprecation, and breaking-change evidence;
- contributor names if the repository includes acknowledgements.

## 2. Filter and classify

Exclude merge noise, conflict-resolution commits, sync-only commits, release bookkeeping, reverts immediately reapplied, and internal churn with no observable impact.

Use the repository's categories. With no precedent, use only non-empty sections from:

- Highlights
- Features
- Improvements
- Bug fixes
- Security
- Breaking changes
- Deprecations
- Upgrade notes

Conventional Commit types are signals, not truth. Read the diff/PR when a subject is ambiguous. A `refactor` can be user-visible; a `feat` can be internal infrastructure.

## 3. Write for the audience

- Describe observable outcome and why it matters; do not copy commit subjects verbatim.
- Remove internal ticket IDs from public notes unless repository precedent keeps them.
- Link advisories for security items without exposing exploit details beyond the project's disclosure policy.
- Put required actions, compatibility limits, and irreversible migrations in Upgrade notes or Breaking changes.
- Mark uncertain claims and identify the artifact needed to verify them.

Compare the draft with the actual range one final time so every bullet maps to evidence and every major user-facing change is represented.

## 4. Publish safely

Preview the final Markdown and destination first. When publishing, use a temporary body file or the hosting provider's structured API to avoid shell interpolation. Return the release/PR URL and list any intentionally omitted or unverified items.
