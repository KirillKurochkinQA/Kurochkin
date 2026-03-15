from base.base_page import BasePage
from data.urls import Urls

class CheckoutStepOnePage(BasePage):
    _PAGE_URL = Urls.CHECKOUT_STEP_ONE_PAGE

    _FIRST_NAME_FIELD = "//input[@id='first-name']"
    _LAST_NAME_FIELD = "//input[@id='last-name']"
    _POSTAL_CODE_FIELD = "//input[@id='postal-code']"
    _CONTINUE_BUTTON = "//input[@id='continue']"

    def enter_first_name_field(self):
        ...

    def enter_last_name_field(self):
        ...

    def enter_postal_code_field(self):
        ...

    def enter_continue_button(self):
        ...