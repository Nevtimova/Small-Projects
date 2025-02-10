import numpy as np

ROWS = 6
COLS = 7


class ConnectFour:
    def __init__(self):
        self.board = np.zeros((ROWS, COLS), dtype=int)
        self.current_player = 1

    def print_board(self):
        print(np.flip(self.board, 0))

    def drop_piece(self, col):
        if col < 0 or col >= COLS or self.board[ROWS - 1][col] != 0:
            print("Invalid move. Try again.")
            return False
        for row in range(ROWS):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                return True
        return False

    def check_winner(self):
        for row in range(ROWS):
            for col in range(COLS - 3):
                if self.board[row][col] == self.current_player and all(
                        self.board[row][col + i] == self.current_player for i in range(4)):
                    return True

        for row in range(ROWS - 3):
            for col in range(COLS):
                if self.board[row][col] == self.current_player and all(
                        self.board[row + i][col] == self.current_player for i in range(4)):
                    return True

        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if self.board[row][col] == self.current_player and all(
                        self.board[row + i][col + i] == self.current_player for i in range(4)):
                    return True

        for row in range(3, ROWS):
            for col in range(COLS - 3):
                if self.board[row][col] == self.current_player and all(
                        self.board[row - i][col + i] == self.current_player for i in range(4)):
                    return True
        return False

    def switch_player(self):
        self.current_player = 3 - self.current_player

    def reset_game(self):
        self.board = np.zeros((ROWS, COLS), dtype=int)
        self.current_player = 1

    def play(self):
        while True:
            self.print_board()
            try:
                col = int(input(f"Player {self.current_player}, choose a column (0-{COLS - 1}): "))
                if self.drop_piece(col):
                    if self.check_winner():
                        self.print_board()
                        print(f"Player {self.current_player} wins!")
                        break
                    self.switch_player()
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    game = ConnectFour()
    game.play()
