# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
#   Сохраните его итератор.
# ✔ Далее выведите первые 5 пар ключ-значение,
#   обращаясь к итератору, а не к словарю.

text = 'Создайте из строки словарь, где ключ — буква, а значение — код буквы.'
my_dict = {item: ord(item) for item in text}
iter_dict = iter(my_dict.items())
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
