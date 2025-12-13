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