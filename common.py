import logging
import sys


def get_logger(logger_name: str) -> logging.Logger:
    logger = logging.Logger(logger_name)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s]: %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


class ImageSearchError(Exception):
    pass
