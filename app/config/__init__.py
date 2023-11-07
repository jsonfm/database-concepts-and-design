import os

from dotenv import load_dotenv

from app.logger import logger


class Config:
    def __init__(self):
        if os.getenv("ENV") == "dev":
            logger.info("Loading DEVELOPMENT config")
            load_dotenv(".env.dev")
        else:
            logger.info("Loading PRODUCTION config")
            load_dotenv()

        self.DB_URL = os.environ.get("DB_URL", "")
        self.SECRET_KEY = os.environ.get("SECRET_KEY", "ultrasecret")


config = Config()
