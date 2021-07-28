import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = 'api/v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:postgres@localhost:5432/mini_project"

    class Config:
        env_file = '.env'


settings = Settings()
