class Game:

    def __init__(self):
        self.board = [0, 1, 2,
                      3, 4, 5,
                      6, 7, 8]

    def TicTacToe_draw(self):
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print()

    def Player_1(self):
        location = int(input("Player 1, Enter your desired board location:"))
        if self.board[location] != "X" and self.board[location] != "O":
            self.board[location] = "X"
        else:
            print("This spot is taken, please choose somewhere else.")

    def Player_2(self):
        location = int(input("Player 2, Enter your desired board location: "))
        if self.board[location] != "X" and self.board[location] != "O":
            self.board[location] = "O"
        else:
            print("This spot is taken, please choose somewhere else.")

        # Check if any player wins!

    def Check_Winner(self, x_or_o):
        # Row
        if self.board[0] == x_or_o and self.board[1] == x_or_o and self.board[2] == x_or_o:
            return True
        if self.board[3] == x_or_o and self.board[4] == x_or_o and self.board[5] == x_or_o:
            return True
        if self.board[6] == x_or_o and self.board[7] == x_or_o and self.board[8] == x_or_o:
            return True

        # Column
        if self.board[0] == x_or_o and self.board[3] == x_or_o and self.board[6] == x_or_o:
            return True
        if self.board[1] == x_or_o and self.board[4] == x_or_o and self.board[7] == x_or_o:
            return True
        if self.board[2] == x_or_o and self.board[5] == x_or_o and self.board[8] == x_or_o:
            return True

        # Diagonal
        if self.board[0] == self.x_or_o and self.board[4] == self.x_or_o and self.board[8] == self.x_or_o:
            return True
        if self.board[2] == self.x_or_o and self.board[4] == self.x_or_o and self.board[6] == self.x_or_o:
            return True


play_game = Game()


def Play_Game():
    while True:
        Game.Player_1()
        Game.TicTacToe_draw()
        if Game.Check_Winner("X"):
            print("Player 1 Wins")
            break;

        Game.Player_2()
        Game.TicTacToe_draw()
        if Game.Check_Winner("O"):
            print("Player 2 Wins")
            break;
