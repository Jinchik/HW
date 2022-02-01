# Курс: «Введение в язык
# программирования Python
# Модуль 3. Циклы.
# Часть 3


# Задание 1
# Напишите программу, которая запрашивает два
# целых числа x и y, после чего вычисляет и выводит
# значение x в степени y.
# x = int(input("Enter please num 1 "))
# y = int(input("Enter please num 2 "))
# print(f"{x} ** {y} == {x ** y}", sep=" " )
#
#



# Задание 2
# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.

# x = 100
# y = 999
# sum = 0
# for i in range(x, y+1):
#     if i % 11 ==0 or i % 22 ==0 or i % 33 ==0 or i % 44 ==0 or i % 55 ==0 or i % 66 ==0 or i % 77 ==0 or i % 88 ==0 or i % 99 ==0:
#         sum = sum+1
# print(sum)
#



# Задание 3
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

# x = 100
# y = 999
# sum = 0
# for i in range(x, y+1):
#     if i !=0 or i !=1 or i !=2 or i !=3 or i !=4 or i !=5 or i !=6 or i !=7 or i !=8 or i !=9:
#         sum = sum+1
# print(sum)




# Задание 4
# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.


# a = str(input('enter number'))
# for i in a:
#     if i == '3' or i == '6':
#         continue
#     print(i, end = ' ')
#


while True:
    num = input('Please, enter a number:')
    for i in range(len(num)):
        if num[i] == '6' or num[i] == '3':
            print(num)
            continue
        else:
            print(num[i], end='')
    print()

s = ''
while True:
    num = input('Please, enter a number:')
    for i in range(len(num)):
        if num[i] == '6' or num[i] == '3':
            continue
        else:
            s = s + num[i]
print(int(s))