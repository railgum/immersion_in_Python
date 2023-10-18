# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def func():
    while True:
        try:
            num = input('Введите число: ')
            num = float(num)
            return int(num) if int(num) == num else num
        except Exception as e:
            print(f'Ошибка {e}')

print(func())