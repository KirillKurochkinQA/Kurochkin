# Задача №1
# Создай строку, которая содержит твоё имя (или любое другое слово, если не хочешь использовать имя). Выведи эту строку на экран.
name = "Kirill"
print(name)

# Задача №2
# Создай строку "Hello". Выведи на экран первый символ этой строки.
result = "Hello"
result_0 = result[0]
print(result_0)

# Задача №3
# Создай строку "Python". Используя срез, выведи на экран последние три символа этой строки.
name = "Python"
result = name[-3:]
print(result)

# Задача №4
# Создай две строки: "Привет" и "мир". Объедини их в одну строку и выведи результат на экран.
string_1 = "Привет"
string_2 = "мир"
result = string_1 + " " + string_2
print(result)

# Задача №5
# Создай переменную name со значением "Алекс". Используя f-строку, выведи на экран фразу:
# "Привет, Кирилл!"
# (Используй переменную name внутри f-строки.)
name = "Кирилл"
message = f"Привет, {name}!"
print(message)

# Задача №6
# Создай строку " Python " (с пробелами в начале и конце).
# Выведи на экран эту строку, но без пробелов в начале и конце.
string = " Python "
string_strip = string.strip()
print(string_strip)

# Задача №7
# Создай строку "python".
# Выведи на экран эту строку, но в верхнем регистре (все буквы заглавные).
name = "python"
up_name = name.upper()
print(up_name)

# Задача №8
# Создай строку "Добро пожаловать" и выведи её длину (количество символов, включая пробелы).
welcome = "Добро пожаловать"
result = len(welcome)
print(result)

# Задача №9
# Создай строку "test".
# Создай новую строку, которая состоит из этой строки, повторённой 3 раза подряд.
# Выведи результат на экран.
string = "test"
new_string = string*3
print(new_string)

# Задача №10
# Создай строку "Hello, World!".
# Выведи на экран символ, который стоит на 8-й позиции (индекс 7).
string = "Hello, World!"
result = string[7]
print(result)

# Задача №11
# Создай строку " Пробелы в начале и в конце ".
# Убери пробелы в начале и в конце, а затем проверь, начинается ли строка с "Пробелы".
# Выведи результат проверки (True или False).
string = " Пробелы в начале и в конце "
string_strip = string.strip()
start_string = string_strip.startswith("Пробелы")
print(start_string)

# Задача №12
# Создай строку "hello world".
# Замени в ней слово "world" на "Python".
# Выведи результат.
text = "hello world"
new_text = text.replace("world", "Python")
print(new_text)

# Задача №13
# Создай строку "Python" и выведи на экран её длину.
# Затем создай ещё одну строку "Java" и тоже выведи её длину.
# Сравни длины обеих строк и выведи результат (True или False):
# "Длина строки 'Python' больше, чем длина строки 'Java'".
text_py = "Python"
print(len(text_py))
text_ja = "Java"
print(len(text_ja))
text = len(text_py) > len(text_ja)
print(text)

# Задача №14
# Создай строку "Hello, my name is Bob".
# Проверь, содержится ли в ней слово "name".
# Выведи результат (True или False).
text = "Hello, my name is Bob"
result = "name" in text
print(result)

# Задача №15
# Создай строку "Python" и выведи на экран символ, который находится посередине.
# Если строка состоит из чётного количества символов — выведи второй символ из середины.
text = "Python"
result = text[3]
print(result)

# Задача №16
# Создай строку " Привет, друг! " (с лишними пробелами).
# Убери пробелы в начале и в конце, а затем замени все двойные пробелы на одинарные.
# Выведи итоговую строку.
text = " Привет,  друг! "
text_strip = text.strip()
text_replace = text_strip.replace("  ", " ")
print(text_replace)

# Задача №17
# Создай строку "123" и выведи её длину.
# Затем создай строку "abc" и тоже выведи её длину.
# Сравни длины: выведи True, если длина "123" равна длине "abc", иначе — False.
text = "123"
print(len(text))
string = "abc"
print(len(string))
result = len(text) == len(string)
print(result)

# Задача №18
# Создай строку "Python" и выведи её в обратном порядке.
# (Используй срез, чтобы перевернуть строку.)
text = "Python"
result = text[::-1]
print(result)

# Задача №19
# Создай строку "Hello, World!".
# Раздели строку на две части: до запятой и после.
# Выведи каждую часть отдельно.
text = "Hello, World!"
split_text = text.split(",")
split1 = split_text[0]
split2 = split_text[1]
print(split1)
print(split2)

# Задача №20
# Создай строку " abc ".
# Убери пробелы в начале и в конце, а затем проверь, начинается ли строка с "a" и заканчивается ли на "c".
# Выведи результат проверки (True или False).
text = " abc "
text_strip = text.strip()
result = text_strip.startswith("a") and text_strip.endswith("c")
print(result)

# Задача №21
# Создай строку "Python".
# Выведи третий символ этой строки.
text = "Python"
result = text[2]
print(result)

# Задача №22
# Создай строку " Кирилл " (с пробелами в начале и в конце).
# Убери пробелы и выведи строку.
name = " Кирилл "
result = name.strip()
print(result)

# Задача №23
# Создай строку "Hello World".
# Найди позицию (индекс), где начинается слово "World".
# Выведи этот индекс.
text = "Hello World"
index = text.find("World")
print(index)

# Задача №24
# Создай строку " abc ".
# Убери пробелы в начале и в конце, а затем выведи длину новой строки.
text = " abc "
result = text.strip()
print(len(result))

# Задача №25
# Создай строку "Hello".
# Повтори её 4 раза подряд, добавляя между каждой копией пробел.
# Выведи результат.
text = "Hello"
result = (text + " ") * 4
print(result)

# Задача №26
# Создай строку "Python" и выведи на экран символ с индексом 1.
text = "Python"
result = text[1]
print(result)

# Задача №27
# Создай строку " abc def ".
# Убери пробелы в начале и в конце, а затем посчитай, сколько раз в строке встречается буква "a".
# Выведи результат.
text = " abc def "
result = text.strip()
result = result.count("a")
print(result)

# Задача №28
# Создай строку "Hello, World!".
# Выведи срез строки, который содержит только слово "World".
text = "Hello, World!"
result = text[7:12:]
print(result)

# Задача №29
# Создай строку " Python ".
# Убери пробелы в начале и в конце, а затем проверь, начинается ли строка с "P" и заканчивается на "n".
# Выведи результат проверки (True или False).
text = "Python"
text_1 = text.strip()
result = text_1.startswith("P") and text_1.endswith("n")
print(result)

# Задача №30
# Создай строку "Hello".
# Проверь, равна ли строка "Hello" или "hello" (без учёта регистра).
# Выведи результат (True или False).
text = "Hello"
result = text.lower() == "hello"
print(result)
