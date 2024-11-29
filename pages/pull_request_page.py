from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PullRequestPage(BasePage):
    """Page object for GitHub pull request actions."""

    NEW_PR_BUTTON = (By.XPATH, "//a[contains(text(),'New pull request')]")
    BASE_BRANCH_DROPDOWN = (By.ID, "base")
    HEAD_BRANCH_DROPDOWN = (By.ID, "head")
    PR_TITLE_FIELD = (By.ID, "pull_request_title")
    PR_BODY_FIELD = (By.ID, "pull_request_body")
    CREATE_PR_BUTTON = (By.XPATH, "//button[contains(text(),'Create pull request')]")

    def __init__(self, driver, owner, repo_name):
        super().__init__(driver)
        self.owner = owner
        self.repo_name = repo_name

    def load(self):
        """Navigate to the pull requests page."""
        self.navigate_to(f"https://github.com/{self.owner}/{self.repo_name}/pulls")

    def create_pull_request(self, base_branch, head_branch, title, body):
        """Create a pull request."""
        self.click(self.NEW_PR_BUTTON)
        self.select_dropdown(self.BASE_BRANCH_DROPDOWN, base_branch)
        self.select_dropdown(self.HEAD_BRANCH_DROPDOWN, head_branch)
        self.send_keys(self.PR_TITLE_FIELD, title)
        self.send_keys(self.PR_BODY_FIELD, body)
        self.click(self.CREATE_PR_BUTTON)

    def is_pull_request_created(self, title):
        """Verify that the pull request has been created."""
        return self.is_element_present((By.PARTIAL_LINK_TEXT, title))

    def select_dropdown(self, locator, value):
        """Select an option from a dropdown by its value."""
        dropdown = self.find_element(locator)
        dropdown.click()
        option = dropdown.find_element(By.XPATH, f"//option[@value='{value}']")
        option.click()
