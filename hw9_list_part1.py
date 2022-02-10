# Модуль 4. Строки. Списки.
# Часть 1
# Задание 1
# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.




# text = input("Please, enter the text ")
# if text != text[::-1]:
#     print("It is not palindrome")
# else:
#     print("It is palindrome")
#
#
#
# text = input("Please, enter the text ")
# for i in range(len(text)):
#     if text[i] != text[-i-1]:
#         print("It is not palindrome")
#         break
# else:
#     print("It is palindrome")




#
# Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.


mytext = "Python is the best language!"
mytext_temp = mytext.lower()
listold = list(mytext.split())
listnew = list(mytext_temp.split())
word = ["Python", "is", "best"]
for i in range(len(listnew)) :
    print(listnew[i])
    for j in word :

        if j in listnew[i] :
            listold[i] = listnew[i].upper()
print(' '.join(listold))



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




# #Вариант работает при точном совпадении регистра
#
# text = '''The Star Wars franchise depicts the adventures of characters "A long time ago in a galaxy far, far away",[5] in which humans and many species of aliens (often humanoid) co-exist with robots (typically referred to in the films as 'droids'), who may assist them in their daily routines; space travel between planets is common due to lightspeed hyperspace technology.[6][7][8] Spacecraft range from small starfighters, to huge capital ships such as the Star Destroyers, to space stations such as the moon-sized Death Stars. Telecommunication includes two-way audio and audiovisual screens, and holographic projections.
#
# A mystical power known as the Force is described in the original film as "an energy field created by all living things ... [that] binds the galaxy together".[9] Through training and meditation, those whom "the Force is strong with" are able to perform various superpowers (such as telekinesis, precognition, telepathy, and manipulation of physical energy).[10] The Force is wielded by two major knightly orders at conflict with each other: the Jedi, peacekeepers of the Galactic Republic who act on the light side of the Force through non-attachment and arbitration, and the Sith, who use the dark side by manipulating fear and aggression. While Jedi Knights can be numerous, the Dark Lords of the Sith (or 'Darths') are intended to be limited to two: a master and their apprentice.[11]
#
# Force-wielders are very limited in numbers in comparison to the population. The Jedi and Sith prefer the use of a weapon called a lightsaber, a blade of energy that can cut through virtually any surface and deflect energy bolts. The rest of the population, as well as renegades and soldiers, use laser-powered blaster firearms. In the outer reaches of the galaxy, crime syndicates such as the Hutt cartel are dominant. Bounty hunters are often employed by both gangsters and governments. Illicit activities include smuggling and slavery.'''
# word_list = ['Star','Wars','Force','slavery']
# for word in word_list:
# 	if word in text:
# 		text = text.replace(word,word.upper())
# print(text)
#
# #Не чувствителен к регистру, но обратите внимание, что воздействует только на "чистые слова", самое последнее слова, является один целым с точкой, потому его не меняет
# text = '''The Star Wars franchise depicts the adventures of characters "A long time ago in a galaxy far, far away",[5] in which humans and many species of aliens (often humanoid) co-exist with robots (typically referred to in the films as 'droids'), who may assist them in their daily routines; space travel between planets is common due to lightspeed hyperspace technology.[6][7][8] Spacecraft range from small starfighters, to huge capital ships such as the Star Destroyers, to space stations such as the moon-sized Death Stars. Telecommunication includes two-way audio and audiovisual screens, and holographic projections.
#
# A mystical power known as the Force is described in the original film as "an energy field created by all living things ... [that] binds the galaxy together".[9] Through training and meditation, those whom "the Force is strong with" are able to perform various superpowers (such as telekinesis, precognition, telepathy, and manipulation of physical energy).[10] The Force is wielded by two major knightly orders at conflict with each other: the Jedi, peacekeepers of the Galactic Republic who act on the light side of the Force through non-attachment and arbitration, and the Sith, who use the dark side by manipulating fear and aggression. While Jedi Knights can be numerous, the Dark Lords of the Sith (or 'Darths') are intended to be limited to two: a master and their apprentice.[11]
#
# Force-wielders are very limited in numbers in comparison to the population. The Jedi and Sith prefer the use of a weapon called a lightsaber, a blade of energy that can cut through virtually any surface and deflect energy bolts. The rest of the population, as well as renegades and soldiers, use laser-powered blaster firearms. In the outer reaches of the galaxy, crime syndicates such as the Hutt cartel are dominant. Bounty hunters are often employed by both gangsters and governments. Illicit activities include smuggling and slavery.'''
# word_list = ['Star','Wars','Force','slavery']
# text_list = text.split(' ')
# for i in range(len(word_list)):
# 		for j in range(len(text_list)):
# 				if word_list[i].lower() == text_list[j].lower():
# 						text_list[j] = text_list[j].upper()
# upper_text = ''
# for text_word in text_list:
# 		upper_text = upper_text + ' ' + text_word
# print(upper_text)
# 2.0#Не чувствителен к регистру, но обратите внимание, что воздействует только на "чистые слова", самое последнее слова, является один целым с точкой, потому его не меняет
text = '''The Star Wars franchise depicts the adventures of characters "A long time ago in a galaxy far, far away",[5] in which humans and many species of aliens (often humanoid) co-exist with robots (typically referred to in the films as 'droids'), who may assist them in their daily routines; space travel between planets is common due to lightspeed hyperspace technology.[6][7][8] Spacecraft range from small starfighters, to huge capital ships such as the Star Destroyers, to space stations such as the moon-sized Death Stars. Telecommunication includes two-way audio and audiovisual screens, and holographic projections.

A mystical power known as the Force is described in the original film as "an energy field created by all living things ... [that] binds the galaxy together".[9] Through training and meditation, those whom "the Force is strong with" are able to perform various superpowers (such as telekinesis, precognition, telepathy, and manipulation of physical energy).[10] The Force is wielded by two major knightly orders at conflict with each other: the Jedi, peacekeepers of the Galactic Republic who act on the light side of the Force through non-attachment and arbitration, and the Sith, who use the dark side by manipulating fear and aggression. While Jedi Knights can be numerous, the Dark Lords of the Sith (or 'Darths') are intended to be limited to two: a master and their apprentice.[11]

Force-wielders are very limited in numbers in comparison to the population. The Jedi and Sith prefer the use of a weapon called a lightsaber, a blade of energy that can cut through virtually any surface and deflect energy bolts. The rest of the population, as well as renegades and soldiers, use laser-powered blaster firearms. In the outer reaches of the galaxy, crime syndicates such as the Hutt cartel are dominant. Bounty hunters are often employed by both gangsters and governments. Illicit activities include smuggling and slavery.'''
word_list = ['Star','Wars','Force','slavery']
text_list = text.split(' ')
for i in range(len(word_list)):
		for j in range(len(text_list)):
				if word_list[i].lower() in text_list[j].lower():
						text_list[j] = text_list[j].upper()
upper_text = ''
for text_word in text_list:
		upper_text = upper_text + ' ' + text_word
print(upper_text)

# 'slavery' == 'slavery.' 1.0 FALSE
# 'slavery' in 'slavery.' 2.0 TRUE
# 'slavery' in 'slavery' 2.0 TRUE







# Задание 3
# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный
# результат.



# text = 'Is something is here? Really Something is here. Belive me! '
# print(text.count('. ')+text.count('! ')+text.count('? '))
