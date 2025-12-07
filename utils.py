import logging
from logging.handlers import RotatingFileHandler

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra='allow',
        str_strip_whitespace=True,
    )


def setup_logging(log_file: str = "mirror_bot.log", max_bytes: int = 5 * 1024 * 1024, backup_count: int = 5):
    """Set up the logging configuration with file size limits and backups."""
    # Create a rotating file handler
    handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,  # Max file size (5 MB in this example)
        backupCount=backup_count  # Number of backup files to keep
    )

    # Set the logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Set up the root logger
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            handler,  # Use the rotating file handler
            logging.StreamHandler()  # Log to console
        ]
    )
