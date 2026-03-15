from base.base_page import BasePage
from data.urls import Urls

class CheckoutCompletePage(BasePage):
    _PAGE_URL = Urls.CHECKOUT_COMPLETE_PAGE

    _BACK_HOME_BUTTON = "//button[@id='back-to-products']"

    def click_back_home_button(self):
        ...