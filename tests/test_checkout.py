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
        login_page.login_success(settings.USERNAME, settings.PASSWORD)

    @pytest.mark.flaky
    @pytest.mark.smoke
    def test_complete_checkout(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_to_cart_by_name("Sauce Labs Backpack",expected_count=1)
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info_success("张", "三", "100000")
        checkout.finish()

        assert "Thank you" in checkout.get_complete_header()

    @pytest.mark.flaky
    @pytest.mark.regression
    def test_checkout_missing_info(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_to_cart_by_name("Sauce Labs Backpack",expected_count=1)
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("", "", "")
        # 缺少信息时继续，会停在当前页，简单断言页面元素还在
        assert checkout.is_loaded()

    @pytest.mark.flaky
    @pytest.mark.regression
    def test_checkout_complete_header(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_to_cart_by_name("Sauce Labs Backpack",expected_count=1)
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info_success("张", "三", "100000")
        checkout.finish()

        assert "Thank you" in checkout.get_complete_header()

    @pytest.mark.flaky
    @pytest.mark.regression
    def test_cancel_checkout_keeps_cart(self, driver):
        """结账中途取消，购物车商品保留"""
        inventory = InventoryPage(driver)
        inventory.add_to_cart_by_name("Sauce Labs Backpack",expected_count=1)
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.is_loaded()
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.cancel()

        cart = CartPage(driver)
        cart.wait_item_count(1)
        assert cart.get_item_count() == 1

    @pytest.mark.flaky
    @pytest.mark.regression
    def test_form_data_not_persisted_on_refresh(self, driver):
        """填写信息后刷新，表单数据清空"""
        inventory = InventoryPage(driver)
        inventory.add_to_cart_by_name("Sauce Labs Backpack",expected_count=1)
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.is_loaded()
        cart.wait_item_count(1)
        cart.checkout()

        checkout = CheckoutPage(driver)
        assert checkout.is_loaded()
        checkout.input_text(checkout.FIRST_NAME, "张")
        checkout.input_text(checkout.LAST_NAME, "三")

        # 刷新页面
        driver.refresh()

        # 验证表单已清空
        first_name_value = driver.find_element(*checkout.FIRST_NAME).get_attribute("value")
        assert first_name_value == ""