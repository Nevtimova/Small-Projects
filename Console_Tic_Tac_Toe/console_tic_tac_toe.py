import math


def tic_tac_toe():
    player_one, player_two = None, None
    board = [" "] * 9
    loop = True

    def setup():
        nonlocal player_one, player_two
        player_one = [input("Enter player one name: "), input("Choose X or O: ")]
        player_two = [input("Enter player two name: "), "O" if player_one[1] == "X" else "X"]
        print(f"{player_one[0]} is {player_one[1]}, {player_two[0]} is {player_two[1]}")

    def draw_board():
        for i in range(0, 9, 3):
            print(" | ".join(board[i:i + 3]))
            if i < 6:
                print("--+---+--")

    def check_if_won(player):
        nonlocal loop
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        if any(board[a] == board[b] == board[c] == player[1] for a, b, c in win_conditions):
            print(f"{player[0]} wins!")
            loop = False

    def play():
        nonlocal loop
        current, other = player_one, player_two
        while loop:
            try:
                move = int(input(f"{current[0]}, choose a position (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = current[1]
                    draw_board()
                    check_if_won(current)
                    current, other = other, current
                else:
                    print("Invalid move, try again.")
            except (ValueError, IndexError):
                print("Choose a valid number between 1 and 9.")

    setup()
    draw_board()
    play()

# Uncomment to play:
# tic_tac_toe()
