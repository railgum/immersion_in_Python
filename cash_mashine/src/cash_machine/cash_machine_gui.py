import re
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import OK, showinfo, INFO
from operations_gui import Operation

DIVIDER = 50  # Минимальная банкнота`
TAKING_OFF = 0.015  # Процент за снятие
MIN_WITHDRAWAL = 30  # Минимальная сумма за снятие
MAX_WITHDRAWAL = 600  # Максимальная сумма за снятие
ACCRUAL = 0.03  # Начисление за операции
TAX = 0.1  # Процент налога на богатство
WEALTH_TAX = 5_000_000  # Сумма на счете, определяющая богатство
COUNT_INCORRECT_ANSWER = 3  # Количество неправильно введенных данных

message_code_dict = {'error_enter': 'Ошибка ввода',
                     'not_integer': 'Это не число',
                     'successfully': 'Операция выполнена успешно',
                     'error_divider': 'Число не кратно 50',
                     'accrual': 'Вам бонус!',
                     'wealth': 'Вычтен налог на богатство'}


def menu(cm):
    """Вывод графического меню"""
    def show_balance():
        """Функция вывода баланса из экземпляра класса"""
        balance_text['text'] = cm.show()

    def operation_click(operation: bool):
        """Функция обработки операции"""
        def clear():
            """Функция очистки введенного значения"""
            operation_entry.delete(0, END)

        def validate(newval):
            """Функция проверки вводимого значения"""
            result = re.match(r'\d*$', newval) is not None
            if not result:
                errmsg.set('Необходимо вводить цифры')
            else:
                errmsg.set('')
            return result
        def run_operation():
            """Функция вывода окно сообщения о результате операции"""
            amount = int(number.get())
            print(amount)
            cm.transaction(amount, operation)
            showinfo(title='Результат операции', detail=message_code_dict[cm.result_message],
                     icon=INFO, default=OK)
            show_balance()
            operation_window.destroy()

        operation_window = Toplevel()
        operation_window.title('Операция Ы')
        operation_window.geometry('300x200')
        number = StringVar()
        errmsg = StringVar()
        check = (operation_window.register(validate), '%P')
        operation_entry = ttk.Entry(operation_window, textvariable=number, validate='key',
                                    validatecommand=check)
        operation_entry.pack(padx=5, pady=15)
        operation_entry.focus_set()
        error_label = ttk.Label(operation_window, foreground='red', textvariable=errmsg)
        error_label.pack(pady=5)
        operation_frame = ttk.Frame(operation_window, borderwidth=3, relief=GROOVE, padding=5,
                                    width=100, height=100)
        btn_add = ttk.Button(operation_frame, text='Ввод', command=run_operation)
        btn_add.grid(row=0, column=0, padx=10, pady=5)
        btn_del = ttk.Button(operation_frame, text='Удалить', command=clear)
        btn_del.grid(row=0, column=1, padx=10, pady=5)
        operation_frame.pack()
        close_btn = ttk.Button(operation_window, text='Выйти',
                               command=lambda: operation_window.destroy())
        close_btn.pack(pady=10)

    window = Tk()
    window.title("Добро пожаловать")
    window.iconphoto(False, PhotoImage(file='icon_bank.png'))
    window.geometry('350x400')
    piggy_image = PhotoImage(file='piggy-bank.png')
    btn_bg = ttk.Label(image=piggy_image, compound='bottom')
    btn_bg.pack()

    frame_balance = ttk.Frame(borderwidth=3, relief=GROOVE, padding=5, width=100, height=100)
    btn_balance = ttk.Button(frame_balance, text='Проверить баланс', command=show_balance)
    btn_balance.pack(anchor='n', pady=7, ipadx=38)

    balance_text = ttk.Label(frame_balance)
    balance_text.pack()
    frame_balance.pack(anchor=CENTER, padx=5, pady=5)

    frame_operation = ttk.Frame(borderwidth=2, relief=GROOVE, padding=5, width=100, height=50)
    add_ = ttk.Button(frame_operation, text='Внести', command=lambda: operation_click(True))
    with_ = ttk.Button(frame_operation, text='Снять', command=lambda: operation_click(False))

    add_.grid(row=0, column=0, padx=10, pady=5)
    with_.grid(row=0, column=1, padx=10, pady=5)
    frame_operation.pack(anchor=CENTER, padx=5, pady=5)
    close_btn = ttk.Button(text='Закрыть и выйти', command=lambda: window.destroy())
    close_btn.pack(pady=10)

    window.mainloop()


# if __name__ == '__main__':
#     CM = Operation(MIN_WITHDRAWAL, MAX_WITHDRAWAL, TAX, ACCRUAL, TAKING_OFF, WEALTH_TAX, DIVIDER)
#     menu(CM)
