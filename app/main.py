from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import get_settings
from app.core.database import get_engine, init_db
from app.routers import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_settings()
    engine = get_engine()
    init_db(engine)
    yield
    engine.dispose()


app = FastAPI(title="Debt Advisor API", lifespan=lifespan)

app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "Debt Advisor API"}
