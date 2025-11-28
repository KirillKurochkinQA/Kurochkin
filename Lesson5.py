# Задача 1.
# Создай пустой словарь и добавь в него три пары «ключ — значение»:
# ключ 'name' со значением 'Alice',
# ключ 'age' со значением 25,
# ключ 'city' со значением 'Paris'.
# Проверь, что словарь содержит все три пары.
result = dict()
result["name"] = "Alice"
result["age"] = 25
result["city"] = "Paris"
print(result)

# Задача 2.
# Дан словарь: student = {"name": "Иван", "grade": 85, "subject": "Математика"}
# Напиши код, который проверяет, существует ли в словаре ключ 'grade', и выводит True, если он есть, или False, если нет.
# Используй для этого оператор, предназначенный специально для проверки наличия ключа в словаре.
student = {"name": "Иван", "grade": 85, "subject": "Математика"}
if "grade" in student:
    print(True)
else:
    print(False)
# вариант 2 предложенный ИИ
student = {"name": "Иван", "grade": 85, "subject": "Математика"}
print("grade" in student)

# Задача 3.
# Дан словарь: car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
# Напиши код, который удаляет из словаря элемент с ключом "year" и выводит получившийся словарь.
# Используй способ удаления элемента по ключу, который выдаёт ошибку, если такого ключа нет (это нормально — в этой задаче ключ точно существует)
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
del car["year"]
print(car)

# Задача 4.
# Дан словарь: book = {"title": "1984", "author": "George Orwell", "pages": 328}
# Напиши код, который получает все ключи словаря и выводит их в виде списка.
# Используй встроенный метод словаря, предназначенный специально для получения ключей.
book = {"title": "1984", "author": "George Orwell", "pages": 328}
keys = list(book.keys())
print(keys)

# Задача 5.
# Дан словарь: product = {"name": "Laptop", "price": 999, "in_stock": True}
# Напиши код, который получает значение по ключу "price" и выводит его на экран.
# Используй прямой доступ к элементу словаря по ключу.
product = {"name": "Laptop", "price": 999, "in_stock": True}
print(product["price"])

# Задача 6.
# Дан словарь: weather = {"city": "Moscow", "temperature": -5, "wind": "north"}
# Напиши код, который получает все значения словаря и выводит их в виде списка.
# Используй встроенный метод словаря, предназначенный специально для получения значений.
weather = {"city": "Moscow", "temperature": -5, "wind": "north"}
values = list(weather.values())
print(values)

# Задача 7.
# Дан словарь: user = {"login": "kirill123", "email": "kirill@example.com", "active": True}
# Напиши код, который проверяет, содержится ли значение "kirill@example.com" среди значений этого словаря,
# и выводит True, если содержится, или False, если нет.
# Используй подходящий способ проверки наличия значения в словаре.
user = {"login": "kirill123", "email": "kirill@example.com", "active": True}
print("kirill@example.com" in user.values())

# Задача 8.
# Дан словарь: settings = {"theme": "dark", "notifications": True, "language": "ru"}
# Напиши код, который обновляет значение ключа "language" на "en" и затем выводит весь словарь.
# Используй прямое присваивание по ключу (тот же способ, что и при добавлении нового элемента).
settings = {"theme": "dark", "notifications": True, "language": "ru"}
settings["language"] = "en"
print(settings)

# Задача 9.
# Дан словарь: data = {"x": 10, "y": 20, "z": 30}
# Напиши код, который получает все пары «ключ — значение» в виде списка кортежей и выводит его.
# Используй встроенный метод словаря, предназначенный специально для получения таких пар.
data = {"x": 10, "y": 20, "z": 30}
data_items = list(data.items())
print(data_items)

# Задача 10.
# Дан словарь: profile = {"name": "Anna", "age": 30, "country": "Germany"}
# Напиши код, который проверяет, есть ли в словаре ключ "phone", и если его нет — добавляет его со значением "unknown".
# После этого выведи обновлённый словарь.
# Используй проверку с оператором in и условную конструкцию if.
profile = {"name": "Anna", "age": 30, "country": "Germany"}
if "phone" in profile:
    print(profile)
else:
    profile["phone"] = "unknown"
    print(profile)

# Задача 11.
# Дан словарь: inventory = {"apples": 5, "bananas": 3, "oranges": 8}
# Напиши код, который удаляет элемент с ключом "bananas" из словаря без ошибки, даже если такого ключа нет.
# После этого выведи получившийся словарь.
# Используй метод словаря, который безопасно удаляет элемент по ключу (не вызывает ошибку, если ключа нет).
inventory = {"apples": 5, "bananas": 3, "oranges": 8}
inventory.pop("bananas", None)
print(inventory)

# Задача 12
# Дан словарь: info = {"name": "Kirill", "role": "tester"}
# Напиши код, который проверяет, есть ли в словаре ключ "email".
# Если его нет, добавь ключ "email" со значением "no email".
# После этого выведи обновлённый словарь.
# Используй только:
# оператор in для проверки,
# присваивание по ключу для добавления,
# if / else.
info = {"name": "Kirill", "role": "tester"}
if "email" in info:
    print(info)
else:
    info["email"] = "no email"
    print(info)

# Задача 13.
# Дан словарь: device = {"type": "phone", "brand": "Samsung"}
# Напиши код, который проверяет, есть ли в словаре значение "Samsung".
# Если оно есть — выведи True, если нет — выведи False.
# Используй только то, что ты уже применял ранее: оператор in и метод .values().
device = {"type": "phone", "brand": "Samsung"}
print("Samsung" in device.values())

# Задача 14.
# Дан словарь: user_data = {"username": "kirill_k", "is_active": True}
# Напиши код, который добавляет в словарь новый элемент с ключом "last_login" и значением "2025-11-22", а затем выводит обновлённый словарь.
# Используй прямое присваивание по ключу (так же, как при обновлении или добавлении элементов).
user_data = {"username": "kirill_k", "is_active": True}
user_data["last_login"] = "2025-11-22"
print(user_data)

# Задача 15.
# Дан словарь: record = {"id": 101, "status": "completed", "priority": "high"}
# Напиши код, который проверяет, есть ли в словаре ключ "priority".
# Если ключ есть — выведи его значение.
# Если ключа нет — выведи сообщение "Ключ не найден".
# Используй проверку с оператором in и условную конструкцию if/else.
record = {"id": 101, "status": "completed", "priority": "high"}
if "priority" in record:
    print(record["priority"])
else:
    print("Ключ не найден")

# Задача 16.
# Дан словарь:
# cache = {"token": "abc123", "expires_in": 3600}
# Напиши код, который удаляет из словаря элемент с ключом "token" и сразу после этого проверяет, остался ли он в словаре.
# Если ключ "token" всё ещё есть — выведи True, иначе — False.
# Используй оператор del для удаления и оператор in для проверки.
cache = {"token": "abc123", "expires_in": 3600}
del cache["token"]
print("token" in cache)

# Задача 17.
# Дан словарь: options = {"verbose": False, "retry": 3}
# Напиши код, который добавляет в словарь пару "timeout": 10, только если ключ "timeout" ещё не существует. После этого выведи словарь.
# Используй проверку с оператором in и условную конструкцию if.
options = {"verbose": False, "retry": 3}
if "timeout" in options:
    print(options)
else:
    options["timeout"] = 10
    print(options)

# Задача 18.
# Дан словарь: mapping = {"a": 1, "b": 2, "c": 3}
# Напиши код, который выводит значение по ключу "b", не используя прямой доступ вроде mapping["b"].
# Вместо этого сначала получи список всех значений словаря, затем — список всех ключей, и используй их, чтобы найти нужное значение по позиции ключа "b".
mapping = {"a": 1, "b": 2, "c": 3}
keys = list(mapping.keys())
values = list(mapping.values())
index = keys.index("b")
print(values[index])

# Задача 19.
# Дан словарь: flags = {"debug": False, "cache": True, "logging": True}
# Напиши код, который выводит все значения словаря по одному, каждое — на новой строке.
# Используй только метод .values() и цикл for.
flags = {"debug": False, "cache": True, "logging": True}
flags_values = flags.values()
for flag in flags_values:
    print(flag)

# Задача 20.
# Дан словарь: grades = {"math": 92, "english": 87, "history": 89}
# Напиши код, который выводит все ключи словаря по одному, каждый — на новой строке.
# Используй только метод .keys() и цикл for.
grades = {"math": 92, "english": 87, "history": 89}
grades_keys = grades.keys()
for grade in grades_keys:
    print(grade)