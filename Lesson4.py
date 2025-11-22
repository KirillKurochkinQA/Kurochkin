# Задача 1: Условный оператор if
# Создай переменную score и присвой ей любое числовое значение от 0 до 100.
# Напиши условие: если score больше или равно 50, выведи строку "Passed", в противном случае ничего не выводи.
# Пока не используем else, только if.
score = 10
if score >= 50:
    print("Passed")

# Задача 2: Логические операции в условиях
# Создай две переменные: a и b. Присвой им любые целые числа.
# Напиши условие: если a больше 10 и b меньше 20, выведи "Correct".
# Используй логический оператор and.
a = 2
b = 3
if a > 10 and b < 20:
    print("Correct")

# Задача 3: Оператор elif
# Создай переменную number и присвой ей любое целое число.
# Напиши условие:
# Если number больше 0 — выведи "Positive".
# Если number меньше 0 — выведи "Negative".
# Если number равно 0 — выведи "Zero".
# Используй if, elif и else.
number = 15
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Задача 4: Тернарный оператор
# Создай переменную age и присвой ей любое целое число.
# Используй тернарный оператор, чтобы присвоить переменной status значение "adult" — если age больше или равно 18, и "minor" — в противном случае.
# Затем просто выведи значение переменной status.
age = 29
status = "adult" if age >= 18 else "minor"
print(status)

# Задача 5: Логические операции
# Создай три переменные: x, y, z и присвой им любые целые числа.
# Напиши условие: если x больше y или z равно 0, выведи "Condition met".
# Используй логический оператор or.
x = 10
y = 20
z = 5
if x > y or z == 0:
    print("Condition met")

# Задача 6: Оператор else
# Создай переменную temperature и присвой ей любое числовое значение.
# Напиши условие:
# Если temperature больше 30 — выведи "Hot".
# В противном случае — выведи "Not hot".
temperature = 0
if temperature > 30:
    print("Hot")
else:
    print("Not hot")

# Задача 7: Оператор if
# Создай переменную name и присвой ей любую строку.
# Напиши условие: если name равно "Admin", выведи "Welcome, Admin!".
# Не используй else.
name = "Admin"
if name == "Admin":
    print("Welcome, " + name + "!")

# Задача 8: Логические операции в условиях
# Создай переменные is_student и has_discount, присвой им логические значения (True или False).
# Напиши условие: если is_student равно True и has_discount равно False, выведи "Apply discount".
# Используй логический оператор and.
is_student = True
has_discount = False
if is_student == True and has_discount == False:
    print("Apply discount")
# более питоновский вариант
is_student = True
has_discount = False
if is_student and not has_discount:
    print("Apply discount")

# Задача 9: Тернарный оператор
# Создай переменную is_sunny и присвой ей логическое значение (True или False).
# Используй тернарный оператор, чтобы присвоить переменной message значение "Let's go outside!" — если is_sunny равно True, и "Stay inside." — в противном случае.
# Затем выведи message.
is_sunny = False
message = "Let's go outside!" if is_sunny else "Stay inside."
print(message)

# Задача 10: Оператор elif
# Создай переменную grade и присвой ей любое целое число от 0 до 100.
# Напиши условие:
# Если grade от 90 до 100 — выведи "A".
# Если grade от 80 до 89 — выведи "B".
# Если grade от 70 до 79 — выведи "C".
# В остальных случаях — выведи "F".
grade = 95
if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade < 90:
    print("B")
elif grade >= 70 and grade < 80:
    print("C")
else:
    print("F")


# Задача 11: Логические операции
# Создай переменные x и y и присвой им любые целые числа.
# Напиши условие: если либо x больше 0, либо y больше 0 (но не оба сразу), выведи "Exactly one is positive".
x = 15
y = 5
if x > 0 and y <= 0 or x <= 0 and y > 0:
    print("Exactly one is positive")

# Задача 12: Оператор else
# Создай переменную logged_in и присвой ей логическое значение (True или False).
# Напиши условие:
# Если logged_in равно True — выведи "Access granted".
# В противном случае — выведи "Access denied".
logged_in = True
if logged_in:
    print("Access granted")
else:
    print("Access denied")

# Задача 13: Логические операции в условиях
# Создай переменные a, b и c и присвой им любые целые числа.
# Напиши условие: если хотя бы одно из чисел отрицательное, выведи "There is a negative number".
# Используй логический оператор or.
a = 1
b = 0
c = -1
if a < 0 or b < 0 or c < 0:
    print("There is a negative number")

# Задача 14: Тернарный оператор
# Создай переменную speed и присвой ей любое число (целое или дробное).
# Используй тернарный оператор, чтобы присвоить переменной status значение "Fast" — если speed больше 60, и "Slow" — в противном случае.
# Выведи значение status.
speed = 60
status = "Fast" if speed > 60 else "Slow"
print(status)

# Задача 15: Оператор elif
# Создай переменную day и присвой ей целое число от 1 до 7 (1 — понедельник, 7 — воскресенье).
# Напиши условие с использованием if, elif, else, которое выводит:
# "Weekday" — если день от 1 до 5,
# "Weekend" — если день 6 или 7,
# "Invalid day" — если число вне диапазона 1–7.
day = 6
if 1 <= day <= 5:
    print("Weekday")
elif 6 <= day <= 7:
    print("Weekend")
else:
    print("Invalid day")