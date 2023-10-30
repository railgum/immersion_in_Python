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
WEALTH_TAX = 5_000_000


def check_multiplicity(monee):
    return monee % DIVIDER == 0


def show(amount):
    print(f'На вашем счете: {amount} у.е.')
    return amount


if __name__ == '__main__':
    from menu import Menu

    start_cash_mashine = Menu(TAX, ACCRUAL, WEALTH_TAX)