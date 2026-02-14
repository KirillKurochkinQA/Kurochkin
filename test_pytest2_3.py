### Остановка тестов после N падений

from selenium import webdriver

class TestLogin:    # Название тестового класса

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):     # Тест упадет
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://", "Ошибка"

    def test_open_books_page(self):     # Тест упадет
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://", "Ошибка"

    def test_open_profile_page(self):     # Тест пройдет
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка"

    def teardown_method(self):
        self.driver.quit()