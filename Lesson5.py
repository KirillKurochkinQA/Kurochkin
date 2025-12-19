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

# Задача 21.
# Дан словарь: person = {"name": "Kirill", "age": 29, "city": "Moscow"}
# Напиши код, который выводит каждую пару «ключ — значение» в формате:
# name = Kirill
# age = 29
# city = Moscow
person = {"name": "Kirill", "age": 29, "city": "Moscow"}
for key, value in person.items():
    print(f"{key} = {value}")

# Задача 22.
# Дан словарь: counts = {"a": 10, "b": 20, "c": 15}
# Напиши код, который находит и выводит ключ, соответствующий максимальному значению в словаре.
# В данном случае это "b", потому что у него значение 20.
counts = {"a": 10, "b": 20, "c": 15}
max_value = 0
max_key = 0
for key, value in counts.items():
    if value > max_value:
        max_value = value
        max_key = key
print(max_key)

# Задача 23.
# Дан словарь: status = {"server": "running", "db": "connected", "cache": "active"}
# Напиши код, который проверяет, все ли значения в словаре равны строке "running".
# Если все значения — "running", выведи True.
# Если хотя бы одно значение отличается — выведи False.
status = {"server": "running", "db": "connected", "cache": "active"}
all_running = True
for value in status.values():
    if value != "running":
        all_running = False
        break
print(all_running)

# Задача 24.
# Дан словарь: data = {"x": 5, "y": 5, "z": 5}
# Напиши код, который проверяет, все ли значения в словаре одинаковые.
# Если да — выведи True.
# Если нет — выведи False.
data = {"x": 5, "y": 5, "z": 5}
number = list(data.values())[0]
result = True
for value in data.values():
    if value != number:
        result = False
        break
print(result)

# Задача 25.
# Дан словарь: settings = {"theme": "dark", "language": "ru", "notifications": True}
# Напиши код, который создаёт копию этого словаря, изменяет в копии значение ключа "language" на "en",
# а затем выводит оба словаря — исходный и копию — чтобы убедиться, что оригинал не изменился.
settings = {"theme": "dark", "language": "ru", "notifications": True}
settings_copy = settings.copy()
settings_copy["language"] = "en"
print(settings)
print(settings_copy)

# Задача 26.
# Дан словарь: defaults = {"timeout": 30, "retries": 3, "debug": False}
# Напиши код, который обновляет этот словарь значениями из другого словаря:
# overrides = {"retries": 5, "debug": True}
# После обновления выведи итоговый словарь defaults.
defaults = {"timeout": 30, "retries": 3, "debug": False}
overrides = {"retries": 5, "debug": True}
defaults.update(overrides)
print(defaults)

# Задача 27.
# Дан словарь: params = {"host": "localhost", "port": 8000, "secure": False}
# Напиши код, который проверяет, содержит ли словарь хотя бы один ключ из списка:
# required_keys = ["host", "token", "user"]
# Если хотя бы один из этих ключей есть в params, выведи True.
# Если ни одного — выведи False.
params = {"host": "localhost", "port": 8000, "secure": False}
required_keys = ["host", "token", "user"]
found = False
for key in required_keys:
    if key in params:
        found = True
        break
print(found)

# Задача 28.
# Дан словарь, в котором все значения — строки:
# env = {"DB_HOST": "127.0.0.1", "DB_PORT": "5432", "DEBUG": "TRUE"}
# Напиши код, который заменяет все значения в словаре на их версию в нижнем регистре, используя метод .lower().
# После этого выведи обновлённый словарь.
env = {"DB_HOST": "127.0.0.1", "DB_PORT": "5432", "DEBUG": "TRUE"}
for key, value in env.items():
    value = value.lower()
    env[key] = value
print(env)

# Задача 29.
# Дан словарь:
# data = {"name": "Alice", "score": "95", "active": "true"}
# Напиши код, который преобразует значения в нужные типы данных по следующим правилам:
# "score" → целое число (int)
# "active" → логическое значение (True, если строка "true", иначе False)
# "name" остаётся строкой (ничего не делаем)
# После преобразований выведи обновлённый словарь.
data = {"name": "Alice", "score": "95", "active": "true"}
data["score"] = int(data["score"])
data["active"] = data["active"] == "true"
print(data)

# Задача 30.
# Дан словарь:
# config = {"host": "example.com", "port": "80", "ssl": "false"}
# Напиши код, который:
# Преобразует значение "port" в целое число.
# Преобразует значение "ssl" в логическое:
# True, если строка равна "true" (в нижнем регистре),
# False, если "false".
# Остальные значения остаются без изменений.
# После этого выведи обновлённый словарь.
config = {"host": "example.com", "port": "80", "ssl": "false"}
config["port"] = int(config["port"])
config["ssl"] = config["ssl"] == "true"
print(config)

# Задача 31.
# Дан словарь: user_input = {"username": "admin", "password": "secret123", "role": "user"}
# Напиши код, который очищает значения в словаре от лишних пробелов по краям (если бы они были), используя метод .strip().
# Даже если в текущем словаре пробелов нет — примени .strip() ко всем значениям, чтобы код работал в общем случае.
# После обработки выведи обновлённый словарь.
user_input = {"username": "admin", "password": "secret123", "role": "user"}
for key, value in user_input.items():
    user_input[key] = value.strip()
print(user_input)

# Задача 32.
# Дан словарь:raw_data = {"name": "  Kirill  ", "city": "  Moscow ", "status": " active "}
# Напиши код, который удаляет лишние пробелы в начале и конце каждого значения (с помощью .strip()) и заменяет значение "active" (после очистки) на булево True.
# После всех преобразований выведи обновлённый словарь.
raw_data = {"name": "  Kirill  ", "city": "  Moscow ", "status": " active "}
for key, value in raw_data.items():
    raw_data[key] = value.strip()
    if raw_data[key] == "active":
        raw_data[key] = True
print(raw_data)

# Задача 33.
# Дан словарь: data = {"id": "101", "valid": "yes", "count": "0"}
# Напиши код, который преобразует значения по следующим правилам:
# "id" → целое число (int)
# "valid" → True, если значение "yes"; False, если "no"
# "count" → целое число (int)
# После преобразований выведи обновлённый словарь.
data = {"id": "101", "valid": "yes", "count": "0"}
data["id"] = int(data["id"])
data["valid"] = data["valid"] == "yes"
data["count"] = int(data["count"])
print(data)

# Задача 34.
# Дан словарь: flags = {"feature_x": "on", "feature_y": "off", "debug_mode": "on"}
# Напиши код, который заменяет значения в словаре по следующему правилу:
# "on" → True
# "off" → False
# Остальные возможные значения (если бы они были) оставляй без изменений.
# Выведи обновлённый словарь.
flags = {"feature_x": "on", "feature_y": "off", "debug_mode": "on"}
for key, value in flags.items():
    if flags[key] == "on":
        flags[key] = True
    elif flags[key] == "off":
        flags[key] = False
print(flags)

# Задача 35.
# Дан словарь: metadata = {"version": "2.1", "public": "true", "downloads": "1500"}
# Напиши код, который преобразует значения по следующим правилам:
# "version" остаётся строкой (без изменений),
# "public" → True, если значение "true"; иначе False,
# "downloads" → целое число (int).
# После преобразований выведи обновлённый словарь.
metadata = {"version": "2.1", "public": "true", "downloads": "1500"}
metadata["public"] = metadata["public"] == "true"
metadata["downloads"] = int(metadata["downloads"])
print(metadata)

# Задача 36.
# Дан словарь: options = {"auto_save": "1", "dark_theme": "0", "notifications": "1"}
# Напиши код, который преобразует все значения в словаре в булевый тип по следующему правилу:
# "1" → True
# "0" → False
# После преобразования выведи обновлённый словарь.
options = {"auto_save": "1", "dark_theme": "0", "notifications": "1"}
for key, value in options.items():
    if options[key] == "1":
        options[key] = True
    elif options[key] == "0":
        options[key] = False
print(options)

# Задача 37.
# Дан словарь: settings = {"timeout": "30", "retries": "0", "verbose": "true", "log_level": "info"}
# Напиши код, который преобразует значения только для следующих ключей:
# "timeout" → целое число (int)
# "retries" → целое число (int)
# "verbose" → True, если значение "true"; иначе False
# Ключ "log_level" должен остаться без изменений (остаётся строкой).
# После преобразований выведи обновлённый словарь.
settings = {"timeout": "30", "retries": "0", "verbose": "true", "log_level": "info"}
settings["timeout"] = int(settings["timeout"])
settings["retries"] = int(settings["retries"])
settings["verbose"] = True if settings["verbose"] == "true" else False
print(settings)