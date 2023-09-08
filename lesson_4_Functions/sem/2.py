# Задание №2
# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

text = input('Введите строку: ')

def my_func(data: str):
    my_set = set(data)
    my_lst = []
    for item in my_set:
        my_lst.append(ord(item))
    my_lst.sort(reverse=True)
    return my_lst

print(my_func(text))