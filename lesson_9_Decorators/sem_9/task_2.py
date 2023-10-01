# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Она должна проверять, входят ли переданные в функцию-угадайку числа
# в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
import random
from typing import Callable


def deco(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        a, b, *_ = args
        if a not in range(1, 101):
            print(f'Недопустимый диапазон')
            a = random.randint(1, 100)
        if b not in range(1, 11):
            print(f'Недопустимый диапазон')
            b = random.randint(1, 10)
        func(a, b)

    return wrapper()


@deco
def inner(a, b):
    print(f'У тебя {b} попыток...')
    while b:
        quess = int(input('Введите число: '))
        if quess > a:
            print(f'Число меньше, чем {quess}')
        elif quess < a:
            print(f'Число больше, чем {quess}')
        else:
            print(f'Угадал за  {b}! Это число - {a}')
            break
        b -= 1
    else:
        print(f'Сорян, попытки закончились :(')
