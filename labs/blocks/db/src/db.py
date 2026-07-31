"""SQLite 資料層 —— 最小可用實作。

這塊積木預先處理了五個最常見的 schema 錯誤（見 migrations/001_init.sql 的註解）。
對應 skill：/data-pipe

用法：
    from db import Database
    db = Database("data/app.db")
    db.migrate()
    db.upsert_rate(run_date="2026-07-31", currency="USD", rate=31.2450, source="bank-a")
"""

from __future__ import annotations

import math
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

# 金額放大倍數：用整數存最小單位，避免浮點數誤差（0.1 + 0.2 != 0.3）
SCALE = 10_000


def to_storage(value: float) -> int:
    """外部浮點數 → 內部整數。無條件捨去，不四捨五入。"""
    return math.floor(value * SCALE)


def from_storage(value: int) -> float:
    """內部整數 → 外部浮點數。"""
    return value / SCALE


def utc_now() -> str:
    """一律用 UTC。本地時間在跨時區與日光節約時會出事。"""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class Database:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def connect(self):
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        # 外鍵約束預設是關的，一定要手動開
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def migrate(self) -> list[str]:
        """依序執行 migrations/ 下未套用過的 .sql，回傳套用了哪些。"""
        applied: list[str] = []
        mig_dir = Path(__file__).parent.parent / "migrations"
        with self.connect() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS _migrations ("
                "  name TEXT PRIMARY KEY,"
                "  applied_at TEXT NOT NULL)"
            )
            done = {r["name"] for r in conn.execute("SELECT name FROM _migrations")}
            for sql_file in sorted(mig_dir.glob("*.sql")):
                if sql_file.name in done:
                    continue
                conn.executescript(sql_file.read_text(encoding="utf-8"))
                conn.execute(
                    "INSERT INTO _migrations (name, applied_at) VALUES (?, ?)",
                    (sql_file.name, utc_now()),
                )
                applied.append(sql_file.name)
        return applied

    def upsert_rate(
        self,
        *,
        run_date: str,
        currency: str,
        rate: float,
        source: str,
        delta_1d: float | None = None,
    ) -> None:
        """冪等寫入：同一天同一幣別重跑不會產生重複列。

        冪等性是 ETL 的生死線 —— 重跑會炸的管線你不敢重跑，出事就沒救。
        這裡靠 UNIQUE(run_date, currency) + ON CONFLICT 保證，不靠應用層檢查。
        """
        with self.connect() as conn:
            conn.execute(
                """
                INSERT INTO rates (run_date, currency, rate, delta_1d, source, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(run_date, currency) DO UPDATE SET
                    rate       = excluded.rate,
                    delta_1d   = excluded.delta_1d,
                    source     = excluded.source,
                    created_at = excluded.created_at
                """,
                (
                    run_date,
                    currency,
                    to_storage(rate),
                    to_storage(delta_1d) if delta_1d is not None else None,
                    source,
                    utc_now(),
                ),
            )

    def get_rates(self, run_date: str) -> list[dict]:
        """讀出某天的匯率。已軟刪除的不會出現。"""
        with self.connect() as conn:
            rows = conn.execute(
                "SELECT * FROM rates WHERE run_date = ? AND deleted_at IS NULL"
                " ORDER BY currency",
                (run_date,),
            ).fetchall()
        return [
            {
                "currency": r["currency"],
                "rate": from_storage(r["rate"]),
                "delta_1d": from_storage(r["delta_1d"]) if r["delta_1d"] is not None else None,
                "source": r["source"],
            }
            for r in rows
        ]

    def soft_delete(self, *, run_date: str, currency: str) -> None:
        """軟刪除。重要資料永遠不要硬刪 —— 誤刪不可逆。"""
        with self.connect() as conn:
            conn.execute(
                "UPDATE rates SET deleted_at = ? WHERE run_date = ? AND currency = ?",
                (utc_now(), run_date, currency),
            )
