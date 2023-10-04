# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    _instance = []

    def __new__(cls, value: int, text: str):
        instance = super().__new__(cls)
        instance.value = value
        instance.text = text
        instance.list_arch = cls._instance.copy()
        cls._instance.append(instance)
        return instance

    # def __init__(self, value: int, text: str):
    #     self.value = value
    #     self.text = text

    def __str__(self):
        return f'{self.value} {self.text} | {self.list_arch}'

    def __repr__(self):
        return f'({self.value} {self.text})'


a = Archive(5, 'что-то')
b = Archive(9, 'ещё чо-нть')
c = Archive(2, 'ну и ещё чо-нть')

print(a)
print(b)
print(c)
print(a)
