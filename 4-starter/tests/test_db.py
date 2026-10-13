from app.db import connect, init_db


def test_connect_creates_parent_directory(tmp_path):
    path = tmp_path / "nested" / "dir" / "app.db"

    conn = connect(str(path))
    conn.close()

    assert path.exists()


def test_rows_are_accessible_by_column_name(tmp_path):
    conn = connect(str(tmp_path / "app.db"))
    row = conn.execute("SELECT 1 AS answer").fetchone()
    conn.close()

    assert row["answer"] == 1


def test_foreign_keys_are_enforced(tmp_path):
    conn = connect(str(tmp_path / "app.db"))
    enabled = conn.execute("PRAGMA foreign_keys").fetchone()[0]
    conn.close()

    assert enabled == 1


def test_init_db_runs_schema_file(tmp_path):
    schema = tmp_path / "schema.sql"
    schema.write_text("CREATE TABLE IF NOT EXISTS sample (id INTEGER PRIMARY KEY);")
    conn = connect(str(tmp_path / "app.db"))

    init_db(conn, schema_path=schema)
    init_db(conn, schema_path=schema)  # 重跑不會壞
    tables = [r["name"] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    conn.close()

    assert "sample" in tables


def test_init_db_accepts_the_shipped_empty_schema(tmp_path):
    conn = connect(str(tmp_path / "app.db"))

    init_db(conn)  # 預設的 app/schema.sql 只有註解，要能跑
    conn.close()
