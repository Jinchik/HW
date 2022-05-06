# Чистый Python
# 1. Напишите программу, которая получает длины двух катетов в
# прямоугольном треугольнике и выводит его площадь. Каждое число
# записано в отдельной строке.

# def triangle_square(a, b):
#     try:
#         while a != "0" and b != "0":
#             if a != 0 and b != 0 and a.isdigit() and b.isdigit():
#                 a = int(a)
#                 b = int(b)
#                 print(a * b / 2)
#                 a = input("Please enter the  1 leg or 0 to break ")
#                 b = input("Please enter the  2 leg or 0 to break ")
#
#             elif a.isalpha() or b.isalpha():
#                 print("You entered the letter")
#                 break
#     except:
#         print("oops you broke something")
#
#
# try:
#     a = input("Please enter the  1 leg or 0 to break ")
#     b = input("Please enter the  2 leg or 0 to break ")
#     print(triangle_square(a, b))
# except ValueError:
#     print("You wrote a wrong number o letter")

# 2. В школе решили набрать три новых математических класса. Так как
# занятия по математике у них проходят в одно и то же время, было
# решено выделить кабинет для каждого класса и купить в них новые
# парты. За каждой партой может сидеть не больше двух учеников.
# Известно количество учащихся в каждом из трёх классов. Сколько
# всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа: количество
# учащихся в каждом из трех классов.


# def amount_of_students(a,b,c):
#     try:
#         while a != "0" and b != "0" and c != "0":
#             if a != 0 and b != 0 and c != 0 and a.isdigit() and b.isdigit() and c.isdigit():
#                 a = int(a)
#                 b = int(b)
#                 c = int(c)
#                 print ((a+b+c) // 2)
#                 a = input("Please enter the amount of students in 1 grade ")
#                 b = input("Please enter the amount of students in 2 grade ")
#                 c = input("Please enter the amount of students in 3 grade ")
#
#             elif a.isalpha() or b.isalpha() or c.isalpha() :
#                 print("You entered the letter or 0")
#                 break
#     except:
#         print("oops you broke something")
# try:
#     a = input("Please enter the amount of students in 1 grade ")
#     b = input("Please enter the amount of students in 2 grade ")
#     c = input("Please enter the amount of students in 3 grade ")
#     print(amount_of_students(a,b,c))
# except ValueError:
#     print("You wrote a wrong number o letter")
#


# 3. Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2
# (если два совпадает) или 0 (если все числа различны).

# def same_numb(a, b, c):
#     try:
#         while type(a) != str or type(b) != str or type(c) != str or a != str(" ") or b != str(" ") or c != str(" "):
#             same = 0
#             if a == b and b == c:
#                 same += 3
#                 print(f"All numbers are equal {same}")
#                 same = 0
#                 a = int(input("Please enter the 1 number or s to end "))
#                 b = int(input("Please enter the 2 number or s to end "))
#                 c = int(input("Please enter the 3 number or s to end "))
#
#             elif a == b or a == c or b == c:
#                 same += 2
#                 print(f"Two numbers are equal {same}")
#                 same = 0
#                 a = int(input("Please enter the 1 number or s to end "))
#                 b = int(input("Please enter the 2 number or s to end "))
#                 c = int(input("Please enter the 3 number or s to end "))
#             else:
#                 same = 0
#                 print(f"No equal numbers {same}")
#                 a = int(input("Please enter the 1 number or s to end "))
#                 b = int(input("Please enter the 2 number or s to end "))
#                 c = int(input("Please enter the 3 number or s to end "))
#     except ValueError:
#         return "You wrote letter or entered '_'!"
#     except:
#         return "You broke something"
#
#
# try:
#     a = int(input("Please enter the 1 number or s to end "))
#     b = int(input("Please enter the 2 number or s to end "))
#     c = int(input("Please enter the 3 number or s to end "))
#     print(same_numb(a, b, c))
#
# except ValueError:
#     print("You wrote letter or entered '_'!")
# except:
#     print("You broke something")

# 4. Дано натуральное число. Требуется определить, является ли год с
# данным номером високосным. Если год является високосным, то
# выведите YES, иначе выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является високосным, если его номер
# кратен 4, но не кратен 100, а также если он кратен 400.

# def leap_year(a):
#     try:
#         while type(a) != str or a != str(" "):
#
#             if a % 4 == 0 and a % 100 > 0 or a % 400 == 0:
#                 print(f"Yes it is a Leap year! {a}! By the way, if you want to stop, just print any letter...")
#                 a = int(input("Please enter the Year: "))
#             else:
#
#                 print(f"No it isn't a Leap year! {a}! By the way, if you want to stop, just print any letter...")
#                 a = int(input("Please enter the Year: "))
#
#     except ValueError:
#         return "You wrote letter or entered '_'!"
#     except:
#         return "You broke something"
#
#
# try:
#     a = int(input("Please enter the Year: "))
#     print(leap_year(a))
#
# except ValueError:
#     print("You wrote letter or entered '_'!")
# except:
#     print("You broke something")


# 5. Дано положительное действительное число X. Выведите его первую
# цифру после десятичной точки.

# def numb_after_dot(a):
#     try:
#         while str(float(a)) != str or str(a) != str(" "):
#             a = str(int(a*10))[-1]
#             print(a)
#             a = float(input("Please enter the number to know the first number after the . : "))
#
#
#     except ValueError:
#         return "You wrote letter or entered '_'!"
#     except:
#         return "You broke something"
#
#
# try:
#     a = float(input("Please enter the number to know the first number after the . : "))
#     print(numb_after_dot(a))
#
# except ValueError:
#     print("You wrote letter or entered '_'!")
# except:
#     print("You broke something")


# 6. Факториалом числа n называется произведение 1 × 2 × ... × n.
# Обозначение: n!.
# По данному натуральному n вычислите значение n!. Пользоваться
# математической библиотекой math в этой задаче запрещено.

# try:
#     def facto(a):
#         f = int(1)
#         x = int(a[:])
#         while x != int(0) or str(float(a)) != a.isalpha() or str(a) != str(" "):
#             x = int(a[:])
#             for i in range(1, int(a) + 1):
#                 f = int(i) * int(f)
#                 x -= 1
#                 if x == 0:
#                     print(f)
#                     f = 1
#                     break
#             a = input("Please enter the number to know it's factorial, or any letter ot '_' to break . : ")
#
# except ValueError:
#     print("You wrote letter or entered '_'!")
# except:
#     print("You broke something")
#
#
# try:
#     a = input("Please enter the number to know it's factorial, or any letter ot '_' to break . : ")
#     print(facto(a))
# except ValueError:
#     print("You wrote letter or entered '_'!")
# except:
#     print("You broke something")

# 7. Дано два числа a и b. Выведите гипотенузу треугольника с заданными
# катетами.

# try:
#     def hypotenuse(x, y):
#         z = float()
#         while (x, y) != int(0) or str(float(x, y)) != (x, y).isalpha() or str(x, y) != str(" "):
#             z = (float(x) ** 2 + float(y) ** 2)**0.5
#             print(float(z))
#             x = input("Please enter the number the 1 Cathetus or any letter ot '_' to break:  ")
#             y = input("Please enter the number the 2 Cathetus or any letter ot '_' to break:  ")
#
#
# except ValueError:
#     print("You wrote letter or entered '_'!")
# except:
#     print("You broke something")
#
# try:
#     x = input("Please enter the number the 1 Cathetus or any letter ot '_' to break:  ")
#     y = input("Please enter the number the 2 Cathetus or any letter ot '_' to break:  ")
#     print(hypotenuse(x,y))
# except ValueError:
#     print("You wrote letter or entered '_'!")
# except:
#     print("You broke something")

# 8. Дано N чисел: сначала вводится число N, затем вводится ровно N целых
# чисел. Подсчитайте количество нулей среди введенных чисел и
# выведите это количество. Вам нужно подсчитать количество чисел,
# равных нулю, а не количество цифр.

x = int(input("Please enter the number"))
y = 0
z = 0

for i in range(x):
    y = i + y
    for j in str(y):
        if j == "0":
            z +=1
print(z)









# 9. Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и
# выведите получившуюся строку.
# При решении этой задачи не стоит пользоваться циклами и
# инструкцией if.
# 10.Дана строка. Найдите в этой строке второе вхождение буквы f, и
# выведите индекс этого вхождения. Если буква f в данной строке
# встречается только один раз, выведите число -1, а если не встречается
# ни разу, выведите число -2.
# 11.Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и
# выведите получившуюся строку.
# При решении этой задачи не стоит пользоваться циклами и
# инструкцией if.
# 12.Программа получает на вход последовательность целых
# неотрицательных чисел, каждое число записано в отдельной строке.
# Последовательность завершается числом 0, при считывании которого
# программа должна закончить свою работу и вывести количество
# членов последовательности (не считая завершающего числа 0). Числа,
# следующие за числом 0, считывать не нужно.
# 13.Последовательность состоит из натуральных чисел и завершается
# числом 0. Определите, сколько элементов этой последовательности
# больше предыдущего элемента.
# 14.Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.
# д.). Если элементов нечетное число, то последний элемент остается на
# своем месте.
# 15.Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.
# Работа с помощью Selenium.
# Провести тест, с записью результатов.
# Можно написать тест любого сайта, на котором есть регистрация и radio button,
# checkbox
# Критерии: вход на сайт, запись полученных результатов, запись выбранных вариантов,
# проверка на все возможные варианты ответа.
# Варианты сайтов: .
# https://replit.com/
# https://myshows.me/
