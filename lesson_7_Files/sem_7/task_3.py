# ✔ Напишите функцию, которая открывает на чтение созданные в
#   прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное
#   строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными
#   буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
#   сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

def my_func():
    data_1 = []
    data_2 = []
    data_3 = []
    with open('task_1_file.txt', encoding='utf-8') as file_1, \
            open('task_2_file.txt', encoding='utf-8') as file_2, \
            open('task_3_file.txt', 'a', encoding='utf-8') as file_res:
        data_1 = file_1.readline()
        data_2 = file_2.readline()
        max_size = max(len(data_1), len(data_2))
        min_size = min(len(data_1), len(data_2))

        for i in range(max_size):
            a, b = data_1[i%max_size].split('|')
            mul = a * b
            if mul < 0:
                data_3.append(f'{data_2[i%max_size].lower()} | {abc(mul)}')
            else:
                data_3.append(f'{data_2[i%max_size].upper()} | {int(mul)}')
        file_res.write('\n'.join(data_3))