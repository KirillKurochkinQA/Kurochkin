from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Опции
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--window-size=2560,1440')
options.add_argument('--disable-cache')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Локаторы и переменные
BASE_URL = "https://www.stoloto.ru"
TELEPHONE_FIELD = ("xpath", "//input[@inputmode='tel']")
CONTINUE_BUTTON = ("xpath", "//button[text()='Продолжить']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
AUTH_BUTTON = ("xpath", "//button[text()='Войти']")
RL_IMAGE_AFTER_AUTH = ("xpath", "//img[@class='DialogItem_img__cRhjI']")
CLOSE_BUTTON = ("xpath", "//button[@class='CloseButton_btn__Y3PWt Modal_closeBtn__aapH7']")

# Переход на страницу Промокоды их хэдера меню (c применением Pytest)
class TestPromocodesFromMenuHeader:
    
    def setup_method(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(f"{BASE_URL}/auth")
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5)
        assert "/auth" in self.driver.current_url
        wait.until(EC.element_to_be_clickable(TELEPHONE_FIELD)).clear()
        wait.until(EC.element_to_be_clickable(TELEPHONE_FIELD)).send_keys("+79299115035")
        wait.until(EC.element_to_be_clickable(CONTINUE_BUTTON)).click()
        wait.until(EC.url_to_be(f"{BASE_URL}/auth/login?available=SMS_CODE&from=reg_phone&passwordless=0"))
        wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).clear()
        wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys("123456")
        wait.until(EC.element_to_be_clickable(AUTH_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(RL_IMAGE_AFTER_AUTH))
        self.driver.find_element(*CLOSE_BUTTON).click()
        
    def test_promocodes_from_menu_header(self):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5)
        MENU_HEADER_LOCATOR = ("xpath", "//span[text()='Меню']")
        PROMOCODES_IN_MENU_HEADER_LOCATOR = ("xpath", "//a[text()='Промокоды']")
        MENU_HEADER = self.driver.find_element(*MENU_HEADER_LOCATOR)
        PROMOCODES_IN_MENU_HEADER = self.driver.find_element(*PROMOCODES_IN_MENU_HEADER_LOCATOR)
        action = ActionChains(self.driver)
        action.move_to_element(MENU_HEADER).move_to_element(PROMOCODES_IN_MENU_HEADER).click().perform()
        wait.until(EC.url_to_be(f"{BASE_URL}/private/promocodes/?int=sitemap"))
        assert "/private/promocodes/?int=sitemap" in self.driver.current_url
        self.driver.quit()