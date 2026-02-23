import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument('--window-size=1920,1080')
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
BASE_URL = "https://www.saucedemo.com/"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "Kirill"
LAST_NAME = "Kurochkin"
POSTAL_CODE = "149985"

driver = webdriver.Chrome(options=options)
driver.get(BASE_URL)
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
assert driver.current_url == BASE_URL

login_field = driver.find_element("xpath", "//input[@id='user-name']")
login_field.clear()
login_field.send_keys(LOGIN)
assert login_field.get_attribute("value") == LOGIN, "Логин введен неправильно"

password_field = driver.find_element("xpath", "//input[@id='password']")
password_field.clear()
password_field.send_keys(PASSWORD)
assert password_field.get_attribute("value") == PASSWORD, "Пароль введен неправильно"

login_button = driver.find_element("xpath", "//input[@id='login-button']")
login_button.click()
wait.until(EC.url_to_be(f"{BASE_URL}inventory.html"))
assert driver.current_url == f"{BASE_URL}inventory.html", "URL не совпадает с ожидаемым результатом"

add_bike_light_button = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
add_bike_light_button.click()

shopping_cart_badge = driver.find_element("xpath", "//span[@data-test='shopping-cart-badge']")
assert shopping_cart_badge.text == "1", "Товар не добавился в корзину"

shopping_cart_button = driver.find_element("xpath", "//a[@data-test='shopping-cart-link']")
shopping_cart_button.click()
wait.until(EC.url_to_be(f"{BASE_URL}cart.html"))
assert driver.current_url == f"{BASE_URL}cart.html", "URL не совпадает с ожидаемым результатом"

checkout_button = driver.find_element("xpath", "//button[@id='checkout']")
checkout_button.click()
wait.until(EC.url_to_be(f"{BASE_URL}checkout-step-one.html"))
assert driver.current_url == f"{BASE_URL}checkout-step-one.html", "URL не совпадает с ожидаемым результатом"

first_name_field = driver.find_element("xpath", "//input[@id='first-name']")
first_name_field.clear()
first_name_field.send_keys(FIRST_NAME)
assert first_name_field.get_attribute("value") == FIRST_NAME, "Введено неправильное имя"

last_name_field = driver.find_element("xpath", "//input[@id='last-name']")
last_name_field.clear()
last_name_field.send_keys(LAST_NAME)
assert last_name_field.get_attribute("value") == LAST_NAME, "Введена неправильная фамилия"

postal_code_field = driver.find_element("xpath", "//input[@id='postal-code']")
postal_code_field.clear()
postal_code_field.send_keys(POSTAL_CODE)
assert postal_code_field.get_attribute("value") == POSTAL_CODE, "Введен неправильный почтовый индекс"

continue_button = driver.find_element("xpath", "//input[@id='continue']")
continue_button.click()
wait.until(EC.url_to_be(f"{BASE_URL}checkout-step-two.html"))
assert driver.current_url == f"{BASE_URL}checkout-step-two.html", "URL не совпадает с ожидаемым результатом"

finish_button = driver.find_element("xpath", "//button[@id='finish']")
finish_button.click()
wait.until(EC.url_to_be(f"{BASE_URL}checkout-complete.html"))
assert driver.current_url == f"{BASE_URL}checkout-complete.html", "URL не совпадает с ожидаемым результатом"

back_home_button = driver.find_element("xpath", "//button[@id='back-to-products']")
back_home_button.click()
wait.until(EC.url_to_be(f"{BASE_URL}inventory.html"))
assert driver.current_url == f"{BASE_URL}inventory.html", "URL не совпадает с ожидаемым результатом"

burger_button = driver.find_element("xpath", "//button[@id='react-burger-menu-btn']")
burger_button.click()

logout_button = wait.until(EC.element_to_be_clickable(("xpath", "//a[@id='logout_sidebar_link']")))
logout_button.click()
wait.until(EC.url_to_be(f"{BASE_URL}"))
assert driver.current_url == BASE_URL, "URL не совпадает с ожидаемым результатом"

driver.quit()
print("Все тесты пройдены успешно")