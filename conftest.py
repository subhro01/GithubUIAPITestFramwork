import os
import pytest
from datetime import datetime
from utils.browser_setup import setup_browser
from utils.api_helpers import APIHelper

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
    driver = setup_browser()
    yield driver
    driver.quit()

# API fixture
@pytest.fixture(scope="module")
def api():
    token = os.getenv("GITHUB_TOKEN", "<YOUR_PERSONAL_ACCESS_TOKEN>")
    return APIHelper(token)
