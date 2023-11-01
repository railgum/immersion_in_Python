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
from operations import Operation

DIVIDER = 50               # Минимальная банкнота
TAKING_OFF = 0.015         # Процент за снятие
MIN_WITHDRAWAL = 30        # Минимальная сумма за снятие
MAX_WITHDRAWAL = 600       # Максимальная сумма за снятие
ACCRUAL = 0.03             # Начисление за операции
TAX = 0.1                  # Процент налога на богатство
WEALTH_TAX = 5_000_000     # Сумма на счете, определяющая богатство
COUNT_INCORRECT_ANSWER = 3 # Количество неправильно введенных данных

def menu():
    print('Добро пожаловать в программу "Банкомат"\n\n')
    menu = (
        'Доступные действия:\n'
        '1 - Пополнить счет\n'
        '2 - Снять наличные\n'
        '3 - Показать баланс\n'
        '0 - Выход')
    print(menu)
    incorrect_answer = 0

    while incorrect_answer < COUNT_INCORRECT_ANSWER:
        answer = input('Введите номер действия:>> ')
        if not answer.isdigit():
            print('Нужно ввести число от 1 до 3')
            incorrect_answer += 1
            continue
        else:
            if answer == '1':
                cm.addition()
                print(menu)
            if answer == '2':
                cm.removal()
                print(menu)
            if answer == '3':
                print(cm.show())
                print(menu)
            if answer == '0':
                exit(0)

    print('Похоже, вы делаете что-то не так((')
    exit(0)


if __name__ == '__main__':
    cm = Operation(MIN_WITHDRAWAL, MAX_WITHDRAWAL, TAX, ACCRUAL, TAKING_OFF, WEALTH_TAX, DIVIDER)
    menu()
