import time
import allure
from base.base_test import BaseTest

@allure.epic("Основная функция сайта")
@allure.feature("Покупка авторизованным пользователем")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Здесь по идее можно написать какое-то описание")
@allure.tag("smoke", "regression", "ui")
class TestLoginBuyLogout(BaseTest):

    @allure.title("Авторизация, покупка, разлогин")
    @allure.id(1)
    @allure.story("Покупка товара")
    @allure.suite("Тест на проверку покупки авторизованным пользователем и разлогин")
    def test_login_buy_logout(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(login=self.credentials.LOGIN)
        self.login_page.enter_password(password=self.credentials.PASSWORD)
        self.login_page.click_login_button()
        self.inventory_page.is_opened()
        time.sleep(1)