def test_health_reports_ok_and_checks_database(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok", "llm_provider": "fake"}


def test_app_exposes_llm_for_route_handlers(client, fake_llm):
    # 學員寫的 API 要從 request.app.state.llm 取得 LLM，測試時才換得成假的
    assert client.app.state.llm is fake_llm
