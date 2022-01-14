# Курс: «Введение в язык
# программирования Python
# Модуль 2. Операторы ветвлений
# Часть 1
# Задание 1
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.
# Задание 2
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
# Задание 3
# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.


# #1 TASK


# num1 = int(input("Enter yor first number "))
# num2 = int(input("Enter yor second number "))
# num3 = int(input("Enter yor third number "))
# oper = input("Please enter + or * ")
# if oper == "+":
#     print(num1 + num2 + num3)
# else:
#     print(num1 * num2 * num3)


# 2 TASK


#
# num1 = int(input("Enter you're first number "))
# num2 = int(input("Enter you're second number "))
# num3 = int(input("Enter you're third number "))
# opera = input("Please choose 'Biggest', 'Lowest','Arithmetic mean' ")
# if opera == 'Biggest':
#     if num1 > num2 > num3:
#         print(num1)
#     elif num1 < num2 < num3:
#         print(num3)
#     elif num1 < num2 > num3:
#         print(num2)
#     elif num1> num2 < num3:
#         print(num3)
# elif opera == 'Lowest':
#      if num1 < num2 < num3:
#          print(num1)
#      elif num1 > num2 > num3:
#          print(num3)
#      elif num1 > num2 < num3:
#          print(num2)
#      elif num1< num2 > num3:
#          print(num3)
# elif opera == 'Arithmetic mean':
#     print((num1 + num2 + num3) / 3)
# else:
#     print("Error")


# Task 3

#
# num1 = int(input("Enter amount of meters you want to convert "))
# opera = input("Please choose what you want to convert in: miles, inches, yards ")
# if opera == 'miles':
#     print(num1/1609)
# elif opera == 'inches':
#     print(num1/0.0254)
# elif opera == 'yards':
#     print((num1/0.9144))
# else:
#     print("Error")
