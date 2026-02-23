### Использование фикстур через request.cls и ее вызов с помощью маркера (декоратора)

import pytest
from selenium import webdriver

# Вызываем фикстуру над классом
class TestExample:

    @pytest.mark.usefixtures("driver")
    def test_example_cls(self):
        # Обращаясь через self к данным, мы легко получаем к ним доступ
        print(self.login, self.password)