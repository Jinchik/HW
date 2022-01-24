# Задание 1
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.

num1 = int(input("Please enter the 1 number "))
num2 = int(input("Please enter the 2 number "))
while num1 <= num2 and num1 != 0 and num2 != 0 and num1 > 0 and num2 > 0:
    if num1 % 7 == 0:
        print(num1)
    num1 = num1 + 1
else:
    print("You entered 0 or number less then 0 ")

# Задание 2
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.

num1 = int(input("Please enter the number, that is lower then 2 : "))
num2 = int(input("Please enter the number, that is higher then 1 : "))
while num1 <= num2 and num1 != 0 and num2 != 0 and num1 > 0 and num2 > 0:
    print(num1)
    num1 = num1 + 1


num1 = int(input("Please enter the number, that is higher then 2 : "))
num2 = int(input("Please enter the number, that is lower then 1 : "))
while num1 >= num2 and num1 != 0 and num2 != 0 and num1 > 0 and num2 > 0:
    print(num1)
    num1 = num1 - 1



num1 = int(input("Please enter the number, that is higher then 2 : "))
num2 = int(input("Please enter the number, that is lower then 1 : "))
while num1 >= num2 and num1 != 0 and num2 != 0 and num1 > 0 and num2 > 0:
    if num1 % 7 == 0:
        print(num1)
    num1 = num1 - 1



num1 = int(input("Please enter the number, that is higher then 2 : "))
num2 = int(input("Please enter the number, that is lower then 1 : "))
count = 0
while num1 >= num2 and num1 != 0 and num2 != 0 and num1 > 0 and num2 > 0:
    if num1 % 5 == 0:
        print(num1)
        count = count + 1
    num1 = num1 - 1
print(f"Number of countes are: {count}")













# Задание 3
# Пользователь вводит с клавиатуры два числа (начало
# и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно вывеДомашнее задание
# 1
# сти слово Buzz. Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
# само число.






num1 = int(input("Please enter the number, that is lower then 2 : "))
num2 = int(input("Please enter the number, that is higher then 1 : "))
while num1 <= num2 and num1 != 0 and num2 != 0 and num1 > 0 and num2 > 0:
    if num1 % 3 == 0:
        print(f"{num1} Fizz")
    elif num1 % 5 == 0:
        print(f"{num1} Buzz")
    if num1 % 3 == 0 and num1 %5 == 0:
        print(f"{num1} Fizz Buzz")
    elif num1 % 5 == 0:
        print(num1)
    num1 = num1 + 1
