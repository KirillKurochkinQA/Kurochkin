### Создание тестовых методов (тестов)

from selenium import webdriver

class TestLogin: # Название тестового класса

    def test_open_login_page(self): # Название теста
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/login")
        assert driver.current_url == "https://demoqa.com/login", "Открыта некорректная страница"