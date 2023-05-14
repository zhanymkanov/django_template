from enum import Enum

from pydantic import BaseSettings, PostgresDsn


class Environment(str, Enum):
    LOCAL = "local"
    PRODUCTION = "production"

    @property
    def is_debug(self) -> bool:
        return self == self.LOCAL


class Config(BaseSettings):
    ENVIRONMENT: Environment = Environment.PRODUCTION
    SECRET_KEY: str
    ALLOWED_HOSTS: list[str]
    CSRF_ORIGINS: list[str]
    DATABASE_URL: PostgresDsn


config = Config()
