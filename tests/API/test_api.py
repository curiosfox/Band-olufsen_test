import pytest
from tests.API.test_api_helper import TestAPIHelper


@pytest.mark.usefixtures("load_variables")
@pytest.mark.api
class TestAPI(TestAPIHelper):
    def test_get_users_success(self, request, requests_mock):
        """Test get_users method for successful response."""
        
        requests_mock.get(f'{request.cls.base_url}/users', json=request.cls.mock_user_response)

        users = request.cls.api_client.get_users()
        assert len(users) == 1
        assert users[0].id == 1
        assert users[0].name == "Test User"

    def test_get_posts_success(self, request, requests_mock):
        """Test get_posts method for successful response."""

        requests_mock.get(f'{request.cls.base_url}/posts', json=request.cls.mock_post_response)

        posts = request.cls.api_client.get_posts()
        assert len(posts) == 1
        assert posts[0].id == 1
        assert posts[0].title == "Test Title"

    @pytest.mark.parametrize("status_code", [400, 404, 500])
    def test_get_users_failure(self, request, requests_mock, status_code):
        """Test get_users method when API returns an error."""

        requests_mock.get(f'{request.cls.base_url}/users', status_code=status_code)
        users = request.cls.api_client.get_users()
        assert users == []

    @pytest.mark.parametrize("status_code", [400, 404, 500])
    def test_get_posts_failure(self, request, requests_mock, status_code):
        """Test get_posts method with different failure status codes."""

        requests_mock.get(f'{request.cls.base_url}/posts', status_code=status_code)

        posts = request.cls.api_client.get_posts()
        assert posts == []
