# # num1 = int(input("Please neter a number "))
# # num2 = int(input("Please neter a number "))
# # num3 = int(input("Please neter a number "))
# # opt = (input("Enter the sign "))
# # if opt == "+":
# #     print(f"{num1} + {num2} + {num3} ==" , num1+num2+num3)
# #     print(num1+num2+num3)
# #     elif (num1 != 0, num2 != 0, num3 != 0):
# #     print("Good to go, it isn't 0")
# # s = 'Hello World!'
# # for letter in range(len(word)):
# #     print(word [letter])
# # h = 'Hello World!'
# # #      0123456789
# # #  -      987654321
# # s = 'Hello World!'
# # for i in range(1, len(s)+1):
# #     print(s[-i])
#
# #
# # myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# #
# # uniques = []
# # for number in myList:
# #     if number not in uniques:
# #         uniques.append(number)
# #
# # print("The list with unique elements only:")
# # print(uniques)
#
#
#
# # my_list = [8, 10, 8, 8, 8, 6, 2, 4]
# # new_num = []
# # for i in range(len(my_list)):
# #
# #     if my_list[i] != my_list[i] + 1:
# #
# #         new_num.append(my_list[i])
# # print(new_num)
# # d =dict
# #
# # my_list = [8, 10, 6, 2, 4]  # list to sort
# # swapped = True  # It's a little fake, we need it to enter the while loop.
# #
# # while swapped:
# #     swapped = False  # no swaps so far
# #     for i in range(len(my_list) - 1):
# #         if my_list[i] > my_list[i + 1]:
# #             swapped = True  # a swap occurred!
# #             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# #
# # print(my_list)
#
#
#
#
# # def eazy_num(list):
# #     n = list[0]
# #     counter = 0
# #     for i in range(1, n + 1):
# #         if n % i == 0:
# #             counter += 1
# #         return 'Easy number' if counter == 2 else 'Not Easy number'
# #
# #
# # eazy_num([7, 2, 6, 8, 11])
#
#
#
# def simple(number):
#     for some_number in range(2,number):
#         if number%some_number == 0:
#             return False
#     return True
#
# def simple_list(list_of_numbers):
#     new_list = []
#     for number in list_of_numbers:
#         if simple(number):
#             new_list.append(number)
#     l = len(new_list)
#     return l
#
#
# random_list = [1,4,5,7,3,5,6,8,137,42,65]
# print(simple_list(random_list))
#
#
#
#
#
#
# def simple_numbers_count_m1(numbers):
#     count = 0
#     for number in numbers:
#         number = str(number)
#         if number.lstrip("-").isnumeric():
#             number = int(number)
#             if number >= 2:
#                 simple = True
#                 for i in range(2, number):
#                     if number % i == 0:
#                         simple = False
#                         break
#                 if simple:
#                     count = count + 1
#             else:
#                 continue
#         else:
#             return "INCORRECT ENTRY!"
#     return count
#
#
# some_numbers = [2, 42, 137, 1, 3, -2]
# print(simple_numbers_count_m1(some_numbers))
# print()
#
#
#
#
#
#
#
#
#
# s = '-23+12'
# number1 = ''
# number2 = ''
# symb = ['+', '-', '*', '/']
#
# for i in range(len(s)):
#     n = s[i]
#     for j in symb:
#         if n == j:
#             number1 = s[:i]
#             number2 = s[i + 1:]
#             mark = n
# if mark == '+':
#     print(number1, '+', number2, '=', int(number1) + int(number2))
# elif mark == '-':
#     print(number1, '-', number2, '=', int(number1) - int(number2))
# elif mark == '*':
#     print(number1, '*', number2, '=', int(number1) * int(number2))
# elif mark == '/':
#     print(number1, '/', number2, '=', int(number1) / int(number2))
#
#
#
#
# #Variables
# a = str(input("Input some impression: "))
# operators = ['+', '-', '*', '/']
# operator = 0
# operator_index = 0
# # Cycle for enumerating type of operator
# for i in a:
#     for b in operators:
#         if b == i:
#             operator = b
#             break
# # Enumerating operator's index
# operator_index = a.index(operator)
# # Calculating and printing results
# if operator == "+":
#     print(int(a[:operator_index]) + int(a[operator_index+1:]))
# elif operator == "-":
#     print(int(a[:operator_index]) - int(a[operator_index+1:]))
# elif operator == "*":
#     print(int(a[:operator_index]) * int(a[operator_index+1:]))
# elif operator == "/":
#     print(int(a[:operator_index]) / int(a[operator_index+1:]))
# else:
#     print("You input something wrong! ")
#
#
#
#
#
#  numbers = input('Enter the operation (possible +, -, *, / ): ')
# # operator1 = '+'
# # operator2 = '-'
# # operator3 = '*'
# # operator4 = '/'
# # if operator1 in numbers:
# #     a, b = numbers.split('+')
# #     print(int(a) + int(b))
# # elif operator2 in numbers:
# #     a,b = numbers.split('-')
# #     print(int(a) - int(b))
# # elif operator3 in numbers:
# #     a,b = numbers.split('*')
# #     print(int(a) * int(b))
# # elif operator4 in numbers:
# #     a,b = numbers.split('/')
# #     print(int(a) / int(b))
# # else:
# #     print("Uncorrected operation")
#
#
# x=float(input("Введите значение x ="))   y=float(input("Введите значение y ="))   z=input("Введите оператор (+, -, /, *, mod, pow, div) =")   if z==+:      result=x+y   elif z==-:     result=x-y   elif z==pow:     result=pow(x,y)   elif z==*:      result=x*y    elif y!=0:     if z==/:       result=x/y     elif z==div:        result=x//y     elif z==mod:        result=x%y      elif y==0:      result="Деление на 0!"   print("Результат вычислений =",result)
# Все авторские права на этот материал принадлежат исключительно сайту Информатика. В случае обнаружения нарушения условий копирования наших материалов, будут предприняты соответствующие санкции к нарушителям: обращение к хостинговой компании и другие меры в соответствии с действующим законодательством РФ. Источник материала: http://inphormatika.ru/programming/python/zadachi_python/kak_sozdat_kalkulyator_na_pitone_.html
#
#





