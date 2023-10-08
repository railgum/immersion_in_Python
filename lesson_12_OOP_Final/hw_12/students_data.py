import csv


class MakeCsvExample:
    def __init__(self, path_to_file: str, list_csv: list):
        self.list_csv = list_csv
        self.path = path_to_file
        with open(path_to_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(list_csv)

    def add_value(self, text: str):
        pass


class CheckName:
    """Дескриптор проверки имени студента"""

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not value.istitle() or value.replace(' ', '').isalpha():
            raise ValueError('Имя некорректно')
        self.value = value


class Student:
    name = CheckName()
    # __slots__ = open()

    def __init__(self, name: str, subjects_file: str = None):
        self.name = name
        self.file = subjects_file

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


s = Student('Dic Ker sdr')
print(s.name)
