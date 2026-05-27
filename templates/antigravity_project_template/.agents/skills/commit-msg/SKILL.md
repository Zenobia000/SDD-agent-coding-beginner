---
name: commit-msg
description: 生成 Conventional Commits 1.0 格式的 commit message + WHY/WHAT/IMPACT body。**主動觸發時機**：使用者說「commit」「提交」「生 commit message」「準備 push」「git commit」，且 `/verify` 已過、`/sync-it` 無 drift、有 staged changes。
---

# /commit-msg — Conventional Commits 生成器

## 🚨 自動觸發訊號（AI 主動偵測）

依 `rules/07-proactive-skill-trigger.md`，AI 要監測對話、發現訊號主動建議。

### 強訊號（高機率該觸發）

- 「commit」「提交」「我要 commit 了」
- 「生 commit message」「寫 commit」「幫我寫 message」
- 「準備 push」「要 push 了」
- 「git commit」「git 提交」
- `/verify` 全綠 + `/sync-it` 無 drift + `git status` 有 staged 變更

### 中訊號（建議但詢問）

- 「告一段落」「先存個檔」
- 對話切換到「準備提交」的氛圍

### 反訊號（這些不要觸發 commit-msg）

- 還有紅燈測試 → 先建議 `/verify` 修
- 還有 critical drift → 先建議 `/sync-it` 修
- 沒有 staged changes → 提醒使用者 `git add`
- 使用者剛口頭說「commit」但其實還在寫 code（看上下文）

### 主動建議的話術範例

> 你說「準備 push」 — `/verify` 全綠 ✅、`/sync-it` 無 drift ✅、有 staged changes。
>
> 建議跑 `/commit-msg`。它會掃 staged 變更，依 Conventional Commits 1.0 + WHY/WHAT/IMPACT 格式生 message。比起「fix bug」這種沒資訊的訊息，6 個月後的你（與 AI）會感激今天的自己。
>
> 要生嗎？

---

## 何時觸發

- 使用者說「commit」「提交」「生 commit message」
- 使用者打 `/commit-msg`
- `/verify` 全綠後

## 不要觸發的情況

- 還有紅燈測試 → 先跑 `/verify` 修
- 還有 drift → 先跑 `/sync-it` 修
- 沒有 staged changes → 提醒使用者 `git add`

---

## 大廠對標

採 **Conventional Commits 1.0**（業界標準，與 semantic-release / changelog 工具相容）+ **AI 時代 commit 分層策略**（讓未來 AI 讀 git log 能站在前人肩膀上）。

---

## Conventional Commits 格式

```
<type>(<scope>): <subject>

<body — WHY/WHAT/IMPACT 分層>

<footer — issue refs / breaking changes>
```

### Type 對照表

| Type | 用途 | AI 讀取深度 |
|---|---|---|
| `feat` | 新功能 | 讀 subject + body 完整 |
| `fix` | 修 bug | 讀 subject + root cause |
| `refactor` | 重構（無行為改變） | 讀 subject + 動機 |
| `perf` | 效能改善 | 讀 subject + before/after 數據 |
| `docs` | 文件 | 只讀 subject |
| `test` | 測試 | 只讀 subject |
| `chore` | 雜事（依賴升級等） | 只讀 subject |
| `ci` | CI/CD | 只讀 subject |
| `style` | 格式（空白 / 引號 — 無語意） | 只讀 subject |

### Scope（選填，建議寫）

`feat(auth):` / `fix(payment):` / `refactor(summarizer):`

---

## 執行步驟

### Step 1：掃描 staged changes

```bash
git status --short
git diff --cached --stat
git diff --cached
```

抓出：
- 改了哪些檔案
- 主要的程式碼變動內容
- 是否涉及 contract / spec / migration / config

### Step 2：判斷 type

依變動內容自動判斷：

| 看到 | 判斷 |
|---|---|
| 新增 endpoint / 新增 function / 新增 component | `feat` |
| 修 bug + 對應的測試 | `fix` |
| 改命名 / 抽函式 / 移動 code（無行為變動） | `refactor` |
| 改演算法 / 加 cache（行為相同但更快） | `perf` |
| 只動 `docs/`、`README.md`、`*.md` | `docs` |
| 只動 `tests/`、新增測試 | `test` |
| `package.json` / `pyproject.toml` 升版本 | `chore` |
| `.github/workflows/` | `ci` |

**多種變動混在一起 → 提醒使用者拆 commit**（一個 commit 做一件事）。

### Step 3：生 subject（< 72 字元、祈使句）

```
✅ feat(summarizer): add Chinese summary support
✅ fix(api): prevent token reuse after rotation
✅ refactor(billing): extract pricing rules into dedicated module

❌ feat: 加了一些功能
❌ Updated stuff
❌ misc fixes
```

### Step 4：生 body（依 type 分層）

#### feat — WHY / WHAT / IMPACT 完整

```
feat(summarizer): add Chinese summary with word count validation

WHY: 學員主要需求是把英文新聞變成中文摘要，且需要嚴格的字數範圍
（80-120 字）以保持「快速掃讀」的可用性。

WHAT: 接 Gemini 1.5 Flash API，prompt 內含字數約束指令；產出後做
post-validation，若超出範圍則重試 1 次（max retry）。失敗則回降
級訊息「服務暫時無法使用」。

IMPACT: docs/api-contract.md §6 endpoint schema 已更新（新增
word_count 欄位）；新增 4 個 unit test + 2 個 integration test，
coverage 從 0 → 87%。需要環境變數 GEMINI_API_KEY。
```

#### fix — WHY + root cause

```
fix(auth): prevent refresh token reuse after rotation

Root cause: refresh token 未在 Redis 中失效，導致舊 token 在 TTL
窗口內仍可 replay。

加上 jti claim + 一次性 invalidate 防止 replay。
```

#### refactor — WHY 就好

```
refactor(billing): extract pricing rules into dedicated module

Pricing 邏輯散在 3 個 service，無法單元測試。抽出獨立 module 後
能對每個 rule 寫單獨測試（見新增的 tests/unit/test_pricing.py）。
```

#### docs / test / chore / ci — subject 一行即可

```
docs(api): update authentication endpoint examples
test(summarizer): add edge case for 0-length input
chore(deps): bump google-generativeai to 0.8.3
```

### Step 5：footer（如有）

```
Closes #123
BREAKING CHANGE: API path /api/summary 移除，改用 /v1/summaries
Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
```

### Step 6：展示給使用者確認

```
我為這次 staged changes 生了 commit message：

────────────────────────────────────
feat(summarizer): add Chinese summary with word count validation

WHY: 學員主要需求...

WHAT: 接 Gemini 1.5 Flash API...

IMPACT: docs/api-contract.md §6...
────────────────────────────────────

確認後我幫你跑：
  git commit -m "[above]"

或你想調整哪段？
```

**不要直接 commit** — 等使用者確認。

---

## 鐵律

1. **一個 commit 做一件事** — 多種 type 混在一起就拆 commit
2. **Subject 用祈使句** — `add` 不是 `added` 不是 `adds`
3. **Subject ≤ 72 字** — Body 給細節
4. **feat 必須有 WHY + WHAT + IMPACT 三段** — 這是給未來 AI 與自己的禮物
5. **breaking change 必須在 footer 標 `BREAKING CHANGE:`** — semantic-release 會抓
6. **不要寫「fix bug」「update code」「misc」** — 沒有任何資訊

---

## 反例（不要這樣寫）

```
❌ update                       # 改了什麼？
❌ fix bug                      # 哪個 bug？
❌ wip                          # PR 階段都不該有這個
❌ feat: 改了 summarizer.py     # 改了什麼？為什麼？
❌ 1234567890                   # 真的有人這樣寫
```

---

## 觸發範例

使用者：「ok 我要 commit」

AI（你）：
> `/verify` 已全綠 ✅、`/sync-it` 無 drift ✅，跑 `/commit-msg`。
>
> 掃 staged：
> - `app/summarizer.py` +120 / -10
> - `tests/unit/test_summarizer.py` +85
> - `docs/api-contract.md` +25
>
> 判斷：`feat`（新增功能 + 對應測試 + 文件同步）
> Scope：`summarizer`
>
> 生 message：
>
> ─────────────────
> feat(summarizer): add Chinese summary with word count validation
>
> WHY: 學員主要需求...
> [完整 body]
> ─────────────────
>
> 確認後跑 commit？或要調整？
