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
import copy


class Matrix:

    def __init__(self, rows: int, cols: int):
        self.rows = rows if rows > 0 else 1
        self.cols = cols if cols > 0 else 1
        self.matrix = [[0] * self.cols for _ in range(self.rows)]
    def data(self, data):
        self.matrix = copy.deepcopy(data)
        return self.matrix

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                matrix_result = [[0 for row in range(other.cols)] for col in range(self.rows)]
                for row in range(self.rows):
                    for col in range(self.cols):
                        matrix_result[row][col] += self.matrix[row][col] + other.matrix[row][col]
                return matrix_result
            else:
                return f'Матрицы разных размеров'
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols == other.rows:
                matrix_result = [[0 for row in range(other.cols)] for col in range(self.rows)]
                for i in range(self.rows):
                    for j in range(other.cols):
                        for k in range(self.cols):
                            matrix_result[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return matrix_result
            else:
                return f'Такие матрицы невозможно перемножить'
        raise TypeError

    # def __mul__(self, other):
    #     if isinstance(other, Matrix):
    #         if self.cols == other.rows:
    #             matrix_result = []
    #             for i in range(self.rows):
    #                 list_value = []
    #                 for j in range(other.cols):
    #                     elem, temp_res = 0, 0
    #                     for k in range(self.cols):
    #                         temp_res = self.matrix[i][k] * other.matrix[k][j]
    #                         elem += temp_res
    #                     list_value.append(elem)
    #                 matrix_result.append(list_value)
    #             return matrix_result
    #         else:
    #             return f'Такие матрицы невозможно перемножить'
    #     raise TypeError

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                return all([
                    self.matrix[i][j] == other.matrix[i][j] for j in range(self.cols) for i
                    in range(self.rows)])
            else:
                return False
        raise TypeError

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.matrix)

    def __repr__(self):
        return f'Matrix({self.matrix})'


matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)
