import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config.settings import settings

class TestCart:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        login_page = LoginPage(driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)

    @pytest.mark.flaky
    @pytest.mark.smoke
    def test_add_and_remove_item(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.get_item_count() == 1
        cart.remove_first_item()
        assert cart.get_item_count() == 0

    @pytest.mark.flaky
    @pytest.mark.regression
    def test_cart_empty_checkout(self, driver):
        inventory = InventoryPage(driver)
        inventory.go_to_cart()
        cart = CartPage(driver)
        # 空购物车点结账应该跳回或提示，这里验证页面可操作
        assert cart.is_loaded() == True