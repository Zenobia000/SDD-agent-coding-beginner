"""etl 積木的測試 —— 重點全部在 Validate 那一段。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from pipeline import (  # noqa: E402
    Result,
    extract,
    normalize_number,
    run,
    transform,
    validate,
)


def ok_source(value):
    return lambda: value


def bad_source():
    raise RuntimeError("boom")


def simple_mapper(name, payload):
    return [{"currency": c, "rate": r, "source": name} for c, r in payload.items()]


# ---------------------------------------------------------------- Extract


def test_single_source_failure_does_not_kill_batch():
    """單筆隔離：一個來源掛掉，其他照常。"""
    raw, missing = extract({"a": ok_source({"USD": 31.2}), "b": bad_source})
    assert set(raw) == {"a"}
    assert missing == ["b"]


def test_all_sources_failure_does_not_write():
    """全失敗時不寫入，保留上一版。"""
    written = []
    res = run({"a": bad_source}, simple_mapper, written.append)
    assert res.ok is False
    assert written == []              # ← 最重要的斷言
    assert "所有來源都失敗" in res.reason


# ---------------------------------------------------------------- Transform


def test_normalize_strips_thousand_separator():
    assert normalize_number("31,245.50") == 31245.50


def test_normalize_converts_fullwidth_digits():
    """全形數字是真實會遇到的格式（部分亞洲網站）。"""
    assert normalize_number("３１．２４") == 31.24


def test_transform_isolates_bad_row():
    """轉不動的單筆隔離，不炸掉整批。"""
    def flaky(name, payload):
        if name == "bad":
            raise ValueError("格式不認得")
        return simple_mapper(name, payload)

    rows = transform({"a": {"USD": 31.2}, "bad": {}}, flaky)
    assert len(rows) == 1


# ---------------------------------------------------------------- Validate ★


def test_validate_rejects_empty_batch():
    assert validate([]).ok is False


def test_validate_skips_count_check_on_cold_start():
    """冷啟動：prev_count=0 時不做筆數比對。

    0 → N 的變動率是無限大，不跳過的話首次執行永遠會被擋。
    這是所有「跟上次比」邏輯的共同盲點。
    """
    rows = [{"currency": "USD", "rate": 31.2, "source": "a"}]
    assert validate(rows, prev_count=0).ok is True


def test_validate_flags_large_count_change():
    rows = [{"currency": "USD", "rate": 31.2, "source": "a"}]
    v = validate(rows, prev_count=10)
    assert v.ok is False
    assert any("筆數變動" in f for f in v.failures)


def test_validate_flags_empty_required_field():
    rows = [{"currency": "USD", "rate": None, "source": "a"}]
    v = validate(rows)
    assert v.ok is False
    assert any("rate 為空" in f for f in v.failures)


def test_validate_flags_out_of_range():
    rows = [{"currency": "USD", "rate": 9999.0, "source": "a"}]
    v = validate(rows, numeric_ranges={"rate": (20.0, 40.0)})
    assert v.ok is False
    assert any("超出範圍" in f for f in v.failures)


def test_validate_flags_duplicate_key():
    rows = [
        {"currency": "USD", "rate": 31.2, "source": "a"},
        {"currency": "USD", "rate": 31.3, "source": "b"},
    ]
    v = validate(rows)
    assert v.ok is False
    assert any("重複" in f for f in v.failures)


# ---------------------------------------------------------------- 主流程


def test_run_does_not_load_when_validation_fails():
    """這是整塊積木最重要的一條測試。

    驗證不過就不進 Load —— 這一行是「可信管線」和
    「自動產生髒資料機」的唯一差別。
    """
    written = []
    res = run(
        {"a": ok_source({"USD": 9999.0})},
        simple_mapper,
        written.append,
        numeric_ranges={"rate": (20.0, 40.0)},
    )
    assert res.ok is False
    assert written == []              # ← 沒有任何東西被寫進去
    assert "驗證未通過" in res.reason


def test_run_loads_when_all_checks_pass():
    written = []
    res = run({"a": ok_source({"USD": 31.2})}, simple_mapper, written.append)
    assert res.ok is True
    assert len(written) == 1
    assert res.missing_sources == []


def test_run_reports_missing_sources_but_still_loads():
    """部分來源掛掉時，其餘照常寫入並註明缺哪個。"""
    written = []
    res = run(
        {"a": ok_source({"USD": 31.2}), "b": bad_source},
        simple_mapper,
        written.append,
    )
    assert res.ok is True
    assert res.missing_sources == ["b"]
    assert len(written) == 1
