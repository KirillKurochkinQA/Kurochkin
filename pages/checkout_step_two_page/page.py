from base.base_page import BasePage
from data.urls import Urls

class CheckoutStepTwoPage(BasePage):
    _PAGE_URL = Urls.CHECKOUT_STEP_TWO_PAGE

    _FINISH_BUTTON = "//button[@id='finish']"

    def click_finish_button(self):
        ...
