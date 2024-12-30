import os
from app.utils.logger import Logger

from dotenv import load_dotenv
load_dotenv()


class BaseSettings:
    DEBUG = False
    LOGGER = Logger().get_logger()


class DevelopmentSettings(BaseSettings):
    DEBUG = True


def get_settings():
    env = os.getenv("ENVIRONMENT", "development")
    match env:
        case "development":
            return DevelopmentSettings()
        case _:
            raise ValueError(f"Invalid environment: {env}")


settings = get_settings()
