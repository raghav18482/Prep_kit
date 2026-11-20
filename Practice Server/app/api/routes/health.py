from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.database import get_db

router = APIRouter()


@router.get("/health")
def health(db: Session = Depends(get_db)):
    # Runs a tiny query to confirm the database is reachable.
    db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}
