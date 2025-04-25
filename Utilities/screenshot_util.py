
import os
import datetime


class ScreenshotUtil:
    @staticmethod
    def capture_screenshot(driver, test_name):
        screenshot_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Screenshots'))

        # Create the directory if it doesn't exist
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_file = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_file)

        driver.save_screenshot(screenshot_path)
        return screenshot_path