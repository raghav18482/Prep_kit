# Redis connection setup (redis-py).
import redis

from app.core.config import settings

# One shared client; redis-py keeps a connection pool internally.
# decode_responses=True returns str instead of bytes.
redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)


def get_redis() -> redis.Redis:
    """FastAPI dependency: returns the shared Redis client."""
    return redis_client
