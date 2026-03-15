from data.credentials import Credentials
from pages.login_page.page import LoginPage
from pages.inventory_page.page import InventoryPage
from pages.cart_page.page import CartPage
from pages.checkout_step_one_page.page import CheckoutStepOnePage
from pages.checkout_step_two_page.page import CheckoutStepTwoPage
from pages.checkout_complete_page.page import CheckoutCompletePage


class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_step_one_page = CheckoutStepOnePage(self.driver)
        self.checkout_step_two_page = CheckoutStepTwoPage(self.driver)
        self.checkout_complete_page = CheckoutCompletePage(self.driver)