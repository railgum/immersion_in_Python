# Напишите следующие функции:
# 1. Нахождение корней квадратного уравнения
# 2. Генерация csv файла с тремя случайными числами
#    в каждой строке. 100-1000 строк.
# 3. Декоратор, запускающий функцию нахождения корней квадратного
#    уравнения с каждой тройкой чисел из csv файла.
# 4. Декоратор, сохраняющий переданные параметры и
#    результаты работы функции в json файл.


import csv
import json
import math
import random as rnd
from typing import Callable
from functools import wraps

NUM_STR_MIN = 10
NUM_STR_MAX = 25
NUMBER_LINES = 100


def csv_gen(a: int = NUMBER_LINES):
    data = []
    for _ in range(a):
        data.append((rnd.randint(-100, 100), rnd.randint(-100, 100), rnd.randint(-100, 100)))
    with open('random_files_3.csv', 'w') as file:
        csv_writer = csv.writer(file, dialect='excel', delimiter=';')
        csv_writer.writerows(data)


def read_from_csv(file_name):
    def deco_quadro(func: Callable):
        @wraps(func)
        def wrapper():
            with open(file_name, 'r', newline='') as file:
                csv_file = csv.reader(file)
                for line in csv_file:
                    tmp_line = (s.replace(' ', '') for s in line)
                    args = (int(j) for j in tmp_line)
                    res = func(*args)
                    yield res

        return wrapper

    return deco_quadro


def json_log(func):
    json_file = []

    def wrapper(*args):
        for res in func(*args):
            print(res)
            if res:
                tmp_dict = {'args': args, 'result': res}
                json_file.append(tmp_dict)
                with open('result.json', 'w', encoding='utf-8') as file:
                    json.dump(json_file, file, indent=4, ensure_ascii=False)

            else:
                break

    return wrapper


@json_log
@read_from_csv('random_files_3.csv')
def roots_eq(a: int, b: int, c: int):
    if a != 0:
        discrim = b * b - 4 * a * c
        sqr = math.sqrt(abs(discrim))

        if discrim > 0:
            return [(-b + sqr) / (2 * a), (-b - sqr) / (2 * a)]
        elif discrim == 0:
            return [-b / (2 * a), -b / (2 * a)]
        else:
            return [f'{-b / (2 * a)} + i{sqr}', f'{-b / (2 * a)} - i{sqr}']
    else:
        return [f'Уравнение некорректно']


if __name__ == '__main__':
    csv_gen()
    # roots_eq()
