# Домашнее задание 1
# Создать 4 переменных разных типов и указать в них данные.
# Например: color, age, animal, alcohol и так далее.
# С использованием данных переменных написать программу, которая выводит текст, по аналогии с тем, как делали на паре.
color = "brown"
age = "about 15-20 years"
animal = "monkey"
alcohol = "fermented fruits"
name = input("Hello, what is your name? ")
print(
    f" Nice to meet you {name} \n I want to tell you about {animal} \n Their color is {color} \n They are living {age} \n And really like {alcohol}!")
end_of_hw = input(" That is the whole story, please press enter to exit, good luck ")
# Домашнее задание 2
# Создать программу которая при вводе данных в переменную метр преобразует его в фут, дюйм, милю и
# литр в пинту, галлон, баррель.
# С использованием данных результатов написать программу, которая выводит текст, по аналогии с тем, как делали на паре.
meter = int(input(
    "Hello, do you want some conversion? Ok, let's start with meter, how many meters do you want to be converted?  "))
litre = int(input("Now it's time for litres "))
foot = meter * 0.3
inch = foot / 100 * 2.54
mile = meter / 1482
pint = litre * 0.56
gallon = litre / 3.79
barrel = litre / 158.9
print(
    f"Soooo, what we got here? You entered {meter} this is the amount of meters:\n {foot} it is the amount in foots\n {inch} it is the amount in inches\n {mile} it is the amount in miles. Great!")
print("Now is is time for litres! \n", "You entered", litre, "litres, great \n", pint, "It is the amount in pints \n",
      gallon, "It is the amount in gallons \n", barrel, "It is the amount in barrels")
EndOfThis = input(
    "Great, I think that is it. I gave you all knowladge I had. Press enter to end this great conversion and good luck")
