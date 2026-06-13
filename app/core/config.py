from fuctools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "My FastAPI Application"
    debug: bool = False
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    """Get application settings."""
    return Settings()