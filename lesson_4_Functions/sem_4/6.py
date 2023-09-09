# Задание №6
# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def my_func(lst_num: list[int], index_1: int, index_2: int) -> int:
    index_1, index_2 = sorted([index_1, index_2])
    # Проверка не нужна!!!!
    # if index_2 > len(lst_num):
    #     index_2 = len(lst_num) - 1
    # if index_1 < 0:
    #     index_1 = 0
    return sum(lst_num[index_1:index_2+1]) # срезы не выходят за границы списка