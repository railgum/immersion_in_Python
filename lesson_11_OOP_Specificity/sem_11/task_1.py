# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

from datetime import datetime


class MyStr(str):
    def __new__(cls, author, value):
        instance = super().__new__(cls, value)
        return instance
    def __init__(self, author, value):
        self.author = author
        self.create_time = datetime.now()
        self.value = value


a = MyStr('rail', 'моя строка')
print(a)
print(a.author, a.create_time)
