# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv


def print_csv_to_picklestring(path):
    with open(path, 'r', encoding='utf-8', newline='') as file:
        csv_file = csv.reader(file)
