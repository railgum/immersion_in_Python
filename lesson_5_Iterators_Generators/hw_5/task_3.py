# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

name = ['Виктор', 'Маргaрита', 'Анатолий']
stavka = [10000, 20000, 15000]
prem = ['10.25%', '7.4%', '14.2%']
# Это я для себя:
# def my_func(name: str, stavka: int, prem: str):
#     yield {name[i]: stavka[i] * float(prem[i][:-1]) / 100 for i in range(len(
#         name))}
print(
    *({name[i]: stavka[i] * float(prem[i][:-1])/100} for i in range(len(name)))
)