import random  # Import the random module to generate random choices for the computer.
from colorama import Fore  # Import Fore from colorama for colored text in the terminal.

# Initialize the scores for the player and the computer.
player_score = 0
computer_score = 0

# Infinite loop to keep the game running until the user decides to quit.
while True:
    # Prompt the user to choose rock, paper, or scissors, with green-colored text.
    player_move = input(Fore.GREEN + "Choose [r]ock, [p]aper, or [s]cissors: ").lower()

    # Map the user's shorthand input to the full word (e.g., 'r' -> 'rock').
    if player_move == "r":
        player_move = "rock"
    elif player_move == "p":
        player_move = "paper"
    elif player_move == "s":
        player_move = "scissors"
    else:
        # Exit the program if the user enters an invalid input.
        raise SystemExit("Invalid input. Exiting the game.")

    # Define the possible moves for the computer.
    moves = ["rock", "paper", "scissors"]

    # Randomly select one of the moves for the computer.
    computer_move = random.choice(moves)

    # Display the computer's choice in white-colored text.
    print(Fore.WHITE + f"The computer chose {computer_move}.")

    # Determine the outcome of the game.
    if player_move == computer_move:
        # If both moves are the same, it's a draw.
        print("It's a draw!")
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "scissors" and computer_move == "paper") or \
         (player_move == "paper" and computer_move == "rock"):
        # Check all winning conditions for the player.
        print("You win!")
        player_score += 1  # Increment the player's score.
    else:
        # If none of the above conditions are met, the player loses.
        print("You lose!")
        computer_score += 1  # Increment the computer's score.

    # Display the current scores in blue-colored text.
    print(Fore.BLUE + f"Score -> Player: {player_score}, Computer: {computer_score}")

    # Ask the user if they want to play again, with red-colored text.
    play_again = input(Fore.RED + "Do you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        # If the user wants to play again, the loop continues.
        continue
    elif play_again == "no":
        # If the user doesn't want to play again, thank them and exit the loop.
        print("Thanks for playing!")
        break
    else:
        # Exit the program if the user enters an invalid input at this stage.
        raise SystemExit("Invalid input. Exiting the game.")
