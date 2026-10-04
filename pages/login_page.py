from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    INVENTORY_TITLE = (By.CLASS_NAME, "title")

    def is_loaded(self):
        return self.is_element_present(self.USERNAME_INPUT)

    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def login_success(self, username, password):
        """登录成功，等商品页"""
        self.login(username, password)
        # 登录后等商品页加载
        self.find(self.INVENTORY_TITLE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click_visibility(self.LOGOUT_LINK)
        # 登出后等登录页
        self.find(self.USERNAME_INPUT)

    def reset_app_state(self):
        self.click(self.MENU_BUTTON)
        self.click_visibility(self.RESET_LINK)