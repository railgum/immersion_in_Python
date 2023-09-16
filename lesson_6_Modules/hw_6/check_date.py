import sys

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


def check_date(*date_user):
    MIN_YEAR = 1
    MAX_YEAR = 9999
    month_30 = [4, 6, 9, 11]

    if date_user:
        usr_date = str(list(*date_user))
        print(usr_date.split('.'))
    else:
        while True:
            date = input('Введите дату в формате DD.MM.YYYY: ').split('.')
            print(date)
            if (len(date[0]) or len(date[1])) != 2 or len(date[2]) != 4:
                print('Неверный формат даты')
            else:
                usr_date = list(map(int, date))
                break

    month_febr = 29 if __check_leap_year(usr_date[2]) else 28
    if (usr_date[2] > MAX_YEAR or usr_date[2] < MIN_YEAR) \
            or (usr_date[0] > 31 or usr_date[0] < 1) \
            or (usr_date[1] > 12 or usr_date[1] < 1):
        return f'Дата не существует'
    if usr_date[1] == 2 and usr_date[0] > month_febr:
        return f'Дата не существует'
    if usr_date[1] in month_30 and usr_date[0] > 30:
        return f'Дата не существует'
    if month_febr == 28:
        return f'Дата существует'
    else:
        return f'Дата существует и год високосный'


print(check_date('12.15.2015'))
