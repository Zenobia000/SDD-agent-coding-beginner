"""api 積木的測試 —— 每個測試對應一個真實的漏洞或壞習慣。"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from contract import (  # noqa: E402
    Field,
    NotFoundError,
    Schema,
    endpoint,
    require_owner,
)

RATE_SCHEMA = Schema(
    [
        Field("currency", str, choices=("USD", "JPY", "EUR")),
        Field("note", str, required=False, max_len=20),
    ]
)


# ---------------------------------------------------------------- 輸入驗證


def test_missing_required_field_returns_400():
    @endpoint(schema=RATE_SCHEMA)
    def handler(data, actor_id):
        return {"ok": True}

    status, body = handler({})
    assert status == 400
    assert body["error"]["field"] == "currency"


def test_unknown_field_is_rejected_not_ignored():
    """未知欄位要拒絕，不要靜默忽略。

    靜默忽略會讓打錯欄位名的呼叫端以為成功了 —— 這種 bug 最難查。
    """
    @endpoint(schema=RATE_SCHEMA)
    def handler(data, actor_id):
        return {"ok": True}

    status, body = handler({"currency": "USD", "currncy": "JPY"})
    assert status == 400
    assert "currncy" in body["error"]["message"]


def test_wrong_type_returns_400():
    @endpoint(schema=RATE_SCHEMA)
    def handler(data, actor_id):
        return {"ok": True}

    status, _ = handler({"currency": 123})
    assert status == 400


def test_value_outside_choices_returns_400():
    @endpoint(schema=RATE_SCHEMA)
    def handler(data, actor_id):
        return {"ok": True}

    status, _ = handler({"currency": "XXX"})
    assert status == 400


def test_optional_field_can_be_omitted():
    @endpoint(schema=RATE_SCHEMA)
    def handler(data, actor_id):
        return {"got": data}

    status, body = handler({"currency": "USD"})
    assert status == 200
    assert "note" not in body["got"]


# ---------------------------------------------------------------- 錯誤形狀


def test_unexpected_exception_does_not_leak_internals():
    """絕不把 stack trace 或內部訊息回傳給使用者。

    錯誤訊息洩漏是 OWASP 的常見項目，也是攻擊者最愛的偵察來源。
    """
    @endpoint()
    def handler(data, actor_id):
        raise RuntimeError("psycopg2 connection to 10.0.3.7:5432 failed, user=admin")

    status, body = handler({})
    assert status == 500
    assert "10.0.3.7" not in str(body)
    assert "psycopg2" not in str(body)
    assert body["error"]["message"] == "伺服器發生錯誤，請稍後再試"


def test_error_shape_is_stable():
    """錯誤結構固定，呼叫端才寫得出處理邏輯。"""
    @endpoint(schema=RATE_SCHEMA)
    def handler(data, actor_id):
        return {}

    _, body = handler({})
    assert set(body) == {"error"}
    assert {"code", "message"} <= set(body["error"])


# ---------------------------------------------------------------- 授權（IDOR）


def test_other_users_resource_is_not_accessible():
    """換個 id 就能看別人資料 = IDOR。最常見也最常漏的漏洞。"""
    resource = {"id": "1002", "owner_id": "bob", "secret": "bob 的資料"}
    with pytest.raises(NotFoundError):
        require_owner(resource, actor_id="alice")


def test_owner_can_access_own_resource():
    resource = {"id": "1001", "owner_id": "alice"}
    assert require_owner(resource, actor_id="alice") is resource


def test_missing_and_forbidden_are_indistinguishable():
    """資源不存在與無權存取都回 404。

    回 403 等於告訴攻擊者「這個 id 存在」—— 那本身就是資訊洩漏，
    可以拿來列舉有效 id。
    """
    with pytest.raises(NotFoundError) as missing:
        require_owner(None, actor_id="alice")
    with pytest.raises(NotFoundError) as forbidden:
        require_owner({"owner_id": "bob"}, actor_id="alice")
    assert str(missing.value) == str(forbidden.value)


# ---------------------------------------------------------------- 正常路徑


def test_valid_request_reaches_handler_with_clean_data():
    @endpoint(schema=RATE_SCHEMA)
    def handler(data, actor_id):
        return {"currency": data["currency"], "actor": actor_id}

    status, body = handler({"currency": "JPY"}, actor_id="alice")
    assert status == 200
    assert body == {"currency": "JPY", "actor": "alice"}
