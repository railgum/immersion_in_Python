# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def make_json(file_name: str):
    with (
        open(file_name, encoding='utf-8') as f_origin,
        open(f'{file_name}_json', 'a', encoding='utf-8') as f_json
    ):
        # print(list(f_origin))
        tmp = []
        while res := f_origin.readline():
            res = res.strip().split('|')
            tmp.append((res[0].title(), res[1]))
        # print(tmp)
        json.dump(tmp, f_json, indent=2, separators=(',', ':'))


make_json('../../lesson_7_Files/sem_7/task_3_file.txt')
