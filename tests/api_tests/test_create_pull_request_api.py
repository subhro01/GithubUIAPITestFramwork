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


@pytest.fixture(scope="session")
def repo_details(config):
    """Fixture to provide repository owner and name."""
    return config["github"]["owner"], config["github"]["repository_name"]


@pytest.fixture(scope="session", autouse=True)
def logger():
    """Setup logger for the session."""
    return setup_logger()


class TestGitHubCreatePullRequestAPI:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, logger):
        """Setup and teardown for API tests."""
        self.logger = logger
        self.logger.info("Starting GitHub API Create pull request tests")
        yield
        self.logger.info("GitHub API Create pull request tests completed")

    def test_create_pull_request(self, api_token, repo_details):
        """Test to create a GitHub pull request via the API."""
        owner, repo = repo_details
        self.logger.info(f"Attempting to create a pull request for repository: {owner}/{repo}")

        # Define the API endpoint and headers for the request
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        headers = {
            "Authorization": f"token {api_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Define the data payload for creating a pull request
        data = {
            "title": "Test Pull Request",
            "head": "feature-branch",  # Ensure this branch exists in the repository
            "base": "main",  # The target branch for the pull request
            "body": "This PR was created via the API"
        }

        # Sending POST request to create a pull request
        self.logger.info("Sending POST request to create a pull request")
        response = requests.post(url, headers=headers, json=data)

        # Log the response status and check for successful creation
        self.logger.info(f"Received response with status code: {response.status_code}")
        assert response.status_code == 201, f"Failed to create pull request. Response: {response.json()}"

        # Validate the details of the pull request created
        pr = response.json()
        assert pr["title"] == "Test Pull Request", "Pull request title mismatch"
        assert pr["head"]["ref"] == "feature-branch", "Pull request head branch mismatch"
        assert pr["base"]["ref"] == "main", "Pull request base branch mismatch"

        # Log the successful creation of the pull request
        self.logger.info(f"Pull request created successfully with title: {pr['title']}")
