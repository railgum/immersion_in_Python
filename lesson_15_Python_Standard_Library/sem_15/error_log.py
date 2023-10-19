# Напишите программу, которая использует модуль logging
# для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

FORMAT = '{asctime:<20} - {levelname:<10} - {msg}'

logger = logging.getLogger(__name__)
logging.basicConfig(filename='errors.log', filemode='w', encoding='utf-8',
                    level=logging.ERROR, style='{', format=FORMAT)

def func(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        logger.error(msg=e)

func(100,0)