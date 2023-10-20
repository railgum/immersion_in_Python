# Напишите код, который запускается из командной строки
# и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование

import os
import logging
from collections import namedtuple
from pprint import pprint


def dir_walker(full_path: str = os.getcwd()):
    result = {}
    for path, dir_list, file_list in os.walk(full_path):
        for cur_dir in dir_list:
            result[os.path.join(path, cur_dir)] = {'name': cur_dir,
                                                   'parent_path': path,
                                                   'type': 'DIR'
                                                   }
        for cur_file in file_list:
            result[os.path.join(path, cur_file)] = {'name': cur_file.split('.')[0],
                                                    'ext': cur_file.split('.')[1],
                                                    'parent_path': path,
                                                    'type': 'FILE'
                                                    }
    return result


# ScanDir = namedtuple('ScanDir', dir_walker('X:\Geek\Developer\\1_block\\5_БД\seminar1'))

print(dir_walker('X:\Geek\Developer\\1_block\\5_БД\seminar1'))
