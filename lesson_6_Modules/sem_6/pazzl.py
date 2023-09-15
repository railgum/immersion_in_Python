# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана
# загадка или ноль, если попытки исчерпаны.

def game_pazzl(pzl_str: str, answer: list, count: int) -> int:
    temp_count = 1
    answer = list(map(lambda x: x.lower(), answer))
    while temp_count <= count:
        usr_answer = input(pzl_str).lower()
        if usr_answer in answer:
            return temp_count
        temp_count +=1
    return 0