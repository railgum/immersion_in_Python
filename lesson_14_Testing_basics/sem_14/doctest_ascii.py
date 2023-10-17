# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
from string import ascii_lowercase


def ascii_func(text: str):
    """
    >>> ascii_func('text') == 'text'
    True
    >>> ascii_func('TexT') == 'text'
    True
    >>> ascii_func('te.xT') == 'text'
    True
    >>> ascii_func('TПЮфыext') == 'text'
    True
    >>> ascii_func('tЯю;eXt') == 'text'
    True
    """

    result = ''
    for i in text:
        if i.lower() in ascii_lowercase + ' ':
            result += i
    return result.lower()

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
