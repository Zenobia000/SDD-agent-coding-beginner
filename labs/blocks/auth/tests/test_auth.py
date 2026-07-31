"""auth 積木的測試 —— 每條對應一個真實的攻擊手法。"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from auth import (  # noqa: E402
    AuthError,
    SessionStore,
    hash_password,
    login,
    verify_password,
)


# ---------------------------------------------------------------- 密碼


def test_password_is_not_stored_in_plaintext():
    h = hash_password("correct horse battery")
    assert "correct horse battery" not in h


def test_same_password_produces_different_hashes():
    """每次 salt 不同 —— 這讓彩虹表失效。

    如果兩次雜湊一樣，表示沒有加 salt，是嚴重錯誤。
    """
    assert hash_password("same-password-123") != hash_password("same-password-123")


def test_correct_password_verifies():
    h = hash_password("correct horse battery")
    assert verify_password("correct horse battery", h) is True


def test_wrong_password_fails():
    h = hash_password("correct horse battery")
    assert verify_password("wrong password here", h) is False


def test_short_password_rejected():
    with pytest.raises(ValueError):
        hash_password("short")


def test_malformed_stored_hash_does_not_crash():
    """壞掉的儲存值要回 False，不要拋例外。

    拋例外會變成 500，而 500 和 401 的差別會洩漏資訊。
    """
    assert verify_password("anything", "not-a-valid-hash") is False
    assert verify_password("anything", "") is False


# ---------------------------------------------------------------- Session


def test_session_token_is_unpredictable():
    store = SessionStore()
    tokens = {store.create("alice").token for _ in range(50)}
    assert len(tokens) == 50
    assert all(len(t) >= 32 for t in tokens)


def test_session_expires():
    """session 一定要有過期時間。永不過期的 session 是資產也是負債。"""
    store = SessionStore(ttl=100)
    s = store.create("alice", now=1000.0)
    assert store.get(s.token, now=1050.0) is not None      # 還沒到期
    assert store.get(s.token, now=1100.0) is None          # 剛好到期
    assert store.get(s.token, now=9999.0) is None          # 早就過期


def test_revoke_removes_session():
    store = SessionStore()
    s = store.create("alice")
    store.revoke(s.token)
    assert store.get(s.token) is None


def test_revoke_all_for_user():
    """改密碼 / 偵測到入侵時，要能一次踢掉該使用者的所有 session。"""
    store = SessionStore()
    for _ in range(3):
        store.create("alice")
    store.create("bob")
    assert store.revoke_all_for_user("alice") == 3
    assert len(store._sessions) == 1


def test_unknown_token_returns_none():
    assert SessionStore().get("made-up-token") is None


# ---------------------------------------------------------------- 登入


def test_login_succeeds_with_correct_credentials():
    users = {"alice": hash_password("alice-password-1")}
    store = SessionStore()
    s = login("alice", "alice-password-1", users=users, store=store)
    assert s.user_id == "alice"
    assert store.get(s.token) is not None


def test_unknown_user_and_wrong_password_give_same_message():
    """帳號列舉防護：兩種失敗回同一個訊息。

    分開回報「查無此帳號」和「密碼錯誤」，等於免費提供攻擊者
    一份有效帳號清單。
    """
    users = {"alice": hash_password("alice-password-1")}
    store = SessionStore()

    with pytest.raises(AuthError) as no_user:
        login("nobody", "whatever-password", users=users, store=store)
    with pytest.raises(AuthError) as bad_pw:
        login("alice", "wrong-password-x", users=users, store=store)

    assert str(no_user.value) == str(bad_pw.value) == "帳號或密碼錯誤"


def test_failed_login_creates_no_session():
    users = {"alice": hash_password("alice-password-1")}
    store = SessionStore()
    with pytest.raises(AuthError):
        login("alice", "wrong-password-x", users=users, store=store)
    assert len(store._sessions) == 0
