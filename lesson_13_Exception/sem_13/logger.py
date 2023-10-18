# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

from user import *


class Logan:
    db = {}

    def __init__(self, path_to_file):
        self.__class__.db = load_json(path_to_file)


    def authorize(self, the_id, name):
        user = User(name, the_id)
        if user in self.__class__.db:
            self.level = self.__class__.db[str(the_id)]['level']
        else:
            raise Exception('Пользователь не найден')

path_to_json_file = 'my_json.json'
logger = Logan(path_to_json_file)
print(logger.authorize(5,'sasa'))