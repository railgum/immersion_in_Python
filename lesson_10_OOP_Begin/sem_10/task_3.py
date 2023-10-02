# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Human:
    def __init__(self, first_name, second_name, last_name, age, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self._age = age
        self.__gender = gender

    def full_name(self):
        return (f'{self.last_name} {self.first_name} {self.second_name}')

    def show_age(self):
        return self._age
    def show_gender(self):
        return self.__gender
    def birthday(self):
        self._age += 1


rail = Human('Раиль', 'Раисович', 'Гумеров', 44, 'М')
# print(rail.full_name())
# print(rail.show_age())
# rail.birthday()
# print(rail.show_age())