---
name: verify
description: 跑全套品質驗證（lint + type + test + coverage + security）並產出報告。用於 commit 前、PR 前、sprint 結尾。
---

# /verify — Quality Gate 三合一

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
