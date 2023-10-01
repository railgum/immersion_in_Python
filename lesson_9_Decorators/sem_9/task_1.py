# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
import random


def outer():
    a = random.randint(1, 100)
    b = random.randint(1, 10)

    def inner():
        nonlocal a, b
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

    return inner


example = outer()
example()