from typing import Any
from animal import *


class AnimalFactory:
    def __new__(cls,animal_type, *args, **kwargs) -> [Mammal, Bird, Fish, Animal, Any]:
        try:
            animal = super().__new__(animal_type)
            animal.__init__(*args, **kwargs)
            return animal
        except Exception as exc:
            print(f'{exc.__class__.__name__} {exc}')
            return Animal('Cadaver', 1000)


def main():
    dog = AnimalFactory(M)