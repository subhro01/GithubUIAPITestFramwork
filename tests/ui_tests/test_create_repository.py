import pytest
from pages.login_page import LoginPage
from pages.repository_page import RepositoryPage
from utils.logger import setup_logger
from utils.report_helper import generate_html_report
from utils.browser_setup import get_driver
from utils.config_loader import load_config


class TestCreateRepository:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup and teardown for each test."""
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

    def test_create_repository(self):
        """Test case for creating a GitHub repository through the UI."""
        self.logger.info("Starting the test: Create GitHub Repository via UI")

        try:
            # Navigate to GitHub Login Page
            self.logger.info("Navigating to GitHub login page")

            # Log in first (using LoginPage)
            self.logger.info("Attempting to log in")
            login_page = LoginPage(self.driver)
            login_page.load()
            login_page.login("valid_username", "valid_password")
            assert login_page.login_successful(), "Login failed"
            self.logger.info("Login successful")

            # Create a repository
            self.logger.info("Navigating to repository creation page")
            repo_page = RepositoryPage(self.driver, "valid_owner", "test-repo")
            repo_page.load()
            self.logger.info("Attempting to create a repository")
            repo_page.create_repository(
                repo_name="test-repo",
                private=True,
                description="This is a test repository"
            )
            assert repo_page.is_repository_created(), "Repository creation failed"
            self.logger.info("Repository created successfully")

        except Exception as e:
            self.logger.error(f"Test failed with error: {e}")
            raise e  # Reraise the exception for pytest to capture
