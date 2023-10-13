class InvalidNameError(ValueError):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message
class InvalidAgeError(ValueError):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
class Person:
    def __init__(self, first_name: str, second_name: str, last_name: str, age: int):
        if not isinstance((first_name, last_name, second_name), str) or any(
                [len(first_name.strip()) == 0, len(second_name.strip()) == 0,
                 len(last_name.strip()) == 0]):
            raise InvalidNameError(f'InvalidName')
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        if not isinstance(age, int) or 0 > age > 120:
            raise InvalidAgeError(f'Invalid age')
        self._age = age

    def full_name(self):
        return (f'{self.last_name} {self.first_name} {self.second_name}')

    def show_age(self):
        return self._age

    def birthday(self):
        self._age += 1

class Employee(Person):
    def __init__(self, id_number, first_name, second_name, last_name, age):
        super().__init__(first_name, second_name, last_name, age)
        self.__id = Employee.check_id(id_number)

    @classmethod
    def check_id(cls, id_number):
        if len(str(id_number)) == 6:
            return id_number
        raise ValueError(f'ID ')

    @property
    def access_level(self):
        return sum(map(int, str(self.__id))) % 7