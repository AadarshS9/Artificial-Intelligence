#Q10)Connect Four Game
import numpy as np
import random

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)
        self.computer = 1

    def move(self, piece, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = piece
                break

    def is_column_full(self, col):
        return self.board[0][col] != 0

    def check_win(self, piece):
        # Check rows
        for row in self.board:
            for i in range(len(row) - 3):
                if all(cell == piece for cell in row[i:i+4]):
                    return True

        # Check columns
        for col in range(7):
            for i in range(len(self.board) - 3):
                if all(self.board[i+k][col] == piece for k in range(4)):
                    return True

        # Check diagonals
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == piece and self.board[i+1][j+1] == piece and \
                   self.board[i+2][j+2] == piece and self.board[i+3][j+3] == piece:
                    return True
                if self.board[i][j+3] == piece and self.board[i+1][j+2] == piece and \
                   self.board[i+2][j+1] == piece and self.board[i+3][j] == piece:
                    return True

        return False

    def print_board(self):
        for row in self.board:
            print(" ".join(map(str, row)))
        print("\n")
        #0print("1 2 3 4 5 6 7\n")

    def play(self):
        while True:
            self.print_board()
            col = -1
            while col < 0 or col > 6 or self.is_column_full(col):
                col = int(input("Enter column number (1-7): ")) - 1
                if self.is_column_full(col):
                    print("Column is full. Choose another column.")
            print("Your move:")
            self.move(2, col)  # Human's turn
            if self.check_win(2):
                self.print_board()
                print("You win!")
                break
            self.print_board()
            col = random.randint(0, 6)
            while self.is_column_full(col):
                col = random.randint(0, 6)
            print("Computer's move:")
            self.move(1, col)  # Computer's turn
            if self.check_win(1):
                self.print_board()
                print("Computer wins!")
                break

game = ConnectFour()
game.play()
