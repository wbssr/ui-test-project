import pytest
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import settings
from utils.data_loader import load_json

USERS_DATA = load_json(
    os.path.join("config", "test_data", "users.json")
)

class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize("user", USERS_DATA["valid_users"])
    def test_login_success(self, driver, user):
        """数据驱动：多个有效用户登录成功"""
        login_page = LoginPage(driver)
        login_page.login(user["username"], user["password"])

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_loaded()

    @pytest.mark.regression
    @pytest.mark.parametrize("user", USERS_DATA["invalid_users"])
    def test_login_invalid(self, driver, user):
        """数据驱动：多个无效用户登录失败"""
        login_page = LoginPage(driver)
        login_page.login(user["username"], user["password"])

        assert user["expected"] in login_page.get_error_message()

    @pytest.mark.regression
    def test_logout_keeps_cart(self, driver):
        """退出登录后重新登录，购物车商品保留"""
        login_page = LoginPage(driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)

        inventory = InventoryPage(driver)
        inventory.add_to_cart_by_name("Sauce Labs Backpack")
        assert inventory.get_cart_badge_count() == 1

        login_page.logout()

        # 重新登录
        login_page.login(settings.USERNAME, settings.PASSWORD)
        inventory = InventoryPage(driver)
        assert inventory.get_cart_badge_count() == 1

    @pytest.mark.regression
    def test_reset_app_state_clears_cart(self, driver):
        """Reset App State 清空购物车"""
        login_page = LoginPage(driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)

        inventory = InventoryPage(driver)
        inventory.add_to_cart_by_name("Sauce Labs Backpack")
        assert inventory.get_cart_badge_count() == 1

        login_page.reset_app_state()

        # 刷新页面
        driver.refresh()
        inventory = InventoryPage(driver)
        assert inventory.get_cart_badge_count() == 0