import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.settings import settings

class TestCheckout:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        login_page = LoginPage(driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)

    @pytest.mark.smoke
    def test_complete_checkout(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("张", "三", "100000")
        checkout.finish()

        assert "Thank you" in checkout.get_complete_header()

    @pytest.mark.regression
    def test_checkout_missing_info(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("", "", "")
        # 缺少信息时继续，会停在当前页，简单断言页面元素还在
        assert checkout.is_loaded() == True

    @pytest.mark.regression
    def test_checkout_complete_header(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("张", "三", "100000")
        checkout.finish()

        assert "Thank you" in checkout.get_complete_header()