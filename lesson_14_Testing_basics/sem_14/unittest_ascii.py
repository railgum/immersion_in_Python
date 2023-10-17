# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import unittest
from ascii_func import ascii_func


class TestAscii(unittest.TestCase):
    def setUp(self) -> None:
        self.correct = 'text'
        self.first = 'TexT'
        self.second = 'Te.?xT'
        self.third = 'TЮЯвexT'
        self.fourth = 'Te.,Чюю.xT'

    def test_1(self):
        self.assertEqual(self.correct, ascii_func(self.first))

    def test_2(self):
        self.assertTrue(self.correct == ascii_func(self.second))

    def test_3(self):
        self.assertFalse(self.correct is ascii_func(self.third))

    def test_4(self):
        self.assertRaises(ValueError, ascii_func, None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
