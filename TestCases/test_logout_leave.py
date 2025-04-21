from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import Dashboard
from PageObjects.LeavePage import Leave
import time

class Test_002_Leave_Logout:

    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_leave_functionality(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(3)

        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)

        self.dp = Dashboard(self.driver)
        self.dp.click_my_leave()
        time.sleep(3)

        leave_page = Leave(self.driver)
        result = leave_page.is_leave_page_loaded()
        self.driver.quit()

        assert result, "Leave page did not load"

    def test_logout(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(3)

        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)

        self.dp = Dashboard(self.driver)
        self.dp.click_logout()
        time.sleep(3)

        assert "login" in self.driver.current_url.lower()
        self.driver.quit()
