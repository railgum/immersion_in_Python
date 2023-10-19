# Функция получает на вход текст вида: “1-й четверг ноября”,
# “3я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответствует формату.

import datetime
import logging


my_format = '{levelname:<8} - {asctime:<20} - {funcName}- {msg}'
logger = logging.getLogger(__name__)
logging.basicConfig(filename='date.log', filemode='a', encoding='utf-8',
                    level=logging.INFO, style='{', format=my_format)
WEEKDAYS = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6,
}
MONTHS = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12,
}


def convert_date(received_date: str) -> datetime:
    day, weekday, month = received_date.split(' ')
    try:
        day = int(day.split('-')[0])
        if 1 > day > 5:
            logger.error(msg='День не соответствует формату')
    except ValueError as e:
        logger.error(msg=e)

    for k, v in WEEKDAYS.items():
        if weekday in k:
            weekday = v
            break
    else:
        logger.error(msg='Неверный формат дня недели')

    for k, v in MONTHS.items():
        if month[:3] in k:
            month = v
            break
    else:
        logger.error(msg='Неверный формат месяца')

    cur_year = datetime.datetime.now().year
    first_months_weekday = datetime.date(year=cur_year, month=month, day=1).weekday()
    return f'{cur_year}\n{first_months_weekday}'

print(convert_date('2-й четверг января'))