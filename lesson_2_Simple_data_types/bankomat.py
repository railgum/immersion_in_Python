import os

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

DIVIDER = 50
TAKING_OFF = 0.015
MIN_WITHDRAWAL = 30
MAX_WITHDRAWAL = 600
ACCRUAL = 0.03
TAX = 0.1
WEALT_TAX = 5_000_000


def check_multiplicity(monee):
    return monee % DIVIDER == 0


def addition(amount, count_refill):
    incorrect_answer = 3
    while incorrect_answer > 0:
        if amount > 5_000_000:
            print('Вычтен налог на богатство')
            amount -= amount * TAX
            show(amount)
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


def removal(amount, count_cut):
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


def show(amount):
    print(f'На вашем счете: {amount} у.е.')
    return amount

def menu():
    os.system("cls")
    menu = ('Добро пожаловать в программу "Банкомат"\n\n'
            'Доступные действия:\n'
            '1 - Пополнить счет\n'
            '2 - Снять наличные\n'
            '3 - Показать баланс\n'
            '0 - Выход')
    print(menu)
    incorrect_answer = 3
    amount = 0
    count_refill = 0
    count_cut = 0
    while incorrect_answer > 0:
        answer = input('Введите номер действия:>> ')
        if not answer.isdigit():
            print('Нужно ввести число от 1 до 3')
            incorrect_answer -= 1
            continue
        else:
            if answer == '1':
                os.system("cls")
                amount, count_refill = addition(amount, count_refill)
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


if __name__ == '__main__':
    menu()
