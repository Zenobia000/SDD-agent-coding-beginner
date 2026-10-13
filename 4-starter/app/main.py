"""FastAPI 進入點。啟動：uvicorn app.main:create_app --factory --reload"""

import sqlite3
from collections.abc import Iterator

from fastapi import Depends, FastAPI, Request

from app.config import Settings, load_settings
from app.db import connect, init_db
from app.llm import LLMClient, build_llm


def get_db(request: Request) -> Iterator[sqlite3.Connection]:
    """每個 request 一條連線，用完關掉。在路由函式參數寫 db=Depends(get_db) 取得。"""
    conn = connect(request.app.state.settings.database_path)
    try:
        yield conn
    finally:
        conn.close()


def create_app(settings: Settings | None = None, llm: LLMClient | None = None) -> FastAPI:
    settings = settings or load_settings()

    conn = connect(settings.database_path)
    try:
        init_db(conn)
    finally:
        conn.close()

    app = FastAPI(title="LeaveBot")
    app.state.settings = settings
    app.state.llm = llm if llm is not None else build_llm(settings)

    @app.get("/health")
    def health(db: sqlite3.Connection = Depends(get_db)) -> dict[str, str]:
        db.execute("SELECT 1").fetchone()
        return {"status": "ok", "database": "ok", "llm_provider": settings.llm_provider}

    # 你的 API 從這裡往下加，或拆到 app/ 底下的其他模組再 include 進來。

    return app
