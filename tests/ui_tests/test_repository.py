import pytest
from pages.login_page import LoginPage
from pages.repository_page import RepositoryPage
from utils.logger import setup_logger
from utils.report_helper import generate_html_report
from utils.browser_setup import get_driver
from utils.config_loader import load_config


class TestNavigation:
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

    def test_navigation(self):
        """Test case for navigating between repository tabs."""
        self.logger.info("Starting the test: Navigation between repository tabs")

        try:
            github_config = self.config["github"]

            # Log in first (using LoginPage)
            self.logger.info("Attempting to log in")
            login_page = LoginPage(self.driver)
            login_page.load()  # Navigates to the login page
            login_page.login(github_config["username"], github_config["password"])
            assert login_page.login_successful(), "Login failed"
            self.logger.info("Login successful")

            # Navigate to Repository Page
            self.logger.info(f"Navigating to repository: {github_config['repository_name']}")
            repo_page = RepositoryPage(self.driver, github_config["owner"], github_config["repository_name"])
            repo_page.load()  # Navigates to the repository page

            # Navigate to Issues Tab
            self.logger.info("Navigating to the Issues tab")
            repo_page.click(repo_page.TAB_ISSUES)
            assert repo_page.is_element_present(repo_page.ISSUE_LIST), "Issues tab content is not visible"
            self.logger.info("Issues tab navigation successful")

            # Navigate to Pull Requests Tab
            self.logger.info("Navigating to the Pull Requests tab")
            repo_page.click(repo_page.TAB_PULL_REQUESTS)
            assert repo_page.is_element_present(repo_page.PULL_REQUEST_LIST), "Pull Requests tab content is not visible"
            self.logger.info("Pull Requests tab navigation successful")

        except Exception as e:
            self.logger.error(f"Test failed with error: {e}")
            raise e
