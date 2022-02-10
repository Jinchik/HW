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
list1 = [1,7,23,88,666,4,3,2,0,1,5]
list2 = [19,12,23,8,686,3,3,2,0,9,5]
lisplus=[]
liswithoutsame =[]





# listplus =[list1]+[list2]#2 in 1
# print(listplus)
# liswithoutsame = list(set(listplus[0]))
# print(liswithoutsame)




for num1 in list1:
    lisplus.append(num1)
for num2 in list2:
    lisplus.append(num2)
# print(lisplus)   #2 in 1
for number in range (len(lisplus)):

    if lisplus[number] != lisplus[number+1] :

        liswithoutsame.append(lisplus[number])
        print(liswithoutsame)


