import pytest
from unittest.mock import MagicMock
from tests.App.test_main_app_helper import TestAppHelper


@pytest.mark.usefixtures("load_variables")
class TestApp(TestAppHelper):
    def test_print_user_data(self, request, monkeypatch):
        """Test print_user_data method."""

        self.main_app.api_obj.get_users = MagicMock(return_value=[self.mock_user])
        fake_stdout = MagicMock()
        monkeypatch.setattr('sys.stdout', fake_stdout)
        self.main_app.print_user_data()

        assert fake_stdout.write.called

    def test_print_posts_data(self, request, monkeypatch):
        """Test print_posts_data method."""

        self.main_app.api_obj.get_posts = MagicMock(return_value=[self.mock_post])

        fake_stdout = MagicMock()
        monkeypatch.setattr('sys.stdout', fake_stdout)
        self.main_app.print_posts_data()

        assert fake_stdout.write.called

    def test_main_process_invalid_choice(self, request, monkeypatch):
        """Test main_process method with invalid user input."""

        inputs = iter(['invalid', '4', '3'])  # Simulate user inputs

        def mock_input(prompt):
            return next(inputs)

        monkeypatch.setattr('builtins.input', mock_input)

        # Mock methods
        self.main_app.exit_app = MagicMock()
        self.main_app.print_user_data = MagicMock()
        self.main_app.print_posts_data = MagicMock()

        self.main_app.main_process()

        assert self.main_app.exit_app.call_count == 1
        assert self.main_app.print_user_data.call_count == 0
        assert self.main_app.print_posts_data.call_count == 0

    def test_main_process_sucess(self, request, monkeypatch):
        """Test main_process method when user selects option 1."""
        inputs = iter(['1', '3'])  # Simulate user entering '1' then '3' to exit

        def mock_input(prompt):
            return next(inputs)

        monkeypatch.setattr('builtins.input', mock_input)

        # Mock methods called within main_process
        self.main_app.print_user_data = MagicMock()
        self.main_app.exit_app = MagicMock()

        self.main_app.main_process()

        # Assert that print_user_data was called
        self.main_app.print_user_data.assert_called_once()
        # Assert that exit_app was called
        self.main_app.exit_app.assert_called_once()
