"""db 積木的測試 —— 每個測試釘住一個「最常見錯誤」的防護。"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from db import Database, from_storage, to_storage  # noqa: E402


@pytest.fixture
def db(tmp_path):
    d = Database(tmp_path / "test.db")
    d.migrate()
    return d


def test_migrate_is_idempotent(tmp_path):
    """重跑 migrate 不會重複套用 —— 部署腳本可以無腦重跑。"""
    d = Database(tmp_path / "x.db")
    first = d.migrate()
    second = d.migrate()
    assert first == ["001_init.sql"]
    assert second == []


def test_money_stored_as_integer_not_float(db):
    """③ 用整數存最小單位。浮點數會有 0.1+0.2!=0.3 的誤差。"""
    db.upsert_rate(run_date="2026-07-31", currency="USD", rate=31.2450, source="a")
    rows = db.get_rates("2026-07-31")
    assert rows[0]["rate"] == 31.2450


def test_truncate_does_not_round_up():
    """無條件捨去，不是四捨五入 —— 這是金融資料的常見 spec。"""
    assert to_storage(31.24505) == 312450          # 不是 312451
    assert from_storage(312450) == 31.2450


def test_upsert_same_day_is_idempotent(db):
    """⑤ 冪等性：同一天同一幣別重跑不產生重複列。

    這是 ETL 的生死線。重跑會炸的管線你不敢重跑，出事就沒救。
    """
    for _ in range(3):
        db.upsert_rate(run_date="2026-07-31", currency="USD", rate=31.24, source="a")
    assert len(db.get_rates("2026-07-31")) == 1


def test_upsert_updates_value_on_conflict(db):
    """冪等不等於「忽略後續寫入」—— 後寫的值要生效。"""
    db.upsert_rate(run_date="2026-07-31", currency="USD", rate=31.00, source="a")
    db.upsert_rate(run_date="2026-07-31", currency="USD", rate=32.00, source="b")
    rows = db.get_rates("2026-07-31")
    assert len(rows) == 1
    assert rows[0]["rate"] == 32.00
    assert rows[0]["source"] == "b"


def test_delta_can_be_null_on_cold_start(db):
    """冷啟動：首次執行沒有「昨日」可比，delta_1d 必須可空。

    冷啟動是所有「跟上次比」邏輯的共同盲點。
    """
    db.upsert_rate(run_date="2026-07-31", currency="USD", rate=31.24, source="a")
    assert db.get_rates("2026-07-31")[0]["delta_1d"] is None


def test_soft_delete_hides_row_but_keeps_data(db):
    """④ 軟刪除：查不到，但資料還在（誤刪可還原）。"""
    db.upsert_rate(run_date="2026-07-31", currency="USD", rate=31.24, source="a")
    db.soft_delete(run_date="2026-07-31", currency="USD")
    assert db.get_rates("2026-07-31") == []
    with db.connect() as conn:
        row = conn.execute("SELECT deleted_at FROM rates").fetchone()
    assert row["deleted_at"] is not None


def test_created_at_is_always_set(db):
    """② 沒有 created_at 的表，出事時無法回溯。"""
    db.upsert_rate(run_date="2026-07-31", currency="USD", rate=31.24, source="a")
    with db.connect() as conn:
        row = conn.execute("SELECT created_at FROM rates").fetchone()
    assert row["created_at"].endswith("+00:00")     # UTC
