# Задача 1
# Создай текстовый файл с именем hello.txt и запиши в него строку "Привет, мир!" с помощью контекстного менеджера with
with open("hello.txt","w", encoding='utf-8') as file:
    file.write("Привет, мир!")

# Задача 2
# Прочитай содержимое файла hello.txt (который ты создал в предыдущей задаче) с помощью контекстного менеджера with и выведи его на экран.
with open("hello.txt","r", encoding='utf-8') as file:
    content = file.read()
    print(content)

# Задача 3
# Создай файл lines.txt и запиши в него три строки:
# Первая строка
# Вторая строка
# Третья строка
# Используй контекстный менеджер with и метод, подходящий для записи нескольких строк за раз.
with open("lines.txt","w", encoding='utf-8') as file:
    file.write("Первая строка\nВторая строка\nТретья строка\n")

# Задача 4
# Прочитай файл lines.txt построчно с помощью цикла for и выведи каждую строку на экран без лишних пустых строк между ними.
with open("lines.txt","r", encoding='utf-8') as file:
    contents = file.readlines()
    for line in contents:
        print(line.strip())

# Задача 5
# Создай файл log.txt. Если он уже существует — не перезаписывай его, а добавь в конец новую строку:
# "Новая запись в логе"
# (с символом новой строки в конце).
# Используй подходящий режим открытия файла и контекстный менеджер with.
with open("log.txt","a", encoding='utf-8') as file:
    file.write("Новая запись в логе\n")

# Задача 6
# Создай файл counter.txt.
# Если он ещё не существует — запиши в него число 1.
# Если файл уже существует — прочитай число из него, увеличь его на 1 и запиши обратно.
with open("counter.txt", "r", encoding='utf-8') as file:
    content = file.read()
    number = int(content)
    number += 1
with open("counter.txt", "w", encoding='utf-8') as file:
    file.write(str(number))

# Задача 7
# Создай файл notes.txt, если он ещё не существует.
# Затем добавь в него строку, введённую пользователем через input(), и сохраняй каждую новую запись с новой строки.
with open("notes.txt", "a", encoding='utf-8') as file:
    text = input()
    file.write(text + "\n")

# Задача 8
# Прочитай файл notes.txt и выведи только те строки, которые содержат слово "маме" (регистр учитывается — ищи именно такую форму).
# Используй контекстный менеджер with, цикл и проверку с помощью оператора in.
with open("notes.txt", "r", encoding='utf-8') as file:
    for line in file:
        if "маме" in line:
            print(line, end="")

# Задача 9
# Создай файл backup.txt и скопируй в него всё содержимое файла notes.txt.
# Если notes.txt не существует — выведи сообщение "Исходный файл не найден." и ничего не записывай.
with open("notes.txt", "r", encoding='utf-8') as file:
    content = file.read()
with open("backup.txt", "w", encoding='utf-8') as file:
    file.write(content)

# Задача 10
# Создай файл summary.txt.
# Затем прочитай файл notes.txt и подсчитай, сколько в нём строк.
# Запиши в summary.txt строку вида:
# В файле notes.txt 3 строки.
# (вместо 3 должно быть реальное число строк).
# Используй только то, что ты уже знаешь: with, open, циклы или методы чтения, str() для преобразования числа.
with open("notes.txt", "r", encoding='utf-8') as file:
    content = file.readlines()
    len_content = len(content)
    text = f"В файле notes.txt {len_content} строк"
with open("summary.txt", "w", encoding='utf-8') as file:
    file.write(text)