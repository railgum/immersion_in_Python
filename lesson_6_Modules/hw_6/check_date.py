
def __check_leap_year(year: int):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True


def check_date(date: str = '01.01.0001'):
    MIN_YEAR = 1
    MAX_YEAR = 9999
    month_30 = [4, 6, 9, 11]
    usr_date = list(map(int, date.split('.')))
    print(date.split('.'))
    if len(str(usr_date[2])) != 4 \
            or len(str(usr_date[0])) != 2 \
            or len(str(usr_date[1])) != 2:
        return f'{date} - Неверный формат даты'
    else:
        month_febr = 29 if __check_leap_year(usr_date[2]) else 28
        if (usr_date[2] > MAX_YEAR or usr_date[2] < MIN_YEAR) \
                or (usr_date[0] > 31 or usr_date[0] < 1) \
                or (usr_date[1] > 12 or usr_date[1] < 1):
            return f'{date} - Дата не существует'
        if usr_date[1] == 2 and usr_date[0] > month_febr:
            return f'{date} - Дата не существует'
        if usr_date[1] in month_30 and usr_date[0] > 30:
            return f'{date} - Дата не существует'
        if month_febr == 28:
            return f'{date} - Дата существует'
        else:
            return f'{date} - Дата существует и год високосный'

# print(check_date('12.12.2012'))
