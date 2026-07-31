"""API 契約層 —— 輸入驗證、錯誤形狀、授權檢查。

刻意跟框架解耦：這裡是純 Python，可以接到 FastAPI / Flask / Django，
也可以直接跑測試。**驗證邏輯不該綁在某個框架上。**

三個設計決定：
  ① 驗證在**邊界**做一次，不是散在各處 if
  ② 錯誤回應有**固定結構**，且絕不吐 stack trace 給使用者
  ③ 每個資源存取都檢查**歸屬**（防 IDOR —— 換個 id 就看到別人資料）

對應 skill：/spec-it（定契約）、/sec-scan（第 ④ 維度）
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

# ---------------------------------------------------------------- 錯誤形狀


class ApiError(Exception):
    """所有對外錯誤的基底。

    對外訊息與對內細節分開：
      - message : 給使用者看的，不含任何內部資訊
      - detail  : 只進 log，永遠不回傳給呼叫端
    """

    status = 500
    code = "internal_error"

    def __init__(self, message: str, *, detail: str = "", field: str = "") -> None:
        super().__init__(message)
        self.message = message
        self.detail = detail
        self.field = field

    def to_response(self) -> dict:
        body: dict[str, Any] = {"error": {"code": self.code, "message": self.message}}
        if self.field:
            body["error"]["field"] = self.field
        return body


class ValidationError(ApiError):
    status = 400
    code = "validation_error"


class UnauthorizedError(ApiError):
    status = 401
    code = "unauthorized"


class ForbiddenError(ApiError):
    status = 403
    code = "forbidden"


class NotFoundError(ApiError):
    status = 404
    code = "not_found"


# ---------------------------------------------------------------- 輸入驗證


@dataclass
class Field:
    name: str
    type: type
    required: bool = True
    min_len: int | None = None
    max_len: int | None = None
    choices: tuple | None = None


@dataclass
class Schema:
    fields: list[Field] = field(default_factory=list)

    def validate(self, payload: dict | None) -> dict:
        """在邊界驗證一次，之後下游可以信任資料。

        丟出第一個錯誤就停 —— 一次回報一個問題，比一次丟五個好處理。
        """
        if payload is None:
            raise ValidationError("請求內容不可為空")

        known = {f.name for f in self.fields}
        # 未知欄位一律拒絕，不要靜默忽略。
        # 靜默忽略會讓打錯欄位名的呼叫端以為成功了。
        for key in payload:
            if key not in known:
                raise ValidationError(f"不認得的欄位：{key}", field=key)

        clean: dict[str, Any] = {}
        for f in self.fields:
            if f.name not in payload:
                if f.required:
                    raise ValidationError(f"缺少必要欄位：{f.name}", field=f.name)
                continue

            value = payload[f.name]
            if not isinstance(value, f.type):
                raise ValidationError(
                    f"{f.name} 型別不符，應為 {f.type.__name__}", field=f.name
                )
            if f.min_len is not None and len(value) < f.min_len:
                raise ValidationError(f"{f.name} 至少需要 {f.min_len} 個字元", field=f.name)
            if f.max_len is not None and len(value) > f.max_len:
                raise ValidationError(f"{f.name} 不可超過 {f.max_len} 個字元", field=f.name)
            if f.choices is not None and value not in f.choices:
                raise ValidationError(
                    f"{f.name} 必須是 {'、'.join(map(str, f.choices))} 之一", field=f.name
                )
            clean[f.name] = value
        return clean


# ---------------------------------------------------------------- 授權


def require_owner(resource: dict | None, actor_id: str, *, owner_key: str = "owner_id"):
    """每個資源存取都檢查歸屬 —— 這是防 IDOR 的唯一正確做法。

    UI 上藏起來不算數。「換個 id 就能看到別人資料」是最常見也最常漏的漏洞。

    刻意的設計：資源不存在與無權存取**都回 404**。
    回 403 等於告訴攻擊者「這個 id 是存在的」，那本身就是資訊洩漏。
    """
    if resource is None:
        raise NotFoundError("找不到指定的資料")
    if resource.get(owner_key) != actor_id:
        raise NotFoundError("找不到指定的資料")
    return resource


# ---------------------------------------------------------------- 端點包裝


def endpoint(
    schema: Schema | None = None,
) -> Callable[[Callable], Callable]:
    """把處理函式包成「驗證 → 執行 → 統一錯誤形狀」。

    用法：
        @endpoint(schema=Schema([Field("currency", str, choices=("USD","JPY"))]))
        def get_rate(data, actor_id): ...
    """

    def decorator(handler: Callable) -> Callable:
        def wrapped(payload: dict | None = None, actor_id: str = "") -> tuple[int, dict]:
            try:
                data = schema.validate(payload) if schema else (payload or {})
                result = handler(data, actor_id)
                return 200, result
            except ApiError as exc:
                # detail 只進 log，不回傳。絕不把 stack trace 給使用者。
                return exc.status, exc.to_response()
            except Exception as exc:  # noqa: BLE001
                # 未預期的錯誤：對外只回通用訊息，細節留在伺服器端。
                internal = ApiError("伺服器發生錯誤，請稍後再試", detail=repr(exc))
                return internal.status, internal.to_response()

        wrapped.__name__ = handler.__name__
        return wrapped

    return decorator
