# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.


from typing import Callable
import logging


def deco(func: Callable) -> Callable:
    my_format = '{msg}'
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='decor.log', filemode='a', encoding='utf-8',
                        level=logging.INFO, style='{', format=my_format)

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        str_args, str_kwargs = '', ''
        if args:
            str_args = 'args: ' + ','.join(args)
        if kwargs:
            str_kwargs = 'kwargs: ' + ', '.join(
                [f'{key} = {value}' for key, value in kwargs.items()])
        logger.info(msg=f'result: {result}, ' + f'{str_args}' + (
            ', ' if str_args and str_kwargs else '') + f'{str_kwargs}')
        return result

    return wrapper

@deco
def some_func(a: str, b: str):
    return a + '_' + b
#
#
# some_func('Один', 'Два')
# some_func(b='Что-то', a='Где-то')
# some_func('Когда', b='Почему')
