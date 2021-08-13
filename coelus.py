
def check_place(y_min, y_max, x_min, x_max, table, block_type,): # оценивает кол-во пустых клеток по горизонтали и вертикали от фигуры
        kol_no_empty = 0
        for cells in range(len(table))[y_min:y_max]:
            if cells < y_min or cells > y_max:
                for cell in table[cells][x_min, x_max]:
                    if cell == 0:
                        kol_no_empty += 1
            elif cells >= y_min and cells <= y_max:
                for cell in table[cells]:
                    if cell == 0:
                        kol_no_empty += 1
        return kol_no_empty


def check_square(figure, table_size):# проверяет соответствует ли размер фигур размеру стола
    for size in figure:
        if table_size[0] < size[0][0] and table_size[1] < size[0][0] or table_size[1] < size[0][1] and table_size[0] < size[0][1]:
            return True

def check_sum_cells(square_size, L_size, table_size): # проверяет сумму клеток всех фигур и сумму клеток стола
    sum_cells = 0
    for square in square_size:
        sum_cells += (square[0][0] * square[0][1]) * square[1]
    for L in L_size:
        sum_cells += (L[0][0] + L[0][1] - 1) * L[1]
    sum_table = table_size[0] * table_size[1]
    if sum_table < sum_cells:
        return True

def check_growing(arr, n): # проверяет есть ли в ряду последовательное возрастание
    massiv = []
    for i in range(len(arr) - n + 1):
        el = arr[i:i + n]
        if el == list(range(min(el), max(el) + 1)):
             massiv.append([el[0], el[-1]])
    return massiv

def add_square(table, square):# функция добавления прямоугольного полилмино на стол
    x_square = square[0]
    y_square = square[1]
    all_empty_cells = []
    now_y = len(table)-1
    if x_square == y_square:
        for row in reversed(table):
                empty_cells = []
                if now_y - y_square + 1>= 0:
                    for cell in range(len(row)):
                        if row[cell] == 0:
                            empty_cells.append(cell)
                    grows = check_growing(empty_cells, x_square)
                    if grows:
                        for grow in grows:
                            min_x = grow[0]
                            max_x = grow[1]
                            fits = 1

                            for y in range(y_square):
                                if 1 in table[now_y - y][grow[0]:grow[1] + 1]:
                                    fits = 0
                            if fits == 1:
                                all_empty_cells.append(
                                [check_place(now_y - y_square + 1, now_y + 1,min_x, max_x, table, 'l'), min_x, max_x, now_y,
                                 y_square, x_square])
                now_y -= 1
                continue
    else:
        for rotate in range(2):
            now_y = len(table) - 1
            if rotate == 1:
                x_square = square[1]
                y_square = square[0]
            for row in reversed(table):
                empty_cells = []
                if now_y - y_square + 1 >= 0:
                    for cell in range(len(row)):
                        if row[cell] == 0:
                            empty_cells.append(cell)
                    grows = check_growing(empty_cells, x_square)
                    if grows:
                        for grow in grows:
                            min_x = grow[0]
                            max_x = grow[1]
                            fits = 1
                            for y in range(y_square):
                                if 1 in table[now_y - y][grow[0]:grow[1] + 1]:
                                    fits = 0
                            if fits == 1:
                                all_empty_cells.append(
                                [check_place(now_y - y_square + 1, now_y + 1,min_x, max_x, table, 'l'), min_x, max_x, now_y,
                                 y_square, x_square])
                now_y -= 1
                continue

    best_place = sorted(all_empty_cells, key=lambda x: (x[0]))
    if best_place != []:
        best_place = best_place[0]
        for y in range(best_place[4]):
            table[best_place[3] - y][best_place[1]:best_place[2] + 1] = [1] * best_place[5]
        return False
    else:
        return True
def add_L(table, L):# функция добавления L-полилмино на стол
    x_L = L[1]
    y_L = L[0]
    all_empty_cells = []
    for rotate in range(4):
        if rotate == 0: #0
            y_L = L[0]
            x_L = L[1]
            now_y = len(table) - y_L
            for row in reversed(table[0:len(table) - y_L + 1]):
                empty_cells = []
                if now_y - y_L + 1 >= 0:
                    for cell in range(len(row)):
                        if row[cell] == 0:
                            empty_cells.append(cell)
                    grows = check_growing(empty_cells, x_L)
                    if grows:
                        for grow in grows:
                            min_x = grow[0]
                            max_x = grow[1]
                            fits = 1
                            for y in range(y_L):
                                if table[now_y + y][max_x] == 1:
                                    fits = 0
                            if fits == 1:
                                all_empty_cells.append(
                                [check_place(now_y - y_L, now_y,min_x, max_x, table, 'l'), rotate, min_x, max_x, now_y, y_L, x_L])
                now_y -= 1
                continue

        elif rotate == 1:#3pi/2
            y_L = L[1]
            x_L = L[0]
            now_y = len(table) - y_L
            for row in reversed(table[0:len(table) - y_L + 1]):
                empty_cells = []
                if now_y - y_L + 1 >= -1:
                    for cell in range(len(row)):
                        if row[cell] == 0:
                            empty_cells.append(cell)
                    grows = check_growing(empty_cells, x_L)
                    if grows:
                        for grow in grows:
                            min_x = grow[0]
                            max_x = grow[1]
                            fits = 1
                            for y in range(y_L):
                                if table[now_y + y][grow[0]] == 1:
                                    fits = 0
                            if fits == 1:
                                all_empty_cells.append(
                                [check_place(now_y, now_y + y_L,min_x, max_x, table, 'l'), rotate, min_x, max_x, now_y, y_L, x_L])
                now_y -= 1
                continue
        elif rotate == 2:#pi
            x_L = L[1]
            y_L = L[0]
            now_y = len(table) - 1
            for row in reversed(table):
                empty_cells = []
                if now_y - y_L + 1 >= 0:
                    for cell in range(len(row)):
                        if row[cell] == 0:
                            empty_cells.append(cell)
                    grows = check_growing(empty_cells, x_L)
                    if grows:
                        for grow in grows:
                            min_x = grow[0]
                            max_x = grow[1]
                            fits = 1
                            for y in range(y_L):
                                if table[now_y - y][grow[0]] == 1:
                                    fits = 0
                            if fits == 1:
                                all_empty_cells.append(
                                [check_place(now_y, now_y + y_L,min_x, max_x, table, 'l'), rotate, min_x, max_x, now_y, y_L,
                                 x_L])
                now_y -= 1
                continue
        elif rotate == 3:#pi/2

            y_L = L[1]
            x_L = L[0]
            now_y = len(table) - 1
            for row in reversed(table):
                empty_cells = []
                if now_y - y_L + 1 >= 0:
                    for cell in range(len(row)):
                        if row[cell] == 0:
                            empty_cells.append(cell)
                    grows = check_growing(empty_cells, x_L)
                    if grows:
                        for grow in grows:
                            min_x = grow[0]
                            max_x = grow[1]
                            fits = 1
                            for y in range(y_L):
                                if table[now_y - y][max_x] == 1:
                                    fits = 0
                            if fits == 1:
                                all_empty_cells.append(
                                [check_place(now_y - y_L, now_y,min_x, max_x, table, 'l'), rotate, min_x, max_x, now_y, y_L,
                                 x_L])
                now_y -= 1
                continue
    best_place = sorted(all_empty_cells, key=lambda x: (x[0], -x[3]))
    if best_place != []:
        best_place = best_place[0]
        for y in range(best_place[5]):
            if y == 0:
                table[best_place[4]][best_place[2]:best_place[3] + 1] = [1] * best_place[6]
            else:
                if best_place[1] == 0:
                    table[best_place[4] + y][best_place[3]] = 1
                elif best_place[1] == 1:
                    table[best_place[4] + y][best_place[2]] = 1
                elif best_place[1] == 2:
                    table[best_place[4] - y][best_place[2]] = 1
                elif best_place[1] == 3:
                    table[best_place[4] - y][best_place[3]] = 1
        return False
    else:
        return True


def placing_blocks():# функция растоновки полиомино
    for block in sizes:
        if block[3] == 'l':
            for i in range(block[2]):
                if add_L(table, block[1]):
                    print("Ложь")
                    return False
        elif block[3] == 's':
            for i in range(block[2]):
                if add_square(table, block[1]):
                    print("Ложь")
                    return False
    return True
table_size = eval(input('Введите размер стола в формате(a,b):'))
square_size = eval(input('Введите тапл-пары прямоугольных полиомино в формте[((a,b),n)]:'))
L_size = eval(input('Введите тапл-пары L-полиомино в формте[((a,b),n)]:'))
# table_size = (3,5)
# square_size = [((2, 2), 1)]
# L_size = [((3, 2), 1),((2,2),2)]
sizes = []
kol_blocks = 0
for square in square_size:
    sizes.append([square[0][0] * square[0][1],(square[0][0],square[0][1]), square[1],'s'])
    kol_blocks += square[1]
for L in L_size:
    sizes.append([L[0][0] + L[0][1] - 1,(L[0][0],L[0][1]), L[1], 'l'])
    kol_blocks += L[1]
status_blocks = [0] * kol_blocks
sizes = sorted(sizes, key=lambda x: (x[0], -x[2]),reverse=True)
if check_square(square_size, table_size) or check_square(L_size, table_size) or check_sum_cells(square_size, L_size, table_size):
    print("Ложь")
else:
    table = [[0 for _ in range(table_size[0])] for _ in range(table_size[1])]
    if placing_blocks():
        print("Правда")

