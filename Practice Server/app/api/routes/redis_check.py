from fastapi import APIRouter, Depends, HTTPException
from redis import Redis
from redis.exceptions import RedisError

from app.db.redis_client import get_redis

router = APIRouter()


@router.get("/redis/ping")
def redis_ping(r: Redis = Depends(get_redis)):
    # PING checks the connection, then a SET/GET round-trip proves read/write works.
    try:
        r.ping()
        r.set("practice:ping", "pong", ex=60)  # expires after 60s
        value = r.get("practice:ping")
    except RedisError as e:
        raise HTTPException(status_code=503, detail=f"Redis unavailable: {e}")
    return {"status": "ok", "redis": "connected", "test_value": value}
