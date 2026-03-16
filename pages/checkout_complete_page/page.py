import allure

from base.base_page import BasePage
from data.urls import Urls

class CheckoutCompletePage(BasePage):
    _PAGE_URL = Urls.CHECKOUT_COMPLETE_PAGE

    _BACK_HOME_BUTTON = "//button[@id='back-to-products']"

    @allure.step("Пользователь нажимает на кнопку Домой")
    def click_back_home_button(self):
        self.driver.find_element(*self._BACK_HOME_BUTTON).click()