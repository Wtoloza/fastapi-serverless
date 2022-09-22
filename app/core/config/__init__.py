from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Awesome API"

    class Config:
        env_file = "app/core/config/.env"


@lru_cache
def get_settings():
    return Settings()
