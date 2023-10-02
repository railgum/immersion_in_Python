from animal import *

class AnimalFactory:
    def make_instance(self, class_name, *args, **kwargs):
        example = self._get_class_type(class_name)
        return example(*args, **kwargs)

    def _get_class_type(self, class_name):
        dict_classes = {'dog': Dog, 'bird': Bird, 'fish': Fish}
        return dict_classes[class_name.lower()]

f1 = AnimalFactory()
dog_fact = f1.make_instance('dog', 'Тузик', 5, 'Тяв!')
print(dog_fact.name)
print(dog_fact.spec)

