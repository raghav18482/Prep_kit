# App-wide settings. Values are read from environment variables / the .env file.
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Practice Server"
    API_PREFIX: str = "/api/v1"
    DATABASE_URL: str = "postgresql+psycopg://postgres:postgres@localhost:5432/practice_db"
    REDIS_URL: str = "redis://localhost:6379/0"

    # Frontend URLs allowed to call this API (CORS).
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
