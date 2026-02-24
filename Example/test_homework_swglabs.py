# import time
import pytest
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType

BASE_URL = "https://www.saucedemo.com/"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"

@allure.epic("Swag Labs")
@allure.feature("Login and buy")
@allure.story("Pages")
@pytest.mark.usefixtures("driver")
class TestBuyInventory:

    @pytest.mark.regression
    @allure.title("Покупка товара авторизованным пользователем из корзины")
    @allure.severity(Severity.CRITICAL)
    @allure.link(url="https://www.saucedemo.com/documentation", name="Документация по сайту")
    def test_login_and_buy(self):
        with allure.step("Пользователь открывает сайт https://www.saucedemo.com/"):
            self.driver.get(BASE_URL)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Главная страница сайта",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Пользователь проверяет URL на корректность: https://www.saucedemo.com/"):
            assert self.driver.current_url == BASE_URL, "URL не совпадает с ожидаемым"

        with allure.step("Пользователь вводит данные в поле логин"):
            login_field = self.driver.find_element("xpath", "//input[@id='user-name']")
            login_field.clear()
            login_field.send_keys(LOGIN)
        with allure.step("Пользователь проверяет введеный логин на корректность"):
            assert login_field.get_attribute("value") == LOGIN, "Логин введен неправильно"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Поле логин - корректный ввод",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Пользователь вводит данные в поле пароль"):
            password_field = self.driver.find_element("xpath", "//input[@id='password']")
            password_field.clear()
            password_field.send_keys(PASSWORD)
        with allure.step("Пользователь проверяет введеный пароль на корректность"):
            assert password_field.get_attribute("value") == PASSWORD, "Пароль введен неправильно"

        with allure.step("Пользователь нажимает на кнопку входа"):
            login_button = self.driver.find_element("xpath", "//input[@id='login-button']")
            login_button.click()
            self.wait.until(EC.url_to_be(f"{BASE_URL}inventory.html"))
        with allure.step("Пользователь проверяет успешную авторизацию и открытие страницы с товарами"):
            assert self.driver.current_url == f"{BASE_URL}inventory.html", "URL не совпадает с ожидаемым результатом"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Успешная авторизация - открытие страницы с товарами",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Пользователь находит товар Лампочка от мотоцикла и нажимает на кнопку добавления товара в корзину"):
            add_bike_light_button = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
            add_bike_light_button.click()
        with allure.step("Пользователь проверяет что на иконке корзины в хэдере 1 товар"):
            shopping_cart_badge = self.driver.find_element("xpath", "//span[@data-test='shopping-cart-badge']")
            assert shopping_cart_badge.text == "1", "Товар не добавился в корзину"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="1 товар в иконке корзины",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Пользователь нажимает на иконку корзины"):
            shopping_cart_button = self.driver.find_element("xpath", "//a[@data-test='shopping-cart-link']")
            shopping_cart_button.click()
        with allure.step("Пользователь переходит в корзину и проверяет успешную загрузку страницы"):
            self.wait.until(EC.url_to_be(f"{BASE_URL}cart.html"))
            assert self.driver.current_url == f"{BASE_URL}cart.html", "URL не совпадает с ожидаемым результатом"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Переход в корзину - успешная загрузка страницы",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Пользователь проверяет, что в корзину добавлена именно Лампочка мотоцикла и она отображается"):
            inventory_item_name_in_shopping_cart = self.driver.find_element("xpath", "//div[text()='Sauce Labs Bike Light']")
            assert inventory_item_name_in_shopping_cart.is_displayed(), "Товар не отображается в корзине"
        with allure.step("Пользователь нажимает на кнопку чекаут"):
            checkout_button = self.driver.find_element("xpath", "//button[@id='checkout']")
            checkout_button.click()
        with allure.step("Пользователь проверяет что совершился переход на страницу первого шага оформления товара"):
            self.wait.until(EC.url_to_be(f"{BASE_URL}checkout-step-one.html"))
            assert self.driver.current_url == f"{BASE_URL}checkout-step-one.html", "URL не совпадает с ожидаемым результатом"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Страница первого шага оформления товара",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Пользователь вводит имя, фамилию и почтовый индекс"):
            first_name_field = self.driver.find_element("xpath", "//input[@id='first-name']")
            first_name_field.clear()
            first_name_field.send_keys(self.first_name)
            assert first_name_field.get_attribute("value") == self.first_name, "Введено неправильное имя"

            last_name_field = self.driver.find_element("xpath", "//input[@id='last-name']")
            last_name_field.clear()
            last_name_field.send_keys(self.last_name)
            assert last_name_field.get_attribute("value") == self.last_name, "Введена неправильная фамилия"

            postal_code_field = self.driver.find_element("xpath", "//input[@id='postal-code']")
            postal_code_field.clear()
            postal_code_field.send_keys(self.postal_code)
            assert postal_code_field.get_attribute("value") == self.postal_code, "Введен неправильный почтовый индекс"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Поля успешно заполнены",
                attachment_type=allure.attachment_type.PNG
            )
            user_data = f"Имя: {self.first_name}\nФамилия: {self.last_name}\nИндекс: {self.postal_code}"
            allure.attach(
                body=user_data,
                name="Сгенерированные данные пользователя",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Пользователь нажимает на кнопку Продолжить"):
            continue_button = self.driver.find_element("xpath", "//input[@id='continue']")
            continue_button.click()
        with allure.step("Пользователь проверяет что совершился переход на страницу второго шага оформления товара"):
            self.wait.until(EC.url_to_be(f"{BASE_URL}checkout-step-two.html"))
            assert self.driver.current_url == f"{BASE_URL}checkout-step-two.html", "URL не совпадает с ожидаемым результатом"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Страница второго шага оформления товара",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Пользователь завершает оформление покупки и нажимает на кнопку Финиш"):
            finish_button = self.driver.find_element("xpath", "//button[@id='finish']")
            finish_button.click()
        with allure.step("Пользователь проверяет переход на страницу успешного офорлмения заказа"):
            self.wait.until(EC.url_to_be(f"{BASE_URL}checkout-complete.html"))
            assert self.driver.current_url == f"{BASE_URL}checkout-complete.html", "URL не совпадает с ожидаемым результатом"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Страница успешного оформления заказа",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Пользователь нажимает на кнопку вернутся на главную"):
            back_home_button = self.driver.find_element("xpath", "//button[@id='back-to-products']")
            back_home_button.click()
        with allure.step("Пользователь проверяет что состоялся переход на главную"):
            self.wait.until(EC.url_to_be(f"{BASE_URL}inventory.html"))
            assert self.driver.current_url == f"{BASE_URL}inventory.html", "URL не совпадает с ожидаемым результатом"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Главная страница после покупки",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Пользователь раскрывает бургер-меню"):
            burger_button = self.driver.find_element("xpath", "//button[@id='react-burger-menu-btn']")
            burger_button.click()

        with allure.step("Пользователь совершает разлогин"):
            logout_button = self.wait.until(EC.element_to_be_clickable(("xpath", "//a[@id='logout_sidebar_link']")))
            logout_button.click()
            self.wait.until(EC.url_to_be(f"{BASE_URL}"))
            assert self.driver.current_url == BASE_URL, "URL не совпадает с ожидаемым результатом"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Пользователь успешно разлогинен",
                attachment_type=allure.attachment_type.PNG
            )