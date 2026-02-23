import pytest
import os
from collections import namedtuple
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
# from faker import Faker
# fake = Faker()

# @pytest.fixture()
# def generate_data():
#    login = fake.email()
#    password = fake.password()
#    NewUser = namedtuple('UserData', ['login', 'password'])  # именованный tuple
#    return NewUser(login, password) # Возвращаем обьект

#@pytest.fixture(name="driver")
#def generate_data1(request):
#    # Генерируем данные
#    request.cls.login = fake.email()
#    request.cls.password = fake.password()

#@pytest.fixture(autouse=True)
#def driver():
#    driver = webdriver.Chrome()
#    yield driver
#    driver.quit()

@pytest.fixture()
def driver(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(autouse=True)
def setup_environment_properties():
    properties = {
        "STAGE": os.environ["STAGE"],
        "BROWSER": os.environ["BROWSER"],
        "PYTHON": os.environ["PYTHON"],
        "MR": os.environ["MR"]
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")