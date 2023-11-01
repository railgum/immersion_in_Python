import os

class Menu:
    def __init__(self, count_incorrect_answer, cm):
        self.incorrect_answer = count_incorrect_answer
        self.cash_machine = cm
    def menu(self):
        os.system("cls")
        menu = ('Добро пожаловать в программу "Банкомат"\n\n'
                'Доступные действия:\n'
                '1 - Пополнить счет\n'
                '2 - Снять наличные\n'
                '3 - Показать баланс\n'
                '0 - Выход')
        print(menu)
        while self.incorrect_answer > 0:
            answer = input('Введите номер действия:>> ')
            if not answer.isdigit():
                print('Нужно ввести число от 1 до 3')
                self.incorrect_answer -= 1
                continue
            else:
                if answer == '1':
                    os.system("cls")
                    self.cash_machine.addition
                    # show(amount)
                    print(menu)
                if answer == '2':
                    os.system("cls")
                    # amount, count_cut = removal(amount, count_cut)
                    # show(amount)
                    self.cash_machine()
                    print(menu)
                if answer == '3':
                    os.system("cls")
                    # show(amount)
                    print(menu)
                if answer == '0':
                    exit(0)

        print('Похоже, вы делаете что-то не так((')
        exit(0)