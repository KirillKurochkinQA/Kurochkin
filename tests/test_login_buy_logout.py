import time

from base.base_test import BaseTest

class TestLoginBuyLogout(BaseTest):

    def test_login_buy_logout(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )
        time.sleep(5)