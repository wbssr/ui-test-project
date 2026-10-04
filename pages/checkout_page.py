from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    CANCEL_BUTTON = (By.ID, "cancel")

    def fill_info(self, first, last, postal):
        self.input_text(self.FIRST_NAME, first)
        self.input_text(self.LAST_NAME, last)
        self.input_text(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BUTTON)

    def finish(self):
        self.click(self.FINISH_BUTTON)

    def cancel(self):
        self.click(self.CANCEL_BUTTON)

    def get_complete_header(self):
        return self.get_text(self.COMPLETE_HEADER)

    def is_loaded(self):
        try:
            self.find(self.CONTINUE_BUTTON)
            return True
        except TimeoutException:
            return False