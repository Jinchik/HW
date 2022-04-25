# Курс: «Введение в язык
# программирования Python
# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Классы. Объекты. Часть 1




# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Car:
    model_name = "Hummer H3"
    year = '2005'
    manufacturer = "General Motors"
    engine_capacity = 3.5
    color = ["Black"]
    price = 126000

    def change_year(self,new_year):
        self.year = new_year
        return self.year

    def change_model(self,new_model_name):
        self.model_name = new_model_name
        return self.model_name

    def change_manuf(self,new_manuf):
        self.manufacturer = new_manuf
        return self.manufacturer

    def change_eng_cap(self,new_eng_cap):
        self.engine_capacity = new_eng_cap
        return self.engine_capacity

    def change_color(self,new_color):
        self.color = new_color
        return self.color

    def change_price(self,new_price):
        self.price = new_price
        return self.price





# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.






# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса