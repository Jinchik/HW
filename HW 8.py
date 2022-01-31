# Курс: «Введение в язык
# программирования Python
# Модуль 3. Циклы.
# Часть 2


# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.



#With for
# x = int(input("Number 1 "))
# y = int(input("Number 2 "))
# sumch = 0
# sumnech = 0
# sum9 = 0
# sum1 = 0
# sum2 = 0
# sum3 = 0
# for i in range(x, y):
#     if i % 2 == 0:
#         sumch = sumch + i
#         sum1 = sum1 + 1
#     if i % 2 != 0:
#         sumnech = sumnech + i
#         sum2 = sum2 + 1
#     if i % 9 == 0:
#         sum9 = sum9 + i
#         sum3 = sum3 + 1
# print(sumch,"Chetnie", sumnech, "nechetnie", sum9, "sum 9")
# print(sumch / sum1, sumnech / sum2, sum9 / sum3 )
#
#
#
#
#
# #With while
# x = int(input("Number 1 "))
# sumch = 0
# sumnech = 0
# sum9 = 0
# sum1 = 0
# sum2 = 0
# sum3 = 0
# while x > 0 and x < 100:
#     x = x + 1
#     if x % 2 == 0:
#         sumch = sumch + x
#         sum1 = sum1 + 1
#     if x % 2 != 0:
#         sumnech = sumnech + x
#         sum2 = sum2 + 1
#     if x % 9 == 0:
#         sum9 = sum9 + x
#         sum3 = sum3 + 1
#
# print(sumch,"Chetnie", sumnech, "nechetnie", sum9, "sum 9")
# print(sumch / sum1, sumnech / sum2, sum9 / sum3 )


# Задание 2
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и символ %, тогда
# вывод на экран будет такой:
# %
# %
# %
# %
# %

# length = int(input("Number  "))
# symbol = str(input("Symbol "))
# for i in range(length):
#     print (symbol)



# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# Домашнее задание
# 1
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»

# x = int(input("Number 1  "))
# y = int(input("Number 2  "))
# for i in range(x,y + 1):
#     if x == 7:
#         print("Goodbye")
#         break
#     print(i)
#     if i > 0:
#         print("Number is positive ")
#     elif i < 0:
#         print("Number is negative ")
#     elif i == 0:
#         print("Number is equal to zero  ")





# Задание 4
# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»



#With For

# x = int(input("Number 1  "))
# y = int(input("Number 2  "))
# if x > y and y < x:
#     print(" 1 number can't be higher then 2-d ")
# sum = 0
# for i in range(x,y + 1):
#     if x == 7 or y == 7:
#         print("Goodbye")
#         break
#     if x >= 0 and y > x:
#         sum = sum + i
# print(sum, "Sum")
# if x < y:
#     print(f" {x} is the Lowest number ")
# if y > x:
#     print(f" {y} is the Biggest number ")
#

# With while


# maxn = 0
# minn = 0
# x = int(input("Enter the Number  "))
#
# sum = 0
# while x != 7:
#     if x == 7:
#         print("Good bye!")
#     sum = sum + x
#     if x > maxn:
#         maxn = x
#     elif x < minn:
#         minn = x
#     x = int(input("Enter the Number, or 7 to stop  "))
# print(maxn, minn, sum,"Max, Min, Sum")
