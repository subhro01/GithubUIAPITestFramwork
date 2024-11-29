from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RepositoryPage(BasePage):
    """Page object for GitHub repository actions."""

    CREATE_REPO_BUTTON = (By.XPATH, "//a[text()='New']")
    REPO_NAME_FIELD = (By.ID, "repository_name")
    REPO_DESCRIPTION_FIELD = (By.ID, "repository_description")
    PRIVATE_CHECKBOX = (By.ID, "repository_visibility_private")
    CREATE_BUTTON = (By.XPATH, "//button[contains(text(),'Create repository')]")

    def __init__(self, driver, owner, repo_name):
        super().__init__(driver)
        self.owner = owner
        self.repo_name = repo_name

    def load(self):
        """Navigate to the repository's creation page."""
        self.navigate_to(f"https://github.com/{self.owner}")

    def create_repository(self, repo_name, private=True, description=""):
        """Create a new repository via the UI."""
        self.click(self.CREATE_REPO_BUTTON)
        self.send_keys(self.REPO_NAME_FIELD, repo_name)
        self.send_keys(self.REPO_DESCRIPTION_FIELD, description)
        if private:
            self.click(self.PRIVATE_CHECKBOX)
        self.click(self.CREATE_BUTTON)

    def is_repository_created(self):
        """Verify that the repository is created and exists on the page."""
        return self.is_element_present((By.PARTIAL_LINK_TEXT, self.repo_name))
