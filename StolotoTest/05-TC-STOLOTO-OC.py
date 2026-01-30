# Переход в личный кабинет после авторизации со страницы кошелька
import time

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
BALANCE_BUTTON = ("xpath", "//span[@class='Account_balance__pONDE']")
ZP_IMAGE_AFTER_AUTH = ("xpath", "//img[@alt='splash_zp_544_3001_05w']")
PROFILE_BUTTON_IN_LK = ("xpath", "//span[text()='Профиль']")

driver = webdriver.Chrome(options=options)
driver.get(f"{BASE_URL}auth")
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

wait.until(EC.element_to_be_clickable(TELEPHONE_FIELD)).clear()
wait.until(EC.element_to_be_clickable(TELEPHONE_FIELD)).send_keys("+79299115035")

wait.until(EC.element_to_be_clickable(CONTINUE_BUTTON)).click()
wait.until(EC.url_to_be(f"{BASE_URL}auth/login?available=SMS_CODE&from=reg_phone&passwordless=0"))

wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).clear()
wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys("123456")

wait.until(EC.element_to_be_clickable(AUTH_BUTTON)).click()

if wait.until(EC.visibility_of_element_located(ZP_IMAGE_AFTER_AUTH)):
    driver.find_element("xpath", "//button[@class='CloseButton_btn__Y3PWt Modal_closeBtn__aapH7']").click()


wait.until(EC.element_to_be_clickable(BALANCE_BUTTON)).click()

wait.until(EC.url_to_be(f"{BASE_URL}private/wallet?int=header"))


wait.until(EC.element_to_be_clickable(PROFILE_BUTTON_IN_LK)).click()

wait.until(EC.url_to_be(f"{BASE_URL}private/data"))

driver.quit()