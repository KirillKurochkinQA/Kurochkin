import allure
from base.base_page import BasePage
from data.urls import Urls

class InventoryPage(BasePage):
    _PAGE_URL = Urls.INVENTORY_PAGE

    _BIKE_LIGHT_ADD_TO_CART = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    _CART_BUTTON = "//a[@data-test='shopping-cart-link']"
    _SIDEBAR_BURGER_BUTTON = "//button[@id='react-burger-menu-btn']"
    _LOGOUT_BUTTON_IN_SIDEBAR = "//a[@id='logout_sidebar_link']"

    @allure.step("Пользователь нажимает на кнопку добавления товара Bike Light")
    def click_button_bike_light_add_to_cart(self):
        ...

    @allure.step("Пользователь нажимает на кнопку корзины")
    def click_cart_button(self):
        ...

    @allure.step("Пользователь нажимает на кнопку бургер-меню для раскрытия сайдбара")
    def click_sidebar_burger_button(self):
        ...

    @allure.step("Пользователь нажимает на кнопку Логаута в сайдбаре")
    def click_logout_button_in_sidebar(self):
        ...

    # тут можно еще добавить шаги для других товаров и кнопок в сайдбаре
