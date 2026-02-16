import time
import pytest
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-cache')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

class TestStolotoOpenPage:

    def test_stoloto_open_page(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.stoloto.ru")
        time.sleep(20)
        self.driver.quit()
