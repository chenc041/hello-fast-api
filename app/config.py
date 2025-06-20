from pathlib import Path
from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'


class Settings(BaseSettings):
    APP_NAME: Annotated[str | None, Field(description="应用名称")] = "FastApi"
    APP_ENV: Annotated[str | None, Field(description="应用环境")] = "local"
    model_config = SettingsConfigDict(env_file=env_path, env_file_encoding='utf-8')


settings = Settings()
