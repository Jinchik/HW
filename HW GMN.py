# Курс:
# Python Junior
# Задание 1
# Доработайте игру «Guess my number», добавив следующие
# функции.
# ■ Улучшите игру так, чтобы после угадывания числа,
# выводился номер попытки, которую сделал пользователь для угадывания магического числа.
# ■ Улучшите игру так, чтобы после угадывания числа,
# выводилось количество потраченных попыток, которые сделал пользователь для угадывания магического
# числа.
# Задание 2
# (Дополнительное, на высокую оценку)
# Добавить возможность играть в игру заново.
# После того как пользователь угадает число, отображается сообщение: «Вы хотите сыграть заново? ([Да] или [Нет])».
# Если пользователь отвечает [Да], игра начинается заново, если
# отвечает [Нет] – игра заканчивается.




# Guess my number
import random
game = True
loose = 0
win = 0
while game:
    secret_number = random.randint(1, 20)
    guess_number = 0
    tries = 1
    while guess_number != secret_number and tries < 15:
        guess_number = int(input("Enter number : "))
        tries = tries + 1
        print(f'It is {tries} attempt')
        if tries >5 and tries < 10:
            print("Be careful!")
            if secret_number <= 10:
                print("Number is lower then 10 ")
            elif secret_number >=10:
                print("Number is higher then 10 ")
        if tries >10:
            print("You almost lost, guess better!")
            if secret_number <= 5:
                print("Number is lower then 5 ")
            elif secret_number >=5:
                print("Number is higher then 5 ")
            elif secret_number <= 10:
                print("Number is lower then 10 ")
            elif secret_number >=10:
                print("Number is higher then 10 ")
            elif secret_number <= 15:
                print("Number is lower then 15 ")
            elif secret_number >=15:
                print("Number is higher then 15 ")
        if secret_number < guess_number:
            print('Your number greater than secret ')
        elif secret_number > guess_number:
            print('Your number less than secret ')

    if tries == 15 :
        print(f'You used {tries} attempts, and you loose!!!')
        loose += 1

    else:
        print(f'You used {tries} attempts, not bad, YOU WON!!!')
        win += 1

    print(f"You have {loose} looses, {win} wins ")
    game = str(input("You WON! Do you want to play more? Write '1', or '0' "))
    if game == '0':
        game = 0
        print("Thank you for game!")
        end=input('Please press enter to exit ')






