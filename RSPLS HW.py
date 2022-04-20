# Домашнее задание №8
# Курс:
# Python Junior
# Задание 1
# Доработайте игру, которую мы делали на уроке.
# ■ Добавьте возможность после окончания игры поиграть
# в игру заново. После окончания игры пользователю
# предлагается сыграть еще раз, если он этого хочет –
# игра начинается заново, иначе заканчивается.
# ■ Если пользователь вводит что-то неправильно – его
# просят ввести свой выбор еще раз, пока он не будет
# правильным.

# Задание 2
# (Дополнительное, на высокую оценку)
# Есть другие варианты игры, которые содержат большее
# количество вариантов – «Камень, ножницы, бумага, ящерица,
# Спок». Переделайте игру по такому принципу.


# Rock Paper Scissors lizard spoke
import random

game = True
global_player1_score = 0
global_player2_score = 0
game_type = str(input('Please enter the game type. pve or pvp '))
if game_type == "pvp" or game_type == "pve":
    print(f'So, you choosed {game_type}')
else:
    print("Please enter a correct value next time")
    game = False
while game:

    player1_choice = ''
    player2_choice = ''
    player1_score = 0
    player2_score = 0
    player1_name = str(input("Enter your name player 1 : "))
    if player1_name == "":
        print('Please enter a name')
        continue
    player2_name = 'Unknown'
    if game_type == 'pvp':
        player2_name = str(input("Enter your name player 2 : "))
        if player1_name == "":
            print('Please enter a name')
            continue
    elif game_type == 'pve':
        player2_name = 'Bot'
    rounds = 3

    for i in range(1, rounds + 1):
        player1_choice = ''
        player2_choice = ''

        while player1_choice != 'r' and player1_choice != 'p' and player1_choice != 's' and player1_choice != 'k' and player1_choice != 'l':
            player1_choice = str(input(f"Enter your choice {player1_name}: [r],[p],[s],[k],[l] : "))
            if player1_choice != 'r' or player1_choice != 'p' or player1_choice != 's' or player1_choice != 'k' or player1_choice != 'l':
                print("Please enter a correct value next time")
                continue
        while player2_choice != 'r' and player2_choice != 'p' and player2_choice != 's' and player2_choice != 'k' and player2_choice != 'l':
            if game_type == 'pvp':
                player2_choice = str(input(f"Enter your choice {player2_name}: [r],[p],[s],[k],[l] : "))
                if player1_choice != 'r' or player1_choice != 'p' or player1_choice != 's' or player1_choice != 'k' or player1_choice != 'l':
                    print("Please enter a correct value next time")
                    continue
            elif game_type == 'pve':
                player2_name = random.choice('rpskl')

        if player1_choice == player2_choice:
            print('Draw round')
        elif player1_choice == 'r':
            if player2_choice == 's':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'p':
            if player2_choice == 'r':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 's':
            if player2_choice == 'p':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'r':
            if player2_choice == 'l':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'l':
            if player2_choice == 'k':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'k':
            if player2_choice == 's':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1

    if player1_score > player2_score:
        print(f'{player1_name} win the game!')
        global_player1_score = global_player1_score + 1
    elif player2_score > player1_score:
        print(f'{player2_name} win the game!')
        global_player2_score = global_player2_score + 1
    else:
        print('Draw game!')
    end = str(input("If you want continue press 1 for yes and 0 for end : "))
    if end == "1":
        print("Let's play again.")
    else:
        game = False
        print("Thnx for the game, and good luck")
