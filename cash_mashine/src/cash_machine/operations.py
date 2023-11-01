class Operation:
    COUNT_INCORRECT_ANSWER = 3
    def __init__(self, min_withdrawal, max_withdrawal, tax, accrual, taking_off, wealth_tax,
                 divider):
        self.result_operation = 0
        self.result_message = ''
        self.count_operation = 0
        self.min_withdrawal = min_withdrawal
        self.max_withdrawal = max_withdrawal
        self.tax = tax
        self.accrual = accrual
        self.taking_off = taking_off
        self.wealth_tax = wealth_tax
        self.divider = divider

    def addition(self):
        self.result_message = ''
        incorrect_answer = 0
        try:
            while incorrect_answer < self.COUNT_INCORRECT_ANSWER:
                if self.result_operation > self.wealth_tax:
                    self.result_message = 'Вычтен налог на богатство'
                    self.result_operation -= self.result_operation * self.tax
                    print(self.show())
                payment = int(input('Введите сумму взноса: '))
                if self.check_multiplicity(payment, self.divider):
                    self.count_operation += 1
                    if self.count_operation % 3 == 0:
                        self.result_operation += payment + payment * self.accrual
                        self.result_message = f'Вы получили дополнительно {payment * self.accrual}'
                        print(self.show())
                        break
                    else:
                        self.result_operation += payment
                        print(self.show())
                        break
                else:
                    self.result_message = 'Сумма взноса должна быть кратна 50!'
                    print(self.show())
                    incorrect_answer += 1
            # else:
            #     self.result_message = 'Извините, что-то пошло не по плану :('
            #     print(self.show())
            return self.result_operation, self.result_message
        except ValueError as e:
            self.result_message = f'Ошибка ввода: {e}'
            return self.result_operation, self.result_message

    def removal(self):
        try:
            incorrect_answer = 3
            while incorrect_answer > 0:
                withdrawal = int(input('Введите сумму снятия: '))
                if self.result_operation > withdrawal:
                    if self.check_multiplicity(withdrawal, self.divider):
                        self.result_operation = ((self.result_operation - withdrawal)
                                                 + withdrawal * self.accrual)
                    else:
                        self.result_message = 'Сумма взноса должна быть кратна 50!'
                        incorrect_answer -= 1
                else:
                    self.result_message = 'Извините, такой суммы на счете нет'
                    continue
        except:
            self.result_message = 'Извините, что-то пошло не по плану :('
            print(self.show())

    @staticmethod
    def check_multiplicity(value, divider):
        return value % divider == 0

    # @staticmethod
    def show(self):
        if self.result_message:
            return (f'На вашем счете: {self.result_operation} у.е.\n'
                    f'{self.result_message}\n'
                    f'Номер операции: {self.count_operation}\n')
        else:
            return (f'На вашем счете: {self.result_operation} у.е.\n'
                    f'Номер операции: {self.count_operation}\n')
