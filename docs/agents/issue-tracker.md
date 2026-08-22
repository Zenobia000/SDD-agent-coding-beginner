# 議題追蹤器

本地 markdown。**不使用 GitHub Issues** —— 這是公開教材 repo，
demo 與練習的票不該進公開 issue 區。

## 位置

`.scratch/<feature>/issues/NNN-<slug>.md`

`.scratch/` 已在 `.gitignore`，因此票不進版控。

## 開一張票

```bash
mkdir -p .scratch/<feature>/issues
cat > .scratch/<feature>/issues/001-<slug>.md <<'EOF'
---
id: 001
title: <一句話>
status: open        # open | in-progress | done
blocked-by: []      # 例：[002, 003]
---

## 目標
## 完成條件
EOF
```

## 列出未關的票

```bash
grep -l 'status: open' .scratch/*/issues/*.md
```

## 阻擋關係

frontmatter 的 `blocked-by`，值是被擋住的票 id 陣列。
`blocked-by: []` 代表可以開工。`/implement-all` 靠這個欄位排程。

## 票的內容

就在檔案本身，沒有外部 body。
