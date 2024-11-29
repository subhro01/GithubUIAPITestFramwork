from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for GitHub login page."""

    USERNAME_FIELD = (By.ID, "login_field")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "commit")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.flash.flash-error")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """Navigate to the GitHub login page."""
        self.navigate_to("https://github.com/login")

    def login(self, username, password):
        """Log in to GitHub with provided username and password."""
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def is_error_message_displayed(self):
        """Check if an error message is displayed for invalid login."""
        return self.is_element_present(self.ERROR_MESSAGE)

    def login_successful(self):
        """Check if login was successful by verifying the presence of the username in the page."""
        return self.is_element_present((By.XPATH, "//summary[contains(@aria-label, 'View profile and more')]"))
