import csv

PATH_CSV = 'subjects.csv'


class MakeCsvExample:
    def __init__(self, path_to_file: str, text: str):
        self.text = text
        self.path = path_to_file
        with open(path_to_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(text.split(','))

    def add_value(self, text: str):
        pass


c = MakeCsvExample(PATH_CSV, 'Математика,Физика,История')
