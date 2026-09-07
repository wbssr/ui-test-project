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
        assert inventory_page.is_loaded() == True

    @pytest.mark.regression
    @pytest.mark.parametrize("user", USERS_DATA["invalid_users"])
    def test_login_invalid(self, driver, user):
        """数据驱动：多个无效用户登录失败"""
        login_page = LoginPage(driver)
        login_page.login(user["username"], user["password"])

        assert user["expected"] in login_page.get_error_message()