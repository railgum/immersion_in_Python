# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
#   суммы цифр id на семь

from task_3 import Human


class Employee(Human):
    def __init__(self, id_number, first_name, second_name, last_name, age, gender):
        super().__init__(first_name, second_name, last_name, age, gender)
        self.__id = Employee.check_id(id_number)
        # self.access_level = sum(map(int, str(id_number))) % 7 # вместо этого можно property

    @classmethod
    def check_id(cls, id_number):
        if len(str(id_number)) == 6:
            return id_number
        raise ValueError

    @property
    def access_level(self):
        return sum(map(int, str(self.__id))) % 7

emp_1 = Employee(459875, 'Bob', 'Daer', 'Er', 55, 'W')
print(emp_1.full_name(), emp_1.access_level)
