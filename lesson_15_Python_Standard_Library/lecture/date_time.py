# Объекты даты и времени неизменяемы, возвращают хэш
# и могут быть ключами словаря, элементами множества и т.д.

from datetime import time, date, datetime, timedelta
d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, second=0, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
second=0, microsecond=24)
# print(f'{d = }\t-\t{d}')
# print(f'{t = }\t-\t{t}')
# print(f'{dt = }\t-\t{dt}')

# delta = timedelta(weeks=1, days=4, hours=3, minutes=4, seconds=5,
# milliseconds=6, microseconds=7)
# print(f'{delta = }\t-\t{delta}')

date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1
# print(f'{delta = }\t-\t{delta}')
birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
# print(f'{new_date = }\t-\t{new_date}')

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
microsecond=24)
print(dt)
print(dt.timestamp())
print(dt.isoformat())
print(dt.weekday())
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))

