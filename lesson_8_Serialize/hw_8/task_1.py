# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий
# размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.
import csv
import json
import os
import pickle
from os.path import getsize, join


def scan_dir(path: str = os.getcwd()):
    file_dict = {}
    file_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        file_dict[f'Каталог - {root}'] = [
            f'Файл - {file_name} = {getsize(join(root, file_name))} байт' for file_name in
            files
        ]
    for key, value in file_dict.items():
        file_list.append([key, value])

    with (
        open('json_file.json', 'w', encoding='utf-8') as json_file,
        open('csv_file.csv', 'w', encoding='utf-8', newline='') as csv_file,
        open('pickle_file.pickle', 'wb') as pickle_file
    ):
        json.dump(file_dict, json_file, indent=4, separators=(',', ':'), ensure_ascii=False)
        csv_writer = csv.writer(csv_file, dialect='excel', delimiter='>')
        csv_writer.writerows(file_list)
        pickle.dump(file_dict, pickle_file)
# scan_dir('../../lesson_8_Serialize')
