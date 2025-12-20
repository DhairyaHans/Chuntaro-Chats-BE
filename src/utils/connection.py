import os
from contextlib import contextmanager
from typing import Iterator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session

load_dotenv()

_engine: Engine | None = None
_SessionLocal: sessionmaker | None = None

def get_db_engine() -> Engine:
    global _engine
    if _engine is not None:
        return _engine

    db_url = os.getenv("DEV_DB_URL")
    if not db_url:
        raise RuntimeError("DEV_DB_URL not found in environment")
    try:
        _engine = create_engine(db_url, future=True)
        return _engine
    except SQLAlchemyError as e:
        raise RuntimeError("Failed to create database engine") from e

def get_sessionmaker() -> sessionmaker:
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(bind=get_db_engine(), autoflush=False, future=True)
    return _SessionLocal

@contextmanager
def get_session() -> Iterator[Session]:
    """
    Use this as a per-request context manager:

    with get_session() as session:
        ... use session ...
        session.commit()  # optional: commit explicitly when desired

    The session will be rolled back on exception and always closed once here.
    """
    SessionLocal = get_sessionmaker()
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()