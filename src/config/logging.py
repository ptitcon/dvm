import os
import logging
import logging.config

from config import ROOT_DIR, LOGS_DIR


def set_up_root_logger() -> logging.Logger:
    os.makedirs(LOGS_DIR, exist_ok=True)
    logging.config.fileConfig(f"{ROOT_DIR}/logging.conf")
    return logging.getLogger()
