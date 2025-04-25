from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Configuration.config import TestConfig


class DriverFactory:
    @staticmethod
    def get_driver(browser=None):
        if browser is None:
            browser = TestConfig.BROWSER

        if browser.lower() == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise Exception("Browser not supported")

        driver.maximize_window()
        driver.implicitly_wait(TestConfig.IMPLICIT_WAIT)
        return driver