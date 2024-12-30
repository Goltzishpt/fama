from pathlib import Path
from loguru import logger


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._configure()
        return cls._instance

    @staticmethod
    def _configure():

        log_path = Path(Path.cwd(), "data", "logs.txt")
        log_path.parent.mkdir(parents=True, exist_ok=True)

        logger.add(
            log_path,
            rotation="10 MB",
            retention="10 days",
            level="INFO",
            format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}",
        )

    @staticmethod
    def get_logger():
        return logger
