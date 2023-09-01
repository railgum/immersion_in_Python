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
ACCRUAL = 0.03
TAX = 0.1

amount = 0

def addition():
    pass
def removal():
    pass
def show():
    pass
def menu():
    os.system("cls")
    menu = ('Добро пожаловать в программу "Банкомат"\n\n'
            'Доступные действия:\n'
            '1 - Пополнить счет\n'
            '2 - Снять наличные\n'
            '3 - Показать баланс\n'
            '0 - Выход')
    print(menu)
    fail_answer = 5
    while fail_answer > 0:
        answer = input('Введите номер действия:>> ')
        if not answer.isdigit():
            print('Нужно ввести число от 1 до 3')
            fail_answer -= 1
            continue
        else:
            if answer == '1':
                os.system("cls")
                addition()
                print(menu)
            if answer == '2':
                os.system("cls")
                removal()
                print(menu)
            if answer == '3':
                os.system("cls")
                show()
                print(menu)
            if answer == '0':
                exit(0)

    print('Похоже, вы делаете что-то не так((')
    exit(0)
if __name__ == '__main__':
    menu()

