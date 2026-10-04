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

    def is_loaded(self):
        return self.get_text(self.PAGE_TITLE) == "Products"

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def sort_by_price_low_to_high(self):
        Select(self.find(self.SORT_DROPDOWN)).select_by_value("lohi")

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRICE)
        return [float(e.text.replace("$", "")) for e in elements]

    def add_to_cart_by_name(self, product_name):
        items = self.driver.find_elements(*self.ITEM)          # 所有商品卡片
        for item in items:
            name = item.find_element(*self.ITEM_NAME).text     # 卡片里的名字
            if name == product_name:
                item.find_element(*self.ADD_BUTTON).click()    # 点这张卡片的按钮
                return
        raise Exception(f"没找到商品: {product_name}")

    def get_cart_badge_count(self):
        """获取购物车角标数量，无角标返回 0"""
        elements = self.driver.find_elements(*self.CART_BADGE)
        if not elements:
            return 0
        return int(elements[0].text)