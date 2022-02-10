# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/
#


exp = list(input("Enter the expression please with +, or-, or*, or/< or**. or//. and numbers under 10 "))
if exp[1] == "+":
    print(int(exp[0]) + int(exp[2]))
elif exp[1] == "-":
    print(int(exp[0]) - int(exp[2]))
elif exp[1] == "*":
    print(int(exp[0]) * int(exp[2]))
elif exp[1] == "/":
    print(int(exp[0]) / int(exp[2]))
elif exp[1] == "**":
    print(int(exp[0]) ** int(exp[2]))
elif exp[1] == "//":
    print(int(exp[0]) // int(exp[2]))

# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.


numbers = [1, 2, 3, 4, -5, 6, 35, -1, -4, 9, 20, 21, 15, 0, 377, 0, 0]
min = 0
max = 0
neg = 0
pos = 0
zer = 0
for number in numbers:
    if number < min:
        min = number
    elif number > max:
        max = number
    elif number < 0:
        neg = neg + 1
    elif number > 0:
        pos = pos + 1
    elif number == 0:
        zer = zer + 1
print(f"min = {min}, max = {max}, neg = {neg}, pos = {pos}, zer = {zer}")
