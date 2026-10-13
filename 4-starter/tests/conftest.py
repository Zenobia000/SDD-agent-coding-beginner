"""共用的測試設定：每個測試都拿到乾淨的暫存資料庫與假 LLM。"""

import pytest
from fastapi.testclient import TestClient

from app.config import Settings
from app.llm import FakeLLM
from app.main import create_app


@pytest.fixture
def settings(tmp_path) -> Settings:
    return Settings(
        database_path=str(tmp_path / "test.db"),
        llm_provider="fake",
        llm_model="",
    )


@pytest.fixture
def fake_llm() -> FakeLLM:
    return FakeLLM(responses=["{}"])


@pytest.fixture
def client(settings, fake_llm) -> TestClient:
    return TestClient(create_app(settings=settings, llm=fake_llm))
