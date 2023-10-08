# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.


class Value:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        setattr(instance, self.param_name, self._validate(value))
    def _validate(self, value: int):
        if not(self.min_value < value < self.max_value):
            raise ValueError
        return value
class Rectangle:
    # __slots__ = ['width', 'height']
    width = Value(10,100)
    height = Value(10,100)

    def __init__(self, width: int, height: int = None):
        self.width = width
        self.height = height if height else width

    # @property
    # def width(self):
    #     return self.width
    #
    # @width.setter
    # def width(self, value):
    #     if value <= 0:
    #         raise ValueError('Недопустимое значение')
    #     self.width = value
    #
    # @property
    # def height(self):
    #     return self.height
    #
    # @height.setter
    # def height(self, value):
    #     if value <= 0:
    #         raise ValueError('Недопустимое значение')
    #     self.height = value

    def perimeter(self):
        return 2 * (self.width + self.height)
    @property
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

a = Rectangle(15,39)
print(a)