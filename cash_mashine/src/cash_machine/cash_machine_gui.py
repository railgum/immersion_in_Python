import PySimpleGUI as sg
import menu

layout = [[sg.Button('Внести', enable_events=True, key='ADD', font='Helvetica 16')],
          [sg.Button('Снять', enable_events=True, key='DEL', font='Helvetica 16')],
          [sg.Button('Баланс', enable_events=True, key='BALANCE', font='Helvetica 16')],
              # затем делаем текст
          [sg.Text('Результат:', size=(25, 1), key='-text-', font='Helvetica 16')]]
# рисуем окно
window = sg.Window('Вас приветствует банк "МММ"', layout, size=(450, 300))

while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
# закрываем окно и освобождаем используемые ресурсы
window.close()