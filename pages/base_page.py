from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger
import os
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        timeout = 100 if os.getenv("CI") else 10
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        logger.info(f"查找元素: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        logger.info(f"点击元素: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        logger.info(f"输入 {text} 到 {locator}")
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text