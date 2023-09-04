# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:6:2])
# print(my_list.pop())
# print(my_list.extend([314, 42]))
# print(my_list.sort(reverse=False))
# print(my_list)

# x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
# y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
# # print(f'{x = }\n{y = }')
# x_ru = x.decode('utf-8')
# y_ru = y.decode('utf-8')
# print(x_ru,y_ru)

numbers_list = [1,3,4,7,2,5,9,4,6,0,4,8,1,9]
numbers_set = []
for i in numbers_list:
    if i not in numbers_set:
        numbers_set.append(i)
print(numbers_list)
print(numbers_set)