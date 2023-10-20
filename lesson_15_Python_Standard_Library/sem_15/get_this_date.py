# Функция получает на вход текст вида: “1-й четверг ноября”,
# “3я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответствует формату.
import calendar
import datetime
import logging

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

MY_FORMAT = '{levelname:<8} - {asctime:<20} - {msg}'
logger = logging.getLogger(__name__)
logging.basicConfig(filename='date.log', filemode='a', encoding='utf-8',
                    level=logging.INFO, style='{', format=MY_FORMAT)


def convert_date(received_date: str) -> datetime:
    day_week_count, weekday, month = received_date.split(' ')
    try:
        day_week_count = int(day_week_count.split('-')[0])
        if day_week_count > 5 or day_week_count < 1:
            logger.error(msg=f'Неверный порядковый номер дня недели: {day_week_count}')
    except ValueError as e:
        logger.error(msg=e)
    print(day_week_count)
    for k, v in WEEKDAYS.items():
        if weekday in k:
            weekday = v
            break
    else:
        logger.error(msg=f'Неверный формат дня недели: {weekday}')

    for k, v in MONTHS.items():
        if month[:3] in k:
            month = v
            break
    else:
        logger.error(msg=f'Неверный формат месяца: {month}')

    cur_year = datetime.date.today().year
    day = None
    count = 0
    for i in calendar.Calendar().itermonthdays2(cur_year, month):
        if i[1] == weekday and i[0] != 0:
            count += 1
            if count == day_week_count and i[0] != 0:
                day = i[0]
                break
    return f'{cur_year} - {month} - {day}'


print(convert_date('6-й четверг октября'))
