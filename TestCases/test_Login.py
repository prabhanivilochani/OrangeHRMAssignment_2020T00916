# TestCases/test_Login.py
import time

from Configuration.config import TestConfig
from PageObjects.LoginPage import Login
from Utilities.base_test import BaseTest
from TestData.test_data import TestData


class Test_001_Login(BaseTest):
    def test_Title(self):
        self.driver.get(TestConfig.BASE_URL)
        self.logger.info("Opened the application URL")
        time.sleep(2)  # Just for demonstration; better to use explicit waits

        act_title = self.driver.title
        exp_title = "OrangeHRM"

        self.assertEqual(act_title, exp_title, "Title verification failed")
        self.logger.info("Title verification passed")

    def test_login(self):
        self.driver.get(TestConfig.BASE_URL)
        self.logger.info("Opened the application URL")

        # Get test data
        test_data = TestData.get_json_data("login_data.json")
        valid_login = test_data["valid_login"]

        self.lp = Login(self.driver)
        self.lp.setUsername(valid_login["username"])
        self.logger.info("Entered username")

        self.lp.setPassword(valid_login["password"])
        self.logger.info("Entered password")

        self.lp.clickLogin()
        self.logger.info("Clicked login button")

        time.sleep(2)  # For demonstration purposes

        act_title = self.driver.title
        exp_title = "OrangeHRM"

        self.assertEqual(act_title, exp_title, "Login test failed")
        self.logger.info("Login test passed")