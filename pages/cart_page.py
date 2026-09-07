from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_loaded(self):
        return self.get_text(self.PAGE_TITLE) == "Your Cart"

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM))

    def remove_first_item(self):
        self.click(self.REMOVE_BUTTON)