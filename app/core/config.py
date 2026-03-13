from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"


# 환경 변수 설정
class Settings(BaseSettings):
    PROJECT_NAME: str = "diary"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str

    DB_ECHO_LOG: bool = False

    model_config = SettingsConfigDict(
        env_file=ENV_PATH, extra="ignore", env_file_encoding="utf-8"
    )


settings = Settings()
