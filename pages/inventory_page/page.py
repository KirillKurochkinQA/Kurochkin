import allure
from base.base_page import BasePage
from data.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    _PAGE_URL = Urls.INVENTORY_PAGE

    _BIKE_LIGHT_ADD_TO_CART = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    _CART_BADGE = "//span[@data-test='shopping-cart-badge']"
    _CART_BUTTON = "//a[@data-test='shopping-cart-link']"
    _SIDEBAR_BURGER_BUTTON = "//button[@id='react-burger-menu-btn']"
    _LOGOUT_BUTTON_IN_SIDEBAR = "//a[@id='logout_sidebar_link']"

    @allure.step("Пользователь нажимает на кнопку добавления товара Bike Light")
    def click_button_bike_light_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self._BIKE_LIGHT_ADD_TO_CART)).click()
        with allure.step("Пользователь проверяет что, количество товаров в корзине увеличилось"):
            assert self.driver.find_element(*self._CART_BADGE).text == "1", "Товар не добавился в корзину"

    @allure.step("Пользователь нажимает на иконку корзины")
    def click_cart_button(self):
        self.wait.until(EC.element_to_be_clickable(self._CART_BUTTON)).click()

    @allure.step("Пользователь нажимает на кнопку бургер-меню для раскрытия сайдбара")
    def click_sidebar_burger_button(self):
        self.wait.until(EC.element_to_be_clickable(self._SIDEBAR_BURGER_BUTTON)).click()

    @allure.step("Пользователь нажимает на кнопку Логаута в сайдбаре")
    def click_logout_button_in_sidebar(self):
        self.wait.until(EC.element_to_be_clickable(self._LOGOUT_BUTTON_IN_SIDEBAR)).click()

    # тут можно еще добавить шаги для других товаров и кнопок в сайдбаре, а так же сортировку.
