# ✔Напишите функцию, которая заполняет файл (добавляет в конец)
# случайными парами чисел.
# ✔Первое число int, второе - float разделены вертикальной чертой.
# ✔Минимальное число - -1000, максимальное - +1000.
# ✔Количество строк и имя файла передаются как аргументы функции.

import random as rnd

L_LIMIT = -1000
H_LIMIT = 1000
def func(filename: str, lines: int):
    with open(filename, 'a+', encoding='UTF-8') as file:
        for _ in range(lines):
            a = rnd.randint(L_LIMIT, H_LIMIT)
            b = rnd.uniform(L_LIMIT, H_LIMIT)
            file.write(f'{a} | {b}\n')


func('task_1_file.txt', 8)