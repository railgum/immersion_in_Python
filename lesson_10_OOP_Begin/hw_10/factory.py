# Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
#    и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
#   верните его из класса-фабрики.
# ○ Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
#   данных), которые вы уже решали. Превратите функции в методы класса, а
#   параметры в свойства. Задачи должны решаться через вызов методов
#   экземпляра.

from animal import *

class AnimalFactory:
    def make_instance(self, class_name, *args, **kwargs):
        example = self._get_class_type(class_name)
        return example(*args, **kwargs)

    def _get_class_type(self, class_name):
        dict_classes = {'dog': Mammal, 'bird': Bird, 'fish': Fish}
        return dict_classes[class_name.lower()]

f1 = AnimalFactory()
dog_fact = f1.make_instance('dog', name='Тузик', age=5, breed='Боксер', spec='Тяв!')

print(dog_fact.get_info())
