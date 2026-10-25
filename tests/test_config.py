from app.core.config import Settings


def make_settings() -> Settings:
    return Settings(
        _env_file=None,
        database_url="postgresql://u:DB-PASSWORD-123@h/db",
        supabase_url="http://localhost:54321",
        supabase_service_role_key="SERVICE-ROLE-456",
        anthropic_api_key="ANTHROPIC-789",
    )


def test_secrets_are_masked_in_repr():
    dumped = repr(make_settings())
    for secret in ("DB-PASSWORD-123", "SERVICE-ROLE-456", "ANTHROPIC-789"):
        assert secret not in dumped


def test_secret_values_still_readable():
    s = make_settings()
    assert s.anthropic_api_key.get_secret_value() == "ANTHROPIC-789"
