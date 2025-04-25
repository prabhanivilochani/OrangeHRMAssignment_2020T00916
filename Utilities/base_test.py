
import unittest
import time
from Utilities.driver_factory import DriverFactory
from Utilities.logger import Logger
from Utilities.html_reporter import HTMLReporter


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reporter = HTMLReporter(report_name=cls.__name__)
        cls.logger = Logger.get_logger(cls.__name__)

    def setUp(self):
        self.driver = DriverFactory.get_driver()
        self.test_start_time = time.time()
        self.logger.info(f"Starting test: {self._testMethodName}")

    def tearDown(self):
        test_duration = time.time() - self.test_start_time
        test_name = self._testMethodName

        # Don't try to detect test failures here - let pytest handle it
        # Just record test info
        self.reporter.add_test_result(
            test_name=test_name,
            status="COMPLETED",  # We don't know if it passed or failed here
            duration=test_duration,
            error_message=None,
            screenshot=None  # Screenshots are handled by pytest hook
        )

        self.logger.info(f"Test {test_name} completed")
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        report_path = cls.reporter.generate_report()
        cls.logger.info(f"Test report generated: {report_path}")