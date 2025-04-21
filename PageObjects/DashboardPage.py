from selenium.webdriver.common.by import By

class Dashboard:

    my_leave_icon_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[5]/button"
    user_dropdown_xpath = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/span"
    logout_xpath = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a"

    def __init__(self, driver):
        self.driver = driver

    def click_my_leave(self):
        self.driver.find_element(By.XPATH, self.my_leave_icon_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.user_dropdown_xpath).click()
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
