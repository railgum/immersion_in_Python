# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат

class Rectangle:
    def __init__(self, side_a, side_b=None):
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a

    def perimetr(self):
        return 2 * (self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.side_b


r_1 = Rectangle(6, 8)
r_2 = Rectangle(9)
print(r_1.perimetr())
print(r_1.area())
print(r_2.perimetr())
print(r_2.area())
