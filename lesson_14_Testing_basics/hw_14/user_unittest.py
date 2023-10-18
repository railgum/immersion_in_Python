# На семинаре 13 был создан проект по работе
# с пользователями (имя, id, уровень)
# Напишите 3-7 тестов pytest (или unittest на ваш выбор)
# для данного проекта
# ОБЯЗАТЕЛЬНО! Используйте фикстуры

import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.first_user = User('Вовка', 5, 6)
        self.second_user = User('Ленка', 11, 2)
        self.third_user = User('Ленка', 12, 2)

    def test_eq(self):
        self.assertTrue(self.first_user == self.first_user)

    def test_level(self):
        self.assertGreater(self.first_user.level, self.second_user.level)

    def test_error(self):
        self.assertRaises(ValueError, User, 'Гошан', 7, 9)

    def test_not_is(self):
        self.assertIsNot(self.second_user, self.third_user)

    def test_false(self):
        self.assertFalse(self.first_user == self.third_user)


if __name__ == '__main__':
    unittest.main(verbosity=2)
