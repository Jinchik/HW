# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Классы. Объекты


# Задание 1
# Реализуйте класс «Человек». Необходимо хранить в
# полях класса: ФИО, дату рождения, контактный телефон,
# город, страну, домашний адрес. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.
#
class Human:
    lfp = "John", "Doe", 'Odinson'
    bd = "01.01.1989"
    numb = "05511111"
    town = 'NY'
    countr = "USA"
    hadr = 'VanHelsing str. house 13. flat 6'

    def naming(self, new_name):
        self.lfp = new_name
        return self.lfp

    def birth(self, new_birth):
        self.bd = new_birth
        return self.bd

    def number(self, new_number):
        self.numb = new_number
        return self.numb

    def city(self, new_city):
        self.town = new_city
        return self.town

    def country(self, new_country):
        self.countr = new_country
        return self.countr

    def homeadr(self, new_homeadr):
        self.hadr = new_homeadr
        return self.hadr


print(Human.lfp)
print(Human.bd)
new_human = Human()
new_human.naming("Tonny")
print(new_human.lfp)
new_human.birth("15.12.1970")
print(new_human.bd)


# Задание 2
# Создайте класс «Город». Необходимо хранить в полях класса: название города, название региона, название
# страны, количество жителей в городе, почтовый индекс
# города, телефонный код города. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.

class Town:
    tow_name = "Kyiv"
    region = 'Kyivskaya'
    country = "Ukraine"
    countofpeople = 2900000
    postal = '01xxx–04xxx'
    telcode = '+380 44'

    def townnaming(self, new_town):
        self.tow_name = new_town
        return self.tow_name

    def regnaming(self, new_reg):
        self.region = new_reg
        return self.region

    def countnaming(self, new_countr):
        self.country = new_countr
        return self.country

    def livingpeoplechange(self, amount_of_people):
        self.countofpeople = amount_of_people
        return self.countofpeople

    def peoplerise(self):
        self.countofpeople = self.countofpeople + 1000

    def postcodechange(self, new_postal):
        self.postal = new_postal
        return self.postal

    def telcodechange(self, new_code):
        self.telcode = new_code
        return self.telcode


new_town = Town()
print(new_town.countofpeople)
new_town.peoplerise()
print(new_town.countofpeople)
new_town.peoplerise()
new_town.peoplerise()
new_town.peoplerise()
print(new_town.countofpeople)
new_town.livingpeoplechange(3000000)
print(new_town.countofpeople)
new_town.townnaming("Odesa")
print(new_town.tow_name)


# Задание 3
# Создайте класс «Страна». Необходимо хранить в
# полях класса: название страны, название континента,
# количество жителей в стране, телефонный код страны,
# название столицы, название городов страны. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
#
class Country:
    country_name = "Ukraine"
    continent = 'Europe'
    capital = "Kyiv"
    countofpeople = 48000000
    name_of_towns = ["Odesa", "Kyiv", "Nikolaev", "Kherson", "Kharkiv", "Mariupol"]
    telcode = '+380'

    def coutrynaming(self, new_country):
        self.country_name = new_country
        return self.country_name

    def contnaming(self, new_conti):
        self.continent = new_conti
        return self.continent

    def capnaming(self, new_cap):
        self.country = new_cap
        return self.capital

    def livingpeoplechange(self, amount_of_people):
        self.countofpeople = amount_of_people
        return self.countofpeople

    def peoplerise(self):
        self.countofpeople = self.countofpeople + 100000

    def townschanging(self, new_town):
        self.name_of_towns = new_town
        return self.name_of_towns

    def telcodechange(self, new_code):
        self.telcode = new_code
        return self.telcode


new_country = Country()
print(new_country.name_of_towns)
new_country.townschanging(["NY", "LA"])
print(new_country.name_of_towns)
new_country.telcodechange("+370")
print(new_country.telcode)
new_country.peoplerise()
new_country.peoplerise()
new_country.peoplerise()
new_country.peoplerise()
print(new_country.countofpeople)

# Задание 4
# Создайте класс «Дробь». Необходимо хранить в полях
# класса: числитель и знаменатель. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса. Также создайте
# методы класса для выполнения арифметических операций (сложение, вычитание, умножение, деление, и т.д.).



class Fraction:
    numerator = 17
    denominator = 87
    add = 0
    subt = 0
    div = 0
    multi = 0

    def numerchange(self, new_numerator):
        self.numerator = new_numerator
        return self.numerator

    def denomchange(self, new_denominator):
        self.denominator = new_denominator
        return self.denominator

    def addition(self):
        self.add = self.numerator + self.denominator
        return self.add

    def subtraction(self):
        self.subt = self.numerator - self.denominator
        return self.subt

    def division(self):
        self.div = self.numerator / self.denominator
        return self.div

    def multiplication(self):
        self.multi = self.numerator * self.denominator
        return self.multi



new_fraction = Fraction()
new_fraction.addition()
print(f"Additing = {new_fraction.add}")
new_fraction.subtraction()
print(f"Subtraction = {new_fraction.subt}")
new_fraction.division()
print(f"Division = {new_fraction.div}")
new_fraction.multiplication()
print(f"Multiplication = {new_fraction.multi}")
