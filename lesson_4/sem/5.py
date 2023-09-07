# Задание №5
# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

name = ['Виктор', 'Маргорита', 'Анатолий']
stavka = [10000, 20000, 15000]
prem = ['10.25%', '7.4%', '14.2%']
def my_func(name: str, stavka: int, prem: str) -> dict:
    dict_salary = dict()
    # stavka
    for item in range(len(name)):
        dict_salary[name[item]] = round(stavka[item] * (float((prem[item][
                                                           :-1]))/100), 2)
    return dict_salary

print(my_func(name, stavka, prem))