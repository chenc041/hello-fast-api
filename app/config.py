from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'

class Settings(BaseSettings):
    APP_NAME: str | None  = "FastApi"
    APP_ENV: str | None = "local"
    class Config:
        env_file = env_path


settings = Settings()
