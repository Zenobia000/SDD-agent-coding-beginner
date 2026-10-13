"""設定：從環境變數讀取，啟動時就檢查，缺東西立刻報錯。"""

import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

DEFAULT_ANTHROPIC_MODEL = "claude-opus-5-5"
SUPPORTED_PROVIDERS = ("fake", "anthropic")
_PLACEHOLDER_VALUES = ("", "changeme")


class ConfigError(ValueError):
    """設定不完整或不合法。訊息要讓學員看得懂該補什麼。"""


@dataclass(frozen=True)
class Settings:
    database_path: str
    llm_provider: str
    llm_model: str


def load_env_file(path: Path, env: Mapping[str, str]) -> dict[str, str]:
    """把 .env 的 KEY=VALUE 併進 env，回傳新的 dict；已存在的值不覆蓋。"""
    merged = dict(env)
    if not path.exists():
        return merged
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = (part.strip() for part in line.split("=", 1))
        if key and key not in merged:
            merged[key] = value
    return merged


def load_settings(env: Mapping[str, str] | None = None) -> Settings:
    source = env if env is not None else load_env_file(Path(".env"), os.environ)

    provider = source.get("LLM_PROVIDER", "fake").strip() or "fake"
    if provider not in SUPPORTED_PROVIDERS:
        raise ConfigError(
            f"LLM_PROVIDER={provider!r} 不支援，可用的值：{', '.join(SUPPORTED_PROVIDERS)}"
        )

    model = source.get("LLM_MODEL", "").strip()
    if provider == "anthropic":
        if source.get("ANTHROPIC_API_KEY", "").strip() in _PLACEHOLDER_VALUES:
            raise ConfigError("LLM_PROVIDER=anthropic 需要在 .env 或環境變數設定 ANTHROPIC_API_KEY")
        model = model or DEFAULT_ANTHROPIC_MODEL

    return Settings(
        database_path=source.get("DATABASE_PATH", "").strip() or "data/leavebot.db",
        llm_provider=provider,
        llm_model=model,
    )
