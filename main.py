from datetime import datetime, timezone

from fastapi import FastAPI

from app.core.database import init_db

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def root():
    return {"message": "Debt Advisor API"}


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
