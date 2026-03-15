import allure
from base.base_page import BasePage
from data.urls import Urls
from data.credentials import Credentials
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    _PAGE_URL = Urls.LOGIN_PAGE

    _LOGIN_FIELD = "//input[@id='user-name']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _LOGIN_BUTTON = "//input[@id='login-button']"


    @allure.step("Пользователь вводит логин")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_FIELD)).send_keys(login)

    @allure.step("Пользователь вводит пароль")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self._PASSWORD_FIELD)).send_keys(password)

    @allure.step("Пользователь нажимает на кнопку входа")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()