# Модуль 4. Строки. Списки.
# Часть 1
# Задание 1
# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.


text = input("Please, enter the text ")
if text != text[::-1]:
    print("It is not palindrome")
else:
    print("It is palindrome")



text = input("Please, enter the text ")
for i in range(len(text)):
    if text[i] != text[-i-1]:
        print("It is not palindrome")
        break
else:
    print("It is palindrome")


#
# Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.


text = "Python is the best language!"
word_list = ["Python", "is", "best"]
for word in word_list:
    if word in text:
        text = text.replace(word, word.upper())
print(text)


text ='Python is the best language!'
word_list = ["Python", "is", "best"]
text_list = text.split(' ')
for i in range(len(word_list)):
    for j in range(len(text_list)):
        if word_list[i].lower() in text_list[j].lower():
            text_list[j] = text_list[j].upper()
upper_text = ''
for text_word in text_list:
    upper_text = upper_text + ' ' + text_word
print(upper_text)









# Задание 3
# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный
# результат.


text = 'Is something is here? Really Something is here. Belive me! '
print(text.count('. ')+text.count('! ')+text.count('? '))
