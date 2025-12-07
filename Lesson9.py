# Задача 1
# Создай класс Car, у которого будет общий атрибут wheels со значением 4.
# У класса должен быть конструктор __init__, принимающий аргумент brand и сохраняющий его как атрибут экземпляра.
# Также создай метод get_info, который выводит строку вида: "Это автомобиль марки <brand> с <wheels> колёсами."
# (используй атрибуты экземпляра и класса внутри метода).
# После этого создай объект этого класса с любой маркой и вызови метод get_info.
class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    def get_info(self):
        print(f"Это автомобиль марки {self.brand} с {self.wheels} колёсами.")

my_car = Car("Hyundai")
my_car.get_info()

# Задача 2
# Создай класс Dog, у которого будет общий атрибут species со значением "Canis familiaris".
# Конструктор класса должен принимать аргумент name и сохранять его как атрибут экземпляра.
# Добавь метод bark, который выводит сообщение: "Гав! Меня зовут <name>."
# Создай объект этого класса с любым именем и вызови метод bark.
class Dog:
    species = "Canis familiaris"
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"Гав! Меня зовут {self.name}.")

my_dog = Dog("Джуси")
my_dog.bark()

# Задача 3
# Создай класс Book. У него не должно быть общих атрибутов.
# Конструктор должен принимать два аргумента: title и author, и сохранять их как атрибуты экземпляра.
# Добавь метод show_info, который выводит строку: "Книга: <title>, Автор: <author>".
# Создай объект этого класса с любыми названием и автором и вызови метод show_info.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}")

my_book = Book("Идиот", "Ф.М. Достоевский")
my_book.show_info()

# Задача 4
# Создай класс Rectangle.
# У него не должно быть общих атрибутов.
# Конструктор должен принимать два аргумента: width и height, и сохранять их как атрибуты экземпляра.
# Добавь метод area, который возвращает (не выводит!) площадь прямоугольника (произведение ширины на высоту).
# Создай объект этого класса с любыми значениями ширины и высоты, вызови метод area и выведи результат на экран.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
my_rectangle = Rectangle(10, 20)
print(my_rectangle.area())

# Задача 5
# Создай класс Person.
# У него должен быть общий атрибут kind со значением "human".
# Конструктор должен принимать один аргумент name и сохранять его как атрибут экземпляра.
# Добавь метод introduce, который выводит строку: "Привет! Меня зовут <name>, я <kind>."
# Создай объект этого класса с любым именем и вызови метод introduce.
class Person:
    kind = "human"
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, я {self.kind}.")

my_person = Person("Kirill")
my_person.introduce()

# Задача 6
# Создай класс Counter.
# У него не должно быть общих атрибутов.
# Конструктор должен инициализировать атрибут экземпляра value значением 0.
# Добавь метод increment, который увеличивает value на 1.
# Добавь метод get_value, который возвращает текущее значение value.
# Создай объект этого класса, вызови метод increment два раза, а затем выведи на экран текущее значение с помощью get_value.
class Counter:
    def __init__(self, value = 0):
        self.value = value
    def increment(self):
        self.value += 1
    def get_value(self):
        return self.value
my_counter = Counter()
my_counter.increment()
my_counter.increment()
print(my_counter.get_value())

# Задача 7
# Создай класс Student.
# У него должен быть общий атрибут school со значением "General School".
# Конструктор должен принимать один аргумент name и сохранять его как атрибут экземпляра.
# Добавь метод study, который выводит строку: "<name> учится в <school>."
# Создай объект этого класса с любым именем и вызови метод study.
class Student:
    school = "General School"
    def __init__(self, name):
        self.name = name
    def study(self):
        print(f"{self.name} учится в {self.school}.")
student = Student("Kirill")
student.study()

# Задача 8
# Создай класс Phone.
# У него не должно быть общих атрибутов.
# Конструктор должен принимать один аргумент model и сохранять его как атрибут экземпляра.
# Добавь метод call, который принимает аргумент contact и выводит строку: "Звоню контакту <contact> с телефона <model>."
# Создай объект этого класса с любым значением model и вызови метод call, передав любое имя контакта.
class Phone:
    def __init__(self, model):
        self.model = model
    def call(self, contact):
        print(f"Звоню контакту {contact} с телефона {self.model}.")
my_model = Phone("iPhone")
my_model.call("Alex")

# Задача 9
# Создай класс Product.
# У него не должно быть общих атрибутов.
# Конструктор должен принимать два аргумента: name и price, и сохранять их как атрибуты экземпляра.
# Добавь метод get_price, который возвращает значение атрибута price.
# Создай объект этого класса с любым названием товара и ценой, затем выведи на экран цену, используя метод get_price.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
my_product = Product("Яблоки", 100)
print(my_product.get_price())

# Задача 10
# Создай класс Cat.
# У него должен быть общий атрибут species со значением "Felis catus".
# Конструктор должен принимать один аргумент name и сохранять его как атрибут экземпляра.
# Добавь метод meow, который выводит строку: "<name> говорит: Мяу!"
# Создай объект этого класса с любым именем и вызови метод meow.
class Cat:
    species = "Felis catus"
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(f"{self.name} говорит: Мяу!")
my_cat = Cat("Дуся")
my_cat.meow()

# Задача 11
# Создай класс BankAccount.
# У него не должно быть общих атрибутов.
# Конструктор должен принимать один аргумент balance и сохранять его как атрибут экземпляра.
# Добавь метод deposit, который принимает сумму amount и увеличивает баланс на эту сумму.
# Добавь метод get_balance, который возвращает текущий баланс.
# Создай объект этого класса с начальным балансом 100, вызови метод deposit с аргументом 50, а затем выведи текущий баланс с помощью get_balance.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def get_balance(self):
        return self.balance
my_bank = BankAccount(100)
my_bank.deposit(50)
get_balance = my_bank.get_balance()
print(get_balance)

# Задача 12
# Создай класс LightBulb.
# У него не должно быть общих атрибутов.
# Конструктор должен инициализировать атрибут экземпляра is_on значением False (лампочка изначально выключена).
# Добавь метод turn_on, который устанавливает is_on в True.
# Добавь метод turn_off, который устанавливает is_on в False.
# Добавь метод status, который выводит строку: "Лампочка включена.", если is_on равен True, и "Лампочка выключена." — если False.
# Создай объект этого класса, вызови turn_on, а затем status.
class LightBulb:
    def __init__(self, is_on = False):
        self.is_on = is_on
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def status(self):
        print("Лампочка включена.") if self.is_on else print("Лампочка выключена.")
my_light = LightBulb()
my_light.turn_on()
my_light.status()

# Задача 13
# Создай класс Movie.
# У него не должно быть общих атрибутов.
# Конструктор должен принимать два аргумента: title и year, и сохранять их как атрибуты экземпляра.
# Добавь метод info, который выводит строку: "Фильм: <title>, Год выпуска: <year>."
# Создай объект этого класса с любым названием фильма и годом, затем вызови метод info.
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    def info(self):
        print(f"Фильм: {self.title}, Год выпуска: {self.year}.")
my_movie = Movie("Тренер", 2020)
my_movie.info()

# Задача 14
# Создай класс Calculator.
# У него не должно быть общих атрибутов.
# Конструктор не должен принимать аргументов и не должен ничего инициализировать (тело можно оставить пустым с помощью pass).
# Добавь метод add, который принимает два аргумента a и b и возвращает их сумму.
# Создай объект этого класса и с его помощью вычисли сумму чисел 7 и 3, затем выведи результат на экран.
class Calculator:
    def __init__(self):
        pass
    def add(self, a, b):
            return a + b
result = Calculator()
print(result.add(7, 3))

# Задача 15
# Создай класс Animal.
# У него должен быть общий атрибут kingdom со значением "Animalia".
# Конструктор должен принимать один аргумент name и сохранять его как атрибут экземпляра.
# Добавь метод classify, который выводит строку: "<name> принадлежит к царству <kingdom>."
# Создай объект этого класса с любым именем и вызови метод classify.
class Animal:
    kingdom = "Animalia"
    def __init__(self, name):
        self.name = name
    def classify(self):
        print(f"{self.name} принадлежит к царству {self.kingdom}.")
my_animal = Animal("Жираф")
my_animal.classify()