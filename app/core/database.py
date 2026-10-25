from collections.abc import Iterator
from functools import lru_cache

from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

from app.core.config import get_settings


@lru_cache
def get_engine() -> Engine:
    """Create the engine on first use, not at import time."""
    return create_engine(get_settings().database_url.get_secret_value())

def init_db(engine: Engine) -> None:
    SQLModel.metadata.create_all(engine)

def get_session()-> Iterator[Session]:
    with Session(get_engine()) as session:
        yield session