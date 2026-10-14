from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, text

from app.core.database import engine


def test_connection():
    try:
        with Session(engine) as session:
            result = session.exec(text("SELECT 1")).first()
            print(f"Connection successful: {result}")
    except SQLAlchemyError as e:
        print(f"Connection failed: {e}")


if __name__ == "__main__":
    test_connection()
