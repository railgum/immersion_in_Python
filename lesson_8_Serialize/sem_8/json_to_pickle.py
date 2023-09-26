# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import pickle
import json


def json_to_pickle(path: str = os.getcwd()):
    file_list = []
    for files in os.walk(path):
        for file in files[2]:
            if file.endswith('.json'):
                file_list.append((os.path.join(files[0], file),
                                  os.path.join(files[0], file.rsplit('.')[0] + '.pickle')))

    # for file in file_list:
    #     with (
    #         open(file[0], 'r', encoding='utf-8') as f_in,
    #         open(file[1], 'wb') as f_out
    #     ):
    #         data = json.load(f_in)
    #         pickle.dump(data, f_out)
    print(file_list)


json_to_pickle()
