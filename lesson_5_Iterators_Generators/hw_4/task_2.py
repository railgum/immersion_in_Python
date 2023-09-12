# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os
path_ex = 'X:/Geek/Developer/block/GitHub/workshop/README.md'

def parse_path(str_path: str) -> tuple:
    path, file_ext = os.path.split(str_path)
    file_name, ext = file_ext.split('.')
    return path, file_name, ext

print(parse_path(path_ex))