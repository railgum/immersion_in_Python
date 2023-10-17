# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре


from string import ascii_lowercase

def ascii_func(text):
    result = ''
    if text is not None:
        for i in text:
            if i.lower() in ascii_lowercase + ' ':
                result += i
        return result.lower()
    raise ValueError('Incorrect text')


print(ascii_func('slvflm:4fv,4FLbf0cdslm'))
