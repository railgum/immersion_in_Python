# Задание №4
# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык
# сортировок.
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
import random


def my_sort(some_lst: list):
    for i in range(len(some_lst)-1):
        for j in range(len(some_lst)-i-1):
            if some_lst[j] > some_lst[j+1]:
                some_lst[j], some_lst[j+1] = some_lst[j+1], some_lst[j]

print(lst := [random.randint(0, 10) for _ in range(20)])
my_sort(lst)
print(lst)
