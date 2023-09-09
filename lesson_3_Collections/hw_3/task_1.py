import random

# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

print(nums := [random.randint(0, 10) for _ in range(0, 20)])
double_nums = []
for i in set(nums):
    if nums.count(i) >= 2:
        double_nums.append(i)

print(double_nums)
