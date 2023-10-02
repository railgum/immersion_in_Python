# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
from math import pi


class Circle:
    # проверка, что радиус > 0!!!

    def __init__(self, rad: float):
        self.rad = Circle.check_radius(rad)

    @classmethod
    def check_radius(cls, rad):
        if rad > 0:
            return rad
        raise ValueError
    def length(self):
        return 2 * self.rad * pi

    def area(self):
        return (self.rad ** 2) * pi


circ_1 = Circle(5)
print(circ_1.area())
print(circ_1.length())
