from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings. Secrets are SecretStr so they never appear in logs/repr."""

    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "Debt Advisor API"
    debug: bool = False

    database_url: SecretStr
    supabase_url: str
    supabase_service_role_key: SecretStr
    anthropic_api_key: SecretStr


@lru_cache
def get_settings() -> Settings:
    """Get application settings."""
    return Settings()
