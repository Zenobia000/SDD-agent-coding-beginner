from types import SimpleNamespace

import pytest

from app.llm import AnthropicLLM, FakeLLM, LLMError, build_llm
from app.config import Settings


# --- FakeLLM：單元測試用的假模型 ----------------------------------------------

def test_fake_returns_responses_in_order():
    llm = FakeLLM(responses=["first", "second"])

    assert llm.complete(system="s", user="u1") == "first"
    assert llm.complete(system="s", user="u2") == "second"


def test_fake_records_every_call():
    llm = FakeLLM(responses=["ok"])

    llm.complete(system="sys", user="明天請特休")

    assert llm.calls == (("sys", "明天請特休"),)


def test_fake_fails_loudly_when_out_of_responses():
    llm = FakeLLM(responses=[])

    with pytest.raises(LLMError, match="FakeLLM"):
        llm.complete(system="s", user="u")


# --- AnthropicLLM：用假的 SDK client 驗證送出去的參數 -------------------------

class _FakeMessages:
    def __init__(self, response):
        self._response = response
        self.kwargs = None

    def create(self, **kwargs):
        self.kwargs = kwargs
        return self._response


def _sdk_client(response):
    messages = _FakeMessages(response)
    return SimpleNamespace(beta=SimpleNamespace(messages=messages)), messages


def _text_response(*texts, stop_reason="end_turn"):
    content = [SimpleNamespace(type="thinking", thinking="")] + [
        SimpleNamespace(type="text", text=t) for t in texts
    ]
    return SimpleNamespace(stop_reason=stop_reason, content=content)


def test_anthropic_sends_system_user_and_model():
    sdk, messages = _sdk_client(_text_response('{"ok": true}'))
    llm = AnthropicLLM(model="claude-test", client=sdk)

    result = llm.complete(system="你是解析器", user="明天請特休")

    assert result == '{"ok": true}'
    assert messages.kwargs["model"] == "claude-test"
    assert messages.kwargs["system"] == "你是解析器"
    assert messages.kwargs["messages"] == [{"role": "user", "content": "明天請特休"}]


def test_anthropic_enables_refusal_fallback():
    sdk, messages = _sdk_client(_text_response("x"))

    AnthropicLLM(model="claude-test", client=sdk).complete(system="s", user="u")

    assert messages.kwargs["betas"] == ["server-side-fallback-2026-07-01"]
    assert messages.kwargs["fallbacks"] == "default"


def test_anthropic_joins_text_blocks_and_skips_thinking():
    sdk, _ = _sdk_client(_text_response("a", "b"))

    assert AnthropicLLM(model="m", client=sdk).complete(system="s", user="u") == "ab"


def test_anthropic_refusal_raises():
    sdk, _ = _sdk_client(_text_response("", stop_reason="refusal"))

    with pytest.raises(LLMError, match="拒絕"):
        AnthropicLLM(model="m", client=sdk).complete(system="s", user="u")


def test_anthropic_empty_text_raises():
    sdk, _ = _sdk_client(_text_response())

    with pytest.raises(LLMError, match="沒有文字"):
        AnthropicLLM(model="m", client=sdk).complete(system="s", user="u")


def test_anthropic_truncated_output_raises():
    sdk, _ = _sdk_client(_text_response('{"half":', stop_reason="max_tokens"))

    with pytest.raises(LLMError, match="max_tokens"):
        AnthropicLLM(model="m", client=sdk).complete(system="s", user="u")


# --- build_llm：依設定挑實作 ---------------------------------------------------

def test_build_llm_fake_by_default(tmp_path):
    settings = Settings(database_path=str(tmp_path / "x.db"), llm_provider="fake", llm_model="")

    assert isinstance(build_llm(settings), FakeLLM)


def test_fake_uses_default_after_responses_run_out():
    llm = FakeLLM(responses=["first"], default="{}")

    assert llm.complete(system="s", user="u") == "first"
    assert llm.complete(system="s", user="u") == "{}"


def test_build_llm_fake_never_runs_out(tmp_path):
    settings = Settings(database_path=str(tmp_path / "x.db"), llm_provider="fake", llm_model="")
    llm = build_llm(settings)

    for _ in range(3):
        llm.complete(system="s", user="u")
