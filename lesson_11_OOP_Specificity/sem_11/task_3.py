# Добавьте к задачам 1 и 2 строки документации для классов.

class Archive:
    """Создание экземпляров класса с сохранением данных предыдущих экземпляров"""
    _instance = []

    def __new__(cls, value: int, text: str):
        instance = super().__new__(cls)
        instance.value = value
        instance.text = text
        instance.list_arch = cls._instance.copy()
        cls._instance.append(instance)
        return instance


    def __str__(self):
        """Переопределение вывода на печать"""
        return f'{self.value} {self.text} | {self.list_arch}'

    def __repr__(self):
        return f'({self.value} {self.text})'