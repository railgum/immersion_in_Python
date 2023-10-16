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

class InvalidIdError(ValueError):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
class Person:
    def __init__(self, first_name: str, second_name: str, last_name: str, age: int):
        if not isinstance(first_name, str) or len(first_name.strip()) == 0:
            raise InvalidNameError(f'Invalid name: {first_name}. Name should be a non-empty string.')
        self.first_name = first_name
        if not isinstance(second_name, str) or len(second_name.strip()) == 0:
            raise InvalidNameError(f'Invalid name: {second_name}. Name should be a non-empty string.')
        self.second_name = second_name
        if not isinstance(last_name,str) or len(last_name.strip()) == 0:
            raise InvalidNameError(f'Invalid name: {last_name}. Name should be a non-empty string.')
        self.last_name = last_name
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')
        self._age = age

    def full_name(self):
        return (f'{self.last_name} {self.first_name} {self.second_name}')

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1

class Employee(Person):
    def __init__(self, first_name, second_name, last_name, age, id_number):
        super().__init__(first_name, second_name, last_name, age)
        self.__id = Employee.check_id(id_number)

    @classmethod
    def check_id(cls, id_number):
        if not len(str(id_number)) == 6:
            raise InvalidIdError(
                f'Invalid id: {id_number}. Id should be a 6-digit positive integer between 100000 and 999999.')
        return id_number

    @property
    def get_level(self):
        return sum(map(int, str(self.__id))) % 7


