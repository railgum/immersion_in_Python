
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.
import random


def generic_puzzle():
    func_dict = {'Зимой и летом - одним цветом': ['ёлка', 'берёза', 'липа'],
                 'Висит груша - нельзя скушать': ['лампочка', 'яблоко', 'рисунок']}
    while func_dict:
        key = random.choice(list(func_dict))
        yield key, func_dict.pop(key)

def my_game(count: int, cnt: int) -> list:
    result = []
    puzzles = generic_puzzle()
    for _ in range(count):
        puzzle = next(puzzles)
        question, answer = puzzle
        temp_cnt = 1
        answer = list(map(lambda x: x.lower(), answer))
        while temp_cnt <= cnt:
            user_str = input(question + ': ').lower()
            if user_str in answer:
                result.append(temp_cnt)
                break
            temp_cnt +=1
        else:
            result.append(0)
    return result
