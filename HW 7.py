# Курс: «Введение в язык
# программирования Python
# Модуль 3. Циклы.
# Часть 3


# Задание 1
# Напишите программу, которая запрашивает два
# целых числа x и y, после чего вычисляет и выводит
# значение x в степени y.
#
x = int(input("Enter please num 1 "))
y = int(input("Enter please num 2 "))
print(f"{x} ** {y} == {x ** y}", sep=" " )





# Задание 2
# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.


two_same = 0
for i in range(100, 999):
    [a], [b], [c] = str(i)
    if [a]==[b] or [a]==[c] or [b]==[c]:
        print(i)
        two_same += 1
print(two_same)



# Задание 3
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

all_dif = 0
for i in range(100, 999):
    [a,b,c] = str(i)
    if [a]!=[b] and [a]!=[c] and [b]!=[c]:
        print(i)
        all_dif += 1
print(all_dif)



# Задание 4
# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.





num = str(input('Please enter the number '))
for digit in num:
    if digit == "3" or digit == "6":
        continue
    print(digit, end="")





while True:
    num = str(input('Please enter the number '))
    for digit in range(len(num)):
        if num[digit] == '6' or num[digit] == '3':
            continue
        else:
            print(num[i], end=' ')
    print()


