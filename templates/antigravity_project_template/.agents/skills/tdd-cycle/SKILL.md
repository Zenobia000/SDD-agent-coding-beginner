---
name: tdd-cycle
description: 引導使用者跑完一輪 Red-Green-Refactor TDD 循環。**主動觸發時機**：使用者說「實作 US-___」「寫 ___ 功能」「我要動手了」「開始 code」「修 ___ bug」，或 `/spec-it` 剛跑完、有測試骨架待填實，或專案有紅燈測試。
---

# /tdd-cycle — Red-Green-Refactor 紅綠燈

## 🚨 自動觸發訊號（AI 主動偵測）

依 `rules/07-proactive-skill-trigger.md`，AI 要監測對話、發現訊號主動建議。

### 強訊號（高機率該觸發）

- 「實作 US-___」「實作 T-___」
- 「寫 ___ 功能」「把 ___ 寫出來」「動手寫 ___」
- 「我要動手了」「開始 code」「開始實作」
- 「修 ___ bug」「___ 跑出錯誤」「___ 不 work」
- `/spec-it` 剛產出測試骨架（`tests/unit/test_*.py` 有多個 `pass`）

### 中訊號（建議但詢問）

- 「加一個 function ___」「寫一個 method ___」
- 「優化 ___」（先問是 refactor 還是行為改變）

### 反訊號（這些不要觸發 tdd-cycle）

- 純樣式 / CSS / 文案修改（無邏輯）
- 純 refactor 無新行為（這時建議 `/verify` 確認測試還綠）
- 沒 PRD / 沒測試骨架 → 先建議 `/spec-it`
- 改 hardcoded value（如 timeout 5s → 10s）

### 主動建議的話術範例

> 你說「實作 US-001」 — `/spec-it` 已經產出 4 個測試骨架了，建議跑 `/tdd-cycle` 紅綠燈。
>
> 它會引導你「寫測試 → 跑（紅）→ 寫實作 → 跑（綠）→ 重構」三步驟，避免一次寫 200 行 code 卻沒測試覆蓋。Solo dev 容易跳測試，這個 skill 會強制你回到 TDD 節奏。
>
> 要跑嗎？

---

## 何時觸發

- 使用者說「實作 US-XXX」「寫 ___ 功能」「我要動手了」
- 使用者打 `/tdd-cycle`
- `/spec-it` 已產出 BDD scenario 與測試骨架，準備開始實作
- 修 bug（先寫一個能重現 bug 的失敗測試）

## 不要觸發的情況

- 純樣式 / 文案修改（沒有行為變動）
- 純 refactor，無新行為（這時跑 `/verify` 即可）
- 沒有 PRD / spec → 先跑 `/spec-it`

---

## 執行步驟（Kent Beck 三步驟）

### Step 0：確認前置

跑這個 skill 前，確認：

- [ ] `docs/PRD.md` 已存在
- [ ] 對應的 user story（US-XXX）已寫好 AC
- [ ] `tests/features/*.feature` 已寫 BDD scenario
- [ ] 對應的 `tests/unit/test_*.py` 已有測試骨架

任一條缺 → 停下，提醒使用者跑 `/spec-it`。

---

### Step 1：RED 🔴 — 寫一個失敗的測試

從 `tests/unit/test_*.py` 的骨架挑一個 `test_xxx(): pass`，把它寫實：

```python
def test_summarize_with_valid_500_word_article_returns_100_word_summary():
    # Arrange
    article = "..." * 500
    summarizer = Summarizer(api_key="test_key")

    # Act
    result = summarizer.summarize(article)

    # Assert
    assert result.success is True
    assert 80 <= result.word_count <= 120
```

**寫完跑測試：**

```bash
pytest tests/unit/test_summarizer.py::test_summarize_with_valid_500_word_article_returns_100_word_summary -v
```

**預期：紅燈** ❌ — 因為 `Summarizer` 還沒實作 / `summarize()` 不存在 / 結果不符。

**鐵律：**
- 如果測試是綠燈 → 表示這個行為已經有了，跳到下一個測試
- 如果測試錯誤是 `ImportError` 之外的事 → 測試本身寫錯了，先修測試

---

### Step 2：GREEN 🟢 — 寫最少的程式碼讓它通過

**只寫足夠讓測試通過的程式**，不多做：

```python
# app/summarizer.py
from dataclasses import dataclass

@dataclass
class SummaryResult:
    success: bool
    word_count: int

class Summarizer:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def summarize(self, article: str) -> SummaryResult:
        # 最簡單能讓測試過的實作
        # 真實版會呼叫 Gemini API
        return SummaryResult(success=True, word_count=100)
```

**跑測試：**

```bash
pytest tests/unit/test_summarizer.py -v
```

**預期：綠燈** ✅

**鐵律：**
- 不要「順便」加其他功能（YAGNI — You Aren't Gonna Need It）
- 如果還是紅燈，**只改實作、不改測試**（除非測試確實寫錯）
- 連續紅燈 3 次 → 停下，回頭看測試是不是描述了不可能的行為

---

### Step 3：REFACTOR 🔵 — 重構（測試保持綠燈）

現在實作很醜（hardcode `word_count=100`）。重構成真實版：

```python
# app/summarizer.py
from dataclasses import dataclass
import google.generativeai as genai

@dataclass
class SummaryResult:
    success: bool
    word_count: int
    summary: str

class Summarizer:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def summarize(self, article: str, max_words: int = 100) -> SummaryResult:
        if not article or len(article) < 100:
            raise ValidationError("Article too short")

        prompt = f"Summarize the following article in {max_words} Chinese words:\n\n{article}"
        response = self.model.generate_content(prompt)
        summary = response.text
        word_count = len(summary)

        return SummaryResult(
            success=True,
            word_count=word_count,
            summary=summary,
        )
```

**每改一步跑測試：**

```bash
pytest tests/unit/test_summarizer.py -v
```

**保持綠燈** ✅。如果重構過程中變紅 → 立刻 revert，思考為何 break。

**重構檢查：**
- 命名清楚嗎？
- 函式長度 < 50 行？
- 有重複邏輯該抽出來嗎？
- 邊界 / 失敗 case 有對應的測試嗎？

---

### Step 4：循環 — 下一個測試

回到 Step 1，挑下一個 `test_xxx(): pass`：

```
RED → GREEN → REFACTOR → RED（下一個） → GREEN → REFACTOR → ...
```

完成順序建議：

1. **Happy path 第一個**（最樂觀的主流程）
2. **邊界 case**（短 / 長 / 空）
3. **失敗 case**（API 掛 / auth 錯）
4. **參數化 case**（多語言 / 多輸入）

---

### Step 5：確認該 user story 全綠燈

跑全套：

```bash
pytest tests/unit/test_summarizer.py -v --cov=app.summarizer --cov-report=term-missing
```

確認：

- [ ] 該 user story 的所有測試全綠
- [ ] Coverage ≥ 80%
- [ ] BDD scenario（`tests/features/*.feature`）也跑得起來
- [ ] 沒有 skip / xfail 殘留

完成 → 跑 `/verify` 做總體驗證，再跑 `/sync-it` 同步文件，最後 `/commit-msg` 生 commit。

---

## 🤝 與 `/explain-code` 的連動（學員卡關時）

TDD 過程使用者常會問：
- 「為什麼這樣寫？」
- 「這段 code 在幹嘛？」
- 「我看不懂這個函式」
- 「Refactor 後變得更複雜了？」

**這時主動建議 `/explain-code`**（不是繼續硬解釋）：

> 你問「為什麼這樣寫」 — 與其我用一段話解釋，建議跑 `/explain-code @app/summarizer.py`。
>
> 它會用「架構師視角 + 紅綠燈訊號 + 導師教學」幫你看懂這段 code 的設計意圖、命名了哪些常見模式、未來可能怎麼演化。比我隨手解釋 systematic。
>
> 看完 `/explain-code` 後回來繼續 `/tdd-cycle` 寫下一個測試。

`/explain-code` 是「中斷工具」 — 用完回到 TDD 主線，不影響進度。

---

## 📝 Issue Logging — 寫入 `tasks/known-issues.md`

跑 TDD 過程常會「**附帶發現**」一些 issue：寫測試時注意到別的 function 有邊界沒處理、發現一個現有 function 命名怪、看到 dead code⋯⋯。

**這些不在當前 task 範圍 → 不要順手修**（會偏離 sprint goal），但**也不能假裝沒看到**（會忘記、累積技術債）。

### 觸發 Issue Logging 的情境

- 寫測試時發現「**另一個 function 也有 bug**」（不在當前 user story 範圍）
- 寫實作時看到「**這段命名混亂 / 重複邏輯 / dead code**」
- Mock 邊界時發現「**真實 API 行為與文件不符**」（但這不是本 task 要修）

### 主動建議的話術

> 我寫 `test_summarize_with_empty_string` 時注意到 `_validate_input()` 對純空白字串（`"   "`）也沒處理 — 這不在 T-102 範圍，但是個真的 bug。
>
> 要不要先記到 `tasks/known-issues.md` 當作 ISSUE-NNN？格式照那邊既有的範本（發現日 / 影響範圍 / 嚴重度 / 重現步驟 / 延後原因）。等 sprint retro 再決定排哪 sprint 修。

### 寫入要求

依 `tasks/known-issues.md` 既有格式寫，9 個欄位都要填：
- 發現日（today）/ 影響範圍 / 嚴重度（Critical/High/Medium/Low）/ 重現步驟 / 預期 / 實際 / 暫時對策 / 修法草案 / 延後原因 / 重評估時機

**鐵律**：Critical 嚴重度**不能**進 known-issues — 當下停下處理（會壞主流程 / 有資料風險 / 有安全漏洞的事不能延後）。

---

## 鐵律

1. **永遠先寫測試**。先寫 code 再補測試 = test-last，不算 TDD
2. **GREEN 階段只寫剛好夠用的程式**（hardcode 都可以）
3. **REFACTOR 階段不改測試行為**（測試是合約）
4. **每個 cycle 跑一次測試**（不要寫完三個測試才跑）
5. **連續紅燈 > 5 分鐘 → 停下重新思考**（不要硬幹）
6. **mock 只 mock 邊界**（API / DB），不 mock 你正在測的對象

---

## 觸發範例

使用者：「實作 US-001 的摘要功能」

AI（你）：
> 跑 `/tdd-cycle` 紅綠燈，開始。
>
> **Step 0 確認前置：**
> - ✅ `docs/PRD.md` US-001 已定義
> - ✅ `tests/features/summarize.feature` Scenario 1 已寫
> - ✅ `tests/unit/test_summarizer.py` 有 4 個測試骨架
>
> **Step 1 RED：** 我把第一個測試 `test_summarize_with_valid_500_word_article_returns_100_word_summary` 寫實⋯⋯
>
> ```python
> [實際的測試 code]
> ```
>
> 跑 `pytest tests/unit/test_summarizer.py::test_xxx -v` → 紅燈 ✅（預期，因 Summarizer 還沒實作）
>
> **Step 2 GREEN：** 寫最少的實作⋯⋯
>
> [繼續]

---

## 與其他 skill 的關係

```
/spec-it    ─→ 產出 BDD + test 骨架
   ▼
/tdd-cycle（這個）  ─→ 寫實作
   ▼
/verify     ─→ 全套驗證
   ▼
/sync-it    ─→ 同步文件
   ▼
/commit-msg ─→ 生 commit
```
