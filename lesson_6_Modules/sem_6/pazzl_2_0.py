
# Добавьте в модуль с загадками функцию, которая принимает на вход
# строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания
# из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

import random


_result = {}
def generic_puzzle():
    func_dict = {'Зимой и летом - одним цветом': ['ёлка', 'берёза', 'липа'],
                 'Висит груша - нельзя скушать': ['лампочка', 'яблоко', 'рисунок'],
                 'Не лает, не кусает - в дом не пускает': ['бомж','налоговая','замок'],
                 'Сто одёжек - и все без застёжек': ['стриптизёрша','капуста','кошелёк']}
    while func_dict:
        key = random.choice(list(func_dict))
        yield key, func_dict.pop(key)

def my_game(count: int, cnt: int) -> list:
    global _result
    puzzles = generic_puzzle()
    for _ in range(count):
        puzzle = next(puzzles)
        question, answer = puzzle
        temp_cnt = 1
        answer = list(map(lambda x: x.lower(), answer))
        while temp_cnt <= cnt:
            user_str = input(question + ': ').lower()
            if user_str in answer:
                _result[question] = temp_cnt
                break
            temp_cnt += 1
        else:
            _result[question] = 0

def show_result():
    global _result
    result = ['Результаты: ']
    max_len = len(max(list(_result), key=len))
    for question, count in _result.items():
        result.append(f'{question:<{max_len}}: Отгадана с {count} попытки')
    return '\n'.join(result)