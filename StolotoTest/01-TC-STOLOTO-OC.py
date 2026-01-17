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

AUTH_BUTTON = ("xpath", "//a[@href='/auth']")
BASE_URL = "https://www.stoloto.ru/"

driver = webdriver.Chrome(options=options)
driver.get(BASE_URL)

wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

wait.until(EC.url_contains(BASE_URL))
auth_button = wait.until(EC.element_to_be_clickable((AUTH_BUTTON)))

auth_button.click()
wait.until(EC.url_contains(f"{BASE_URL}auth"))

driver.quit()