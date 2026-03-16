import allure

from base.base_page import BasePage
from data.urls import Urls

class CartPage(BasePage):
    _PAGE_URL = Urls.CART_PAGE

    _CHECKOUT_BUTTON = "//button[@id='checkout']"
    _BIKE_LIGHT_ITEM_NAME_IN_CART = "//div[@class='inventory_item_name']"

    @allure.step("Пользователь проверяет что товар отображается на странице корзины")
    def is_bike_light_displayed(self):
        assert self.driver.find_element(*self._BIKE_LIGHT_ITEM_NAME_IN_CART).text == "Sauce Labs Bike Light"

    @allure.step("Пользователь нажимает на кнопку Чекаут для продолжения оформления товара")
    def click_checkout_button(self):
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()

    # тут можно добавить еще кнопки вернутся к товарам и удалить товар из корзины