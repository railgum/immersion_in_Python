# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable


def outer(count: int):
    def deco(func: Callable) -> Callable:
        result = []

        def wrapper(*args, **kwargs):
            for _ in range(count):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return deco


@outer(2)
def some_func(a: str, b: str):
    return a + '_' + b


# print(some_func('Один', 'Два'))
