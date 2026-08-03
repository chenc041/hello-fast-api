"""Application settings loaded from environment variables."""

from functools import lru_cache
from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration, overridable via env vars prefixed with ``APP_``."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    name: str = "hello-fastapi"
    debug: bool = False
    api_prefix: str = "/api/v1"


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings instance."""
    return Settings()
