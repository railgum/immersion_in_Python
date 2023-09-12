# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def func(*args):
    dict_result = {}
    for item in range(len(args)):
        if args[item].__hash__:
            dict_result[args[item]] = type(args[item])
        else:
            dict_result[type(args[item])] = type(args[item])
    return dict_result


print(func(5, 'text', 6, [1,2,3], (1,2,3)))


