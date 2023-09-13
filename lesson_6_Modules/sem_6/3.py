from random import randint

def my_func(min_num=0, max_num=100, count=10, *_):
    number = randint(min_num, max_num + 1)
    cnt = 0
    while cnt < count:
        num = int(input('Введите число: '))
        if num == number:
            print(f'Вы угадали число за {cnt} раз')
            break
        elif num < number:
            print('Число меньше загаданного')
        elif num > number:
            print('Число больше загаданного')
        else:
            continue  # Эта строка никогда не отработает
        cnt += 1

    else:
        print(f'Вы не удали число {number} за {count} раз')