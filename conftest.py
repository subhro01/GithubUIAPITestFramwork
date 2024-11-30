import os
import pytest
from datetime import datetime
from utils.browser_setup import get_driver
from utils.config_loader import load_config

# Generate results folder with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    results_dir = "results"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = os.path.join(results_dir, f"report_{timestamp}")
    os.makedirs(report_dir, exist_ok=True)
    config.option.htmlpath = os.path.join(report_dir, "test_report.html")
    config.option.self_contained_html = True

# Browser fixture
@pytest.fixture(scope="function")
def driver():
    # Load WebDriver configuration from config.yaml
    config = load_config()
    webdriver_config = config.get("webdriver", {})

    # Use the get_driver function to initialize the driver based on config
    driver = get_driver(webdriver_config)
    yield driver
    driver.quit()
