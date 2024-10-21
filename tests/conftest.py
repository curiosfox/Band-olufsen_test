import logging
import pytest
from typing import Optional


@pytest.fixture(scope='session')
def test_logger() -> logging.Logger:
    """Creates and configures a logger instance for tests."""
    logger = logging.getLogger('TestLogger')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
