# Напишите функцию для транспонирования матрицы

def print_matrix(matrix):
    for i in matrix:
        print(' '.join(list(map(str, i))))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(matrix)


def trans_matrix(matrix):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result


print('Транспонированная')
print_matrix(trans_matrix(matrix))
