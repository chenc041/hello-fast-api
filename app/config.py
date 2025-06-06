from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'


class Settings(BaseSettings):
    APP_NAME: str
    APP_ENV: str

    model_config = ConfigDict(
        env_file=env_path,
        env_file_encoding='utf-8'
    )


settings = Settings()
