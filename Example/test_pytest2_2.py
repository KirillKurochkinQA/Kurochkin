### Перезапуск тестов в случае падения во время выполнения

from selenium import webdriver

class TestLogin:    # Название тестового класса

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):     # Тест пройдет
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://", "Ошибка"

    def teardown_method(self):
        self.driver.close()