# Collects every route file into one router. Add new route files here.
from fastapi import APIRouter

from app.api.routes import health, items

api_router = APIRouter()
api_router.include_router(health.router, tags=["Health"])
api_router.include_router(items.router)
