import pytest
from pages.login_page import LoginPage
from pages.pull_request_page import PullRequestPage
from utils.logger import setup_logger
from utils.report_helper import generate_html_report
from utils.browser_setup import get_driver
from utils.config_loader import load_config


class TestPullRequest:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup and teardown for each test."""
        # Load configuration
        self.config = load_config()
        self.logger = setup_logger()
        self.logger.info("Loading browser setup based on configuration")

        # Initialize the WebDriver
        self.driver = get_driver(self.config["webdriver"])
        self.logger.info("Browser setup complete")

        yield  # Run the test method

        # Teardown
        self.logger.info("Closing the browser after the test")
        self.driver.quit()
        self.logger.info("Test completed. Generating HTML report")
        report_path = generate_html_report()
        self.logger.info(f"HTML Test Report generated at: {report_path}")

    def test_create_pull_request(self):
        """Test case for creating a pull request."""
        self.logger.info("Starting the test: Create Pull Request")

        try:
            github_config = self.config["github"]

            # Log in first (using LoginPage)
            self.logger.info("Navigating to GitHub login page")
            login_page = LoginPage(self.driver)
            login_page.load()
            self.logger.info("Attempting to log in")
            login_page.login(github_config["username"], github_config["password"])
            assert login_page.login_successful(), "Login failed"
            self.logger.info("Login successful")

            # Create a pull request
            self.logger.info("Navigating to the Pull Request page")
            pr_page = PullRequestPage(self.driver, github_config["owner"], github_config["repository_name"])
            pr_page.load()

            self.logger.info("Creating a pull request from 'feature-branch' to 'main'")
            pr_page.create_pull_request(
                base_branch="main",
                compare_branch="feature-branch",
                title="Test Pull Request",
                description="This PR was created via the UI"
            )
            assert pr_page.is_pull_request_created("Test Pull Request"), "Pull request creation failed"
            self.logger.info("Pull request created successfully")

        except Exception as e:
            self.logger.error(f"Test failed with error: {e}")
            raise e
