import pytest
from collections import namedtuple
from faker import Faker
fake = Faker()

@pytest.fixture()
def generate_data():
    login = fake.email()
    password = fake.password()
    NewUser = namedtuple('UserData', ['login', 'password'])  # именованный tuple
    return NewUser(login, password) # Возвращаем обьект

@pytest.fixture(name="driver")
def generate_data1(request):
    # Генерируем данные
    request.cls.login = fake.email()
    request.cls.password = fake.password()