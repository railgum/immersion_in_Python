# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

from functools import total_ordering
@total_ordering
class Rectangle:
    def __init__(self, side_a, side_b=None):
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.side_a + other.side_a, self.side_b + other.side_b)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.side_a > other.side_a and self.side_b > other.side_b:
                return Rectangle(self.side_a - other.side_a, self.side_b - other.side_b)
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __repr__(self):
        return f'Rectangle({self.side_a}, {self.side_b})'

    def perimetr(self):
        return 2 * (self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.side_b


rect_1 = Rectangle(12, 18)
rect_2 = Rectangle(9, 14)

print(rect_1 + rect_2)
print(rect_1 - rect_2)
print(rect_1 < rect_2)
print(rect_1 == rect_2)
print(rect_1 > rect_2)
print(rect_1 != rect_2)
print(rect_1 >= rect_2)
print(rect_1 <= rect_2)

