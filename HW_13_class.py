# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Классы. Объекты


# Задание 1
# Реализуйте класс «Человек». Необходимо хранить в
# полях класса: ФИО, дату рождения, контактный телефон,
# город, страну, домашний адрес. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.

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
new_human.naming("Tony")
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
    name = "Kyiv"
    region = 'Kyivskaya'
    country = "Ukrain"
    countofpeople = 2900000
    postal = '01xxx–04xxx'
    telcode = '+380 44'

    def townnaming(self, new_town):
        self.name = new_town







# Задание 3
# Создайте класс «Страна». Необходимо хранить в
# полях класса: название страны, название континента,
# количество жителей в стране, телефонный код страны,
# название столицы, название городов страны. Реализуйте
# Практическое задание
# 1
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# Задание 4
# Создайте класс «Дробь». Необходимо хранить в полях
# класса: числитель и знаменатель. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса. Также создайте
# методы класса для выполнения арифметических операций (сложение, вычитание, умножение, деление, и т.д.).
