def start():
    print("Крестики - нолики")
    print("")
    ig1 = input("Введите имя Игрока 1:")
    ig2 = input("Введите имя Игрока 2:")
    return ig1, ig2


def tabl():
    print()
    print("   | 0 | 1 | 2 ")
    print("---------------")
    for i, row in enumerate(pole):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def hod():
    while True:
        mesto = input("Ходите:").split()

        if len(mesto) != 2:
            print(" Введите обе координаты: ")
            continue

        a, b = mesto

        if not (a.isdigit()) or not (b.isdigit()):
            print("Введите кординаты хода:")
            continue

        a, b = int(a), int(b)

        if 0 > a or a > 2 or 0 > b or b > 2:
            print("Координаты от 0 до 2")
            continue

        if pole[a][b] != " ":
            print("Место уже занято")
            continue

        return a, b


def proverka():
    pobeda = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for mesto in pobeda:
        symbols = []
        for c in mesto:
            symbols.append(pole[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Победил", ig1)
            return True
        if symbols == ["0", "0", "0"]:
            print("Победил", ig2)
            return True
    return False


ig1, ig2 = start()
pole = [[" "] * 3 for i in range(3) ]
per = 0
while True:
    per += 1
    tabl()
    if per % 2 == 1:
        print("Ходит", ig1)
    else:
        print("Ходит", ig2)

    a , b = hod()

    if per % 2 == 1:
        pole[a][b] = "X"
    else:
        pole[a][b] = "0"

    if proverka():
        break

    if per == 9:
        print(" Ничья ")
        break
