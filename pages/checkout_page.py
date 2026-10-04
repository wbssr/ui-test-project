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

    def is_loaded(self):
        return self.is_element_present(self.CONTINUE_BUTTON)

    def fill_info(self, first, last, postal):
        self.input_text(self.FIRST_NAME, first)
        self.input_text(self.LAST_NAME, last)
        self.input_text(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BUTTON)

    def fill_info_success(self, first, last, postal):
        self.fill_info(first, last, postal)
        # 点 continue 后，等确认页（finish 按钮出现）
        self.find(self.FINISH_BUTTON)

    def finish(self):
        self.click(self.FINISH_BUTTON)
        # 点 finish 后，等完成页
        self.find(self.COMPLETE_HEADER)

    def cancel(self):
        self.click(self.CANCEL_BUTTON)

    def get_complete_header(self):
        return self.get_text(self.COMPLETE_HEADER)

