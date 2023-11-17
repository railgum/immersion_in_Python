class Menu:
    def __init__(self, cm, count_incorrect_answer):
        self.incorrect_answer = count_incorrect_answer
        self.cm = cm
        self.print_menu = (
            'Доступные действия:\n'
            '1 - Пополнить счет\n'
            '2 - Снять наличные\n'
            '3 - Показать баланс\n'
            '0 - Выход')
        self.message_code_dict = {'error_enter': 'Ошибка ввода',
                                  'not_integer': 'Это не число',
                                  'successfully': 'Операция выполнена успешно',
                                  'error_divider': 'Число не кратно 50',
                                  'accrual': 'Вам бонус!',
                                  'wealth': 'Вычтен налог на богатство'}

    def menu(self):
        print('Добро пожаловать в программу "Банкомат"\n\n')
        print(self.print_menu)
        incorrect_answer = 0
        while incorrect_answer < self.incorrect_answer:
            try:
                answer = int(input('Введите номер действия:>> '))
                if answer in range(0, 4):
                    match answer:
                        case 1:
                            payment = int(input('Введите сумму взноса: '))
                            if not self.check_parameter(payment):
                                self.show_message('not_integer')
                                incorrect_answer += 1
                            else:
                                self.show_message(self.cm.transaction(payment, True))
                                self.cm.show()
                                incorrect_answer = 0
                            print(self.print_menu)
                        case 2:
                            withdrawal = int(input('Введите сумму снятия: '))
                            if not self.check_parameter(withdrawal):
                                self.show_message('not_integer')
                                incorrect_answer += 1
                            else:
                                self.show_message(self.cm.transaction(withdrawal, False))
                                self.cm.show()
                                incorrect_answer = 0
                            print(self.print_menu)
                        case 3:
                            print(self.cm.show())
                            incorrect_answer = 0
                            print(self.print_menu)
                        case 0:
                            print('Спасибо за выбор нашего банка. Всего хорошего!')
                            break
                else:
                    print('Введите число, соответствующее пункту меню!')
                    incorrect_answer += 1
            except ValueError as e:
                print(f'Ошибка - {e}! Нужно ввести цифровое значение!')
                incorrect_answer += 1
                continue
        else:
            print('Похоже, вы делаете что-то не так((. Завершение работы.')
            raise ValueError('Ошибка ввода значения')
    def show_message(self, message_code):
        print(self.message_code_dict[message_code])

    @staticmethod
    def check_parameter(value: int = 0) -> bool:
        return isinstance(value, int)
