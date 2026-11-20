import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.db.database import Base, engine
from app.middleware.setup import setup_middleware
from app.models import item  # noqa: F401  (import models so their tables are registered)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Creates any missing tables on startup. Fine for learning;
    # real projects use Alembic migrations instead.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)
setup_middleware(app)


@app.get("/")
def root():
    return {"message": f"Hello from {settings.APP_NAME}!"}


app.include_router(api_router, prefix=settings.API_PREFIX)
