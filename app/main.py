from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import init_db
from app.routers import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Debt Advisor API", lifespan=lifespan)

app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "Debt Advisor API"}
