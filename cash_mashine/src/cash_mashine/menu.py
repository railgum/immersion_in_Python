import os
from operations import Operation

class Menu:
    def __init__(self, tax, accrual, wealth_tax):
        self.Operation = Operation(tax=tax, accrual=accrual, wealth_tax=wealth_tax)

    def menu(self):
        os.system("cls")
        menu = ('Добро пожаловать в программу "Банкомат"\n\n'
                'Доступные действия:\n'
                '1 - Пополнить счет\n'
                '2 - Снять наличные\n'
                '3 - Показать баланс\n'
                '0 - Выход')
        print(menu)
        # incorrect_answer = 3
        # amount = 0
        # count_refill = 0
        # count_cut = 0
        while incorrect_answer > 0:
            answer = input('Введите номер действия:>> ')
            if not answer.isdigit():
                print('Нужно ввести число от 1 до 3')
                incorrect_answer -= 1
                continue
            else:
                if answer == '1':
                    os.system("cls")
                    # amount, count_refill = addition(amount, count_refill)
                    self.Operation.add()
                    show(amount)
                    print(menu)
                if answer == '2':
                    os.system("cls")
                    amount, count_cut = removal(amount, count_cut)
                    show(amount)
                    print(menu)
                if answer == '3':
                    os.system("cls")
                    show(amount)
                    print(menu)
                if answer == '0':
                    exit(0)

        print('Похоже, вы делаете что-то не так((')
        exit(0)