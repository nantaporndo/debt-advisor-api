import os
import subprocess
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from app.core.config import get_settings
from app.core.database import get_engine
from app.main import app

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_VARS = [
    "DATABASE_URL",
    "SUPABASE_URL",
    "SUPABASE_SERVICE_ROLE_KEY",
    "ANTHROPIC_API_KEY",
]


@pytest.fixture
def no_config(monkeypatch, tmp_path):
    # Run from a dir without .env so pydantic-settings can't pick it up.
    monkeypatch.chdir(tmp_path)
    for var in CONFIG_VARS:
        monkeypatch.delenv(var, raising=False)
    get_settings.cache_clear()
    get_engine.cache_clear()
    yield
    get_settings.cache_clear()
    get_engine.cache_clear()


def test_import_needs_no_config(tmp_path):
    # Fresh process: no conftest env, cwd without .env.
    env = {k: v for k, v in os.environ.items() if k not in CONFIG_VARS}
    env["PYTHONPATH"] = str(REPO_ROOT)
    result = subprocess.run(
        [sys.executable, "-c", "import app.main"],
        cwd=tmp_path,
        check=False,
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr


def test_startup_fails_fast_without_config(no_config):
    # Entering TestClient runs lifespan startup.
    with pytest.raises(ValidationError), TestClient(app):
        pass