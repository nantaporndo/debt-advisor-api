import os

from app.core.config import Settings

# Test-owned config: overrides .env and shell so tests never touch real services.
# Must run before any `app` import that reads settings — conftest.py is loaded before test modules.
Settings.model_config["env_file"] = None
os.environ["DATABASE_URL"] = "postgresql://test:test@localhost:5432/test"
os.environ["SUPABASE_URL"] = "http://localhost:54321"
os.environ["SUPABASE_SERVICE_ROLE_KEY"] = "test-key"
os.environ["ANTHROPIC_API_KEY"] = "test-key"
