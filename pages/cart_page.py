from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")
    CHECKOUT_PAGE_MARKER = (By.ID, "continue")

    def is_loaded(self):
        return self.is_element_present(self.CHECKOUT_BUTTON)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        # 点 checkout 后，等结算页加载
        self.find(self.CHECKOUT_PAGE_MARKER)

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM))

    def wait_item_count(self, n):
        self.wait.until(lambda d: self.get_item_count() == n)

    def remove_item_by_name(self, product_name):
        items = self.driver.find_elements(*self.CART_ITEM)
        for item in items:
            if item.find_element(*self.ITEM_NAME).text == product_name:
                item.find_element(*self.REMOVE_BUTTON).click()
                return
        raise Exception(f"购物车里没有: {product_name}")