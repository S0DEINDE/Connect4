import random


def display(rows, cols, board):
    print("\n     A    B    C    D    E    F    G  ", end="")
    for liner in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(liner, " |", end="")
        for linux in range(cols):
            if board[liner][linux] == "🔵":
                print("", board[liner][linux], end=" |")
            elif board[liner][linux] == "🔴":
                print("", board[liner][linux], end=" |")
            else:
                print(" ", board[liner][linux], end="  |")
    print("\n   +----+----+----+----+----+----+----+")


def mod_structure(picker, turn, board):
    board[picker[0]][picker[1]] = turn


def winner(chip, rows, cols, game):
    for y in range(rows):
        for x in range(cols - 3):
            if game[x][y] == chip and game[x + 1][y] == chip and game[x + 2][y] == chip and game[x-1][y] == chip:
                print("\nGame over", chip, "wins! Thanks for playing C-4 :p")
                return True

    for x in range(rows):
        for y in range(cols - 3):
            if game[x][y] == chip and game[x][y + 1] == chip and game[x][y + 2] == chip and game[x][y + 3] == chip:
                print("\nGame over", chip, "wins! Thanks for playing C-4 :P")
                return True

    for x in range(rows - 3):
        for y in range(3, cols):
            if game[x][y] == chip and game[x + 1][y - 1] == chip and game[x + 2][y - 2] == chip and \
                    game[x + 3][y - 3] == chip:
                print("\nGame over", chip, "wins! Thanks for playing C-4 :p")
                return True

    for x in range(rows - 3):
        for y in range(cols - 3):
            if game[x][y] == chip and game[x + 1][y + 1] == chip and game[x + 2][y + 2] == chip and \
                    game[x + 3][y + 3] == chip:
                print("\nGame over", chip, "wins! Thanks for playing C-4 :p")
                return True
    return False


def coordinate(user):
    coord = [None] * 2
    if user[0] == "A":
        coord[1] = 0
    elif user[0] == "B":
        coord[1] = 1
    elif user[0] == "C":
        coord[1] = 2
    elif user[0] == "D":
        coord[1] = 3
    elif user[0] == "E":
        coord[1] = 4
    elif user[0] == "F":
        coord[1] = 5
    elif user[0] == "G":
        coord[1] = 6
    else:
        print("Sorry, try again!")
    coord[0] = int(user[1])
    return coord


def available(intended, board):
    if board[intended[0]][intended[1]] == '🔴':
        return False
    elif board[intended[0]][intended[1]] == '🔵':
        return False
    else:
        return True


def gravity(intended, board):
    below = [None] * 2
    below[0] = intended[0] + 1
    below[1] = intended[1]

    if below[0] == 6:
        return True

    if available(below, board) is False:
        return True

    return False


# noinspection PyUnresolvedReferences
def main():
    print("~~~~~~~~~~~~~~~~~~~~~ Welcome To ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CONNECT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FOUR!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    letters = ["A", "B", "C", "D", "E", "F", "G"]
    board = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]

    rows = 6
    cols = 7

    leave_loop = False
    t_cnt = 0
    while leave_loop is False:
        if t_cnt % 2 == 0:
            display(rows, cols, board)
            while True:
                picker = input("\nChoose a spot: ")
                coor = coordinate(picker)
                try:
                    if available(coor, board) and gravity(coor, board):
                        mod_structure(coor, '🔵', board)
                        break
                    else:
                        print("Sorry, that's wrong!")
                except:
                    print("User Error! Please try again:")
            t_cnt += 1
            win = winner('🔵', rows, cols, board)
        else:
            while True:
                cpu = [random.choice(letters), random.randint(0, 5)]
                cpu_coord = coordinate(cpu)
                if available(cpu_coord, board) and gravity(cpu_coord, board):
                    mod_structure(cpu_coord, '🔴', board)
                    break
            t_cnt += 1
            win = winner('🔴', rows, cols, board)

        if win:
            display(rows, cols, board)
            break

        print("~~~~~ THANKS FOR USING MY PROGRAM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()


main()
