import pytest
from pages.login_page import LoginPage
from utils.logger import setup_logger
from utils.report_helper import generate_html_report
from utils.browser_setup import get_driver
from utils.config_loader import load_config


class TestLogin:
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

    def test_login_valid_credentials(self):
        """Test case for logging in with valid credentials."""
        self.logger.info("Starting the test: Login with valid credentials")

        try:
            github_config = self.config["github"]

            # Navigate to GitHub Login Page
            self.logger.info("Navigating to GitHub login page")

            # Attempt to log in with valid credentials
            login_page = LoginPage(self.driver)
            login_page.load()
            login_page.login(github_config["username"], github_config["password"])
            assert login_page.login_successful(), "Login with valid credentials failed"
            self.logger.info("Login with valid credentials successful")

        except Exception as e:
            self.logger.error(f"Test failed with error: {e}")
            raise e

    def test_login_invalid_credentials(self):
        """Test case for logging in with invalid credentials."""
        self.logger.info("Starting the test: Login with invalid credentials")

        try:
            # Navigate to GitHub Login Page
            self.logger.info("Navigating to GitHub login page")

            # Attempt to log in with invalid credentials
            login_page = LoginPage(self.driver)
            login_page.load()
            login_page.login("invalid_username", "invalid_password")
            assert login_page.is_error_message_displayed(), "Error message was not displayed for invalid credentials"
            self.logger.info("Error message displayed successfully for invalid credentials")

        except Exception as e:
            self.logger.error(f"Test failed with error: {e}")
            raise e
