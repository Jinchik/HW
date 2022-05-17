# def fun(a):
#     if a > 30:
#         return 5
#
#     else:
#         print(a)
#         return a + fun(a + 3)
#
#
# print(fun(25))


# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         print("Another",n)
#         return 1
#     print(n)
#     return fib(n - 1) + fib(n - 2)
# print(fib(6))

# school_class = {}
#
# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
#
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
#
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
#
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         print(adding)
#         counter += 1
#     print(name, ":", adding / counter)


# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)
# print(f(3))


# def any():
#    print(var + 1, end ='')
# var = 1
# print(var)
# any()
# print(var)


# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# print(tup)
# tup = tup[0]
# print(tup)

# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']
# for i in range(len(my_list) - 1):
#       dictionary[my_list[i]] = (my_list[i], )
# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0])


# class Square:
#
#     @staticmethod
#     def get_squares(a, b):
#         return a * a, b * b
#
#
# print(Square.get_squares(3, 5))


# создаем класс Car
# class Car:
#
#     # создаем конструктор класса Car
#     def __init__(self, model):
#         # Инициализация свойств.
#         self.model = model
#
#     # создаем свойство модели.
#     @property
#     def model(self):
#         return self.__model
#
#     # Сеттер для создания свойств.
#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self.__model = 2000
#         elif model > 2018:
#             self.__model = 2018
#         else:
#             self.__model = model
#
#     def getCarModel(self):
#         return "Год выпуска модели " + str(self.model)
#
#
# carA = Car(2088)
# print(carA.getCarModel())


# import random
# with open('test1.txt', 'r') as file:
#   lines = file.readlines()
#   adjective = lines[random.randint(0, len(lines)-1)][:-1]
#   print(len(lines))
#   print(adjective)
# with open('test1.txt', 'r') as file2:
#   lines2 = file2.readlines()
#   animal = lines2[random.randint(0, len(lines)-1)][:-1]
#   print(animal)
# from fractions import Fraction
# x = Fraction(2,5)
# y = Fraction(1,8)
# print(x+y)
# number = [1, 2, 3]
# print(dir(number))
#
# print('\nReturn Value from empty dir()')
# print(dir())


# from platform import platform
#
# print(platform())
# print(platform(1))
# print(platform(0, 1))
# from platform import machine
#
# print(machine())
#
# from platform import system
#
# print(system())
# from platform import python_implementation, python_version_tuple
#
# print(python_implementation())
#
# for atr in python_version_tuple():
#     print(atr)

# from fractions import Fraction
# class Fract:
#     Fraction.numerator1 = 17
#     Fraction.denominator1 = 87
#     Fraction.numerator2 = 17
#     Fraction.denominator2 = 87
#     add = 0
#     subt = 0
#     div = 0
#     multi = 0
# Fraction.numerator1 = 17
# Fraction.denominator1 = 87
# Fraction.numerator2 = 87
# Fraction.denominator2 = 17
#
# x = Fraction(Fraction.numerator1,Fraction.denominator1)
# y = Fraction(Fraction.numerator2,Fraction.denominator2)
# print(x+y)
# import pygame
#
# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False

#
# a = 15
# print(type(a))
# if type(a) != str:
#     print("hello")

# a , b = float(input()), float(input())
# c =print(round(a + b , 1))


a = int(input("Леша вводит 1 цифру:"))
b = int(input("Леша вводит 2 цифру:"))
symb = str(input("Напиши символ:"))
result = ""
if symb == "+":
    result = int(a) + int(b)
if symb == "-":
    result = int(a) - int(b)
if symb == "*":
    result = int(a) * int(b)
if symb == "+":
    result = int(a) / int(b)
print(f"Это ответ на то что ввел Лёша:{result}")
