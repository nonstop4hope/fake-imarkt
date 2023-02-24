import os
import secrets
from typing import List, Union, Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, AnyHttpUrl, validator, HttpUrl


class Settings(BaseSettings):

    load_dotenv()

    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    # Address settings
    SERVER_NAME: str = os.getenv('SERVER_NAME', 'fake-imarkt')
    SERVER_HOST: str = os.getenv('SERVER_HOST', '127.0.0.1')
    SERVER_PORT: int = os.getenv('SERVER_PORT', 8000)

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str = "Fake-Imarkt"
    SENTRY_DNS: Optional[HttpUrl] = None

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[str, List[str]]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True


settings = Settings()
