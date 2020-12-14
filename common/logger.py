import sys
from logging import Logger, Formatter, StreamHandler


def create_logger(name: str, level: str, formatter: Formatter = None) -> Logger:
    logger = Logger(
        name=name.title(),
        level=level
    )
    log_formatter = formatter or Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M'
    )
    console_handler = StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)
    return logger


