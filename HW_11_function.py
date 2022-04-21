# Курс: «Введение в язык
# программирования Python
# Модуль 5. Функции.
# Тема: Функции. Часть 2
#
#
#
#
#
# Задание 1
# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве параметра. Полученный результат возвращается из функции.

def multifunc(x):
    multi = 1
    for num in x:
        multi = multi * num
    return multi
    print(multi)


a = []
while True:
    b = int(input(f"Please enter numbers to see multi of all number. Enter 0 to stop. \n"))
    if b == 0:
        break
    else:
        a.append(b)
print(multifunc(a))


# Задание 2
# Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.


def min(x):
    min = 0
    for n in x:
        if min > n:
            min = n

    return min


a = []
while True:
    b = int(input(f"Please enter numbers to see lowest number. Enter 0 to stop. \n"))
    if b == 0:
        break
    else:
        a.append(b)
print(min(a))

# Задание 3
# Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.


def simple_numb(n):
    numbers = []
    count = (0)
    for num in n:
        if num % 2 != 0:
            count += 1
            numbers.append(num)
    return (f'count = {count},numbers = {numbers}')


n = []
while True:
    b = int(input(f"Please enter numbers from 2 and higher then 2 to se the list of simple numbers. Enter 0 to stop. \n"))
    if b == 0:
        break
    elif b == 1:
        print("You had to enter number higher then 2 or 2")
        quit()
    else:
        n.append(b)
print(simple_numb(n))

# Задание 4
# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.


def deleting(x):
    dellist = []
    print(f'It is full list = {x}')
    count = 0
    for i in x:
        dellist.append(i)
    for dellist[0] in dellist:
        print(f'{dellist[1]} - This number will be deleted')
        del dellist[1]
        count += 1
    return (f'count of deleted numbers = {count}, Numbers that left = {dellist}')
a = []
while True:
    b = int(input(f"Please enter numbers to fill the list. Enter 0 to stop. \n"))
    if b == 0:
        break
    else:
        a.append(b)
print(deleting(a))






# Задание 5
# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий
# элементы обоих списков.

def twolist(x,y):
    together = []

    for i in x,y:
        for j in i:
            together.append(j)
    return together


a = []
b = a
while True:
    c = int(input(f"Please enter numbers to make 1 list from 2. Enter 0 to stop. \n"))
    if c == 0:
        break
    else:
        a.append(c)
print(twolist(a,b))





# Задание 6
# Напишите функцию, высчитывающую степень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержащий полученные результаты

def degree(x,y):
    degreelist = []
    for i in x:
        d=i**y
        degreelist.append(d)
    return degreelist
a = []
b = int(input("Enter please the degree number, you want to high in. \n"))
while True:
    c = int(input(f"Please enter numbers to make the list. Enter 0 to stop. \n"))
    if c == 0:
        break
    else:
        a.append(c)
print(degree(a,b))

