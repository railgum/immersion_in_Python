
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

    def transaction(self, amount: int, flag: bool):

        """Функция исполнения операции"""
        try:
            if self.check_wealth(self.result_operation, self.wealth_tax):
                self.result_operation -= self.result_operation * self.tax
                print('Вычтен налог на богатство!')
            if self.check_multiplicity(amount, self.divider):
                self.count_operation += 1
                if flag:
                    if self.count_operation % 3 == 0:
                        self.result_operation += (amount + amount * self.accrual)
                        return 'accrual'
                    else:
                        self.result_operation += amount
                        return 'successfully'
                else:
                    if self.count_operation % 3 == 0:
                        self.result_operation = (self.result_operation - (
                                    amount + self._withdrawal(amount))) + (amount * self.accrual)
                        return 'accrual'
                    else:
                        self.result_operation -= (amount + self._withdrawal(amount))
                        return 'successfully'
            else:
                return 'error_divider'
        except ValueError as e:
            return 'error_enter'

    @staticmethod
    def check_wealth(value, tax):
        """Функция проверки на богатство"""
        return value >= tax

    def _withdrawal(self, withdrawal):
        """Вычисление суммы налога при снятии"""
        return (((withdrawal * self.taking_off)
                 if self.min_withdrawal <= (withdrawal * self.taking_off) else self.min_withdrawal)
                if (withdrawal * self.taking_off) < self.max_withdrawal else self.max_withdrawal)

    def show(self):
        """Функция вывода баланса"""
        if self.result_message:
            print(f'На вашем счете: {self.result_operation} у.е.\n'
                  f'{self.result_message}\n'
                  f'Номер операции: {self.count_operation}\n')
        else:
            print(f'На вашем счете: {self.result_operation} у.е.\n'
                  f'Номер операции: {self.count_operation}\n')

    @staticmethod
    def check_multiplicity(value, divider):
        """Функция проверки кратности банкнот"""
        return value % divider == 0
