from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_return_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_health_version_reads_env(monkeypatch):
    monkeypatch.setenv("APP_VERSION","abc123")
    r = client.get("/health")
    assert r.json()["version"] == "abc123"
