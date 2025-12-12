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
class Employee():
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
class Device():
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