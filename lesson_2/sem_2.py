# txt = 'Hello world!'
# print(txt, id(txt))
# txt = txt.replace(' ', '_')
# print(txt, id(txt))
#
# a = с = 2 # !!!
# b = 3
# print(a, id(a), b, id(b), c, id(c))  # !!!
# a = b + c
# print(a, id(a), b, id(b), c, id(c))


# data = [2, 4.5, 'string', True, False, 'faer']
# for i in range(len(data)):
#     print(f'Порядковый номер: {i+1}')
#     print(f'Значение: {data[i]}')


# Двоичная система
# num = int(input('Введите число: '))
# bin_num = num
# binary = ''
# while num > 0:
#     rem = num % 2
#     binary = str(rem) + binary
#     num = num // 2

# print(f'Число в двоичном формате: {binary}')
# print(bin(bin_num))


# Восьмеричная система
# num_2 = int(input('Введите число: '))
# octal = ''
#
# while num_2 > 0:
#     rem_oct = num_2 % 8
#     octal = str(num_2) + octal
#     num_2 = num_2 // 8
# print(f'Число в восьмеричном формате: {octal}')
# print(oct(num_2))

# dia = int(input('Введите диаметр: '))
# if dia > 1000:
#     print('Диаметр не должен превышать 1000')
# print(f'Площадь круга диаметром {dia} - {(dia**2//4)*3.1415}')
# print((f'Длина окружности диаметром {dia} - {dia * 3.1415}'))
# z = int('rail', base=28)
# print(z)

# txt = input('Введите текст: ')
# if txt.isdigit():
#     num_txt = int(txt)
#     print(bin(num_txt), oct(num_txt), hex(num_txt), sep='\n')
# elif txt.isascii():
#     print('Текст в кодировке ASCII')
# else:
#     print('Кодировка неизвестна')
