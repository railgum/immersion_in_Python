import os
import sys
from pprint import pprint
import json
import csv
import pickle


def size_of_dir(dir_path: str) -> int:
    total_size = 0
    for path, _, files in os.walk(dir_path):
        for file in files:
            total_size += sys.getsizeof(os.path.join(path, file))
    return total_size


def file_writer(current_path: str, source: dict[str, dict], json_file=False, csv_file=False,
                pickle_file=False):
    name = os.path.join(current_path, "result")
    file = [['Full_path', 'Name', 'Parent_dir', 'Type', 'Size', ]]
    for key, item in source.items():
        file.append([key, *item.values()])
    if json_file:
        with open(name + '.json', 'w', encoding='utf-8') as json_data:
            json.dump(source, json_data, indent=4, ensure_ascii=False)
    if csv_file:
        with open(name + '.csv', 'w', encoding='utf-8') as csv_data:
            csv.writer(csv_data, dialect='excel', delimiter=';').writerows(file)
    if pickle_file:
        with open(name + '.bin', 'wb') as pickle_data:
            pickle.dump(source, pickle_data)


def dir_walker(full_path: str = os.getcwd()):
    result = {}
    for path, dir_list, file_list in os.walk(full_path):
        for cur_dir in dir_list:
            result[os.path.join(path, cur_dir)] = {'name': cur_dir,
                                                   'path': path,
                                                   'type': 'DIR',
                                                   'size': size_of_dir(os.path.join(path,
                                                                                    cur_dir))}
        for cur_file in file_list:
            result[os.path.join(path, cur_file)] = {'name': cur_file,
                                                    'path': path,
                                                    'type': 'FILE',
                                                    'size': sys.getsizeof(os.path.join(path,
                                                                                       cur_file))}
    # file_writer(full_path, result, json_file=True, pickle_file=True)
    return result

pprint(dir_walker(
    'X:\Geek\Portfolio\InterShop'))
