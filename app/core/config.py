from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "Debt Advisor API"
    debug: bool = False
    database_url: str
    supabase_url: str
    supabase_key: str
    anthropic_api_key: str


@lru_cache
def get_settings() -> Settings:
    """Get application settings."""
    return Settings()