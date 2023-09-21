from functools import lru_cache

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    TOKEN: str

    ADMIN_ID: int

    USE_REDIS: bool = False  # Without redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ""

    DB_SQLITE_DIR: str = "app/db/bot.db"


@lru_cache()
def settings():
    return Settings(
        _env_file=".env",
        _env_file_encoding="utf-8",
    )
