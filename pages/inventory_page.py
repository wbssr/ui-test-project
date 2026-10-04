from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from utils.logger import logger
class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_PAGE_MARKER = (By.ID, "checkout")

    def is_loaded(self):
        return self.is_element_present(self.PAGE_TITLE)

    def go_to_cart(self):
        self.click(self.CART_LINK)
        # 点购物车后，等购物车页加载
        self.find(self.CART_PAGE_MARKER)

    def sort_by_price_low_to_high(self):
        Select(self.find(self.SORT_DROPDOWN)).select_by_value("lohi")
        # 等价格列表变成升序
        self.wait.until(
            lambda d: self.get_product_prices() == sorted(self.get_product_prices())
        )

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRICE)
        return [float(e.text.replace("$", "")) for e in elements]

    def add_to_cart_by_name(self, product_name, expected_count=None):
        items = self.driver.find_elements(*self.ITEM)                       #所有商品
        for item in items:
            if item.find_element(*self.ITEM_NAME).text == product_name:     #指定商品
                item.find_element(*self.ADD_BUTTON).click()
                if expected_count is not None:
                    self.wait.until(lambda d: self.get_cart_badge_count() == expected_count)    #等角标
                return
        raise Exception(f"没找到商品: {product_name}")

    def get_cart_badge_count(self):
        """获取购物车角标数量，无角标返回 0"""
        elements = self.driver.find_elements(*self.CART_BADGE)
        if not elements:
            return 0
        return int(elements[0].text)