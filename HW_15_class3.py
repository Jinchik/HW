# Курс: «Введение в язык
# программирования Python
# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Классы. Объекты. Конструкторы.
# Перегрузка методов. Часть 2


# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# конструктор, а также необходимые перегруженные методы.

import random


class Car:
    age = random.randint(1, 50)

    def __init__(self, model_name, year, manuf, engine, color, price):
        self.model = model_name
        self.year = year
        self.manuf = manuf
        self.engine = engine
        self.color = color
        self.price = price

    def __str__(self):
        return f"The name of the model is {self.model}, it was manufactured by {self.manuf}," \
               f"has engine {self.engine}, it's color is {self.color}m it's price is {self.price}," \
               f" and it's made in {self.year}"


class Hummer(Car):
    __sel_posib = str()

    @property
    def sel_posib(self):
        return self.__sel_posib

    @sel_posib.setter
    def sel_posib(self, new_sel_posib):
        if self.age <= 30 and new_sel_posib == "Sell":
            self.__sel_posib = new_sel_posib
            print("Can be sold")
        else:
            self.__sel_posib = new_sel_posib
            print("I don't need this junk")


car_a = Hummer("H3", 2010, "GM", 3.5, "Black", 30000)
print(car_a)
print(car_a.age)
car_a.sel_posib = "Sell"


# Задание 2
# К уже реализованному классу «Книга» добавьте конструктор, а также необходимые перегруженные методы.
# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:

    rare = random.choice(["Rare", "Not Rare"])
    __money = int()

    def __init__(self, name, year, distr, genre, author, price):
        self.name = name
        self.year = year
        self.distr = distr
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return f"The book {self.name} was written in {self.year} and distributed by {self.distr}. " \
               f"It's genre is {self.genre} and author is" \
               f" {self.author}. It was selling with recommended price {self.price} "

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,new_money):
        if new_money >= 20 and self.rare == "Rare":
            self.__money == new_money
            print("You can buy it.")
        elif new_money <= 20 and self.rare == "Rare":
            self.__money == new_money
            print("You don't have money, sorry.")
        elif new_money >= 20 and self.rare == "Not Rare":
            self.__money == new_money
            print("You have a lot of money, maybe u'll think about better book.")
        elif new_money <= 20 and self.rare == "Not Rare":
            self.__money == new_money
            print("You have a few money, and this book is the only 1 you can have.")



book_a = Book("Just","Testing","The","Code","Sorry","Please")
print(book_a)
print(book_a.rare)
book_a.money = 15
book_a.name = "1984"
print(book_a.name)

# Задание 3
# К уже реализованному классу «Стадион» добавьте
# конструктор, а также необходимые перегруженные методы.

class Stadium:
    def __init__(self, name, year, country, town):
        self.name = name
        self.year = year
        self.country = country
        self.town = town
        self.capacity = random.randint(45000,70000) #Max 50000

    def __str__(self):
        return (
            f"The stadium's name is {self.name}, was opened in {self.year}, the country he placed in is {self.country}, "
            f"and the town is {self.town}, it's max capacity is {self.capacity}")
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self,capacity):
        if capacity >50000:
            self.__capacity = 50000



stad_a = Stadium("Colesium",70,"Rome Impire","Rome")
print(stad_a.capacity)
print(stad_a)


