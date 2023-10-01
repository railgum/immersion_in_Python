# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from task_3 import deco as json_deco
from task_2 import deco as control_deco
from task_4 import outer as counter

@json_deco
@counter(2)
@control_deco
def guess_number(a: int, b: int):
    print(f'У тебя {b} попыток угадать число')
    while b:
        quess = int(input('Введите число: '))
        if quess > a:
            print(f'Число меньше, чем {quess}')
        elif quess < a:
            print(f'Число больше, чем {quess}')
        else:
            print(f'Ты угадал за {b} попыток. Это число - {a}')
            break
        b -= 1
    else:
        print(f'Сорян, попытки закончились')

guess_number(50, 2)