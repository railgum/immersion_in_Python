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

MY_FORMAT = '{msg}'
logger = logging.getLogger(__name__)
logging.basicConfig(filename='scan_dir_NT.log', filemode='w', encoding='utf-8',
                    level=logging.INFO, style='{', format=MY_FORMAT)

def dir_walker(full_path: str = os.getcwd()):
    for path, dir_list, file_list in os.walk(full_path):
        for cur_dir in dir_list:
            Dir = namedtuple('Dir', 'name parent_path is_dir')
            this_dir = Dir(cur_dir, path, True)
            logger.info(
                msg=f'Name: {this_dir.name} -|- Parent: {this_dir.parent_path} -|- Is directory: {this_dir.is_dir}')
        for cur_file in file_list:
            File = namedtuple('File', 'name extension parent_path')
            this_file = File(cur_file.split('.')[0], cur_file.split('.')[1], path)
            logger.info(
                msg=f'Name: {this_file.name} -|- Extension: {this_file.extension} -|- Parent: {this_file.parent_path}')



if __name__ == '__main__':
    dir_walker('X:\Geek\Developer\\1_block\\5_БД\seminar1')
