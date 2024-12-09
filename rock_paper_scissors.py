import random
from colorama import Fore
player_score = 0
computer_score = 0

while True:
    player_move = input(Fore.GREEN + "Choose [r]ock, [p]aper, or [s]cissors: ").lower()

    if player_move == "r":
        player_move = "rock"
    elif player_move == "p":
        player_move = "paper"
    elif player_move == "s":
        player_move = "scissors"
    else:
        raise SystemExit("Invalid input. Exiting the game.")

    moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves)
    print(Fore.WHITE + f"The computer chose {computer_move}.")

    if player_move == computer_move:
        print("It's a draw!")
    elif (player_move == "rock" and computer_move == "scissors") or \
            (player_move == "scissors" and computer_move == "paper") or \
            (player_move == "paper" and computer_move == "rock"):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(Fore.BLUE + f"Score -> Player: {player_score}, Computer: {computer_score}")

    play_again = input(Fore.RED + "Do you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        continue
    elif play_again == "no":
        print("Thanks for playing!")
        break
    else:
        raise SystemExit("Invalid input. Exiting the game.")
