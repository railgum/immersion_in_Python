# Реализуйте класс Matrix, представляющий матрицу и поддерживающий
# следующие операции:
# 1. Инициализация матрицы. Конструктор класса должен принимать
#    количество строк rows и количество столбцов cols и создавать матрицу
#    с нулевыми значениями.
# 2. Операция сложения матриц. Реализуйте метод __add__, который позволяет
#    складывать две матрицы одинаковых размеров.
# 3. Операция умножения матриц. Реализуйте метод __mul__,
#    который позволяет умножать две матрицы с согласованными размерами
#    (количество столбцов первой матрицы должно быть равно количеству
#    строк второй матрицы).
# 4. Сравнение матриц на равенство. Реализуйте метод __eq__,
#    который позволяет сравнивать две матрицы на равенство.
# 5. Представление матрицы в виде строки. Реализуйте метод __str__,
#    который возвращает строковое представление матрицы, где элементы
#    строки разделены пробелами, а строки сами разделены символами новой строки.
# 6. Представление матрицы в виде строки для создания нового объекта.
#    Реализуйте метод __repr__, который возвращает строку,
#    которую можно использовать для создания нового объекта класса Matrix

import random


class Matrix:
    def __init__(self, rows: int = 2, columns: int = 2, matrix: list[list[int]] = None):
        if matrix is None:
            if rows > 1 and columns > 1:
                self.rows = rows
                self.columns = columns
                self.matrix = [[random.randint(0, 100) for _ in range(columns)] for _ in
                               range(rows)]
            else:
                raise ValueError('Невозможно создать данную матрицу')
        else:
            if Matrix._check_matrix(matrix):
                self.rows = len(matrix)
                self.columns = len(matrix[0])
                self.matrix = matrix
            else:
                raise ValueError('Это не матрица')

    def __eq__(self, other):
        if Matrix._same(self, other):
            return all([all([self.matrix[row][column] == other.matrix[row][column]
                             for column in range(self.columns)]) for row in range(self.rows)])
        #     Альтернатива
        #     return all(map(lambda x: x[0] == x[1], zip([y for x in self.matrix for y in x],
        #                                                [y for x in other.matrix for y in x])))
        else:
            raise ValueError

    def __add__(self, other):
        if Matrix._same(self, other):
            return Matrix(matrix=[[self.matrix[i][j] + other.matrix[i][j]
                                   for j in range(self.columns)] for i in range(self.rows)])
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, Matrix):
            new_matrix = [[0] * other.columns for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(other.columns):
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(matrix=new_matrix)
        elif isinstance(other, int | float):
            return Matrix(matrix=[[self.matrix[row][column] * other
                                   for column in range(self.columns)]
                                  for row in range(self.rows)])
        else:
            raise ValueError

    def __str__(self):
        return '\n'.join(''.join([f'{x:^5}' for x in row]) for row in self.matrix) + '\n'

    @staticmethod
    def _same(matrix1, matrix2):
        return isinstance(matrix2, Matrix) and matrix1.rows == matrix2.rows and matrix1.columns == matrix2.columns

    @staticmethod
    def _check_matrix(matrix: list[list[int]]) -> bool:
        return len(set(map(len, matrix))) == 1

a = Matrix()
b = Matrix(4, 3)
print(b)
c = Matrix(matrix=[[4, 5, 1], [3, 3, 2], [4, 8, 2]])
d = Matrix(matrix=[[4, 5, 1], [3, 3, 2], [4, 8, 2]])

print(c == d)
print(c is d)
print(b * c)
print(c * 5)
