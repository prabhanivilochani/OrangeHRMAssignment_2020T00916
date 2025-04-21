
from selenium.webdriver.common.by import By


class Login:

    Username = "username"
    Password = "password"
    btn_login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):

        self.driver.find_element(By.NAME, self.Username).clear()
        self.driver.find_element(By.NAME, self.Username).send_keys(username)


    def setPassword(self, password):

        self.driver.find_element(By.NAME, self.Password).clear()
        self.driver.find_element(By.NAME, self.Password).send_keys(password)


    def clickLogin(self):

        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
