# Test Cases Template (TDD / Unit Test)

> **Layer 3 spec（行為層）— 單元級別的可執行規格**
> 大廠對標：**AAA pattern**（Arrange-Act-Assert，Microsoft / Roy Osherove）+ **Test Pyramid**（Google testing on toilet）+ **F.I.R.S.T.** 原則（Robert C. Martin）
> 寫作時機：寫程式前先寫測試（TDD red-green-refactor）。
> 觸發 skill：`/tdd`

---

## AAA Pattern（每個測試都要長這樣）

```python
def test_summarize_success_returns_100_word_chinese():
    # Arrange — 準備
    article = load_fixture("article_500_words.en.txt")
    api_key = "test_key"
    summarizer = Summarizer(api_key=api_key)

    # Act — 執行
    result = summarizer.summarize(article, target_lang="zh-TW", max_words=100)

    # Assert — 驗證
    assert result.success is True
    assert 80 <= result.word_count <= 120
    assert result.language == "zh-TW"
```

**為什麼 AAA？** 視覺上一眼分辨「準備→動作→檢查」，AI 與人類都好讀。

---

## F.I.R.S.T. 原則（Bob Martin）

每個測試都該符合：

| 字母 | 意思 | 落實 |
|---|---|---|
| **F** | Fast | 單元測試 < 100ms；整體 suite < 10s |
| **I** | Independent | 任意順序執行結果一樣 |
| **R** | Repeatable | 跑 100 次結果都一樣（不依賴時間 / 網路） |
| **S** | Self-Validating | 自動判定 pass/fail，不需要人眼看 |
| **T** | Timely | 寫在程式之前（TDD），不是事後補 |

---

## Test Pyramid（採 Google 推薦比例）

```
        /\
       /  \      E2E（5%）       — 整個流程跑得起來
      /────\
     /      \    Integration（15%）— 模組間整合
    /────────\
   /          \  Unit（80%）       — 單一函式 / 元件
  ────────────
```

**Solo 專案實踐：**
- Unit test 寫到 **80% coverage**
- Integration test 寫 **主流程 + 1-2 個關鍵分支**
- E2E test 寫 **最重要的 1-2 個 user journey**

---

## 命名慣例（採 Roy Osherove `MethodName_Scenario_ExpectedBehavior`）

```python
# ❌ 太模糊
def test_summarize():
def test_summarize_works():
def test_1():

# ✅ 描述性
def test_summarize_with_valid_input_returns_summary():
def test_summarize_with_empty_string_raises_validation_error():
def test_summarize_when_api_fails_returns_fallback_message():
```

格式：`test_<功能>_<情境>_<預期結果>`

---

## Test Suite 結構

```
tests/
├── unit/                          # 80% 覆蓋
│   ├── test_summarizer.py
│   ├── test_validator.py
│   └── test_api_client.py
├── integration/                   # 主流程 + 關鍵分支
│   ├── test_summarize_flow.py
│   └── test_history_persistence.py
├── e2e/                           # 1-2 個 user journey
│   ├── test_main_journey.py
│   └── test_error_recovery.py
├── features/                      # BDD scenarios（Gherkin）
│   ├── summarize.feature
│   └── history.feature
└── fixtures/                      # 共用測試資料
    ├── article_500_words.en.txt
    └── article_too_long.en.txt
```

---

## 標準 Test Case 範本

```python
"""
Test ID:        TC-001
User Story:     US-001
Feature:        英文新聞摘要
Layer:          Unit
Priority:       P0
Author:         <name>
Created:        YYYY-MM-DD
"""

import pytest
from app.summarizer import Summarizer
from app.exceptions import ValidationError, APIError


class TestSummarizer:
    """Test cases for app.summarizer.Summarizer"""

    # =========================================================================
    # Happy path
    # =========================================================================

    def test_summarize_with_valid_500_word_article_returns_100_word_summary(self):
        # Arrange
        article = "..." * 500
        summarizer = Summarizer(api_key="test_key")

        # Act
        result = summarizer.summarize(article)

        # Assert
        assert result.success is True
        assert 80 <= result.word_count <= 120

    # =========================================================================
    # Edge cases
    # =========================================================================

    def test_summarize_with_empty_string_raises_validation_error(self):
        summarizer = Summarizer(api_key="test_key")
        with pytest.raises(ValidationError, match="content cannot be empty"):
            summarizer.summarize("")

    def test_summarize_with_too_long_article_raises_validation_error(self):
        summarizer = Summarizer(api_key="test_key")
        with pytest.raises(ValidationError, match="content exceeds 10000 chars"):
            summarizer.summarize("x" * 10001)

    # =========================================================================
    # Failure cases
    # =========================================================================

    def test_summarize_when_api_returns_503_raises_api_error(self, mock_api):
        mock_api.return_value.status_code = 503
        summarizer = Summarizer(api_key="test_key")

        with pytest.raises(APIError, match="service unavailable"):
            summarizer.summarize("valid article" * 50)

    def test_summarize_with_invalid_api_key_raises_auth_error(self, mock_api):
        mock_api.return_value.status_code = 401
        summarizer = Summarizer(api_key="invalid")

        with pytest.raises(APIError, match="authentication"):
            summarizer.summarize("valid article" * 50)

    # =========================================================================
    # Parametrized cases
    # =========================================================================

    @pytest.mark.parametrize("target_lang,expected_lang", [
        ("zh-TW", "zh-TW"),
        ("zh-CN", "zh-CN"),
        ("ja", "ja"),
    ])
    def test_summarize_with_different_target_languages(self, target_lang, expected_lang):
        summarizer = Summarizer(api_key="test_key")
        result = summarizer.summarize("article" * 100, target_lang=target_lang)
        assert result.language == expected_lang
```

---

## TDD 三步驟（Kent Beck）

每寫一個功能跑這 3 步：

```
1. RED      寫一個失敗的測試（描述你「想要」的行為）
              ↓ pytest 紅燈 ❌
2. GREEN    寫最少的程式碼讓它通過
              ↓ pytest 綠燈 ✅
3. REFACTOR 重構 — 把醜的地方修整齊（測試還是綠燈）
              ↓ pytest 綠燈 ✅
```

**重點**：**先寫測試**。如果你先寫程式再補測試，那叫「測試後寫」（test-last），不叫 TDD。

---

## Mock / Stub / Fake 使用時機

| 工具 | 用在 | 範例 |
|---|---|---|
| **Mock** | 驗證「有沒有被呼叫」 | `mock_api.assert_called_with(...)` |
| **Stub** | 控制「回傳什麼」 | `mock_api.return_value = {...}` |
| **Fake** | 用簡化版替代真實實作 | `FakeDatabase` 用 dict 代 SQL |

**鐵律：**
- 不 mock 你正在測的對象（會變成測試自己）
- 不 mock 簡單的資料物件（直接造資料更清楚）
- E2E test 不 mock（要打到真實服務）

---

## Coverage 目標

| 層 | 目標 | 工具 |
|---|---|---|
| Unit | 80%+ | pytest-cov（python）/ vitest（JS） |
| Integration | 主流程 100% | 同上 |
| E2E | 關鍵 user journey 100% | Playwright / Cypress |

**Coverage 不是越高越好** — 95% 以上常是 over-testing。80% + 主流程 100% 是最佳投報比。

---

## 寫作檢查清單

- [ ] 每個 test 用 AAA pattern（視覺上有三段）
- [ ] 命名符合 `test_功能_情境_預期`
- [ ] 主流程 + 邊界 + 失敗各至少 1 個
- [ ] 沒有依賴執行順序的測試
- [ ] 沒有依賴真實時間 / 真實網路的測試（或明確標記 `@pytest.mark.slow`）
- [ ] Mock 只 mock 邊界（API / DB），不 mock 內部邏輯
- [ ] 對應 user story / API endpoint ID 在 docstring 標明
- [ ] Coverage ≥ 80%
