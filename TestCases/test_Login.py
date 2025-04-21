from selenium import webdriver
from PageObjects.LoginPage import Login
import time

class Test_001_Login:

    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"


    def test_Title(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(5)
        act_title = self.driver.title
        self.driver.quit()


        if act_title == "OrangeHRM":
            assert True
            print("Title matches: Test Passed")
        else:
            assert False
            print("Title doesn't match: Test Failed")


    def test_login(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(3)

        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)

        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(3)
        act_title = self.driver.title
        self.driver.quit()

        if act_title == "OrangeHRM":
            assert True
            print("Title correct: Test Passed")
        else:
            assert False
            print("Title incorrect: Test Failed")
