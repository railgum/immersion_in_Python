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
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, spec, *args):
        super().__init__(*args)
        self.spec = spec


class Bird(Animal):
    def __init__(self,  spec, *args):
        super().__init__(*args)
        self.spec = spec


class Fish(Animal):
    def __init__(self,  spec, *args):
        super().__init__(*args)
        self.spec = spec


pet_1 = Dog('Гав-гав', 'Тузик', 5)
pet_2 = Fish("Ням", "Шарк", 10)
pet_3 = Bird("Чик-чирик", "Королёк", 2, )

for pet in [pet_1, pet_2, pet_3]:
    print(f'{pet.name} {pet.get_spec()}')
