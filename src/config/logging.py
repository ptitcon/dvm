import os
import logging

from config import LOG_DIR

FMT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FMT = "%Y-%m-%d %H:%M:%S"


def set_up_root_logger() -> logging.Logger:
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("Dotfiles")
    logger.setLevel(logging.DEBUG)

    logger.addHandler(create_file_handler())
    logger.addHandler(create_console_handler())

    return logger


def create_file_handler() -> logging.Handler:
    handler = logging.FileHandler(os.path.join(LOG_DIR, "dotfiles.log"))
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(FMT, datefmt=DATE_FMT))
    return handler


def create_console_handler():
    handler = logging.StreamHandler()
    handler.setLevel(logging.WARNING)
    handler.setFormatter(logging.Formatter(FMT, datefmt=DATE_FMT))
    return handler
