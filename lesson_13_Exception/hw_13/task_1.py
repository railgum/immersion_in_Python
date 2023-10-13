# Введите ваше решение ниже

class Rectangle:
    def __init__(self, width: int, height: int = None):
        try:
            if not isinstance(width, int or float) or width <= 0:
                raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        except NameError:
            return f'Такой переменной нет'
        try:
            if not isinstance(height, int or float) or height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
        except NameError:
            return NegativeValueError(f'высота: {height}')
        self._width = width
        self._height = height if height else width


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')
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


class NegativeValueError(ValueError):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

# r = Rectangle(-2)
r = Rectangle(5, -3)