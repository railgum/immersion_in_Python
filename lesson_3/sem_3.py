from pprint import pp
import random
# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.
"""
numbers_list = [1,3,4,7,2,5,9,4,6,0,4,8,1,9]
print(list(set(numbers_list)))
numbers_set = []
for i in numbers_list:
    if i not in numbers_set:
        numbers_set.append(i)
print(numbers_list)
print(numbers_set)
"""

# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
#   ключ — тип элемента, значение — список элементов данного типа.

"""
tuple_ = (1,2,3,'1','2','ret', True, 5, None, [1,4,8], 'dger')
out = dict()
for i in _tuple:
    if type(i) not in out:
        out[type(i)] = []
    out[type(i)].append(i)

pp(out)
"""

# ещё вариант

"""
tuple_ = (1,2,3,'1','2','ret', True, 5, None, [1,4,8], 'dger')
out = dict()
for i in _tuple:
    out.setdefault(type(i), [])
    out[type(i)].append(i)

pp(out)
"""

# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

print(nums := [random.randint(0,10) for _ in range(20)])
i = 0
while i < len(nums):
    item = nums[i]
    if nums.count(item) >= 2:
        nums.remove(item)
        nums.remove(item)
    else:
        i += 1
print(nums)