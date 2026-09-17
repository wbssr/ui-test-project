import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import settings

class TestInventory:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        login_page = LoginPage(driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)

    def test_sort_products(self, driver):
        inventory = InventoryPage(driver)
        inventory.sort_by_price_low_to_high()
        assert inventory.is_loaded() == True

    @pytest.mark.regression
    def test_page_title(self, driver):
        inventory = InventoryPage(driver)
        assert inventory.is_loaded() == True

    @pytest.mark.flaky
    @pytest.mark.regression
    def test_add_two_products(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_backpack_to_cart()
        inventory.add_second_item_to_cart()
        inventory.go_to_cart()

        from pages.cart_page import CartPage
        cart = CartPage(driver)
        assert cart.get_item_count() == 2