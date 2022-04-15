import random
import time

board = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]


def check_horizontal():
    for row in board:
        x_count = 0
        o_count = 0
        for column in board:
            if column == "X":
                x_count += 1
            elif column == "O":
                o_count += 1
        if ((x_count) or (o_count)) == 3:
            return True

    return False


def check_vertical():
    for column in range(3):
        x_count = 0
        o_count = 0
        for row in range(3):
            if board[row][column] == "X":
                x_count += 1
            elif column == "O":
                o_count += 1
        if ((x_count) or (o_count)) == 3:
            return True

    return False


def check_diagonal():
    if (board[0][0] == "X") and (board[1][1] == "X") and (board[2][2] == "X"):
        return True
    elif (board[0][0] == "O") and (board[1][1] == "O") and (board[2][2] == "O"):
        return True
    else:
        return False


def check_available(turn, posx, posy):
    if board[posx][posy] != "?":
        space_taken = True
        while space_taken:
            if (turn % 2) == 0:
                posx = int(input("Select the row of the box 1-3: ")) - 1
                posy = int(input("Select the column of your selected position 1-3: ")) - 1
                if board[posx][posy] != "?":
                    print("Space already taken again! ")
                    continue
                else:
                    return posx, posy
            else:
                print("The computer chose a spot that's already taken! ")
                posx = random.randint(0, 2)
                posy = random.randint(0, 2)
                if board[posx][posy] != "?":
                    print("Player 2 has chosen a box which has already been taken again...")
                    continue
                else:
                    return posx, posy
    else:
        return posx, posy


def run():
    run = True
    turn = 0
    print_board(board)
    while run:
        if (turn % 2) == 0:
            print("Player 1 turn")
            posx = int(input("Select the row of the box 1-3: ")) - 1
            posy = int(input("Select the column of your selected position 1-3: ")) - 1
            while posx > 4 and posy > 4:
                print("positions cannot be any bigger than 3! \n")
                posx = int(input("Select the row of the box 1-3: ")) - 1
                posy = int(input("Select the column of your selected position 1-3: ")) - 1
            posx, posy = check_available(turn, posx, posy)
            board[posx][posy] = "X"
            print_board(board)
            if (check_horizontal() or check_vertical() or check_diagonal()) is True:
                print("Player 1 Has Won!")
                run = False
                continue
            turn += 1

        elif (turn % 2) != 0:
            print("Player 2 is choosing...\n")
            time.sleep(1)
            posx = random.randint(0, 2)
            posy = random.randint(0, 2)
            posx, posy = check_available(turn, posx, posy)
            board[posx][posy] = "O"
            print("The computer chose row ", posx, " and column ", posy)
            print_board(board)
            if (check_horizontal() or check_vertical() or check_diagonal()) is True:
                print("Player 2 Has Won :(")
                run = False
                continue
            turn += 1


def print_board(board):
    print("")
    for row in board:
        print(row)
    print("")


def main():
    while True:
        choice = input("Do you want to play [Y/N]: ").upper()
        if choice == "Y":
            run()
        elif choice == "N":
            print("Okay. Bye!")
        else:
            print("invalid input.")

main()
