### PyTest. Фикстуры

import pytest
from selenium import webdriver

class TestExample:

    def test_login(self, generate_data):
        login = generate_data.login
        password = generate_data.password
        print(login)
        print(password)