# Курс: «Введение в язык
# программирования Python
# Модуль 2. Операторы ветвлений
# Часть 2
# Задание 1
# Пользователь вводит с клавиатуры номер дня недели
# (1-7). Необходимо вывести на экран названия дня недели. Например, если 1, то на экране надпись понедельник,
# 2 — вторник и т.д.
# Задание 2
# Пользователь вводит с клавиатуры номер месяца
# (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.
# Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»
# Задание 4
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания

Task 4


weekd = int(input('Please enter a number of the day of the week '))
if weekd == 1:
    print("It is Monday, my friend :( ")
elif weekd == 2:
    print("It is Thuesday, my friend :\ ")
elif weekd == 3:
    print("It is Wednesday, my friend :/ ")
elif weekd == 4:
    print("It is Thursday, my friend :! ")
elif weekd == 5:
    print("It is Friday, my friend WEEEE ")
elif weekd == 6:
    print("It is Saturday, my friend :) ")
elif weekd == 7:
    print("It is Sunday, my friend :D ")

