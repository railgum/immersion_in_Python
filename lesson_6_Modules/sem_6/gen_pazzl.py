# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.


def game_pazzl(pzl_str: str, answer: list, count: int) -> int:
    pzl_dict = {'Зимой и летом одним цветом': ['берёза', 'ёлка', 'липа'],
                'Не лает, не кусает - в дом не пускает': ['замок', 'кошка', 'сторож']}
    temp_count = 1
    answer = list(map(lambda x: x.lower(), answer))
    while temp_count <= count:
        usr_answer = input(pzl_str).lower()
        if usr_answer in answer:
            return temp_count
        temp_count +=1
    return 0