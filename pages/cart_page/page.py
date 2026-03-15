from base.base_page import BasePage
from data.urls import Urls

class CartPage(BasePage):
    _PAGE_URL = Urls.CART_PAGE

    _CHECKOUT_BUTTON = "//button[@id='checkout']"
    _CONTINUE_SHOPPING_BUTTON = ""
    _REMOVE_BUTTON = ""

    def click_checkout_button(self):
        ...

    # тут можно добавить еще кнопки вернутся к товарам и удалить товар из корзины