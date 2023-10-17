# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest
from ascii_func import ascii_func


def test_1():
    assert ascii_func('text') == 'text'


def test_2():
    assert ascii_func('TexT') == 'text'


def test_3():
    assert ascii_func('te.xT') == 'text'


def test_4():
    assert ascii_func('TПЮфыext') == 'text'


def test_5():
    assert ascii_func('tЯю;eXt') == 'text'


if __name__ == '__main__':
    pytest.main(['-v'])
