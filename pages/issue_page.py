from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IssuePage(BasePage):
    """Page object for GitHub issue actions."""

    NEW_ISSUE_BUTTON = (By.XPATH, "//a[contains(text(),'New issue')]")
    ISSUE_TITLE_FIELD = (By.ID, "issue_title")
    ISSUE_BODY_FIELD = (By.ID, "issue_body")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Submit new issue')]")

    def __init__(self, driver, owner, repo_name):
        super().__init__(driver)
        self.owner = owner
        self.repo_name = repo_name

    def load(self):
        """Navigate to the issues page for the repository."""
        self.navigate_to(f"https://github.com/{self.owner}/{self.repo_name}/issues")

    def create_issue(self, title, body):
        """Create a new issue."""
        self.click(self.NEW_ISSUE_BUTTON)
        self.send_keys(self.ISSUE_TITLE_FIELD, title)
        self.send_keys(self.ISSUE_BODY_FIELD, body)
        self.click(self.SUBMIT_BUTTON)

    def is_issue_created(self, title):
        """Verify that the issue has been created."""
        return self.is_element_present((By.PARTIAL_LINK_TEXT, title))
