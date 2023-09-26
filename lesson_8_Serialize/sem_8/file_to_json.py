# Напишите функцию, которая в бесконечном цикле запрашивает имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
import os

PATH_DB = 'user_db.json'


def load_json():
    if os.path.exists(PATH_DB):
        with open(PATH_DB, 'r', encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def input_name():
    return input('Введите имя: ')


def input_id(dict_users: dict):
    list_id = set()
    for users in dict_users.values():
        for user in users:
            for u_id in user:
                list_id.add(u_id)
    while True:
        u_id = input('Введите ID: ')
        if u_id not in list_id:
            return u_id
        print('Этот ID занят, введите другой')


def input_lvl():
    while True:
        lvl = input('Введите уровень доступа: ')
        if lvl.isdigit() and 0 < int(lvl) < 8:
            return lvl


def get_list_id(db: dict):
    users_id_list = set()
    for user in db.values():
        users_id_list.add(user[1])
    return users_id_list


def create_users():
    while True:
        user_db = load_json()
        name = input_name()
        if not name:
            break
        u_id = input_id(user_db)
        lvl = input_lvl()
        if lvl in user_db:
            user_db[lvl].append({u_id: name})
        else:
            user_db[lvl] = [{u_id: name}]
        with open(PATH_DB, 'w', encoding='utf-8') as file:
            json.dump(user_db, file, indent=4, ensure_ascii=False)


create_users()
