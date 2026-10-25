import os

# Test-owned config: overrides .env and shell so tests never touch real services.
# Must run before any `app` import — conftest.py is loaded before test modules.
os.environ["DATABASE_URL"] = "postgresql://test:test@localhost:5432/test"
os.environ["SUPABASE_URL"] = "http://localhost:54321"
os.environ["SUPABASE_KEY"] = "test-key"
os.environ["ANTHROPIC_API_KEY"] = "test-key"