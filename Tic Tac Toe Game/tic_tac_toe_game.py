board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]


def TicTacToe_draw():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print()


def Player_1():
    location = int(input("Player#1, Enter your desired board location: "))
    if board[location] != 'X' and board[location] != 'O':
        board[location] = 'X'
    else:
        print('This spot is taken, please choose somewhere else')


def Player_2():
    location = int(input("Player#2, Enter your desired board location: "))
    if board[location] != 'X' and board[location] != 'O':
        board[location] = 'O'
    else:
        print('This spot is taken, please choose somewhere else')


def Check_Winner(X_or_O):
    if board[0] == X_or_O and board[1] == X_or_O and board[2] == X_or_O:
        return True
    if board[3] == X_or_O and board[4] == X_or_O and board[5] == X_or_O:
        return True
    if board[6] == X_or_O and board[7] == X_or_O and board[8] == X_or_O:
        return True
    if board[0] == X_or_O and board[3] == X_or_O and board[6] == X_or_O:
        return True
    if board[1] == X_or_O and board[4] == X_or_O and board[7] == X_or_O:
        return True
    if board[2] == X_or_O and board[5] == X_or_O and board[8] == X_or_O:
        return True

    # Diagonal terms
    if board[0] == X_or_O and board[4] == X_or_O and board[8] == X_or_O:
        return True
    if board[2] == X_or_O and board[4] == X_or_O and board[6] == X_or_O:
        return True


while True:
    Player_1()
    TicTacToe_draw()
    if Check_Winner('X'):
        print("Player #1 Wins")
        break;

    Player_2()
    TicTacToe_draw()
    if Check_Winner('O'):
        print("Player #2 Wins")
        break;