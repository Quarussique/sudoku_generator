from random import randint as ramdom

field = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]


def swap_columns():
    global field
    temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    rand1 = ramdom(0, 2)
    rand2 = ramdom(0, 2)
    if rand1 == 0:
        if rand2 == 0:
            for i in range(9):
                temp[i] = field[i][0]
                field[i][0] = field[i][1]
                field[i][1] = temp[i]
        if rand2 == 1:
            for i in range(9):
                temp[i] = field[i][1]
                field[i][1] = field[i][2]
                field[i][2] = temp[i]
        if rand2 == 2:
            for i in range(9):
                temp[i] = field[i][2]
                field[i][2] = field[i][0]
                field[i][0] = temp[i]
    if rand1 == 1:
        if rand2 == 0:
            for i in range(9):
                temp[i] = field[i][3]
                field[i][3] = field[i][4]
                field[i][4] = temp[i]
        if rand2 == 1:
            for i in range(9):
                temp[i] = field[i][4]
                field[i][4] = field[i][5]
                field[i][5] = temp[i]
        if rand2 == 2:
            for i in range(9):
                temp[i] = field[i][5]
                field[i][5] = field[i][3]
                field[i][3] = temp[i]
    if rand1 == 2:
        if rand2 == 0:
            for i in range(9):
                temp[i] = field[i][6]
                field[i][6] = field[i][7]
                field[i][7] = temp[i]
        if rand2 == 1:
            for i in range(9):
                temp[i] = field[i][7]
                field[i][7] = field[i][8]
                field[i][8] = temp[i]
        if rand2 == 2:
            for i in range(9):
                temp[i] = field[i][8]
                field[i][8] = field[i][6]
                field[i][6] = temp[i]


def swap_rows():
    global field
    temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    rand1 = ramdom(0, 2)
    rand2 = ramdom(0, 2)
    if rand1 == 0:
        if rand2 == 0:
            for i in range(9):
                temp = field[0]
                field[0] = field[1]
                field[1] = temp
        if rand2 == 1:
            for i in range(9):
                temp = field[1]
                field[1] = field[2]
                field[2] = temp
        if rand2 == 2:
            for i in range(9):
                temp = field[2]
                field[2] = field[0]
                field[0] = temp
    if rand1 == 1:
        if rand2 == 0:
            for i in range(9):
                temp = field[3]
                field[3] = field[4]
                field[4] = temp
        if rand2 == 1:
            for i in range(9):
                temp = field[4]
                field[4] = field[5]
                field[5] = temp
        if rand2 == 2:
            for i in range(9):
                temp = field[5]
                field[5] = field[3]
                field[3] = temp
    if rand1 == 2:
        if rand2 == 0:
            for i in range(9):
                temp = field[6]
                field[6] = field[7]
                field[7] = temp
        if rand2 == 1:
            for i in range(9):
                temp = field[7]
                field[7] = field[8]
                field[8] = temp
        if rand2 == 2:
            for i in range(9):
                temp = field[8]
                field[8] = field[6]
                field[6] = temp


def transpose():
    global field
    field_t = []
    for i in range(9):
        field_t.append([])
        for j in range(9):
            field_t[i].append(field[i][j])
    for i in range(9):
        for j in range(9):
            field_t[i][j] = field[j][i]
    field = field_t


def show_field():
    global field
    for line in field:
        print(line)
    print('- - - - - - - - - - - - - -')


def swap_big_rows():
    global field
    rand1 = ramdom(0, 2)
    temp = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    if rand1 == 0:
        for i in range(0, 3):
            temp[i] = field[i].copy()
            field[i] = field[i+3].copy()
            field[i+3] = temp[i]
    if rand1 == 1:
        for i in range(0, 3):
            temp[i] = field[i].copy()
            field[i] = field[i+6].copy()
            field[i+6] = temp[i]
    if rand1 == 2:
        for i in range(0, 3):
            temp[i] = field[i+3].copy()
            field[i+3] = field[i+6].copy()
            field[i+6] = temp[i]


def swap_big_columns():
    transpose()
    swap_big_rows()
    transpose()


for i in range(10000):
    rand1 = ramdom(0, 4)
    if rand1 == 0:
        swap_rows()
    elif rand1 == 1:
        swap_columns()
    elif rand1 == 2:
        swap_big_rows()
    elif rand1 == 3:
        swap_big_columns()
    else:
        transpose()
show_field()

i = 0
j = 0
print('┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┓')
for line in field:
    j = 0
    i += 1
    print('┃', end='')
    for cell in line:
        j += 1
        if ramdom(0, 10) > 6:
            print('', cell, end=' ')
        else:
            print(' .', end=' ')
        if j % 3 == 0 and j != 9:
            print('┃', end='')
    print('┃')
    if i % 3 == 0 and i != 9:
        print('┣━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┫')
print('┗━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┛')
