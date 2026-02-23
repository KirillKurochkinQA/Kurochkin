#  Задача №1
# Создай класс TestResult, который будет представлять результат прохождения теста.
#
# Требования:
#
# У объекта должны быть следующие атрибуты:
# tester_name (имя тестировщика — строка)
# test_name (название теста — строка)
# status (статус — строка: либо "passed", либо "failed")
# duration_sec (длительность в секундах — целое число)
# Реализуй конструктор __init__, принимающий все эти параметры.
# Добавь метод is_successful(), который возвращает True, если статус "passed", и False в противном случае.
# Добавь метод to_dict(), который возвращает словарь с теми же полями (tester_name, test_name, status, duration_sec).
# Создай отдельную функцию вне класса с именем filter_successful(results), которая:
# принимает список объектов TestResult,
# возвращает список только тех объектов, у которых статус "passed" (используй метод is_successful()).
class TestResult:
    def __init__(self, tester_name, test_name, status, duration_sec):
        self.tester_name = tester_name
        self.test_name = test_name
        self.status = status
        self.duration_sec = duration_sec
    def is_successful(self):
        return self.status == "passed"
    def to_dict(self):
        result = {"tester_name": self.tester_name,"test_name": self.test_name, "status": self.status, "duration_sec": self.duration_sec}
        return result

def filter_successful(results):
    successful = []
    for result in results:
        if result.is_successful():
            successful.append(result)
    return successful

#  Задача №2
# Создай базовый класс Animal, а затем два дочерних класса: Dog и Cat.
# Требования:
# Класс Animal:
# Имеет атрибуты: name (имя, строка) и species (вид, строка).
# В конструкторе (__init__) принимает name и автоматически устанавливает species как "unknown".
# Имеет метод make_sound(), который возвращает строку: "Some generic sound".
# Класс Dog (наследуется от Animal):
# В конструкторе вызывает конструктор родителя, но устанавливает species как "dog".
# Переопределяет метод make_sound(), чтобы он возвращал "Woof!".
# Класс Cat (наследуется от Animal):
# Аналогично: вызывает родительский конструктор, но устанавливает species как "cat".
# Переопределяет make_sound() → возвращает "Meow!".
# Дополнительно:
# Создай функцию show_animal_info(animal), которая принимает объект типа Animal (или его потомка) и выводит:
# Name: {name}
# Species: {species}
# Sound: {make_sound()}
class Animal:
    def __init__(self, name):
        self.name = name
        self.species = "unknown"
    def make_sound(self):
        return "Some generic sound"
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "dog"
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "cat"
    def make_sound(self):
        return "Meow!"
def show_animal_info(animal):
    print(f"""Name: {animal.name}
Species: {animal.species}
Sound: {animal.make_sound()}""")
show_animal_info(Cat("Juicy"))

# Задача №3
# Создай класс TestReport, который умеет сохранять результаты теста в файл и загружать их обратно.
# Требования:
# Конструктор __init__ принимает:
# test_name (строка)
# status ("passed" или "failed")
# duration_sec (целое число)
# Метод save_to_file(filename):
# Сохраняет данные объекта в текстовый файл с именем filename.
# Формат записи — одна строка в формате (через запятую):
# test_name,status,duration_sec
# Используй контекстный менеджер with open(...).
# Статический метод load_from_file(filename):
# Читает одну строку из файла filename.
# Разбирает её (разделяет по запятой).
# Создаёт и возвращает новый объект TestReport с этими данными.
# Предполагается, что файл всегда содержит ровно одну корректную строку.

class TestReport:
    def __init__(self, test_name, status, duration_sec):
        self.test_name = test_name
        self.status = status
        self.duration_sec = duration_sec
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            line = f"{self.test_name},{self.status},{self.duration_sec}"
            f.write(line)
    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as f:
            line = f.readline()
            parts = line.strip().split(",")
            return TestReport(parts[0], parts[1], int(parts[2]))