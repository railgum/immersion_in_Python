# ✔Напишите функцию, которая генерирует псевдоимена.
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
#  среди которых обязательно должны быть гласные.
# ✔Полученные имена сохраните в файл.
import random


# def get_names(count):
#     letters_1 = 'аоуиею'
#     letters_2 = 'кдлфмр'
#     names = [random.choice(i) for i in zip(letters_1, letters_2)]
#     with open('names.txt', 'a', encoding='utf-8') as n:
#         for _ in range(count):
#             n.writelines(''.join(names).capitalize())
#
#
# get_names(5)

import random as rnd
import string

letter = string.ascii_lowercase
vowels = 'aeiouy'


def generate_name():
    size = rnd.randint(4, 7)
    name = rnd.sample(letter, size - 1)
    name.append(rnd.choice(vowels))
    rnd.shuffle(name)
    name = ''.join(name).title()
    return name


def write_names_to_file(filename: str, count: int):
    names = []
    with open(filename, 'a+', encoding='UTF-8') as file:
        for _ in range(count):
            names.append(generate_name())
        file.write('\n'.join(names))


write_names_to_file('task_2_file.txt', 10)