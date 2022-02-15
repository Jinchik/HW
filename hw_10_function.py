# Модуль 5. Функции.
# Тема: Функции. Часть 1


# Задание 1
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

def gates():
    print(
        "\"Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself."
        "\"\n\t\t\t\t\t\t\t\t\t\tBill Gates")


gates()


# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.

def even(a, b):
    for number in range(a, b):
        if number % 2 == 0:
            print(number)


a = int(input("Please enter the number 1 "))
b = int(input("Please enter the number 2 "))

even(a, b)


# Задание 3
# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.

def square(width, height, symbol, logic, space=" "):
    if logic == False:
        for i in range(height):
            if i == 0 or i == (height - 1):
                print(width * symbol)
            else:
                print(symbol + ((width - 2) * space) + symbol)
    elif logic == True:
        for i in range(height):
            print(width * symbol)


width = int(input("Please enter the Width "))
height = int(input("Please enter the Height "))
symbol = (input("Please enter the Symbol "))
logic = (input("Do you want to fill the square? 1 for yeah, 0 for nope. "))
if logic == "1":
    logic = True
elif logic == '0':
    logic = False

square(width, height, symbol, logic)


# Задание 4
# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.


def min(a, b, c, d, e):
    biggest = 0
    for number in (a, b, c, d, e):
        if number > biggest:
            biggest = number
    print(biggest)


a = int(input("1 number "))
b = int(input("2 number "))
c = int(input("3 number "))
d = int(input("4 number "))
e = int(input("5 number "))
min(-a, b, c, d, e)


# Задание 5
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
# нижняя граница), их нужно поменять местами.

def sum(a, b):
    summ = 0
    if a > b:
        a, b = b, a
    for number in range(a, b):
        summ += number
    print(summ)


a = int(input("Please enter the number 1 "))
b = int(input("Please enter the number 2 "))
sum(a, b)

# Задание 6
# Напишите функцию, которая считает количество
# цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.

def length(numbers):
    for number in range(len(numbers)):
        print(number + 1)
    print(len(numbers))


numbers = input("Please enter the number  ")
length(numbers)

# Задание 7
# Напишите функцию, которая проверяет является ли
# число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
# true, иначе false.
# «Палиндром» — это число, у которого первая часть
# цифр равна второй перевернутой части цифр. Например,
# 123321 — палиндром (первая часть 123, вторая 321, которая
# после переворота становится 123), 546645 — палиндром,
# а 421987 — не палиндром.


def pali(num):
    for i in range(len(num)):
        if num[i] != num[-i - 1]:
            # print("False")
            return False

    else:
        # print("True")
        return True


num = input("Please enter the number ")

print(pali(num))
