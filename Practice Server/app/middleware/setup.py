# Registers all middleware in one place.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.middleware.logging import RequestLoggingMiddleware


def setup_middleware(app: FastAPI) -> None:
    # Note: the middleware added LAST runs FIRST (it wraps the others).

    # Built-in: lets a frontend on another origin (e.g. React on :3000) call this API.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Custom: request ID + timing + logging. Added last, so it wraps everything.
    app.add_middleware(RequestLoggingMiddleware)
