import requests
import pytest
from utils.config_loader import load_config
from utils.logger import setup_logger


@pytest.fixture(scope="session")
def config():
    """Fixture to load configuration once per session."""
    return load_config()


@pytest.fixture(scope="session")
def api_token(config):
    """Fixture to provide the GitHub API token."""
    return config["github"]["api_token"]


@pytest.fixture(scope="session", autouse=True)
def logger():
    """Setup logger for the session."""
    return setup_logger()


class TestGitHubAPIAuthentication:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, logger):
        """Setup and teardown for API tests."""
        self.logger = logger
        self.logger.info("Starting GitHub API tests")
        yield
        self.logger.info("GitHub API tests completed")

    def test_authentication(self, api_token):
        """Tests GitHub API authentication."""
        self.logger.info("Testing authentication via GitHub API")

        url = "https://api.github.com/user"
        headers = {
            "Authorization": f"token {api_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        self.logger.info("Sending GET request to GitHub API for user authentication")
        response = requests.get(url, headers=headers)

        self.logger.info(f"Received response with status code: {response.status_code}")
        assert response.status_code == 200, "Authentication failed"

        user = response.json()
        assert "login" in user, "Login key missing in response"
        assert user["login"] != "", "Login value is empty"

        self.logger.info(f"Authentication successful for user: {user['login']}")
