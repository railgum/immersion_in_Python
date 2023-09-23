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
    data_res = []
    with open('task_1_file.txt', encoding='utf-8') as file_1, \
            open('task_2_file.txt', encoding='utf-8') as file_2, \
            open('task_3_file.txt', 'w', encoding='utf-8') as file_res:
        data_1 = file_1.readlines()
        # print(data_1[0].split('|'))
        data_2 = file_2.readlines()
        # print(data_2)
        max_size = max(len(data_1), len(data_2))
        min_size = min(len(data_1), len(data_2))

        for i in range(max_size):
            a, b = data_1[i % min_size].split('|')
            mul = int(a) * float(b[:-2])
            if mul < 0:
                data_res.append(f'{data_2[i % min_size].lower().strip()} | {abs(mul)}')
            else:
                data_res.append(f'{data_2[i % min_size].upper().strip()} | {int(mul)}')
        file_res.write('\n'.join(data_res))


my_func()
