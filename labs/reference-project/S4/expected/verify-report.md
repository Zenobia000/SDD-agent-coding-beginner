# `/verify` 報告 — rate-digest

> 對照重點：**五個維度都真的跑過**，不是宣稱跑過。

---

## 判定

**全綠。可以進 `/sync-it`。**

---

## 五維度

| # | 維度 | 指令 | 結果 |
|---|---|---|---|
| 1 | Format | `ruff format --check .` | ✅ 12 files unchanged |
| 2 | Lint | `ruff check .` | ✅ All checks passed |
| 3 | Type | `mypy src/` | ✅ no issues in 8 files |
| 4 | Test + Coverage | `pytest --cov=src` | ✅ 14 passed, **coverage 87%** |
| 5 | Security | `pip-audit` | ✅ No known vulnerabilities |

---

## 測試明細（第 2 條判準：≥ 3 個且含邊界）

```
tests/test_fetchers.py
  ✅ test_fetch_returns_rate_for_valid_source
  ✅ test_fetch_raises_on_timeout                    ← 邊界
  ✅ test_fetch_returns_none_on_empty_response       ← 邊界
tests/test_normalize.py
  ✅ test_normalize_strips_thousand_separator        ← 邊界
  ✅ test_normalize_converts_fullwidth_digits        ← 邊界
  ✅ test_truncate_does_not_round_up                 ← 這條釘住「無條件捨去」
tests/test_pipeline.py
  ✅ test_single_source_failure_lists_missing
  ✅ test_all_sources_failure_does_not_write_db      ← 最重要的一條
  ✅ test_rerun_same_day_is_idempotent               ← 冪等性
  ... 共 14 個
```

**14 個測試，5 個是邊界 case。**

---

## 未覆蓋的部分（誠實列出）

| 檔案:行 | 為什麼沒測 |
|---|---|
| `src/cli.py:40-52` | argparse 的參數解析，測了價值低 |
| `src/db.py:88-91` | SQLite 連線失敗的分支，需要製造磁碟錯誤 |

**coverage 87%，缺的 13% 列在上面。**
不要為了衝到 100% 寫沒有斷言的測試。

---

## 測試 vs 考卷（容易混淆，這裡說清楚）

| | 這份報告 | `loop-log.md` |
|---|---|---|
| 測的是 | **不會壞**（迴歸） | **做得好**（品質） |
| 失敗代表 | 你改壞了既有行為 | 這版沒比上版好 |
| 現在的狀態 | 14 passed | 10/10 |

**兩者都要有。** 測試全綠但考卷 3/10 是很常見的狀態 ——
它表示「程式沒 bug，但做出來的東西不是使用者要的」。
