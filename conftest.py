import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker
fake = Faker()
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(autouse=True)
def driver(request):

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    request.cls.first_name = fake.first_name()
    request.cls.last_name = fake.last_name()
    request.cls.postal_code = fake.postcode()
    yield driver
    driver.quit()
