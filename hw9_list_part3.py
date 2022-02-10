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



#############

# l = [1,2,3,4,4,5,6,7,8,9,0,1,3]
# for i in range(1,len(l)):
#     if l[i] == l[i-1]:
#         l[i] = ''
# while '' in l:
#     l.remove('')
# print(l)
# l = [1,2,3,4,4,5,6,7,8,9,0,1,3]
# a = 1
# length = len(l)
# while a < length:
#     if l[a] == l[a-1]:
#         l.pop(a)
#     a = a + 1
#     length = len(l)
# print(l)



###############



# s1 = [4,1,2,3,4]
# s2 = [3,10,2,5,7]
# mini = s1[0]
# maxi = s1[0]
# s_minmax = []
# for n in range(len(s1)):
#     if mini > s1[n]:
#         mini = s1[n]
#         s_minmax.append(mini)
#     if maxi < s1[n]:
#         maxi = s1[n]
#         s_minmax.append(maxi)
# print(mini, maxi)
# mini = s2[0]
# maxi = s2[0]
# for n in range(len(s2)):
#     if mini > s2[n]:
#         mini = s2[n]
#         s_minmax.append(mini)
#     if maxi < s2[n]:
#         maxi = s2[n]
#         s_minmax.append(maxi)
# print(s_minmax)
#
# '''# ■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# # ■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.'''
# s1 = [1,2,3,4]
# s2 = [1,2,5,6,8]
# s3 = s1[:]
# for s in s2:
#     if s not in s3:
#         s3.append(s)
#
# s1 = [1,2,3,4]
# s2 = [1,2,5,6,8]
# s3 = s1[:]
# for s in s2:
#     if s in s3:
#         continue
#     else:
#         s3.append(s)
#
#
# s1 = [1,2,3,4]
# s2 = [1,2,5,6,8]
# s_rr = s1[:]
# for i in s2:
#     if i not in s_rr:
#         s_rr.append(i)
# print(s_rr)