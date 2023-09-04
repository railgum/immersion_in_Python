from fractions import Fraction


# 1. Напишите программу, которая получает целое число
#    и возвращает его шестнадцатеричное строковое представление.
#    Функцию hex используйте для проверки своего результата.

# num = int(input('Введите число: '))
# dec_num = num
# hex_digits = '0123456789ABCDEF'
# hex_num = ''
#
# while num > 0:
#     temp_div = num % 16
#     hex_digit = hex_digits[temp_div]
#     hex_num = hex_digit + hex_num
#     num //= 16
#
# print(f'Число {dec_num} в шестнадцатеричном формате - {hex_num}')
# print(f'Проверка: {hex(dec_num)}')


# Универсальное решение (из разбора)

# HEX_ALPHA = '0123456789abcdef'
# num = int(input('Введите число: '))
# base = int(input('Основание системы счисления: '))
# original = num
# result = ''
# while num > 0:
#     result = HEX_ALPHA[num % base] + result
#     num //= base
#
# print(f'Число {original} в {base}-ной системе записывается так: {result}')
# print('Проверка')
# print(f'Двоичное: {bin(original)[2:]}')
# print(f'Восьмеричное: {oct(original)[2:]}')
# print(f'Шестнадцатеричное: {hex(original)[2:]}')


# 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#    Программа должна возвращать сумму и произведение дробей.
#    Для проверки своего кода используйте модуль fractions.

# fract_1 = input('Введите первую дробь в виде a/b: ')
# fract_2 = input('Введите вторую дробь в виде a/b: ')
#
# # проверки пока исключаю
#
# slash_index_1 = fract_1.find('/')
# num_1 = int(fract_1[:slash_index_1])
# denom_1 = int(fract_1[slash_index_1+1:])
#
# slash_index_2 = fract_2.find('/')
# num_2 = int(fract_2[:slash_index_2])
# denom_2 = int(fract_2[slash_index_2+1:])
#
# sum_num = (num_1 * denom_2) + (num_2 * denom_1)
# sum_denom = denom_1 * denom_2
#
# # функции ещё не проходили
#
# gcd = 1
# if sum_num > sum_denom:
#     temp_remains = sum_denom
# else:
#     temp_remains = sum_num
# for i in range(1, temp_remains + 1):
#     if((sum_num % i == 0) and (sum_denom % i == 0)):
#         gcd = i
#
# sum_fraction = f'{sum_num // gcd}/{sum_denom // gcd}'
# print('Сумма дробей: ')
# print(f'Моё решение: {sum_fraction}')
# print(f'Библиотека: {Fraction(num_1, denom_1) + Fraction(num_2, denom_2)}')
#
#
# mult_num = num_1 * num_2
# mult_denom = denom_1 * denom_2
# gcd = 1
# if mult_num > mult_denom:
#     temp_remains = mult_denom
# else:
#     temp_remains = mult_num
# for i in range(1, temp_remains + 1):
#     if((mult_num % i == 0) and (mult_denom % i == 0)):
#         gcd = i
# mult_fraction = f'{mult_num//gcd}/{mult_denom//gcd}'
#
# print('Произведение дробей: ')
# print(f'Моё решение: {mult_fraction}')
# print(f'Библиотека: {Fraction(num_1, denom_1) * Fraction(num_2, denom_2)}')

# Альтернативный метод

fract_1 = input('Введите первую дробь в виде a/b: ').split('/')
fract_2 = input('Введите вторую дробь в виде a/b: ').split('/')

sum_num = int(fract_1[0]) * int(fract_2[1]) + int(fract_1[1]) * int(fract_2[0])
sum_denom = int(fract_1[1]) * int(fract_2[1])
sum_fraction = [sum_num, sum_denom]
multi_fraction = [int(fract_1[0]) * int(fract_2[0]), int(fract_1[1]) * int(fract_2[1])]

# вычисление НОД
a1, b1 = sum_fraction
while b1:
    a1, b1 = b1, a1 % b1

a2, b2 = multi_fraction
while b2:
    a2, b2 = b2, a2 % b2

print(f'Моё решение: {sum_fraction[0] // a1}/{sum_fraction[1] // a1}', f'{multi_fraction[0] // a2}/{multi_fraction[1] // a2}')
fract_fraction_1 = Fraction(f'{fract_1[0]}/{fract_1[1]}')
fract_fraction_2 = Fraction(f'{fract_2[0]}/{fract_2[1]}')
print(f'Библиотека: {fract_fraction_1 + fract_fraction_2}', f'{fract_fraction_1 * fract_fraction_2}')


