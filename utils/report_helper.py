import os
import pytest
from datetime import datetime


def generate_html_report(report_dir="logs"):
    """Generates an HTML report for the test execution."""
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(report_dir, f"test_report_{timestamp}.html")

    pytest.main(["--maxfail=5", "--disable-warnings", "--html=" + report_path])
    return report_path
