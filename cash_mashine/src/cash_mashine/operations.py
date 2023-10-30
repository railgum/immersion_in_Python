class Operation:
    def __init__(self, tax, accrual, wealth_tax):
        self.tax = tax
        self.accrual = accrual
        self.wealth_tax = wealth_tax
        self.operation_results = 0
        self.operation_message = ''

    def add(self):
        incorrect_answer = 3
        while incorrect_answer > 0:
            if self.operation_results > self.wealth_tax:
                self.operation_message = (f'Вычтен налог на богатство')
                self.operation_results -= self.operation_results * self.tax
                # show(amount)
            payment = int(input('Введите сумму взноса: '))
            if check_multiplicity(payment):
                if count_refill == 2:
                    amount += payment + payment * ACCRUAL
                    count_refill = 0
                else:
                    amount += payment
                    count_refill += 1
                return amount, count_refill
            else:
                print('Сумма взноса должна быть кратна 50!')
                incorrect_answer -= 1
        print('Извините, что-то пошло не по плану :(')
        return amount, count_refill

    def withdraw(self, amount):
        incorrect_answer = 3
        while incorrect_answer > 0:
            withdrawal = int(input('Введите сумму снятия: '))
            if amount > withdrawal:
                if check_multiplicity(withdrawal):
                    if count_cut == 2:
                        amount = (amount - withdrawal) + withdrawal * ACCRUAL
                        count_cut = 0
                    else:
                        count_cut += 1
                    return amount, count_cut
                else:
                    print('Сумма взноса должна быть кратна 50!')
                    incorrect_answer -= 1
            else:
                print('Извините, такой суммы на счете нет')
                continue
        print('Извините, что-то пошло не по плану :(')
        return amount, count_cut
        pass
