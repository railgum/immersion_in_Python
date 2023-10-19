# ----------- Так правильно -----------
import logging

# logging.basicConfig(level=logging.NOTSET)
# logger = logging.getLogger(__name__)
# logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
# logger.info('Немного информации о работе кода')
# logger.warning('Внимание! Надвигается буря!')
# logger.error('Поймали ошибку. Дальше только неизвестность')
# logger.critical('На этом всё')

# --------- Подключение внешнего файла ---------------
# from other import log_all
#
# logging.basicConfig(level=logging.WARNING)
# logger = logging.getLogger('Основной файл проекта')
# logger.warning('Внимание! Используем вызов функции из другого модуля')
# log_all()

# -------- Вывод логов в файл --------

# from other import log_all
# logging.basicConfig(filename='project.log.', filemode='w',
#                     encoding='utf-8', level=logging.INFO)
# logger = logging.getLogger('Основной файл проекта')
# logger.warning('Внимание! Используем вызов функции из другого модуля')
# log_all()

# ----------- Форматирование -----------

# from other import log_all
#
# FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
#          'в строке {lineno:03d} функция "{funcName}()" ' \
#          'в {created} секунд записала сообщение: {msg}'
# logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
# logger = logging.getLogger('main')
# logger.warning('Внимание! Используем вызов функции из другого модуля')
# log_all()

logging.basicConfig(
    filename="log.log",
    encoding='utf-8',
    format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
    style='{',
    level=logging.WARNING
)
