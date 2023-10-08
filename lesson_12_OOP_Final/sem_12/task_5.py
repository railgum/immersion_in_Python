# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.


class Rectangle:
    __slots__ = ['width', 'height']
    def __init__(self, width: int, height: int = None):
        self.width = width
        self.height = height if height else width

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('Недопустимое значение')
        self.width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError('Недопустимое значение')
        self.height = value

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height / 1)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.width > other.width and self.height > other.height:
                return Rectangle(self.width - other.width, self.height - other.height / 1)
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
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'Restangle({self.width}, {self.height})'