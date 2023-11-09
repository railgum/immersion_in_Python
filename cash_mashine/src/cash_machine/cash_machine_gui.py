import PySimpleGUI as sg
from operations import Operation

DIVIDER = 50  # Минимальная банкнота
TAKING_OFF = 0.015  # Процент за снятие
MIN_WITHDRAWAL = 30  # Минимальная сумма за снятие
MAX_WITHDRAWAL = 600  # Максимальная сумма за снятие
ACCRUAL = 0.03  # Начисление за операции
TAX = 0.1  # Процент налога на богатство
WEALTH_TAX = 5_000_000  # Сумма на счете, определяющая богатство
COUNT_INCORRECT_ANSWER = 3  # Количество неправильно введенных данных


def add_window():
    layout = [[sg.T('Введите сумму взноса: ')],
              [sg.Input(key='-AMOUNT-')],
              [sg.Button('Показать', key='Show'), sg.Button('Выход', key='Exit')],
              [sg.T('Баланс: '), sg.T(size=(15, 1), key='-BALANS-')]]
    window = sg.Window('Вас приветствует банк...', layout, size=(300, 150), modal=True)

    while True:
        event, values = window.read()
        try:
            amount = int(values['-AMOUNT-'])
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == 'Show':
                window['-BALANS-'].print(CM.transaction(amount, True))
        except ValueError:
                # window.close()


def start_window():
    l_add = sg.Button('Внести', enable_events=True, key='-ADD-')
    l_del = sg.Button('Снять', enable_events=True, key='-DEL-')
    l_bal = sg.Button('Баланс', enable_events=True, key='-BALANCE-')
    layout = [[l_add, l_del, l_bal],
              # [sg.HSep()],
              # [sg.Text('Результат операции:', size=(25, 1), key='-text-', font='Helvetica 16')]
              ]

    window = sg.Window('Вас приветствует банк...', layout, size=(300, 150), modal=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '-ADD-':
            window = add_window()
            window.close()


def main():
    while True:
        layout = [[sg.T('Добро пожаловать в банк...!')],
                  [sg.HSep()],
                  [sg.Button('В меню', key='-START-'),
                   sg.Button('Выход', key='-EXIT-')]
                  ]
        window = sg.Window('Вас приветствует банк...', layout, size=(300, 150), modal=True)
        # получаем события, произошедшие в окне
        event, values = window.read()
        # если нажали на крестик
        if event in (sg.WIN_CLOSED, 'Exit', '-EXIT-'):
            # выходим из цикла
            break
        if event == '-START-':
            window = start_window()

    # закрываем окно и освобождаем используемые ресурсы
    window.close()


if __name__ == '__main__':
    CM = Operation(MIN_WITHDRAWAL, MAX_WITHDRAWAL, TAX, ACCRUAL, TAKING_OFF, WEALTH_TAX, DIVIDER)
    main()
