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


pcost = int(input("Please enter the cost of phone call per minute "))
if pcost > 0:
    time = int(input("Please enter the please enter the time you have been speaking in seconds "))
else:
    print("I can't count anything, if you wont give me a numbers ")
if time > 0:
    oper1 = input(
        "Please enter the what operator you calling from. Choose from this 3: Kyivstar == k, Lifecell == l, MTS == m : ")
    oper2 = input(
        "Please enter the what operator you calling calling to. Choose from this 3: Kyivstar == k, Lifecell == l, MTS == m : ")
else:
    print("So you haven't speak with anyone? ")
sec = 60
minu = time / 60
hour = minu / 60
oper_pricel = (pcost/sec)+(0.12*time)
oper_pricek = (pcost/sec)+(0.13*time)
oper_pricem = (pcost/sec)+(0.14*time)
if oper1 == "l" and oper2 == "l":
    print(
        f"So you spoke {time} in seconds, {minu} in minutes, {hour} in hours. Price you inputed was {pcost} you called from Lifecell to Lifecell and price for this call with your operator will be free. Good luck ")
elif oper1 == "l" and oper2 == "k":
    print(
        f"So you spoke {time} in seconds, {minu} in minutes, {hour} in hours. Price you inputed was {pcost} you called from Lifecell to Kyivstar and price for this call with your operator will be {oper_pricel}. Good luck ")
elif oper1 == "l" and oper2 == "m":
    print(
        f"So you spoke {time} in seconds, {minu} in minutes, {hour} in hours. Price you inputed was {pcost} you called from Lifecell to MTS and price for this call with your operator will be {oper_pricel}. Good luck ")
elif oper1 == "m" and oper2 == "l":
    print(
        f"So you spoke {time} in seconds, {minu} in minutes, {hour} in hours. Price you inputed was {pcost} you called from MTS to Kyivstar and price for this call with your operator will be {oper_pricem}. Good luck ")
elif oper1 == "m" and oper2 == "k":
    print(
        f"So you spoke {time} in seconds, {minu} in minutes, {hour} in hours. Price you inputed was {pcost} you called from MTS to Lifecell and price for this call with your operator will be {oper_pricem}. Good luck ")
elif oper1 == "m" and oper2 == "m":
    print(
        f"So you spoke {time} in seconds, {minu} in minutes, {hour} in hours. Price you inputed was {pcost} you called from MTS to MTS and price for this call with your operator will be free. Good luck ")
elif oper1 == "k" and oper2 == "l":
    print(
        f"So you spoke {time} in seconds, {minu} in minutes, {hour} in hours. Price you inputed was {pcost} you called from Kyivstar to Lifecell and price for this call with your operator will be {oper_pricek}. Good luck ")
elif oper1 == "k" and oper2 == "m":
    print(
        f"So you spoke {time} in seconds, {minu} in minutes, {hour} in hours. Price you inputed was {pcost} you called from Kyivstar to MTS and price for this call with your operator will be {oper_pricek}. Good luck ")
elif oper1 == "k" and oper2 == "k":
    print(
        f"So you spoke {time} in seconds, {minu} in minutes, {hour} in hours. Price you inputed was {pcost*time} you called from Kyivstar to Kyivstar and price for this call with your operator will be free. Good luck ")
else:
    print("Woops, you broke something ")

# Задание 4
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.

#
# finp = int(input("Enter the sales level of the 1 worker "))
# sinp = int(input("Enter the sales level of the 2 worker "))
# tinp = int(input("Enter the sales level of the 3 worker "))
# if finp <= 0 and finp != (1) and sinp <= 0 and sinp != (1) and tinp <= 0 and tinp != (1):
#     print("Incorrect value")
# if finp < 500:
#     f = ((finp * 3 / 100)+200)
#     print("1-t Seller has a low sales rate + salary = ", (finp * 3 / 100)+200)
# elif finp >= 500 and finp <= 1000:
#     f = ((finp * 5 / 100)+200)
#     print("1-t Seller has a midle sales rate + salary = ", (finp * 5 / 100)+200)
# elif finp > 1000:
#     f = ((finp * 8 / 100)+200)
#     print("1-t Seller has a high sales rate + salary = ", (finp * 8 / 100)+200)
# if sinp < 500:
#     s = ((sinp * 3 / 100)+200)
#     print("2-d Seller has a low sales rate + salary = ", (sinp * 3 / 100)+200)
# elif sinp >= 500 and sinp <= 1000:
#     s = ((sinp * 5 / 100)+200)
#     print("2-d Seller has a midle sales rate + salary = ", (sinp * 5 / 100)+200)
# elif sinp > 1000:
#     s = ((sinp * 8 / 100)+200)
#     print("2-d Seller has a high sales rate + salary = ", (sinp * 8 / 100)+200)
# if tinp < 500:
#     t = ((tinp * 3 / 100)+200)
#     print("3-d Seller has a low sales rate + salary = ", (tinp * 3 / 100)+200)
# elif tinp >= 500 and tinp <= 1000:
#     t = ((tinp * 5 / 100)+200)
#     print("3-d Seller has a midle sales rate + salary = ", (tinp * 5 / 100) +200)
# elif tinp > 1000:
#     t = ((tinp * 8 / 100)+200)
#     print("3-d Seller has a high sales rate + salary = ", (tinp * 8 / 100) +200)
# else:
#     print("Oops, you broke something")
#
# best_sales = f
# if s>f:
#     best_sales = s
#     print("Second Seller has the best Salary, and get 200 bonus to his salary ", best_sales + 200)
# elif t>f:
#     best_sales = t
#     print("Third Seller has the best Salary, and get 200 bonus to his salary ", best_sales + 200)
# else:
#     print("First Seller has the best Salary, and get 200 bonus to his salary ", best_sales + 200)
#
