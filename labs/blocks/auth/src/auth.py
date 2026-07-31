"""認證 —— 密碼雜湊、session、權限檢查。

純標準庫實作，沒有外部依賴。**生產環境建議改用 argon2**
（`pip install argon2-cffi`），但這裡用 stdlib 的 scrypt 讓你能直接跑。

三個設計決定：
  ① 密碼**永遠不可逆** —— 用 scrypt，不是 MD5/SHA1，也不是加密
  ② session **一定要有過期時間**
  ③ 比對時用**常數時間**，避免時序攻擊

對應 skill：/sec-scan（第 ④ 維度 認證與授權）
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import os
import secrets
import time
from dataclasses import dataclass

# scrypt 參數。n 越大越慢也越安全；2**14 在一般機器上約 50-100ms。
# 太快 = 攻擊者也能快速暴力破解。**慢是刻意的。**
_SCRYPT_N = 2**14
_SCRYPT_R = 8
_SCRYPT_P = 1
_KEY_LEN = 32
_SALT_LEN = 16

SESSION_TTL_SECONDS = 60 * 60 * 8      # 8 小時


# ---------------------------------------------------------------- 密碼


def hash_password(password: str) -> str:
    """回傳 `scrypt$<salt_b64>$<hash_b64>`。

    每次呼叫的 salt 都不同 —— 所以同樣的密碼會得到不同的雜湊。
    這是**正確**的：它讓彩虹表失效。
    """
    if len(password) < 8:
        raise ValueError("密碼至少 8 個字元")
    salt = os.urandom(_SALT_LEN)
    digest = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=_SCRYPT_N,
        r=_SCRYPT_R,
        p=_SCRYPT_P,
        dklen=_KEY_LEN,
    )
    return "scrypt${}${}".format(
        base64.b64encode(salt).decode(), base64.b64encode(digest).decode()
    )


def verify_password(password: str, stored: str) -> bool:
    """常數時間比對。

    用 `==` 比對雜湊會洩漏「前幾個位元組對了」的資訊，
    攻擊者可以逐位元組試出正確值（時序攻擊）。
    """
    try:
        algo, salt_b64, hash_b64 = stored.split("$")
        if algo != "scrypt":
            return False
        salt = base64.b64decode(salt_b64)
        expected = base64.b64decode(hash_b64)
    except (ValueError, TypeError):
        return False

    actual = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=_SCRYPT_N,
        r=_SCRYPT_R,
        p=_SCRYPT_P,
        dklen=len(expected),
    )
    return hmac.compare_digest(actual, expected)


# ---------------------------------------------------------------- Session


@dataclass
class Session:
    token: str
    user_id: str
    expires_at: float

    @property
    def expired(self) -> bool:
        return time.time() >= self.expires_at


class SessionStore:
    """記憶體版 session store。正式環境換成 Redis / DB，介面不變。"""

    def __init__(self, ttl: int = SESSION_TTL_SECONDS) -> None:
        self._ttl = ttl
        self._sessions: dict[str, Session] = {}

    def create(self, user_id: str, *, now: float | None = None) -> Session:
        # token 用 secrets 而不是 random —— random 是可預測的偽隨機
        token = secrets.token_urlsafe(32)
        s = Session(token=token, user_id=user_id, expires_at=(now or time.time()) + self._ttl)
        self._sessions[token] = s
        return s

    def get(self, token: str, *, now: float | None = None) -> Session | None:
        s = self._sessions.get(token)
        if s is None:
            return None
        if (now or time.time()) >= s.expires_at:
            # 過期就直接清掉，不要留著佔記憶體
            self._sessions.pop(token, None)
            return None
        return s

    def revoke(self, token: str) -> None:
        self._sessions.pop(token, None)

    def revoke_all_for_user(self, user_id: str) -> int:
        """改密碼、偵測到入侵時要能一次踢掉該使用者的所有 session。"""
        targets = [t for t, s in self._sessions.items() if s.user_id == user_id]
        for t in targets:
            self._sessions.pop(t, None)
        return len(targets)


# ---------------------------------------------------------------- 登入


class AuthError(Exception):
    """對外一律用同一個訊息，見 login() 的註解。"""


def login(
    username: str,
    password: str,
    *,
    users: dict[str, str],
    store: SessionStore,
    now: float | None = None,
) -> Session:
    """登入。

    **帳號不存在與密碼錯誤回同一個訊息。**
    分開回報等於提供帳號列舉的管道：攻擊者可以先確認哪些帳號存在，
    再集中火力猜那些帳號的密碼。
    """
    stored = users.get(username)

    if stored is None:
        # 即使帳號不存在也跑一次雜湊，讓回應時間一致（防時序側錄）
        verify_password(password, hash_password("dummy-password-placeholder"))
        raise AuthError("帳號或密碼錯誤")

    if not verify_password(password, stored):
        raise AuthError("帳號或密碼錯誤")

    return store.create(username, now=now)
