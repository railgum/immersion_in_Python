import numbers
import shutil

# Задание

# ✔ Решить задачи, которые не успели решить на семинаре.
# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10
# как на школьной тетрадке.

# term_size = shutil.get_terminal_size()
# print(f'{"ТАБЛИЦА УМНОЖЕНИЯ: ":^{term_size[0]-15}}')
#
# for i in range(2, 11):
#     for j in range(2, 6):
#         print(f'{j} X {i} = {i * j}', end='\t\t')
#     print('\t')
# print()
# for i in range(2, 11):
#     for j in range(6, 10):
#         print(f'{j} X {i} = {i * j}', end='\t\t')
#     print('\t')
#

# ✔ Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

# a = float(input('Введите первую сторону треугольника: '))
# b = float(input('Введите вторую сторону треугольника: '))
# c = float(input('Введите третью сторону треугольника: '))
#
# if a + b > c and a + c > b and b + c > a:
#     print('Треугольник с такими сторонами существует')
#     if a == b and a == c:
#         print('Более того, он равносторонний')
#     elif a == b or a == c or b == c:
#         print('Более того, он равнобедренный')
#     else:
#         print('Обалдеть, он разносторонний')
# else:
#     print('Треугольника с такими сторонами не существует')


# ✔ Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# num = int(input('Введите число в диапазоне от 1 до 100000: '))
# if 1 < num > 100001:
#     print('Неверный диапазон')
# else:
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     print('Число составное') if count > 2 else print('Число простое')
#

