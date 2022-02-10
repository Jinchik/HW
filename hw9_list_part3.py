# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы
# обоих списков;
# ■ Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы
# общие для двух списков;
# ■ Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.
list1 = [1, 7, 23, 88, 666, 4, 3, 2, 0, 1, 5,-1]
list2 = [19, 12, 23, 8, 686, 3, 3, 2, 0, 9, 5,-2]
lisplus = []
liswithoutsame = []
lisonlysame = []
notsame = []
mini = []
maxi = []
temp1 =1
temp2 =0
# #1 way
# listplus =[list1]+[list2]#2 in 1
# print(listplus)
# liswithoutsame = list(set(listplus[0]))
# print(liswithoutsame)# without repeat
# 2 way
for num1 in list1:
    lisplus.append(num1)
for num2 in list2:
    lisplus.append(num2)
print(lisplus)  # 2 in 1
for number in range(1, len(lisplus)):
    if lisplus[number] != lisplus[number - 1]:
        liswithoutsame.append(lisplus[number])
print('without repeat', liswithoutsame)  # without repeat
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            lisonlysame.append(list1[i])
print("lisonlysame", lisonlysame)  # same
for i in lisplus:
    if i not in notsame:
        notsame.append(i)
print("notsame", notsame)  # unic
for k in lisplus:
    if k < temp1:
        temp1 = k
    elif k > temp2:
        temp2 = k
mini.append(temp1)
maxi.append(temp2)
print("Max",maxi,"min",mini)


