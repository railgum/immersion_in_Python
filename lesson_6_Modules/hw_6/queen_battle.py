# Фсё, шо смог. Должно быть тру, но...

usr_disp = [(1, 3), (2, 8), (3, 4), (4, 7), (5, 1), (6, 6), (7, 2), (8, 5)]


def check_queen(disposal: tuple) -> bool:
    count = 0
    temp_list_hor = []
    temp_list_vert = []
    for hor in range(1, 9):
        for vert in range(1, 9):
            print(vert, hor, tuple((hor, vert)))
            if tuple((hor, vert)) in disposal:
                temp_list_vert.append((hor, vert))
                print(f'Вертикаль - {temp_list_vert}')
                if len(temp_list_vert) > 1:
                    # return False
                    pass
            if tuple((vert, hor)) in disposal:
                temp_list_hor.append((vert, hor))
                print(f'Горизонталь - {temp_list_hor}')
                if len(temp_list_hor) > 1:
                    # return False
                    pass
            if disposal[vert - 1][0] == disposal[hor - 1][1] and disposal[vert - 1][1] == \
                    disposal[hor - 1][0]:
                count += 1
                print(count)
    for i in temp_list_vert:
        if temp_list_vert.count(i) > 2:
            # return False
            print(f'Диа {temp_list_vert.count(i)}')
    for i in temp_list_hor:
        if temp_list_hor.count(i) > 2:
            # return False
            print(f'Диа {temp_list_hor.count(i)}')
    return True


print(check_queen(usr_disp))
