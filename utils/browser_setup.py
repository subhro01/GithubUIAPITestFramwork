from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_driver(webdriver_config):
    """Initialize the WebDriver based on the configuration."""
    browser = webdriver_config.get("browser", "chrome").lower()
    implicit_wait = webdriver_config.get("implicit_wait", 10)

    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(), options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(implicit_wait)
    return driver
