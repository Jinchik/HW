# Курс: «Введение в язык
# программирования Python
# Модуль 5. Файлы.
# Тема: Файлы. Часть 1
import random
import time
import re

# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.
#
f1 = open('test1.txt', 'wt')
f2 = open('test2.txt', 'wt')
f3 = open('test3.txt', 'at')

f1.write('Hello, cruel World ')
f2.write('Hello, the world isn\'t cruel')
f1 = open('test1.txt', 'rt')
f2 = open('test2.txt', 'rt')
fr1 = f1.read()
fr2 = f2.read()
print(f1.read())
print(f2.read())
for i in fr1:
    if i not in fr2:
        f3.write(i)
for j in fr2:
    if j not in fr1:
        f3.write(j)
f3 = open('test3.txt', 'rt')
print(f3.read())
f1.close()
f2.close()
f3.close()

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.


countsymb = (0)
countstr = (0)
glas = ("a", "e", "o", "u")
soglas = ("H", "h", "l", "c", "r", "W", "d")
numb = ("1", "2", "3")
countglas = (0)
countsogl = (0)
countnumb = (0)
f1 = open('test1.txt', 'wt')
f1.write('111 Hello, 222 cruel World, 111222 ')
f1 = open('test1.txt', 'rt')
f4 = open('test4.txt', 'at')
fr1 = f1.read()

for i in fr1:
    countsymb += 1
f4.write(f"This is symbols count  {countsymb} ")


for i in fr1:
    if i == " ":
        countstr += 1
f4.write(f"This is words count {countstr} ")


for i in fr1:
    for j in glas:
        if i == j:
            countglas += 1
f4.write(f"This is vowels count {countglas} ")


for i in fr1:
    for j in soglas:
        if i == j:
            countsogl += 1
f4.write(f"This is consonants count {countsogl} ")


for i in fr1:
    for j in numb:
        if i == j:
            countnumb += 1
f4.write(f"This is numbers count {countnumb} ")
f4 = open('test4.txt', 'rt')
print (f4.read())

# Задание 3
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.

count = 0
f1 = open("test1.txt", 'w')
f2 = open("test2.txt", 'w')
f1.write('Hello, cruel World \nHello, cruel World \nHello, cruel World \nHello, cruel World \n')
f1 = open("test1.txt", 'r')
fr1 = f1.read()
i = ("Hello, cruel World ")

while count <=2:
    if i in fr1:
        f2.write(f"{i} \n")
        count += 1
f2 = open("test2.txt", 'r')
fr2 = f2.read()
print(fr2)


# Задание 4
# Дан текстовый файл. Найти длину самой длинной
# строки.

# # maxcount1 = 0
# # maxcount2 = 0
# # maxcount3 = 0
# # maxcount4 = 0
f1 = open("test1.txt", 'w')
f1.write('Hello, cruel World \nHello, cruel World!!!! \nHello, cruel World \nHello, cruel World \n')
f1 = open("test1.txt", 'r')
fr1 = f1.readlines(1)

fr2 = f1.readlines(2)

fr3 = f1.readlines(3)

fr4 = f1.readlines(4)

print(f"This is the longest string {max(fr1,fr2,fr3,fr4)}")

#
# # for i in fr1:
# #     maxcount1 += 1
# # print(maxcount1)
# # for i in range(len(fr2)):
# #     maxcount2 += 1
# # print(maxcount2)
# # for i in range(len(fr3)):
# #     maxcount3 += 1
# # print(maxcount3)
# # for i in range(len(fr4)):
# #     maxcount4 += 1
# # print(maxcount4)
#




# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.

word = ('Hello')
f1 = open("test1.txt", 'w')
f2 = open("test2.txt", 'w')
f1.write('Hello, cruel World \nHello, cruel World!!!! \nHello, cruel World \nHello, cruel World \n')
f1 = open("test1.txt", 'r')
fr1 = f1.read()
print(fr1.count(word))







# Задание 6
# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.
word = input('Enter the word please you want to replace \n')
replace = input('Enter the word please you want to replace with \n')
f1 = open("test1.txt", 'w')
f2 = open("test2.txt", 'w')
f1.write(f'Hello, cruel World \nHello, cruel World!!!! \n{word}, cruel World \nHello, cruel World \n')
f1 = open("test1.txt", 'r')
fr1 = f1.read()
fr1 = fr1.replace(word, replace)
print(fr1)
