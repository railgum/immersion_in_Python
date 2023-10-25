# data = list((1, 2, 3))
# print(f'{data = }, {type(data) = }, {type(list) = }')
#
# import random
# import supermodule
# result1 = random.randint(1, 10)
# # result2 = supermodule.division(random.randint(42))
#
# print(result1)
# print(result2)


# class User:
#     count = []
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
# u1 = User('One', '123-45-67')
# u2 = User('NoOne', '76-54-321')
# u1.count.append(42)
# u1.count.append(73)
# u2.counter = 256
# # u2.count.append(u2.counter)
# # u2.count.append(u1.count[-1])
# print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
# print(f'{u2.name = }, {u2.phone = }, {u2.count = }')

# class Person:
#     max_up = 3
# p1 = Person()
# p2 = Person()
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# p1.max_up = 12
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# Person.max_up = 42
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

class DivStr(str):
    def __init__(self, obj):
        self.obj = str(obj)

    def __truediv__(self, other):
        first = self.obj.endswith('/')
        start = self.obj
        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, DivStr):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)
        if first and second:
            return DivStr(start[:-1] + finish)
        if (first and not second) or (not first and second):
            return DivStr(start + finish)
        if not first and not second:
            return DivStr(start + '/' + finish)


path_1 = DivStr('/home/user/')
path_2 = DivStr('/my_project/workdir')
result = path_1 / path_2
print(f'{result = }, {type(result)}')
print(f'{result / "text" = }')
print(f'{result / 42 = }')
print(f'{result * 3 = }')
