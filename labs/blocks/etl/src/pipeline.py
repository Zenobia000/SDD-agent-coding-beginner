"""ETL 管線 —— Extract → Transform → Validate → Load。

這塊積木的重點是 **Validate 那一段**。
沒有 Validate 的管線是「自動產生髒資料機」：它會很有效率地把錯的資料
送到下游，而且不會有人發現。

對應 skill：/data-pipe
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable

# ---------------------------------------------------------------- 結果型別


@dataclass
class Verdict:
    """驗證結果。二元判準，不給分數。"""

    ok: bool
    failures: list[str] = field(default_factory=list)

    @classmethod
    def passed(cls) -> "Verdict":
        return cls(ok=True)

    @classmethod
    def failed(cls, *reasons: str) -> "Verdict":
        return cls(ok=False, failures=list(reasons))


@dataclass
class Result:
    ok: bool
    rows: list[dict] = field(default_factory=list)
    missing_sources: list[str] = field(default_factory=list)
    reason: str = ""


# ---------------------------------------------------------------- Extract


def extract(
    sources: dict[str, Callable[[], Any]],
) -> tuple[dict[str, Any], list[str]]:
    """逐一抽取。單一來源失敗不影響其他來源。

    失敗處理的原則：**單筆隔離，不要整批失敗**。
    一個來源掛掉就整條管線停擺，是最常見的脆弱設計。
    """
    got: dict[str, Any] = {}
    missing: list[str] = []
    for name, fetch in sources.items():
        try:
            got[name] = fetch()
        except Exception:
            missing.append(name)
    return got, missing


# ---------------------------------------------------------------- Transform

_THOUSAND_SEP = re.compile(r"[,\s_]")


def normalize_number(raw: str) -> float:
    """把各種寫法的數字統一成 float。

    上游一定會改格式，只是不會通知你。所以先正規化再解析，
    不要對外部來源假設格式穩定。
    """
    # 全形 → 半形（３１．２４ → 31.24）
    s = unicodedata.normalize("NFKC", str(raw)).strip()
    # 去千分位與空白
    s = _THOUSAND_SEP.sub("", s)
    return float(s)


def transform(raw: dict[str, Any], mapper: Callable[[str, Any], list[dict]]) -> list[dict]:
    """把各來源的原始格式，轉成統一的內部格式。

    轉不動的**單筆隔離**，不要讓一筆壞資料炸掉整批。
    """
    rows: list[dict] = []
    for name, payload in raw.items():
        try:
            rows.extend(mapper(name, payload))
        except Exception:
            continue
    return rows


# ---------------------------------------------------------------- Validate ★


def validate(
    rows: list[dict],
    *,
    prev_count: int = 0,
    required: Iterable[str] = ("currency", "rate", "source"),
    numeric_ranges: dict[str, tuple[float, float]] | None = None,
    unique_key: tuple[str, ...] = ("currency",),
    max_count_change: float = 0.5,
) -> Verdict:
    """四類檢查。每一條都回 pass / fail，不給分數。

    ① 筆數：跟上批比變動超過門檻要人確認
    ② 非空：關鍵欄位不可為空
    ③ 型別 / 範圍：數值在合理區間
    ④ 唯一性：主鍵沒有重複
    """
    failures: list[str] = []

    # ① 筆數
    if not rows:
        failures.append("空批次：沒有任何資料")
    elif prev_count > 0:
        change = abs(len(rows) - prev_count) / prev_count
        if change > max_count_change:
            failures.append(
                f"筆數變動 {change:.0%}（{prev_count} → {len(rows)}），"
                f"超過門檻 {max_count_change:.0%}"
            )
    # prev_count == 0 時**刻意跳過**筆數比對。
    # 冷啟動是所有「跟上次比」邏輯的共同盲點：0 → N 的變動率是無限大。

    # ② 非空
    for i, row in enumerate(rows):
        for col in required:
            if row.get(col) in (None, ""):
                failures.append(f"第 {i} 筆的 {col} 為空")

    # ③ 型別 / 範圍
    for col, (lo, hi) in (numeric_ranges or {}).items():
        for i, row in enumerate(rows):
            v = row.get(col)
            if v is None:
                continue
            if not isinstance(v, (int, float)):
                failures.append(f"第 {i} 筆的 {col} 不是數值：{v!r}")
            elif not (lo <= v <= hi):
                failures.append(f"第 {i} 筆的 {col}={v} 超出範圍 [{lo}, {hi}]")

    # ④ 唯一性
    seen: set[tuple] = set()
    for i, row in enumerate(rows):
        key = tuple(row.get(k) for k in unique_key)
        if key in seen:
            failures.append(f"第 {i} 筆的 {unique_key} 重複：{key}")
        seen.add(key)

    return Verdict.passed() if not failures else Verdict.failed(*failures)


# ---------------------------------------------------------------- Load


def load(rows: list[dict], writer: Callable[[dict], None]) -> None:
    """寫入。writer 必須是冪等的（見 db 積木的 upsert_rate）。"""
    for row in rows:
        writer(row)


# ---------------------------------------------------------------- 主流程


def run(
    sources: dict[str, Callable[[], Any]],
    mapper: Callable[[str, Any], list[dict]],
    writer: Callable[[dict], None],
    *,
    prev_count: int = 0,
    numeric_ranges: dict[str, tuple[float, float]] | None = None,
) -> Result:
    """完整跑一輪。

    關鍵在最後那個 if：**驗證不過就不進 Load**。
    這一行就是「可信管線」和「自動產生髒資料機」的唯一差別。
    """
    raw, missing = extract(sources)

    if not raw:
        return Result(ok=False, missing_sources=missing, reason="所有來源都失敗，不寫入")

    rows = transform(raw, mapper)
    verdict = validate(rows, prev_count=prev_count, numeric_ranges=numeric_ranges)

    if not verdict.ok:
        return Result(
            ok=False,
            missing_sources=missing,
            reason="驗證未通過：" + "；".join(verdict.failures),
        )

    load(rows, writer)
    return Result(ok=True, rows=rows, missing_sources=missing)
