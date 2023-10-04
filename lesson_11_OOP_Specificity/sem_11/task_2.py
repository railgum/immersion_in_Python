# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    _instance = None

    def __new__(cls, value: int, text: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_arch = []
        else:
            cls._instance.list_arch.append(cls._instance)
        return cls._instance

    def __init__(self, value: int, text: str):
        self.value = value
        self.text = text

    def __str__(self):
        return f'{self.value} {self.text} | {self.list_arch}'

    def __repr__(self):
        return f'{self.value} {self.text}'


a = Archive(5, 'что-то')
b = Archive(9, 'ещё чо-нть')
c = Archive(2, 'ну и ещё чо-нть')

print(a)
print(b)
print(c)
