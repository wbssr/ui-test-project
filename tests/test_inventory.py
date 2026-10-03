import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import settings
from pages.cart_page import CartPage
class TestInventory:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        login_page = LoginPage(driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)

    def test_sort_products(self, driver):
        inventory = InventoryPage(driver)
        inventory.sort_by_price_low_to_high()
        prices = inventory.get_product_prices()  # 需要在页面类加这个方法
        assert prices == sorted(prices)

    @pytest.mark.regression
    def test_page_title(self, driver):
        inventory = InventoryPage(driver)
        assert inventory.is_loaded()

    @pytest.mark.flaky
    @pytest.mark.regression
    def test_add_two_products(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_to_cart_by_name("Sauce Labs Backpack")
        inventory.add_to_cart_by_name("Sauce Labs Bike Light")
        inventory.go_to_cart()
        cart = CartPage(driver)
        cart.wait_item_count(2)
        assert cart.get_item_count() == 2