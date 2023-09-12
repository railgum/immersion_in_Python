# Напишите функцию для транспонирования матрицы


def trans_matrix(matrix):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix)
print(trans_matrix(matrix))

