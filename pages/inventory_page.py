from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def is_loaded(self):
        return self.get_text(self.PAGE_TITLE) == "Products"

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_LINK)

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def sort_by_price_low_to_high(self):
        from selenium.webdriver.support.ui import Select
        Select(self.find(self.SORT_DROPDOWN)).select_by_value("lohi")

    ADD_SECOND_ITEM = (By.ID, "add-to-cart-sauce-labs-bike-light")

    def add_second_item_to_cart(self):
        self.click(self.ADD_SECOND_ITEM)