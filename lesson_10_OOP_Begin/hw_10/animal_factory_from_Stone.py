from typing import Any
from animal import *


class AnimalFactory:
    def __new__(cls, animal_type, *args, **kwargs) -> [Mammal, Bird, Fish, Animal, Any]:
        try:
            animal = super().__new__(animal_type)
            animal.__init__(*args, **kwargs)
            return animal
        except Exception as exc:
            print(f'{exc.__class__.__name__} {exc}')
            return Animal('Cadaver', 1000)


def main():
    dog = AnimalFactory(Mammal, name='Тузик', age=5, breed='дворняга', spec='Тяв')
    fish = AnimalFactory(Fish, name='Немо', age=1, kind='карась', spec='Бульк')
    bird = AnimalFactory(Bird, name='Попка', age=3, breed='ара', spec='попка дурак')
    nonindef = AnimalFactory('Non-type', name='Чудо-юдо', age=150555)

    print(dog.get_info(),'\n')
    print(fish.get_info(),'\n')
    print(bird.get_info(),'\n')
    print(nonindef.get_info())


if __name__ == '__main__':
    main()
