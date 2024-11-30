import pytest
from pages.login_page import LoginPage
from pages.issue_page import IssuePage
from utils.logger import setup_logger
from utils.report_helper import generate_html_report
from utils.browser_setup import get_driver
from utils.config_loader import load_config


class TestCreateIssue:
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

    def test_create_issue(self):
        """Test case for creating an issue through the GitHub UI."""
        self.logger.info("Starting the test: Create GitHub Issue via UI")

        try:
            github_config = self.config["github"]

            # Navigate to GitHub Login Page
            self.logger.info("Navigating to GitHub login page")
            self.driver.get("https://github.com/login")

            # Log in first (using LoginPage)
            self.logger.info("Attempting to log in")
            login_page = LoginPage(self.driver)
            login_page.load()
            login_page.login(github_config["username"], github_config["password"])
            assert login_page.login_successful(), "Login failed"
            self.logger.info("Login successful")

            # Navigate to the Issue Page
            self.logger.info("Navigating to issue creation page")
            issue_page = IssuePage(self.driver, github_config["owner"], github_config["repository_name"])
            issue_page.load()

            # Create an issue
            self.logger.info("Attempting to create an issue")
            issue_title = "Test Issue"
            issue_description = "This issue was created via the UI"
            issue_page.create_issue(issue_title, issue_description)
            assert issue_page.is_issue_created(issue_title), "Issue creation failed"
            self.logger.info("Issue created successfully")

        except Exception as e:
            self.logger.error(f"Test failed with error: {e}")
            raise e
