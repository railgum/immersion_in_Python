import csv

PATH_FILE = 'subjects.csv'
MIN_GRADE = 2
MAX_GRADE = 5
MIN_TEST_SCORE = 0
MAX_TEST_SCORE = 100


class CheckName:
    """Дескриптор проверки имени студента"""

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value: str):
        if not value.istitle():
            raise ValueError(f'ФИО должно начинаться с больших букв')
        if not value.replace(' ', '').isalpha():
            raise ValueError(f'ФИО должно состоять из букав')
        self.value = value


class Student:
    """Создание экземпляра студента"""
    name = CheckName()

    def __init__(self, name: str, subjects_file: str = None):
        self._name = name
        self._file = subjects_file
        self.progress = ()
    @property
    def get_name(self):
        return self._name
    def add_subject(self, subject, grade, test_score):
        pass

    def get_average_grade(self):
        pass

    def get_subjects(self):
        pass

    def get_average_grades(students):
        pass

    def get_subject_average(students, subject):
        pass


s = Student('Иван Иванов', PATH_FILE)
s.add_subject('Математика', 4, 50)
s.add_subject('История', 3, 55)
s.add_subject('Математика', 2, 30)


print(s.progress)
# print(s.get_name)
