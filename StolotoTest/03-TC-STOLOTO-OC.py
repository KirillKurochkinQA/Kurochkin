# Работа с куками (создание файла с куками)
import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--window-size=2560,1440')
options.add_argument('--disable-cache')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

BASE_URL = "https://www.stoloto.ru/"
TELEPHONE_FIELD = ("xpath", "//input[@inputmode='tel']")
CONTINUE_BUTTON = ("xpath", "//button[text()='Продолжить']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
AUTH_BUTTON = ("xpath", "//button[text()='Войти']")

driver = webdriver.Chrome(options=options)
driver.get(f"{BASE_URL}auth")
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

wait.until(EC.element_to_be_clickable(TELEPHONE_FIELD)).clear()
driver.find_element(*TELEPHONE_FIELD).send_keys("+79299115035")

wait.until(EC.element_to_be_clickable(CONTINUE_BUTTON)).click()

wait.until(EC.url_to_be(f"{BASE_URL}auth/login?available=SMS_CODE&from=reg_phone&passwordless=0"))

wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).clear()
driver.find_element(*PASSWORD_FIELD).send_keys("123456")

wait.until(EC.element_to_be_clickable(AUTH_BUTTON)).click()

cookies = driver.get_cookies()
with open("cookies.json", "w") as file:
    json.dump(cookies, file, indent=4)

driver.quit()