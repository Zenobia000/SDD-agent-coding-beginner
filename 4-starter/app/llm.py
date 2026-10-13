"""LLM 介面。業務程式只依賴 LLMClient，測試時換成 FakeLLM，不花錢、結果固定。

要接其他供應商（例如 OpenAI），寫一個有 complete(system=..., user=...) 方法的類別，
再加進 build_llm 即可。
"""

from collections.abc import Sequence
from typing import Any, Protocol

import anthropic

from app.config import Settings

FALLBACK_BETA = "server-side-fallback-2026-07-01"
DEFAULT_MAX_TOKENS = 16000


class LLMError(RuntimeError):
    """呼叫模型失敗，或回傳的東西不能用。"""


class LLMClient(Protocol):
    def complete(self, *, system: str, user: str) -> str: ...


class FakeLLM:
    """依序回傳預先寫好的字串。用完之後回傳 default；沒有 default 就報錯。"""

    def __init__(self, responses: Sequence[str] = (), default: str | None = None) -> None:
        self._responses = tuple(responses)
        self._default = default
        self.calls: tuple[tuple[str, str], ...] = ()

    def complete(self, *, system: str, user: str) -> str:
        index = len(self.calls)
        self.calls = self.calls + ((system, user),)
        if index < len(self._responses):
            return self._responses[index]
        if self._default is not None:
            return self._default
        raise LLMError(f"FakeLLM 只準備了 {len(self._responses)} 個回應，這是第 {index + 1} 次呼叫")


class AnthropicLLM:
    """呼叫 Claude。模型拒答時，伺服器端會自動改由備援模型回答（fallbacks="default"）。"""

    def __init__(self, model: str, client: Any = None, max_tokens: int = DEFAULT_MAX_TOKENS) -> None:
        self._model = model
        self._client = client if client is not None else anthropic.Anthropic()
        self._max_tokens = max_tokens

    def complete(self, *, system: str, user: str) -> str:
        try:
            response = self._client.beta.messages.create(
                model=self._model,
                max_tokens=self._max_tokens,
                system=system,
                messages=[{"role": "user", "content": user}],
                betas=[FALLBACK_BETA],
                fallbacks="default",
            )
        except anthropic.APIConnectionError as exc:
            raise LLMError(f"連不上 Claude API：{exc}") from exc
        except anthropic.RateLimitError as exc:
            raise LLMError("Claude API 請求太頻繁，稍後再試") from exc
        except anthropic.APIStatusError as exc:
            raise LLMError(f"Claude API 回傳錯誤 {exc.status_code}：{exc.message}") from exc

        if response.stop_reason == "refusal":
            raise LLMError("模型拒絕回答這個請求")
        if response.stop_reason == "max_tokens":
            raise LLMError("回應被 max_tokens 截斷，內容不完整")

        text = "".join(block.text for block in response.content if block.type == "text")
        if not text.strip():
            raise LLMError("模型回應裡沒有文字內容")
        return text


def build_llm(settings: Settings) -> LLMClient:
    if settings.llm_provider == "anthropic":
        return AnthropicLLM(model=settings.llm_model)
    return FakeLLM(default="{}")
