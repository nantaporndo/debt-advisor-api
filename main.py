from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Debt Advisor API"}


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
