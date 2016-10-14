read = [[0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0 / empty line
        [0, 0, 1, 0, 0, 0, 0, 0, 0],  # 1     /lines where blocks are generated on
        [0, 0, 1, 1, 0, 0, 0, 0, 0],  # 2     /
        [0, 0, 1, 0, 0, 0, 0, 0, 0],  # 3     /
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4     /
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5 / last line of game
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 14
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 15
        [1, 1, 1, 1, 1, 1, 1, 1, 1]]  # 16 / rida mis on koguaeg täis selleks, et programm saaks aru kus on alumine piir


def alla(andmed, x, y):
    andmed[x + 1][y] = andmed[x][y]
    andmed[x][y] = 0

    return andmed


def kuubik_alla(andmed, x1, y1, x2, y2, x3, y3, x4, y4):
    while not (andmed[x1 + 1][y1] == 1 or andmed[x2 + 1][y2] == 1):
        andmed = alla(andmed, x1, y1)
        x1 += 1

        andmed = alla(andmed, x2, y2)
        x2 += 1

        andmed = alla(andmed, x3, y3)
        x3 += 1

        andmed = alla(andmed, x4, y4)
        x4 += 1

    return andmed


def uus_read(andmed, x1, y1, x2, y2, x3, y3, x4, y4):
    andmed_uus = andmed
    andmed_uus[x1][y1] = 1
    andmed_uus[x2][y2] = 1
    andmed_uus[x3][y3] = 1
    andmed_uus[x4][y4] = 1

    return andmed_uus

read1 = kuubik_alla(read, 3, 2, 2, 3, 2, 2, 1, 2)

uus = uus_read(read1, 3, 3, 3, 4, 2, 3, 1, 3)
print(uus)
read2 = kuubik_alla(uus, 3, 3, 3, 4, 2, 3, 1, 3)
print(read2)
