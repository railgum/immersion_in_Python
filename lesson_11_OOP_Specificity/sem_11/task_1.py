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
        self.create_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.value = value
    # def __str__(self):
        # def __str__(self):
        #     return (f'{self.value} (Автор: {self.author},'
        #             f' Время создания: {self.create_time})')


a = MyStr('rail', 'моя строка')
print(a)
print(a.author, a.create_time)
