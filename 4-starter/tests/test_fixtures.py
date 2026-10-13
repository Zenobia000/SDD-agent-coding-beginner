"""eval 起始集的格式檢查。不檢查 AI，只確保「標準答案」本身沒有寫錯。"""

import json
from datetime import date, timedelta
from pathlib import Path

import pytest

FIXTURE = Path(__file__).parent.parent / "fixtures" / "leave-sentences.jsonl"
PERIODS = {"full", "am", "pm"}
LEAVE_TYPES = {"annual", "personal", "sick", "menstrual", "marriage", "bereavement", None}


def _load():
    lines = FIXTURE.read_text(encoding="utf-8").splitlines()
    return [json.loads(line) for line in lines if line.strip()]


CASES = _load()


def _workdays(start: date, end: date) -> int:
    days = (end - start).days + 1
    return sum(1 for i in range(days) if (start + timedelta(i)).weekday() < 5)


def test_has_at_least_30_cases():
    assert len(CASES) >= 30


def test_ids_are_unique():
    ids = [c["id"] for c in CASES]
    assert len(ids) == len(set(ids))


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_case_shape(case):
    assert set(case) >= {"id", "today", "sentence", "expected", "clarify", "tags"}
    date.fromisoformat(case["today"])
    assert case["sentence"].strip()
    assert isinstance(case["tags"], list)
    if case["clarify"]:
        assert case["expected"] == [], "要追問的句子不該有預期假單"
    else:
        assert case["expected"], "不追問的句子至少要有一筆預期假單"


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_expected_requests_are_consistent(case):
    today = date.fromisoformat(case["today"])
    for req in case["expected"]:
        start = date.fromisoformat(req["start_date"])
        end = date.fromisoformat(req["end_date"])
        assert start <= end
        assert req["period"] in PERIODS
        assert req["leave_type"] in LEAVE_TYPES
        assert start.weekday() < 5 and end.weekday() < 5, "起訖日不該落在週末"
        if req["period"] == "full":
            assert req["days"] == _workdays(start, end)
        else:
            assert start == end and req["days"] == 0.5
        if "past" not in case["tags"]:
            assert start >= today
