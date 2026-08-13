---
name: git-release
description: 更新版本檔中的版本號，彙整兩版本間的 commit 寫成繁體中文發布摘要，打 tag 推上遠端並發佈 release 頁面。
disable-model-invocation: true
argument-hint: 目標版本號，如 v0.8.1
allowed-tools: Bash(git log:*), Bash(git tag:*), Bash(git push:*), Bash(git describe:*), Bash(git commit:*), Bash(git add:*), Bash(gh release:*)
---

# Git Release

Release at the given version: update the version file → summarize changes → tag → push → publish the release page.

## 1. Detect the version file — never assume

Find the project's version source by type: `pyproject.toml`, `package.json`, `.claude-plugin/plugin.json`, `Cargo.toml`, `*.csproj`…

- **Multiple found** → update all of them to the same version. Two files with different version numbers are two files lying to each other.
- **None found** → stop and ask the user where the version lives.

## 2. Bump and commit

Update the version file(s) to the target version, as its own commit (English, following the `/git-commit` format rules):

```
Bump version to 0.8.1
```

## 3. Collect changes between versions

```bash
git describe --tags --abbrev=0        # find the previous tag
git log <previous-tag>..HEAD --oneline --no-merges
date +%Y-%m-%d                        # release date is looked up, not guessed
```

- `--no-merges` drops meaningless automatic merge records.
- **Collapse multiple commits on one feature into a single meaningful entry** — changelog readers care about what changed, not how many times.

## 4. Write the release notes (Traditional Chinese)

Notes are Traditional Chinese; the tag name and the bump commit stay English. Entries are changesets-style — PR, merge commit, author — all three from `gh pr list --state merged --json number,mergeCommit,author`.

```markdown
Release v0.8.1 - 2026-07-28

## 總覽
一小段話：這個版本的主要目的與核心價值。

## 更新日誌

### 新功能

- [#12](<repo>/pull/12) [`930a450`](<repo>/commit/930a450) Thanks [@user](https://github.com/user)! - 一句話的變更摘要

  需要細節才縮排補一段；一句話就夠的不硬加。

### 錯誤修正
### 重構
```

- Empty categories are omitted.
- One entry per feature, citing the PR that landed it. No PR (direct to main) → short sha alone.

## 5. Tag and push

```bash
git tag -l v0.8.1                     # check whether the tag already exists
git tag -a v0.8.1 -m "<release notes>"  # exists → add -f to replace (this skill's stated exception)
git push origin v0.8.1                # replacing an existing tag → git push -f origin v0.8.1
git push                              # the version-bump commit goes up too
```

Before replacing an existing tag, report which commit it currently points to — let the user see what is being overwritten before it is overwritten.

## 6. Publish the release page

A bare tag buries the notes in `git show`; clicking the tag on GitHub must land on a release page.

```bash
gh release view v0.8.1                              # exists → gh release edit to update the notes
gh release create v0.8.1 --title "v0.8.1" --notes-file <notes>   # same notes as the tag, verbatim
```

GitLab remote → `glab release create`. No remote or no forge CLI → the annotated tag is the endpoint; say so in the report.

## Rationalization table

| Excuse | Reality |
| --- | --- |
| "This project is obviously pyproject.toml" | Detection costs three seconds. Assume wrong and the version lands in a file nobody reads. |
| "The commit messages are clear enough, copy them into the changelog" | Commits are process records for developers; a changelog is a result summary for users. Distill, don't transplant. |
| "I know today's date" | You don't. `date +%Y-%m-%d`. |
