# Database connection setup (SQLAlchemy).
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

# The engine manages the connection pool to Postgres.
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Each request gets its own Session (one unit of work).
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# All table models inherit from this Base.
class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency: opens a session per request and always closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
