from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "Debt Advisor API"
    debug: bool = False
    database_url: str
    supabase_url: str
    supabase_key: str
    anthropic_api_key: str

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    """Get application settings."""
    return Settings()