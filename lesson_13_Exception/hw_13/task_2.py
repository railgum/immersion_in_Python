from typing import Union


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or len(text) == 0:
            raise InvalidTextError(f'Invalid text: {text}. Text should be a non-empty string.')
        self.text = text
        if not isinstance(number, (int, float)) or number < 0:
            raise InvalidTextError(
                f'Invalid number: {number}. Number should be a positive integer or float.')
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


# Введите ваше решение ниже

class InvalidTextError(ValueError):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


archive_instance = Archive("Sample text", 42.5)
print(archive_instance)

#
# invalid_archive_instance = Archive("", -5)
# print(invalid_archive_instance)

# invalid_archive_instance = Archive("Sample text", -5)
# print(invalid_archive_instance)