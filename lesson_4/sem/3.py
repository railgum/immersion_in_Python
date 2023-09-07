from pprint import pp
# Задание №3
# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением —
# целое число. Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

diap = input('Введите мин. и макс. число диапазона Unicode: ')

def my_func(data: str) -> dict:
    my_dict = dict()
    lower, upper = sorted(list(map(int, data.split())))
    for i in range(lower, upper + 1):
        my_dict[chr(i)] = i
    return my_dict

pp(my_func(diap))