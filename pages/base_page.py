from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for common functionality across all page objects."""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """Find a single element."""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        """Find a list of elements."""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def navigate_to(self, url):
        """Navigate to a given URL."""
        self.driver.get(url)

    def is_element_present(self, locator):
        """Check if an element is present."""
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def click(self, locator):
        """Click on an element."""
        self.find_element(locator).click()

    def send_keys(self, locator, value):
        """Send keys to an input element."""
        self.find_element(locator).send_keys(value)

    def wait_for_element_to_be_clickable(self, locator):
        """Wait for an element to be clickable."""
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )