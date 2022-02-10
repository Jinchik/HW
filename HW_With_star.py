# ''Задание 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран.
# * Без использования метода count'''

s = 'chairghdcdfchaircdchfchair'
symbol = 'chair'
r = symbol[0]
count = 0
for i in range(len(s)):
    if s[i] == r:
        if symbol == s[i:i + len(symbol)]:
            count += 1
        else:
            continue
print(count)








# '''Задание 5
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите




'''Задание 5
Пользователь вводит с клавиатуры строку, слово для
поиска, слово для замены. Произведите в строке замену
одного слова на другое. Полученную строку отобразите
на экране.
* Без использования метода replace'''

# s = '1chairghdcdfchaircdchfchair'
# symbol = 'chair'
# new_symbol = '*CHAIR*'
# first_symbol = symbol[0]
# new_line = ''
# i = 0
# while i != len(s):
#     if s[i] == first_symbol:
#         if symbol == s[i:i + len(symbol)]:
#             new_line = new_line + new_symbol
#             i = i + len(symbol)
#         else:
#             new_line += s[i]
#             i += 1
#     else:
#         new_line += s[i]
#         i += 1
# print(new_line)










#
# text = "First word, second word"
# word = "second"
# change = "Third"
# for letter in range(len(text)+1):
#     print (text[letter:])
