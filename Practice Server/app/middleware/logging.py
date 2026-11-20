# Custom middleware: runs before and after EVERY request.
import logging
import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("app.requests")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Gives each request an ID, logs it, and measures how long it took."""

    async def dispatch(self, request: Request, call_next):
        # --- BEFORE the route runs ---
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request.state.request_id = request_id  # routes can read this if needed
        start = time.perf_counter()

        response = await call_next(request)  # passes the request on to the route

        # --- AFTER the route runs ---
        duration_ms = (time.perf_counter() - start) * 1000
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time-Ms"] = f"{duration_ms:.2f}"

        logger.info(
            "%s %s -> %s (%.2f ms) [id=%s]",
            request.method,
            request.url.path,
            response.status_code,
            duration_ms,
            request_id,
        )
        return response
