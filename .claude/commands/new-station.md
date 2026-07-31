---
description: 產生一份符合 doc contract 的新站別教材骨架（七段齊全、閘門佔位、對照連結就位）
argument-hint: <編號 0-7> <站名>
arguments: number title
---

# 建立站別教材：S$number $title

依 `.claude/rules/00-doc-contract.md` §2 產生 `curriculum/S$number-$title.md`。

## 動手前先確認

1. 讀 `curriculum/README.md`，確認 S$number 在課表上分配到幾分鐘
2. 讀 S$number-1 那一站的「產出」，那是這一站的**輸入**
3. 讀 `labs/reference-project/RUBRIC.md` 有沒有 S$number 的條目

三項有任何一項查不到，先問使用者，不要自己編。

## 產生的骨架

```markdown
# S$number $title

## 結論卡

| | |
|---|---|
| **做什麼** | <一句話> |
| **為什麼** | <一句話，回扣四拍的哪一拍> |
| **產出** | <具體檔名> |
| **下一步** | <一個動作> |

**這一站對「<對象>」跑一輪四拍。**

## 課堂 15 分鐘版

**老師講**（5 分）：<最多 3 個要點>

**學生做**（10 分）：<一段可直接貼的 prompt 或一條指令>

## 動手

1. <一步一個動作>
2. …

## 閘門

全部打勾才進 S<下一站>。

- [ ] <yes/no 判準>
- [ ] …（最多 5 條）

## 我做對了嗎

對照 `labs/reference-project/S$number/expected/<檔名>`。

差異超過 <具體條件> 就回到「動手」第 <N> 步重跑。

## 回家展開版

<完整原理・變體・進階。課堂不講，長度不限。>

## 下一步

<恰好一句>
```

## 產生後

1. 把 S$number 的「產出」寫進 `labs/reference-project/RUBRIC.md`
2. 修改 S<$number - 1> 的「下一步」指向這一站
3. 跑 `/lesson-check curriculum/S$number-$title.md`

## 硬規則

- ❌ 佔位符不要留空 —— 每一格都要填出真實內容，`<...>` 一個都不能留
- ❌ 閘門寫不出 yes/no 判準 → **停下來**，表示這一站的目標還沒想清楚，先跟使用者確認目標
- ❌ 不要一次產生多站 —— 一次一站，跑完 `/lesson-check` 再開下一站
