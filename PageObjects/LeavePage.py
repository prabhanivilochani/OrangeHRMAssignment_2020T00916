class Leave:

    def __init__(self, driver):
        self.driver = driver

    def is_leave_page_loaded(self):
        return "leave" in self.driver.current_url.lower()
