import allure

from base.base_page import BasePage
from data.urls import Urls

class CheckoutStepTwoPage(BasePage):
    _PAGE_URL = Urls.CHECKOUT_STEP_TWO_PAGE

    _FINISH_BUTTON = "//button[@id='finish']"

    @allure.step("Пользователь нажимает на кнопку Финиш")
    def click_finish_button(self):
        self.driver.find_element(*self._FINISH_BUTTON).click()
