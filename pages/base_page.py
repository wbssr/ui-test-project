from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger
import os
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        timeout = 30 if os.getenv("CI") else 10
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
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_present(self, locator, timeout=3):
        """短时间内探测元素是否存在，不抛异常"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False