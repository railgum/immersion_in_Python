# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def func(some_dict: dict, key, default='Не найдено'):
    try:
        return some_dict[key]
    except KeyError:
        return default

d = {1: 'one'}
print(func(d, 2, 'Nein'))
