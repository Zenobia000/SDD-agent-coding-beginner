"""SQLite 連線。資料表由你依 2_architecture.md 寫進 schema.sql。"""

import sqlite3
from pathlib import Path

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def connect(path: str) -> sqlite3.Connection:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(conn: sqlite3.Connection, schema_path: Path = SCHEMA_PATH) -> None:
    """執行 schema.sql。裡面的 CREATE TABLE 請寫成 IF NOT EXISTS，重跑才不會壞。"""
    conn.executescript(schema_path.read_text(encoding="utf-8"))
    conn.commit()
