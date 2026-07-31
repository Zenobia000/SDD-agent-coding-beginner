---
name: verify
description: 跑全套品質驗證（Format / Lint / Type / Test+Coverage / Security 五維度）並產出報告。**主動觸發時機**：使用者說「commit 前檢查」「準備 commit」「上線前」「跑完了」「都寫完了」「應該沒問題了」「sprint 結束」，或 `/tdd-cycle` 剛完成一輪。
---

# /verify — Quality Gate 三合一

## 🚨 自動觸發訊號（AI 主動偵測）

依 `rules/07-proactive-skill-trigger.md`，AI 要監測對話、發現訊號主動建議。

### 強訊號（高機率該觸發）

- 「commit 前檢查」「準備 commit」「我要 commit 了」
- 「上線前」「準備部署」「準備 push」
- 「跑完了」「寫完了」「都做完了」
- 「應該沒問題了」「都綠燈了」
- 「sprint 結束」「sprint 收尾」
- `/tdd-cycle` 剛跑完一輪、所有 sprint task 都打勾

### 中訊號（建議但詢問）

- 「PR 前要做什麼」
- 對話切換到「準備提交」的氛圍

### 反訊號（這些不要觸發 verify）

- 還在 RED-GREEN-REFACTOR 過程中 → 只跑單一測試即可
- 沒寫過任何 code 的新專案
- 使用者正在 debug 跑紅燈 → 不要打斷，先讓他修完

### 主動建議的話術範例

> 你說「應該沒問題了」 — commit 前建議跑 `/verify` 一次。
>
> 它會自動跑 Format / Lint / Type / Test + Coverage / Security 五項檢查（依你的技術棧選工具），3 分鐘內告訴你能不能 commit。比手動跑舒服很多。
>
> 要跑嗎？

---

## 何時觸發

- 使用者說「commit 前檢查」「全跑一次」「準備上線」
- 使用者打 `/verify`
- 每個 sprint 結尾
- `/tdd-cycle` 完成後、`/commit-msg` 之前

## 不要觸發的情況

- 還在 RED-GREEN-REFACTOR 過程中 → 只跑單一測試即可
- 沒寫過任何 code 的新專案

---

## 大廠對標

採 **Google Testing Pyramid**（80/15/5）+ **OWASP secure coding** + **業界 CI 標準**。

5 個維度：
1. **Format** — 程式碼格式一致
2. **Lint** — 靜態分析（不健康的寫法）
3. **Type** — 型別檢查（TypeScript / mypy）
4. **Test + Coverage** — 行為正確 + 覆蓋率夠
5. **Security** — 沒明顯漏洞 / 沒洩 secret

---

## 執行步驟

### Step 1：偵測專案類型

讀取：
- `package.json` → Node / TS
- `pyproject.toml` / `requirements.txt` → Python
- `Cargo.toml` → Rust
- `go.mod` → Go

依語言選對應工具鏈。

### Step 2：依序跑 5 個維度

#### 維度 1：Format

| 語言 | 工具 | 指令 |
|---|---|---|
| JS / TS | Prettier | `npx prettier --check .` |
| Python | Ruff / Black | `ruff format --check .` |
| Go | gofmt | `gofmt -l .` |

**Fail 處理**：跑對應的 `--write` 或 `format` 指令自動修。

#### 維度 2：Lint

| 語言 | 工具 | 指令 |
|---|---|---|
| JS / TS | ESLint | `npx eslint . --max-warnings 0` |
| Python | Ruff | `ruff check .` |
| Go | golangci-lint | `golangci-lint run` |

**Fail 處理**：列出前 5 個 issue + 對應檔案行號，問使用者要先修哪些。

#### 維度 3：Type Check

| 語言 | 工具 | 指令 |
|---|---|---|
| TS | tsc | `npx tsc --noEmit` |
| Python | mypy / pyright | `mypy app/` |
| Go | (built-in) | `go vet ./...` |

**Fail 處理**：型別錯誤先修，不能 `# type: ignore` 帶過（除非寫明理由）。

#### 維度 4：Test + Coverage

| 語言 | 工具 | 指令 |
|---|---|---|
| JS / TS | Vitest / Jest | `npx vitest run --coverage` |
| Python | pytest + coverage | `pytest --cov=app --cov-report=term-missing` |
| Go | go test | `go test -cover ./...` |

**目標：** Unit 80%、Integration 主流程 100%、E2E 關鍵 journey 100%。

**Fail 處理**：
- 紅燈測試 → 不能繼續，先修
- Coverage < 80% → 列出未覆蓋的關鍵函式

#### 維度 5：Security 快掃

| 檢查 | 工具 | 指令 |
|---|---|---|
| 依賴漏洞 | npm audit / pip-audit | `npm audit` / `pip-audit` |
| Secret 洩漏 | gitleaks / detect-secrets | `gitleaks detect --source .` |
| Hardcoded API key | grep | `grep -rE "api[_-]?key.*=.*['\"][A-Za-z0-9]{20,}" --exclude-dir=node_modules` |

**Fail 處理**：
- Critical CVE → 必修，不能 commit
- Hardcoded secret → **立刻 rotate + 從 history 移除**

> **注意 `/verify §5` vs `/sec-scan` 的分工**：
> - `/verify §5 Security` 是 **commit 前的快速掃描**（依賴漏洞 + secret 洩漏）
> - `/sec-scan` 是 **部署 / push 到 public repo 前的雙保險**（涵蓋更廣的 secret pattern + `.gitignore` 覆蓋 + 未填 placeholder）
>
> Commit 前跑 `/verify` 就好；要部署 / push public 前，**額外**再跑一次 `/sec-scan`。

### Step 3：產出 Verify Report

```markdown
# Verify Report — 2026-05-27 11:35

## ✅ Pass（4/5）

### Format ✅
- Prettier: 0 issues
### Lint ✅
- ESLint: 0 errors, 0 warnings
### Type Check ✅
- tsc: no errors
### Security ✅
- npm audit: 0 high/critical
- gitleaks: no secrets found

## ❌ Fail（1/5）

### Test + Coverage ❌
- Tests: 24 passed, 2 failed
- Coverage: 76% (target 80%)

#### 紅燈測試
1. `tests/unit/test_summarizer.py::test_summarize_with_empty_string`
   - Expected: ValidationError("content cannot be empty")
   - Actual: TypeError("NoneType has no attribute 'strip'")
   - 建議修法：在 summarize() 開頭加 `if not content: raise ValidationError(...)`

2. `tests/integration/test_flow.py::test_full_summarize_flow`
   - 失敗原因：mock 設定錯誤
   - 建議修法：mock_api.return_value 改用 dict

#### 未覆蓋的關鍵函式
- `app/summarizer.py:_validate_input` (62-78 行未覆蓋)
- `app/api_client.py:_handle_503` (45-52 行未覆蓋)

建議：先修 2 個紅燈測試，再補 _validate_input 的測試案例。

## 下一步建議
1. 修 test_summarize_with_empty_string（5 分鐘）
2. 修 test_full_summarize_flow（5 分鐘）
3. 補 _validate_input 測試（10 分鐘）
4. 再跑 /verify 確認全綠
5. 跑 /commit-msg 生 commit
```

---

## 📝 Issue Logging — 寫入 `tasks/known-issues.md`

`/verify` 是最容易發現 issue 的時機。但**不是每個 fail 都該當下修** — 有些 fail 屬於「這 sprint 不在 scope、但確實是 bug」，要記下來不能假裝沒看到。

### 觸發 Issue Logging 的情境

| 維度 | 何時要 log issue |
|---|---|
| **Test fail** | 紅燈測試屬於下個 sprint 的 user story / 屬於既有 bug 非本 sprint 範圍 |
| **Coverage 不達標** | 缺的覆蓋是「非主流程的歷史 code」、本 sprint 不打算補 |
| **Lint warning** | 風格 warning 不阻擋功能、批次整理留下個 sprint |
| **Security warning** | 中 / 低嚴重度漏洞（Critical / High 必須當下修，不能 log） |

### 建議的問法

報告產出後，對每個 fail 問使用者：

```
測試 test_xxx 紅燈。三個選項：
1. 現在修（建議，5 分鐘內）
2. 記進 known-issues.md 當 ISSUE-NNN，下個 sprint 處理
3. 它其實已經是 known issue 了（哪個 ISSUE-NNN？）

你選？
```

### 主動建議的話術

> `test_api_503_with_retry` 紅燈，但這跟 `tasks/known-issues.md` 的 ISSUE-002（Gemini 偶發 503）是同類。
>
> 你不在這 sprint 修的話，要不要：
> - 把 ISSUE-002 的「重評估時機」改成 next sprint
> - 或新增 ISSUE-003 補上這個測試案例的失敗細節
>
> 還是現在直接修？

### 寫入要求

依 `tasks/known-issues.md` 既有格式，9 個欄位都要填。

### 鐵律

- **Critical / High Security 漏洞**不能進 known-issues — 必須當下修
- **主流程紅燈**不能進 known-issues — 必須當下修
- **進 known-issues 的 fail 需要「延後原因」明確**（不是「懶得修」）

---

## 一鍵指令（建議寫進 Makefile / package.json scripts）

```makefile
verify: format lint type test security

format:
	ruff format --check .

lint:
	ruff check .

type:
	mypy app/

test:
	pytest --cov=app --cov-report=term-missing --cov-fail-under=80

security:
	pip-audit
	gitleaks detect --source .
```

```bash
make verify
```

---

## 鐵律

1. **5 個維度全綠才能 commit**（紅燈不要 push 上去）
2. **Coverage 不達標不可 merge** — 但允許 warning 通過（< 80% 但 ≥ 75% 可放行，要記原因）
3. **Security fail 必須當下處理** — 不能延後
4. **每個 fail 給具體修法建議** — 不要只說「測試失敗」就丟回去

---

## 觸發範例

使用者：「我寫完了，準備 commit」

AI（你）：
> 跑 `/verify` 全跑一遍。
>
> 偵測到 Python 專案，用 ruff / mypy / pytest / pip-audit。
>
> 跑中⋯⋯
>
> Format ✅ / Lint ✅ / Type ✅ / Security ✅
> Test ❌ — 2 個紅燈 + Coverage 76%（差 4%）
>
> 詳細報告：
> [完整 report]
>
> 建議先修這 2 個紅燈再 commit，要我幫你跑 `/tdd-cycle` 修嗎？
