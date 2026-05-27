---
name: sync-it
description: 比對 code 與文件之間的漂移（drift），列出需要更新的文件並建議修法。**主動觸發時機**：使用者改完 API endpoint / DB schema / user story 行為後，說「文件還對嗎」「PRD 要不要動」「API 改了」，或 `/verify` 過了但有 `docs/` 檔案未動到。
---

# /sync-it — Doc-as-Code Drift Detector

## 🚨 自動觸發訊號（AI 主動偵測）

依 `rules/07-proactive-skill-trigger.md`，AI 要監測對話、發現訊號主動建議。

### 強訊號（高機率該觸發）

- 「我改了 API」「endpoint 改名」「schema 改了」
- 「文件還對嗎」「PRD 還對嗎」「API contract 要不要動」
- 改了 `app/routes/`、`db/migrations/`、`app/models/` 等 contract 邊界檔
- `/verify` 已過綠燈、要 commit 前
- Sprint 結尾、commit 累積 5+ 個沒同步文件

### 中訊號（建議但詢問）

- 對話中提到 endpoint path 變更
- 對話中提到欄位 / response schema 變更
- 改 BDD scenario 但沒改對應的 PRD AC

### 反訊號（這些不要觸發 sync-it）

- 純樣式 / 註解修改 → 無 drift 風險
- 純 refactor，無 contract 改動
- 還沒有任何 spec → 先跑 `/spec-it`

### 主動建議的話術範例

> 你說「我改了 API path 從 /api/summary 到 /v1/summaries」 — 這會讓 `docs/api-contract.md` 漂移。
>
> 建議跑 `/sync-it`，它會比對你的 code 改動與 `docs/`、`tests/features/` 的所有 spec，列出哪些文件要跟著動。漏了 sync 會導致下次 AI 讀過期文件、寫錯前提。
>
> 要跑嗎？

---

## 何時觸發

- 使用者剛跑完 `/tdd-cycle`，準備 commit 前
- 使用者說「文件對嗎」「PRD 還對嗎」「我改了 API，文件要不要動」
- 每個 sprint 結尾，列出本 sprint 累積的 drift
- 使用者打 `/sync-it`

## 不要觸發的情況

- 純樣式 / 注解修改 → 無 drift 風險
- 還沒有任何 spec → 先跑 `/spec-it`

---

## Doc-as-Code 鐵律（大廠 Stripe / Twilio 慣例）

**文件 = code 的一部分**。行為變了，文件先變（或同 PR 同步變）。

文件 vs code drift 是專案腐爛的最大來源：
- AI 讀過期文件 → 寫出基於錯誤前提的程式
- 6 個月後的自己 → 看文件以為這樣，看 code 發現那樣，崩潰
- 新成員 / 學員 → 完全無法相信文件

---

## 執行步驟

### Step 1：掃描 code 與文件

讀取以下檔案：

| 文件類別 | 路徑 |
|---|---|
| PRD | `docs/PRD.md` |
| API contract | `docs/api-contract.md` |
| DB schema | `docs/db-schema.md` |
| BDD scenarios | `tests/features/*.feature` |
| ADR | `adr/ADR-*.md` |
| Backlog | `tasks/backlog.md` |
| Code | `app/`、`src/`、`tests/` |

### Step 2：比對 4 類 drift

#### Drift A：行為不一致（PRD ↔ code）

| 來源 | 內容 | code 實況 | 判斷 |
|---|---|---|---|
| PRD §4 US-001 AC | 「摘要字數 80-120」 | code 沒有字數驗證 | ❌ 應補驗證 OR 改 AC |

#### Drift B：API 合約過期（api-contract.md ↔ endpoint code）

| 來源 | 文件描述 | code 實況 | 判斷 |
|---|---|---|---|
| api-contract §5 | `POST /v1/summaries` | code 是 `POST /api/summary` | ❌ 路徑漂移 |
| api-contract §6 | response 含 `word_count` | code 回傳沒 `word_count` | ❌ schema 漂移 |

#### Drift C：DB schema 過期（db-schema.md ↔ migration）

| 來源 | 文件描述 | migration 實況 | 判斷 |
|---|---|---|---|
| db-schema §4 | `users.is_active` | 最新 migration 已改為 `users.status` | ❌ 文件未更新 |

#### Drift D：測試與 spec 不一致

| 來源 | spec 描述 | test 實況 | 判斷 |
|---|---|---|---|
| BDD scenario | 「文章太短顯示錯誤」 | 無對應 test | ❌ 缺測試 |
| BDD scenario | 「API 失敗顯示降級訊息」 | test 用 mock 跳過 | ⚠ test 強度不足 |

### Step 3：產出 Drift Report

```markdown
# Drift Report — <date>

## 🔴 Critical（必須修，否則 AI 會繼續誤導）

### D-001: API path 漂移
- 文件：`docs/api-contract.md` §5 寫 `POST /v1/summaries`
- 實況：`app/routes.py:23` 是 `POST /api/summary`
- 建議：改 code 對齊文件（路徑命名規範要求 /v1/）

### D-002: PRD AC 未驗證
- 文件：`docs/PRD.md` US-001 AC「字數 80-120」
- 實況：`app/summarizer.py` 沒檢查 word_count
- 建議：補 `if not 80 <= word_count <= 120: regenerate()` + 對應測試

## 🟡 Warning（建議修，但不阻擋 commit）

### D-003: 缺對應測試
- BDD scenario：「文章太短顯示錯誤」
- 實況：`tests/unit/` 無對應 test case
- 建議：補 `test_summarize_with_too_short_article_raises_error`

## 🟢 Info（純文件更新）

### D-004: ADR 提及的舊技術
- ADR-0002 寫「採用 Vue」
- 實況：`package.json` 是 React
- 建議：開新 ADR-NNNN superseded ADR-0002，記錄切換動機
```

### Step 4：問使用者裁決

```
我發現 4 處 drift（2 critical / 1 warning / 1 info）。

優先建議處理 Critical：
1. D-001 改 code 對齊 /v1/ 路徑
2. D-002 補字數驗證 + 測試

要我先修這 2 個嗎？或你想先看 Warning / Info？
```

不要直接動手 — 等使用者選。

### Step 5：依使用者選擇執行

- 改 code → 跑 `/tdd-cycle`（先寫測試重現問題）
- 改文件 → 直接 edit，但要更新 `last-synced-with` frontmatter（如有）
- 兩邊都改 → 一個 commit 修一邊，不要混在一起

---

## 文件 frontmatter（建議所有 spec 文件加）

```markdown
---
title: API Contract
version: 1.3.0
last-synced-with: src/routes/v1/summaries.ts:1-150
last-updated: 2026-05-27
status: active
---
```

`/sync-it` 跑時會優先檢查 `last-synced-with` 指向的 code 範圍。

---

## 鐵律

1. **發現 drift 不直接動手，先列 report 給使用者裁決**
2. **Critical drift 必須在 commit 前修掉**（commit hook 可選擇性 block）
3. **改 code 對齊 spec ≠ 改 spec 對齊 code** — 兩個方向決策不同，由人決定
4. **不要靜默更新文件** — 每次 sync 都要顯示 diff 給使用者確認
5. **ADR 永遠不能被「sync」覆寫** — 要推翻就寫新 ADR

---

## 觸發範例

使用者：「我寫完了，要 commit 了」

AI（你）：
> 等等，先跑 `/sync-it` 檢查 drift。
>
> 掃描中⋯⋯
>
> 我發現 3 處 drift：
>
> 🔴 **D-001**: `app/routes.py:23` 用 `/api/summary`，但 `docs/api-contract.md` 寫 `/v1/summaries`
> 🟡 **D-002**: BDD scenario「文章太短顯示錯誤」沒有對應 unit test
> 🟢 **D-003**: ADR-0002 提的 Vue 跟現在 package.json 的 React 不一致
>
> 建議先處理 D-001（critical），有 2 個方向：
>
> 1. 改 code 把路徑改成 `/v1/summaries`（推薦，對齊命名規範）
> 2. 改 spec 把路徑改成 `/api/summary`（如果你已經對外公布）
>
> 你選哪個？

---

## 與其他 skill 的關係

```
/tdd-cycle  ─→ 寫完 code + test
   ▼
/sync-it（這個）─→ 列出 drift
   ▼
（修完 drift）
   ▼
/verify     ─→ 跑全套驗證
   ▼
/commit-msg ─→ 生 commit
```
