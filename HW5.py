# Задание 1
# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без
# остатка) нужно вывести слово Fizz. Если число кратно 5
# нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
# вывести само число.
# Если пользователь ввел значение не в диапазоне от 1
# до 100 требуется вывести сообщение об ошибке.


# num = int(input("Please enter a number from 1 to 100 "))
# if num > 100 or num <= 0:
#     print(f"Oh no, I asked you to enter between 1 and 100, and you entered {num}")
# elif num % 3 != 0 and num % 5 != 0:
#     print(num)
# elif num % 3 == 0 and num % 5 == 0:
#     print("Fizz Buzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(("Unknown Error"))
# end1 = input("Great, well dont, press enter to exit")

# Задание 2
# Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
# до седьмой включительно.


# num = int(input("Please enter the number "))
# power = int(input("Please enter the power between 1 and 7 "))
# if num > 0 and power >= 1 and power <= 7:
#     print(f" {num} ** {power}  = " ,  num ** power)
# else:
#     print("You entered incorrect number or incorreect power ")

# Задание 3
# Написать программу подсчета стоимости разговора
# для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.


# Писал поздно, не правильно понял задание,не правильно задание понял. Решил не удалять, оставил этот вариант и правильный.


# s = 1
# m = s / 60
# h = m / 60
# coin = 1
# hr = coin / 100
# hrpm = m*hr
# hrlc = hrpm + 0.1
# hrmt = hrpm + 0.2
# hrky = hrpm + 0.3

# oper = (input("Please enter lifeCell, or mts or kyivstar "))
# time = int(input("Please enter time in seconds "))
# if oper != ("lifeCell" or "mts" or "kyivstar") and time <=0:
#     print("Incorrect value was printed ")
# elif oper == "lifeCell":
#     print(time*m, "It's your time in minutes", time * h, "it's your time in hours", "price per one min on " , oper, "are ", hrlc,"in hrn" )
# elif oper == "mts":
#     print(time*m, "It's your time in minutes", time * h, "it's your time in hours. ", "Price per one min on " ,oper, "are ", hrmt, "in hrn" )
# elif oper == "kyivstar":
#     print(time*m, "It's your time in minutes", time * h, "it's your time in hours", "price per one min on " , oper, "are ", hrky, "in hrn" )
# else:
#     print("Unknown Error")
# dif = input("Please enter two different operators to count the difference between their cost(Without spaces). Enter pleease l for lifeCell, and or m for mts and k or kyivstar ")
# if dif != ("l m" or "m l" or "k m" or "m k" or "k l" or "l k"):
#     print("Incorrect value was printed ")
# elif dif == "l m" or dif == "m l":
#     print(f"Mts is {hrlc - hrmt} cheaper ")


# Задание 4
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.


finp = int(input("Enter the sales level of the 1 worker "))
sinp = int(input("Enter the sales level of the 2 worker "))
tinp = int(input("Enter the sales level of the 3 worker "))
if finp <= 0 and finp != (1) and sinp <= 0 and sinp != (1) and tinp <= 0 and tinp != (1):
    print("Incorrect value")
if finp < 500:
    f = ((finp * 3 / 100)+200)
    print("1-t Seller has a low sales rate + salary = ", (finp * 3 / 100)+200)
elif finp >= 500 and finp <= 1000:
    f = ((finp * 5 / 100)+200)
    print("1-t Seller has a midle sales rate + salary = ", (finp * 5 / 100)+200)
elif finp > 1000:
    f = ((finp * 8 / 100)+200)
    print("1-t Seller has a high sales rate + salary = ", (finp * 8 / 100)+200)
if sinp < 500:
    s = ((sinp * 3 / 100)+200)
    print("2-d Seller has a low sales rate + salary = ", (sinp * 3 / 100)+200)
elif sinp >= 500 and sinp <= 1000:
    s = ((sinp * 5 / 100)+200)
    print("2-d Seller has a midle sales rate + salary = ", (sinp * 5 / 100)+200)
elif sinp > 1000:
    s = ((sinp * 8 / 100)+200)
    print("2-d Seller has a high sales rate + salary = ", (sinp * 8 / 100)+200)
if tinp < 500:
    t = ((tinp * 3 / 100)+200)
    print("3-d Seller has a low sales rate + salary = ", (tinp * 3 / 100)+200)
elif tinp >= 500 and tinp <= 1000:
    t = ((tinp * 5 / 100)+200)
    print("3-d Seller has a midle sales rate + salary = ", (tinp * 5 / 100) +200)
elif tinp > 1000:
    t = ((tinp * 8 / 100)+200)
    print("3-d Seller has a high sales rate + salary = ", (tinp * 8 / 100) +200)
else:
    print("Oops, you broke something")

best_sales = f
if s>f:
    best_sales = s
    print("Second Seller has the best Salary, and get 200 bonus to his salary ", best_sales + 200)
elif t>f:
    best_sales = t
    print("Third Seller has the best Salary, and get 200 bonus to his salary ", best_sales + 200)
else:
    print("First Seller has the best Salary, and get 200 bonus to his salary ", best_sales + 200)

