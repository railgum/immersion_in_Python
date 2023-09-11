# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

from math import sqrt


# функция проверки числа на простоту
def check_simplisity(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True


# Генератор простых чисел
def simple_nums_generator():
    n = 1
    while True:
        n += 1
        if check_simplisity(n):
            yield n


gen = simple_nums_generator()
for i in range(20):
    print(f'{i + 1} число - {next(gen)}')
