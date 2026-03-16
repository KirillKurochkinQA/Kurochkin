import allure

from base.base_page import BasePage
from data.urls import Urls

class CheckoutStepOnePage(BasePage):
    _PAGE_URL = Urls.CHECKOUT_STEP_ONE_PAGE

    _FIRST_NAME_FIELD = "//input[@id='first-name']"
    _LAST_NAME_FIELD = "//input[@id='last-name']"
    _POSTAL_CODE_FIELD = "//input[@id='postal-code']"
    _CONTINUE_BUTTON = "//input[@id='continue']"

    @allure.step("Пользователь вводит свое имя")
    def enter_first_name_field(self):
        self.driver.find_element(*self._FIRST_NAME_FIELD).send_keys(self.faker.first_name())
        first_name = self.faker.first_name()
        allure.attach(
            body=first_name,
            name="Имя",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Пользователь вводит свою фамилию")
    def enter_last_name_field(self):
        self.driver.find_element(*self._LAST_NAME_FIELD).send_keys(self.faker.last_name())
        last_name = self.faker.last_name()
        allure.attach(
            body=last_name,
            name="Фамилия",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Пользователь вводит свой почтовый индекс")
    def enter_postal_code_field(self):
        self.driver.find_element(*self._POSTAL_CODE_FIELD).send_keys(self.faker.postcode())
        postal_code = self.faker.postcode()
        allure.attach(
            body=postal_code,
            name="Почтовый индекс",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Пользователь нажимает на кнопку Продолжить")
    def click_continue_button(self):
        self.driver.find_element(*self._CONTINUE_BUTTON).click()