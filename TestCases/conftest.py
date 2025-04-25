
import pytest
import os
from datetime import datetime
from Utilities.driver_factory import DriverFactory
from Utilities.screenshot_util import ScreenshotUtil
from Utilities.logger import Logger


@pytest.fixture(scope="function")
def setup(request):
    driver = DriverFactory.get_driver()
    request.cls.driver = driver
    request.cls.logger = Logger.get_logger(request.cls.__name__)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.instance.driver if hasattr(item.instance, "driver") else None
        if driver and report.failed:
            test_name = item.nodeid.split("::")[-1]
            screenshot_path = ScreenshotUtil.capture_screenshot(driver, test_name)
            print(f"Screenshot saved to: {screenshot_path}")