# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyExeption(Exception):
    def __init__(self, msg: str):
        self.message = msg

    def __str__(self):
        return f'Моё исключение: {self.message}'


# class LevelError()


