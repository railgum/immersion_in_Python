# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

# class Dog:
#     def __init__(self, name, age, breed='Лайка'):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#     def show_info(self):
#         return (f'{self.breed}')
#
#
# class Bird:
#     def __init__(self, name, age, family='Аист'):
#         self.name = name
#         self.age = age
#         self.family = family
#
#     def show_info(self):
#         return (f'{self.family}')
#
#
# class Fish:
#     def __init__(self, name, age, kind='Акула'):
#         self.name = name
#         self.age = age
#         self.kind = kind
#
#     def show_info(self):
#         return (f'{self.kind}')


# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, age, **_):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec

    def get_info(self) -> str:
        return (f'{"Type:":8}{type(self).__name__}'
                f'\n{"Name:":8}{self.name}'
                f'\n{"Age:":8}{self.age} years')


class Mammal(Animal):
    def __init__(self, name, age, breed, spec, **_):
        super().__init__(name, age)
        self.spec = spec
        self.breed = breed

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Breed:":8}{self.breed}'
                f'\n{"Spec:":8}{self.spec}')


class Bird(Animal):
    def __init__(self, name, age, breed, spec, **_):
        super().__init__(name, age)
        self.breed = breed
        self.spec = spec

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Breed:":8}{self.breed}'
                f'\n{"Spec:":8}{self.spec}')


class Fish(Animal):
    def __init__(self, name, age, kind, spec, **_):
        super().__init__(name, age)
        self.kind = kind
        self.spec = spec

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Kind:":8}{self.kind}'
                f'\n{"Spec:":8}{self.spec}')
