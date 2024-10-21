import logging

import pytest

from App.main import MainApp
from App.models import User, Post


class TestAppHelper(object):
    """ Helper class for Test APP class """
    @staticmethod
    def get_log_obj() -> object:
        """ Generate a log object for testing the App"""

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

    @pytest.fixture(scope='class')
    def load_variables(self, request) -> None:
        """ Load test variables to be utilized """

        request.cls.mock_user = User(
            id=1,
            name="Test User",
            username="testuser",
            email="testuser@example.com",
            address=None,  # Simplify for testing
            phone="123-456-7890",
            website="testuser.com",
            company=None  # Simplify for testing
        )
        request.cls.mock_post = Post(
            userId=1,
            id=1,
            title="Test Title",
            body="Test body content."
        )
        request.cls.test_logger = self.get_log_obj()
        request.cls.main_app = MainApp(request.cls.test_logger)
