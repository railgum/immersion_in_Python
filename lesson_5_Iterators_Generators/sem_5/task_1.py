# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.


# use_str = input('Введите 4 или более числа через знак "/": ' )
def create_dict(str_):
    a,b,c,*d = map(int, str_.split('/'))
    return {b:a, c:d}

# print(create_dict(use_str))

def func(a, b, c, *args):
    return {b: a, c: args}
