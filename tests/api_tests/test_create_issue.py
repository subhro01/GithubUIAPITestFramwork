import requests
import pytest
from utils.config_loader import load_config  # Import the centralized config loader
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


class TestGitHubAPICreateIssue:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, logger):
        """Setup and teardown for API tests."""
        self.logger = logger
        self.logger.info("Starting GitHub API Create Issue tests")
        yield
        self.logger.info("GitHub API Create Issue tests completed")

    def test_create_issue(self, api_token, repo_details):
        """Tests the creation of a GitHub issue via the API."""
        owner, repo = repo_details
        self.logger.info(f"Creating an issue for repository: {owner}/{repo}")

        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        headers = {
            "Authorization": f"token {api_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "title": "Test Issue",
            "body": "This issue was created via the API"
        }

        self.logger.info("Sending POST request to create an issue")
        response = requests.post(url, headers=headers, json=data)

        self.logger.info(f"Received response with status code: {response.status_code}")
        assert response.status_code == 201, f"Failed to create issue. Response: {response.json()}"

        issue = response.json()
        assert issue["title"] == "Test Issue", "Issue title mismatch"
        assert issue["body"] == "This issue was created via the API", "Issue body mismatch"

        self.logger.info(f"Issue created successfully with title: {issue['title']}")
