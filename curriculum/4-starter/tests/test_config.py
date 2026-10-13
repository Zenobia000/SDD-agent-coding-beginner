import pytest

from app.config import ConfigError, DEFAULT_ANTHROPIC_MODEL, load_env_file, load_settings


def test_defaults_to_fake_provider_without_any_env():
    settings = load_settings({})

    assert settings.llm_provider == "fake"
    assert settings.database_path == "data/leavebot.db"


def test_anthropic_requires_credentials():
    with pytest.raises(ConfigError, match="ANTHROPIC_API_KEY"):
        load_settings({"LLM_PROVIDER": "anthropic"})


def test_anthropic_rejects_placeholder_key():
    with pytest.raises(ConfigError, match="ANTHROPIC_API_KEY"):
        load_settings({"LLM_PROVIDER": "anthropic", "ANTHROPIC_API_KEY": "changeme"})


def test_anthropic_uses_default_model_when_unset():
    settings = load_settings({"LLM_PROVIDER": "anthropic", "ANTHROPIC_API_KEY": "sk-test"})

    assert settings.llm_model == DEFAULT_ANTHROPIC_MODEL


def test_model_can_be_overridden():
    settings = load_settings(
        {"LLM_PROVIDER": "anthropic", "ANTHROPIC_API_KEY": "sk-test", "LLM_MODEL": "my-model"}
    )

    assert settings.llm_model == "my-model"


def test_unknown_provider_fails_fast():
    with pytest.raises(ConfigError, match="LLM_PROVIDER"):
        load_settings({"LLM_PROVIDER": "openai"})


def test_settings_are_immutable():
    settings = load_settings({})

    with pytest.raises(AttributeError):
        settings.llm_provider = "anthropic"


def test_env_file_does_not_override_existing_values(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("# 註解\nLLM_PROVIDER=anthropic\nDATABASE_PATH = x.db\n\nBROKEN_LINE\n")

    merged = load_env_file(env_file, {"LLM_PROVIDER": "fake"})

    assert merged == {"LLM_PROVIDER": "fake", "DATABASE_PATH": "x.db"}


def test_missing_env_file_returns_env_unchanged(tmp_path):
    env = {"A": "1"}

    assert load_env_file(tmp_path / "nope.env", env) == {"A": "1"}
