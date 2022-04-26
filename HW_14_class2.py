# Курс: «Введение в язык
# программирования Python
# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Классы. Объекты. Часть 1


# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# Old attempt
# class Car:
#     price = "Hummer H3"
#     year = '2005'
#     manufacturer = "General Motors"
#     engine_capacity = 3.5
#     color = ["Black"]
#     price = 126000
#
#     def change_year(self,new_year):
#         self.year = new_year
#         return self.year
#
#     def change_model(self,new_model_name):
#         self.price = new_model_name
#         return self.price
#
#     def change_manuf(self,new_manuf):
#         self.manufacturer = new_manuf
#         return self.manufacturer
#
#     def change_eng_cap(self,new_eng_cap):
#         self.engine_capacity = new_eng_cap
#         return self.engine_capacity
#
#     def change_color(self,new_color):
#         self.color = new_color
#         return self.color
#
#     def change_price(self,new_price):
#         self.price = new_price
#         return self.price
#

# New attempt
class Car:
    def add(self, model, year, manuf, engine, color, price):
        self.model = model
        self.year = year
        self.manuf = manuf
        self.engine = engine
        self.color = color
        self.price = price

    def aboutcar(self):
        return (
            f"Model {self.model} was made in {self.year} by {self.manuf}, with engine capacity {self.engine}. Color of the car is"
            f" {self.color} and price is {self.price} ")

    def modelchange(self, new_model):
        self.model = new_model

    def yearchange(self, new_year):
        self.year = new_year

    def manufchange(self, new_manuf):
        self.manuf = new_manuf

    def enginechange(self, new_engine):
        self.engine = new_engine

    def colorchange(self, new_color):
        self.color = new_color

    def pricechange(self, new_price):
        self.price = new_price

    def pricerise(self):
        self.price = self.price + 1000


hummer = Car()
hummer.modelchange ("Hummer H3")
hummer.yearchange(2010)
hummer.manufchange("GM")
hummer.enginechange(3.5)
hummer.colorchange("Black")
hummer.pricechange(20000)
print(hummer.aboutcar())
hummer.pricerise()
print(hummer.aboutcar())

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.
#
class Book:
    def add(self, name, year, distributed, genre, author, price):
        self.name = name
        self.year = year
        self.distributed = distributed
        self.genre = genre
        self.author = author
        self.price = price

    def aboutbook(self):
        return (
            f"The book {self.name} was written in {self.year} and distributed by {self.distributed}. It's genre is {self.genre} and author is"
            f" {self.author}. It was selling with recommended price {self.price} ")

    def namechange(self, new_name):
        self.name = new_name

    def yearchange(self, new_year):
        self.year = new_year

    def distrchange(self, new_distr):
        self.distributed = new_distr

    def genreechange(self, new_genre):
        self.genre = new_genre

    def authorchange(self, new_author):
        self.author = new_author

    def pricechange(self, new_price):
        self.price = new_price

    def pricerise(self):
        self.price = self.price + 100
b_1984 = Book()
b_1984.namechange("1984")
b_1984.yearchange("1948")
b_1984.distrchange("Secker and Warburg")
b_1984.genreechange("Dystopian")
b_1984.authorchange("George Orwell")
b_1984.pricechange(15)
print(b_1984.aboutbook())
b_1984.pricerise()
print(b_1984.aboutbook())

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса


class Stadium:
    def add(self, name, year, country, town, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.town = town
        self.capacity = capacity

    def aboutstad(self):
        return (
            f"The stadium's name is {self.name}, was opened in {self.year}, the country he placed in is {self.country}, "
            f"and the town is {self.town}, it's max capacity is {self.capacity}")


    def namechange(self, new_name):
        self.name = new_name

    def yearchange(self, new_year):
        self.year = new_year

    def countrychange(self, new_country):
        self.country = new_country

    def townchange(self, new_town):
        self.town = new_town

    def capachange(self, new_capa):
        self.capacity = new_capa

    def caparise(self):
        self.capacity = self.capacity + 1000
colosseum = Stadium()
colosseum.namechange("Colosseum")
colosseum.yearchange(70)
colosseum.countrychange("Rome Impire")
colosseum.townchange("Rome")
colosseum.capachange(65000)
print(colosseum.aboutstad())
colosseum.caparise()
print(colosseum.aboutstad())

