import allure
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.faker = Faker()

    def open(self):
        with allure.step(f"Пользователь открывает страницу {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)

    def is_opened(self):
        with allure.step(f"Пользователь проверяет что открыта страница {self._PAGE_URL}"):
            self.wait.until(EC.url_to_be(self._PAGE_URL))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f"Скриншот открытой страницы {self._PAGE_URL}",
                attachment_type=allure.attachment_type.PNG
            )