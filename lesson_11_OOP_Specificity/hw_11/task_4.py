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
#    которую можно использовать для создания нового объекта класса Matrix.
import numbers


class Matrix:

    def __init__(self, rows: int, cols: int):
        self.rows = rows if rows > 0 else 1
        self.cols = cols if cols > 0 else 1
        self.data = [[0] * cols for _ in range(rows)]

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                result = Matrix(self.rows, other.cols)
                for row in range(self.rows):
                    for col in range(self.cols):
                        result.data[row][col] += self.data[row][col] + other.data[row][col]
                return result
            else:
                return f'Матрицы разных размеров'
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols == other.rows:
                result = Matrix(self.rows, other.cols)
                for i in range(self.rows):
                    for j in range(other.cols):
                        for k in range(self.cols):
                            result.data[i][j] += self.data[i][k] * other.data[k][j]
                return result
            else:
                return f'Такие матрицы невозможно перемножить'
        elif isinstance(other, numbers.Number):
            return [[i * other for i in row] for row in self.data]
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                return all([
                    self.data[i][j] == other.data[i][j] for j in range(self.cols) for i
                    in range(self.rows)])
            else:
                return False
        raise TypeError

    def __str__(self):
        # return '\n'.join(' '.join(map(str, row)) for row in self.data)

        return '\n'.join(
            [' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'


# Создаем матрицы
# matrix1 = Matrix(2, 3)
# matrix1.data = [[1, 2, 3], [4, 5, 6]]
# print(list(map(len, matrix1)))

matrix2 = [[4, 8], [3,3, 2], [4]]
print(set(map(len, matrix2)))
# matrix2 = Matrix(2, 3)
# print(matrix1 * 5)
# matrix2.data = [[7, 8, 9], [10, 11, 12]]
# # Выводим матрицы
# print(matrix1)
# print(matrix2)
# # Сравниваем матрицы
# print(matrix1 == matrix2)
# # Выполняем операцию сложения матриц
# matrix_sum = matrix1 + matrix2
# print(matrix_sum)
# # Выполняем операцию умножения матриц
# matrix3 = Matrix(3, 2)
# matrix3.data = [[1, 2], [3, 4], [5, 6]]
# matrix4 = Matrix(2, 2)
# matrix4.data = [[7, 8], [9, 10]]
# result = matrix3 * matrix4
# print(result)

# эталон
# class Matrix:
#     """
#     Класс, представляющий матрицу.
#
#     Атрибуты:
#     - rows (int): количество строк в матрице
#     - cols (int): количество столбцов в матрице
#     - data (list): двумерный список, содержащий элементы матрицы
#
#     Методы:
#     - __str__(): возвращает строковое представление матрицы
#     - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта
#     - __eq__(other): определяет операцию "равно" для двух матриц
#     - __add__(other): определяет операцию сложения двух матриц
#     - __mul__(other): определяет операцию умножения двух матриц
#     """
#
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.data = [[0 for j in range(cols)] for i in range(rows)]
#
#     def __str__(self):
#         """
#         Возвращает строковое представление матрицы.
#
#         Возвращает:
#         - str: строковое представление матрицы
#         """
#         return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])
#
#     def __repr__(self):
#         """
#         Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.
#
#         Возвращает:
#         - str: строковое представление матрицы
#         """
#         return f"Matrix({self.rows}, {self.cols})"
#
#     def __eq__(self, other):
#         """
#         Определяет операцию "равно" для двух матриц.
#
#         Аргументы:
#         - other (Matrix): вторая матрица
#
#         Возвращает:
#         - bool: True, если матрицы равны, иначе False
#         """
#         if self.rows != other.rows or self.cols != other.cols:
#             return False
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 if self.data[i][j] != other.data[i][j]:
#                     return False
#         return True
#
#     def __add__(self, other):
#         """
#         Определяет операцию сложения двух матриц.
#
#         Аргументы:
#         - other (Matrix): вторая матрица
#
#         Возвращает:
#         - Matrix: новая матрица, полученная путем сложения двух исходных матриц
#         """
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Матрицы должны иметь одинаковые размеры")
#         result = Matrix(self.rows, self.cols)
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 result.data[i][j] = self.data[i][j] + other.data[i][j]
#         return result
#
#     def __mul__(self, other):
#         """
#         Определяет операцию умножения двух матриц.
#
#         Аргументы:
#         - other (Matrix): вторая матрица
#
#         Возвращает:
#         - Matrix: новая матрица, полученная путем умножения двух исходных матриц
#         """
#         if self.cols != other.rows:
#             raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
#         result = Matrix(self.rows, other.cols)
#         for i in range(self.rows):
#             for j in range(other.cols):
#                 for k in range(self.cols):
#                     result.data[i][j] += self.data[i][k] * other.data[k][j]
#         return result
