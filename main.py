# # # # # print("Hey, hey")
# # # # # print("Alex")
# # # # # print("My name is Alex.\t2021\nI live in Somewhere.\t2222")

# # # # # #variables
# # # # # #conditions
# # # # # #loops

# # # # # a='Hello'
# # # # # print(a)
# # # # str string  '5' 'Andrey' - строка
# # # # int integer 5 120 - целые числа
# # # # # float float 5.0 12.4 -1.5 - тип данных с плавующей точкой
# # # # # # bool bolean True False - 1,0 

# # # # #print("Hello, my name is",name)
# # # # print("I have a little",color,pet)
# # # # print("I have a little"+" "+str(color)+" "+str(pet))
# # # # print("I have a little {} {}" .format(color,pet)) #<python 3.6
# # # # print(f"I have a little {color} {pet}")


# # # name="Odessa"
# # # terrain='near the sea'
# # # temperature='25'
# # # color= "black"
# # # pet='cat'
# # # print(f"I live in {name}, It is the beautiful city {terrain}. We have summer with {temperature}C")
# # # about_me = f"I live in {name}, It is the beautiful city {terrain}. We have summer with {temperature}C."
# # # print(about_me)



# # #str - должно быть в ковычках

# # #int  - можно превращать в цифры только если есть цифры (int("5"))

# # #float - преображает числа в дробные, и строки если там есть цифры.

# # #bool - TRUE FALSE 
# # print(bool('True'))
# # print(bool('Anything'))
# # print(bool(''))
# # print(bool(0))
# # print(float("5"))
# # print(str(324234))
# # print(int(5.99999))# - округление вниз
# # print ( str ( 5.0 ) )
# # print(bool(0.0))
# # print(float(False))
# # print(int(False))
# # print(str(True))



# # #SizeConverter
# # #g = int(input("Enter your count of grams : "))
# # #print("You take "+str(g)+"it's equal "+str(g/1000)+" kilograms")

# # #g = int(input("Enter your count of grams : "))
# # #kg = g/1000
# # #print("You take "+str(g)+"it's equal "+str(kg)+" kilograms")
# # +,-,*,/,//,%,**
# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2)
# print(4/2)
# print(5//2)
# print(5%2)
# print(5**2)
# number1=float(input("Enter numer1 : "))
# number2=float(input("Enter numer2 : "))
# print(f'{number1}+{number2}={number1+number2}')
# print(f'{number1}-{number2}={number1-number2}')
# print(f'{number1}*{number2}={number1*number2}')
# print(f'{number1}/{number2}={number1/number2}')
# print(f'{number1}**{number2}={number1**number2}')
# print(f'{number1}//{number2}={number1//number2}')
# print(f'{number1}%{number2}={number1%number2}')

#Правила именования переменных

#SizeConverter
#g = int(input("Enter your count of grams : "))
#print("You take "+str(g)+"it's equal "+str(g/1000)+" kilograms")

#g = int(input("Enter your count of grams : "))
#kg = g/1000
#mg = g*1000
#print("You take "+str(g)+"it's equal "+str(mg)+" kilograms")

byte = int(input("Enter amount of bytes : "))
bit = byte*8
kilobyte = byte/1024
mbyte = byte/1048576
gbyte = byte/1073741824
print(f"You entered {byte} it is : {bit} bits \n {kilobyte} kbits \n {mbyte} mbyte \n {gbyte} gbyte") 
 







 #str
##int
# print(int("5")) #5
# print(int("Hello World")) #ERROR
##float
# print(float("5.5")) #5.5
# print(float("Hello World")) #ERROR
##bool
# print(bool('True'))
# print(bool('False'))
# print(bool('Anything'))
# print(bool(''))

#int
##str
# print(str(5))
# print(str(52323232))
##float
# print(float(5))
# print(float(-5))
##bool
# print(bool(5))
# print(bool(0))
# print(bool(-1))

#float
##int
# print(int(5.9999999999))
##str
# print(str(5.7))
##bool
# print(bool(1.0))
# print(bool(0.00000001))
# print(bool(0.0))

#bool
##int
# print(int(True))
# print(int(False))
##float
# print(float(True))
# print(float(False))
#str
# print(str(True))
# print(str(False))

#Converter
# g = int(input("Enter your count of gramms : "))
# print("You take "+str(g)+" it's equal "+str(g/1000)+" kilogramms")
# kg = g/1000
# print("You take "+str(g)+" it's equal "+str(kg)+" kilogramms")

#Calculator
#+
#-
#*
#/
#//
#%
#**
# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2)
# print(4/2)
# print(5//2)
# print(5%2)
# print(5**2)
# number1 = float(input("Enter number1 : "))
# number2 = float(input("Enter number2 : "))
# print(f'{number1} + {number2} = {number1+number2}')
# print(f'{number1} - {number2} = {number1-number2}')
# print(f'{number1} * {number2} = {number1*number2}')
# print(f'{number1} / {number2} = {number1/number2}')
# print(f'{number1} // {number2} = {number1//number2}')
# print(f'{number1} % {number2} = {number1%number2}')
# print(f'{number1} ** {number2} = {number1**number2}')

#Правила именования переменных
#В начале

#Можно
#a-z
#_
#A-Z

#Нельзя
#а-я А-Я 0-9 +-/""!";%*" ПРОБЕЛ
#Внутри

#Можно
#a-z
#_
#A-Z
#0-9

#Нельзя
#а-я А-Я +-/""!";%*" ПРОБЕЛ

#Style
#nocodestyle
#camelCaseStyle
#snake_case_style
#NOOO
# a1 = 6

#Converter
g = int(input("Enter your count of gramms : "))
kg = g/1000
mg = g*1000
print("You take "+str(g)+" it's equal "+str(mg)+" kilogramms")
#Байт > Бит , Байт > Килобайт , Байт > Мегабайт , Байт > Гигабайт

byte = int(input("Enter count of byte : "))
bit = byte*8
kilobyte = byte/1024
megabyte = kilobyte/1024
gigabyte = megabyte/1024 #byte/1024/1024/1024
print(f"You enter {byte} bytes it's : \n {bit} bits \n {kilobyte} kilobytes \n {megabyte} megabyte \n {gigabyte} gigabyte ")