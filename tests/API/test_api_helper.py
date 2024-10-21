import logging
import pytest

from App.api import ApiClass


class TestAPIHelper(object):
    """ Helper class for TestAPI test class """

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

        request.cls.mock_user_response = [
            {
                "id": 1,
                "name": "Test User",
                "username": "testuser",
                "email": "testuser@example.com",
                "address": {
                    "street": "Test Street",
                    "suite": "Suite 1",
                    "city": "Test City",
                    "zipcode": "12345",
                    "geo": {
                        "lat": "0.0000",
                        "lng": "0.0000"
                    }
                },
                "phone": "123-456-7890",
                "website": "testuser.com",
                "company": {
                    "name": "Test Company",
                    "catchPhrase": "Test Catchphrase",
                    "bs": "Test BS"
                }
            }
        ]
        request.cls.mock_post_response = [
            {
                "userId": 1,
                "id": 1,
                "title": "Test Title",
                "body": "Test body content."
            }
        ]
        request.cls.base_url = 'https://jsonplaceholder.typicode.com'
        request.cls.test_logger = self.get_log_obj()
        request.cls.api_client = ApiClass(request.cls.test_logger)
