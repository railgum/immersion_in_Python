import random

# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

print(nums := [random.randint(0, 10) for _ in range(0, 20)])
origin_nums = nums.copy()
double_nums = set()
for i in nums:
    if nums.count(i) >= 2:
        double_nums.add(i)
        origin_nums.remove(i)

# print(origin_nums)
print(double_nums)
