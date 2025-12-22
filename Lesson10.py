#  Задача 1
# Создайте класс Animal, у которого есть метод speak(), возвращающий строку "Some sound".
# Затем создайте класс Dog, унаследованный от Animal, и переопределите в нём метод speak() так, чтобы он возвращал "Woof!".
# После этого создайте объект класса Dog и вызовите у него метод speak().
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())

# Задача №2
# Создайте базовый класс Vehicle с атрибутом brand (марка), который задаётся при создании объекта.
# Добавьте в этот класс метод start_engine(), который выводит сообщение: "Engine started".
# Затем создайте дочерний класс Car, который наследуется от Vehicle.
# Класс Car должен иметь дополнительный атрибут number_of_doors (количество дверей), также задаваемый при создании.
# Метод start_engine() в Car должен выводить: "Car engine started".
# Создайте объект класса Car, передав ему марку и количество дверей, и вызовите его метод start_engine().
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print("Engine started")


class Car(Vehicle):
    def __init__(self, brand, number_of_doors):
        super().__init__(brand)
        self.number_of_doors = number_of_doors

    def start_engine(self):
        print("Car engine started")


car = Car("Toyota", 4)
car.start_engine()

# Задача №3
# Создайте базовый класс Shape с методом area(), который выводит сообщение "Area calculation not implemented".
# Создайте дочерний класс Square, который:
# Принимает в конструкторе длину стороны (side).
# Переопределяет метод area(), чтобы он возвращал (не выводил!) площадь квадрата (side * side).
# Создайте объект класса Square со стороной 5 и выведите результат вызова его метода area().
class Shape():
    def area(self):
        print("Area calculation not implemented")
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
square = Square(5)
print(square.area())

# Задача №4
# Создайте базовый класс Employee с атрибутом name и методом get_info(), который возвращает строку вида:
# "Employee: <name>".
# Создайте дочерний класс Manager, который:
# Наследуется от Employee,
# Дополнительно принимает атрибут department (отдел),
# Переопределяет метод get_info(), чтобы он возвращал строку:
# "Manager: <name>, Department: <department>".
# Создайте объект класса Manager с именем "Анна" и отделом "Sales", вызовите у него get_info() и выведите результат.
class Employee:
    def __init__(self, name):
        self.name = name
    def get_info(self):
        return f"Employee: {self.name}"
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    def get_info(self):
        return f"Manager: {self.name}, Department: {self.department}"
manager = Manager("Anna", "Sales")
print(manager.get_info())

# Задача №5
# Создайте базовый класс Device с атрибутом name и методом turn_on(), который возвращает строку:
# "<name> is on".
# Создайте дочерний класс Smartphone, который:
# Наследуется от Device,
# Дополнительно принимает атрибут os (операционная система),
# Переопределяет метод turn_on(), чтобы он возвращал:
# "<name> is on. Running <os>".
# Создайте объект Smartphone с именем "MyPhone" и ОС "Android", вызовите turn_on() и выведите результат.
class Device:
    def __init__(self, name):
        self.name = name
    def turn_on(self):
        return f"{self.name} is on"
class Smartphone(Device):
    def __init__(self, name, os):
        super().__init__(name)
        self.os = os
    def turn_on(self):
        return f"{self.name} is on. Running {self.os}"
smartphone = Smartphone("MyPhone", "Android")
print(smartphone.turn_on())

# Задача №6
# Создайте базовый класс Book с атрибутами title и author, и методом get_info(), который возвращает строку:
# "Title: <title>, Author: <author>".
# Создайте дочерний класс Ebook, который:
# Наследуется от Book,
# Дополнительно принимает атрибут file_size (размер файла в МБ),
# Переопределяет метод get_info(), чтобы он возвращал:
# "Title: <title>, Author: <author>, File size: <file_size> MB".
# Создайте объект Ebook с названием "Python Basics", автором "John Doe" и размером файла 5, вызовите get_info() и выведите результат.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}"

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, File size: {self.file_size} MB"

ebook = Ebook("Python Basics", "John Doe", 5)
print(ebook.get_info())

# Задача №7
# Создайте базовый класс Animal с атрибутом name и методом speak(), который возвращает строку:
# "<name> makes a sound".
# Создайте два дочерних класса:
# Cat, который наследуется от Animal и переопределяет speak(), чтобы возвращать:
# "<name> says meow".
# Dog, который также наследуется от Animal и переопределяет speak(), чтобы возвращать:
# "<name> says woof".
# Создайте по одному объекту каждого класса (Cat и Dog) — например, "Whiskers" и "Buddy" — и выведите результат вызова speak() для каждого.
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof"

cat = Cat("Whiskers")
dog = Dog("Buddy")
print(cat.speak())
print(dog.speak())

# Задача №8
# Создайте базовый класс Person с атрибутами name и age, и методом introduce(), который возвращает строку:
# "Hi, I'm <name> and I'm <age> years old."
# Создайте дочерний класс Student, который:
# Наследуется от Person,
# Дополнительно принимает атрибут grade (например, "10th" или 95),
# Переопределяет метод introduce(), чтобы он возвращал:
# "Hi, I'm <name>, I'm <age> years old, and my grade is <grade>."
# Создайте объект Student с именем "Alex", возрастом 16 и оценкой "A", вызовите introduce() и выведите результат.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old, and my grade is {self.grade}."
student = Student("Alex", 16, "A")
print(student.introduce())

# Задача №9
# Создайте базовый класс Appliance с атрибутом brand и методом turn_on(), который возвращает строку:
# "<brand> appliance is on".
# Создайте дочерний класс Microwave, который:
# Наследуется от Appliance,
# Дополнительно принимает атрибут power (мощность в ваттах, например, 1000),
# Переопределяет метод turn_on(), чтобы он возвращал:
# "<brand> microwave is on. Power: <power> W".
# Создайте объект Microwave с брендом "Samsung" и мощностью 1200, вызовите turn_on() и выведите результат.
class Appliance:
    def __init__(self, brand):
        self.brand = brand
    def turn_on(self):
        return f"{self.brand} appliance is on"
class Microwave(Appliance):
    def __init__(self, brand, power):
        super().__init__(brand)
        self.power = power
    def turn_on(self):
        return f"{self.brand} microwave is on. Power: {self.power} W"
microwave = Microwave("Samsung", 1200)
print(microwave.turn_on())

# Задача №10
# Создайте базовый класс Fruit с атрибутом name и методом describe(), который возвращает строку:
# "This is a <name>."
# Создайте дочерний класс Citrus, который:
# Наследуется от Fruit,
# Дополнительно принимает атрибут vitamin_c (в миллиграммах, например, 53),
# Переопределяет метод describe(), чтобы он возвращал:
# "This is a <name>. It contains <vitamin_c> mg of vitamin C."
# Создайте объект Citrus с названием "Orange" и содержанием витамина C 53, вызовите describe() и выведите результат.
class Fruit:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return f"This is a {self.name}."
class Citrus(Fruit):
    def __init__(self, name, vitamin_c):
        super().__init__(name)
        self.vitamin_c = vitamin_c
    def describe(self):
        return f"This is a {self.name}. It contains {self.vitamin_c} mg of vitamin C."
citrus = Citrus("Orange", 53)
print(citrus.describe())

# Задача №11
# Создайте базовый класс Instrument с атрибутом name и методом play(), который возвращает строку:
# "Playing the <name>."
# Создайте дочерний класс Piano, который:
# Наследуется от Instrument,
# Дополнительно принимает атрибут keys (количество клавиш, например, 88),
# Переопределяет метод play(), чтобы он возвращал:
# "Playing the <name> with <keys> keys."
# Создайте объект Piano с названием "Grand Piano" и количеством клавиш 88, вызовите play() и выведите результат.
class Instrument:
    def __init__(self, name):
        self.name = name
    def play(self):
        return f"Playing the {self.name}."
class Piano(Instrument):
    def __init__(self, name, keys):
        super().__init__(name)
        self.keys = keys
    def play(self):
        return f"Playing the {self.name} with {self.keys} keys."
my_instrument = Piano("Grand Piano", 88)
print(my_instrument.play())

# Задача №12
# Создайте базовый класс Vehicle с атрибутом type (например, "vehicle") и методом move(), который возвращает строку:
# "The <type> is moving."
# Создайте дочерний класс Bicycle, который:
# Наследуется от Vehicle,
# В конструкторе не принимает новых атрибутов, но автоматически устанавливает type = "bicycle" (то есть при создании объекта Bicycle атрибут type должен быть "bicycle"),
# Переопределяет метод move() так, чтобы он возвращал:
# "The bicycle is moving quietly."
# Создайте объект Bicycle и выведите результат вызова его метода move().
class Vehicle:
    def __init__(self, type):
        self.type = type
    def move(self):
        return f"The {self.type} is moving."
class Bicycle(Vehicle):
    def __init__(self):
        super().__init__("bicycle")
    def move(self):
        return f"The {self.type} is moving quietly."
my_vehicle = Bicycle()
print(my_vehicle.move())

# Задача №13
# Создайте базовый класс Writer с атрибутом name и методом write(), который возвращает строку:
# "<name> is writing."
# Создайте дочерний класс Novelist, который:
# Наследуется от Writer,
# Дополнительно принимает атрибут genre (например, "fantasy"),
# Переопределяет метод write(), чтобы он возвращал:
# "<name> is writing a <genre> novel."
# Создайте объект Novelist с именем "Tolkien" и жанром "fantasy", вызовите метод write() и выведите результат
class Writer:
    def __init__(self, name):
        self.name = name
    def write(self):
        return f"{self.name} is writing."

class Novelist(Writer):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre
    def write(self):
        return f"{self.name} is writing a {self.genre} novel."

my_object = Novelist("Tolkien", "fantasy")
print(my_object.write())

# Задача №14
# Создайте базовый класс Room с атрибутом name и методом describe(), который возвращает строку:
# "This is the <name>."
# Создайте дочерний класс Kitchen, который:
# Наследуется от Room,
# Дополнительно принимает атрибут appliances (список устройств, например, ["fridge", "oven"]),
# Переопределяет метод describe(), чтобы он возвращал:
# "This is the <name>. Appliances: <appliances>."
# (где <appliances> — это список, например: ['fridge', 'oven'])
# Создайте объект Kitchen с именем "Main Kitchen" и списком устройств ["fridge", "microwave"], вызовите describe() и выведите результат.
class Room:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return f"This is the {self.name}."
class Kitchen(Room):
    def __init__(self, name, appliances):
        super().__init__(name)
        self.appliances = appliances
    def describe(self):
        return f"This is the {self.name}. Appliances: {self.appliances}"
my_object = Kitchen("Main Kitchen", ["fridge", "microwave"].)
print(my_object.describe())