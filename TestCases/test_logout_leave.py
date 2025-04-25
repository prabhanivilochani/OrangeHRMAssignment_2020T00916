# TestCases/test_Logout_Leave.py
import time

from Configuration.config import TestConfig
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import Dashboard
from PageObjects.LeavePage import Leave
from Utilities.base_test import BaseTest
from TestData.test_data import TestData


class Test_002_Leave_Logout(BaseTest):
    def test_leave_functionality(self):
        self.driver.get(TestConfig.BASE_URL)
        self.logger.info("Opened the application URL")

        # Get test data
        test_data = TestData.get_json_data("login_data.json")
        valid_login = test_data["valid_login"]

        self.lp = Login(self.driver)
        self.lp.setUsername(valid_login["username"])
        self.lp.setPassword(valid_login["password"])
        self.lp.clickLogin()
        self.logger.info("Logged in successfully")

        time.sleep(3)  # For demonstration purposes

        self.dp = Dashboard(self.driver)
        self.dp.click_my_leave()
        self.logger.info("Clicked on My Leave")

        time.sleep(2)  # For demonstration purposes

        leave_page = Leave(self.driver)
        result = leave_page.is_leave_page_loaded()

        self.assertTrue(result, "Leave page did not load")
        self.logger.info("Leave page loaded successfully")

    def test_logout(self):
        self.driver.get(TestConfig.BASE_URL)
        self.logger.info("Opened the application URL")

        # Get test data
        test_data = TestData.get_json_data("login_data.json")
        valid_login = test_data["valid_login"]

        self.lp = Login(self.driver)
        self.lp.setUsername(valid_login["username"])
        self.lp.setPassword(valid_login["password"])
        self.lp.clickLogin()
        self.logger.info("Logged in successfully")

        time.sleep(3)  # For demonstration purposes

        self.dp = Dashboard(self.driver)
        self.dp.click_logout()
        self.logger.info("Clicked on logout")

        time.sleep(2)  # For demonstration purposes

        self.assertTrue("login" in self.driver.current_url.lower(), "Logout failed")
        self.logger.info("Logout successful")