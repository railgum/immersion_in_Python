# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.

class Rectangle:
    def __init__(self, width: int, height: int = None):
        self._width = width
        self._height = height if height else width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('Недопустимое значение')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError('Недопустимое значение')
        self._height = value

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self._width + other._width, self._height + other._height / 1)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self._width > other._width and self._height > other._height:
                return Rectangle(self._width - other._width, self._height - other._height / 1)
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area() <= other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self._width} и {self._height}'

    def __repr__(self):
        return f'Restangle({self._width}, {self._height})'



r1 = Rectangle(5,6)
r1.width = 9
print(r1)
r1.width = -4
print(r1)
