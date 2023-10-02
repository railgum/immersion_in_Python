import os
class SplitPath():
    def __init__(self, path):
        self.path = path

    def parse_path(self):
        path, file_ext = os.path.split(self.path)
        file_name, ext = file_ext.split('.')
        return (f'Путь до файла - {path}\n'
                f'Имя файла - {file_name}\n'
                f'Расширение - {ext}')

p1 = SplitPath('Z:\Geek\Developer\Backend_for_Web\immersion_in_Python\lesson_6_Modules\hw_6\check_date.py')
print(p1.parse_path())