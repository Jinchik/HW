# Курс: «Введение в язык
# программирования Python
# Модуль 5. Функции.
# Тема: Функции. Часть 2
#
#
#
#
#
# Задание 1
# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве параметра. Полученный результат возвращается из функции.

# def multifunc(x):
#     multi = 1
#     for num in x:
#         multi = multi * num
#     return multi
#     print(multi)
#
#
# a = []
# while True:
#     b = int(input(f"Please enter numbers to see multi of all number. Enter 0 to stop. \n"))
#     if b == 0:
#         break
#     else:
#         a.append(b)
# print(multifunc(a))


# Задание 2
# Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.


# def min(x):
#     min = 0
#     for n in x:
#         if min < n:
#             min = n
#
#     return min
#
#
# a = []
# while True:
#     b = int(input(f"Please enter numbers to see lowest number. Enter 0 to stop. \n"))
#     if b == 0:
#         break
#     else:
#         a.append(b)
# print(min(a))

# Задание 3
# Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.



# def simplecount(x):
#     simple = []
#     d = 2
#     for n in x:
#         while n % d != 0:
#             d += 1
#             simple.append(n)
#         if n == 0:
#             break
#
#     return simple
#
# a = []
# while True:
#     b = int(input(f"Please enter numbers to see lowest number. Enter 0 to stop. \n"))
#     if b == 0:
#         break
#     else:
#         a.append(b)
# print(simplecount(a))






# Задание 4
# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.


# Задание 5
# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий
# элементы обоих списков.


# Задание 6
# Напишите функцию, высчитывающую степень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержащий полученные результаты