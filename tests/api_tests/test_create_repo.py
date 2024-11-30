import requests
import pytest
from utils.config_loader import load_config  # Import the config loader
from utils.logger import setup_logger  # Import the logger setup


@pytest.fixture(scope="session")
def config():
    """Fixture to load configuration once per session."""
    return load_config()


@pytest.fixture(scope="session")
def api_token(config):
    """Fixture to provide the GitHub API token."""
    return config["github"]["api_token"]


@pytest.fixture(scope="session")
def logger():
    """Setup logger for the session."""
    return setup_logger()


class TestGitHubAPICreateRepo:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, logger):
        """Setup and teardown for API tests."""
        self.logger = logger
        self.logger.info("Starting GitHub API Create Repo tests")
        yield
        self.logger.info("GitHub API Create Repo tests completed")

    def test_create_repo(self, api_token, logger):
        """Test to create a repository via the GitHub API."""
        self.logger.info("Starting test to create a GitHub repository.")

        url = "https://api.github.com/user/repos"
        headers = {
            "Authorization": f"token {api_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "name": "test-repo",
            "description": "Test repository created via API",
            "private": True
        }

        # Sending POST request to create a repository
        self.logger.info(f"Sending POST request to create repository: {data['name']}")
        response = requests.post(url, headers=headers, json=data)

        # Log the response status and check for successful creation
        self.logger.info(f"Received response with status code: {response.status_code}")
        assert response.status_code == 201, f"Failed to create repository. Response: {response.json()}"

        # Validate the repository details
        repo = response.json()
        assert repo["name"] == "test-repo", f"Repository name mismatch: {repo['name']}"
        assert repo["private"] is True, f"Repository privacy mismatch: {repo['private']}"

        # Log successful repository creation
        self.logger.info(f"Repository created successfully: {repo['name']}")
