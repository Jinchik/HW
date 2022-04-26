# Курс: «Введение в язык
# программирования Python
# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Классы. Объекты. Конструкторы.
# Перегрузка методов. Часть 2


# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# конструктор, а также необходимые перегруженные методы.
class Car:
    model = str()
    yearmade = float()
    manufacturer = str()
    engine_capacity = float()
    color = str()
    price = int()
    material = str()
    __age = 0

    def __init__(self, model, manuf, price, yearmade):
        self.name = model
        self.yearmade = yearmade
        self.manufacturer = manuf
        self.price = price
        self.material = "Metal"

    def __str__(self):
        return f"The name of the model is {self.model}, it was manufactured by {self.manufacturer}," \
               f" it's price is {self.price}, and it's made of {self.material} in {self.yearmade}"

    def enginechange(self, new_engine):
        self.engine_capacity = new_engine

    def colorchange(self, new_color):
        self.engine_capacity = new_color

    def agechange(self, new_age):
        self.engine_capacity = new_age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age <= 30:
            self.__age = new_age
            print("can be sold")
            return new_age
        elif new_age >= 30:
            self.__age = new_age
            print("It's junk")
            return new_age


import random


class Selling(Car):
    __sel_pos = str()

    def __init__(self, model, manuf, price, yearmade):
        self.name = model
        self.yearmade = yearmade
        self.manufacturer = manuf
        self.price = price
        self.material = "Metal"
        self.age = random.choice([29,35])

    def __str__(self):
        return f"The name of the model is {self.name}, it was manufactured by {self.manufacturer}," \
               f" it's price is {self.price}, and it's made of {self.material} in {self.yearmade}"

    @property
    def sel_pos(self):
        return self.__sel_pos
    @sel_pos.setter
    def sel_pos(self,new_sel_pos):
        if self.age <= 30 and new_sel_pos == "I want to sell it":
            self.__sel_pos = new_sel_pos
            print("You can sell")
        else:
            print("You can't sell")

hummer = Selling("Hummer H3","GM",15000,2010)
print(hummer)
print(hummer.age)
hummer.sel_pos = ("I want to sell it")



# Задание 2
# К уже реализованному классу «Книга» добавьте конструктор, а также необходимые перегруженные методы.


# Задание 3
# К уже реализованному классу «Стадион» добавьте
# конструктор, а также необходимые перегруженные методы.
