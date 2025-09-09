# #greetings for the game of rock paper scissors
# print("Welcome to the Rock, Paper, Scissors game!")

# list_of_choices = ["Rock", "Paper", "Scissors"]

# user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
# user_choice = int(user_choice)
# print(f"You chose: {list_of_choices[user_choice]}")
# import random
# computer_choice = random.randint(0, 2)
# print(f"Computer chose: {list_of_choices[computer_choice]}")
# if user_choice >= 3 or user_choice < 0:
#     print(f"you typed an invalid number {user_choice}, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
#     print(f"{list_of_choices[user_choice]} beats {list_of_choices[computer_choice]}")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
#     print(f"{list_of_choices[computer_choice]} beats {list_of_choices[user_choice]}")
# elif computer_choice == user_choice:
#     print("It's a draw!")
#     print(f"Both chose {list_of_choices[user_choice]}")
# elif computer_choice > user_choice:
#     print("You lose!")
#     print(f"{list_of_choices[computer_choice]} beats {list_of_choices[user_choice]}")
# elif user_choice > computer_choice:
#     print("You win!")
#     print(f"{list_of_choices[user_choice]} beats {list_of_choices[computer_choice]}")

import random

# Official WRPSA rules
RULES = {
    'rock':     {'beats': 'scissors', 'loses': 'paper'},
    'paper':    {'beats': 'rock',     'loses': 'scissors'},
    'scissors': {'beats': 'paper',    'loses': 'rock'}
}

# List of valid moves
MOVES = list(RULES.keys())

# Function to decide the winner's
'''
Compares the player's choice with the computer's choice
and prints the result.
'''
def decide_winner(player, computer):
    if player == computer:
        print(f"Both chose {player}. It's a tie!")
    elif RULES[player]['beats'] == computer:
        print(f"You win! {player.capitalize()} beats {computer}.")
        print(f"{player} -> {computer}")
        print("******" * 3)
    else:
        print(f"You lose! {computer.capitalize()} beats {player}.")
        print("******" * 3)

# Function to play a round of the game
'''
Prompts the player for their move, generates the computer's move,
and determines the winner.
'''
def play_round():
    player = input(f"Choose your move ({', '.join(MOVES)}): ").strip().lower()
    if player not in MOVES:
        print("Invalid move. Try again.")
        return play_round()
    computer = random.choice(MOVES)
    print(f"Computer chose: {computer}")
    decide_winner(player, computer)

# Main game loop
if __name__ == "__main__":
    try:
        while True:
            print("Welcome to the Rock, Paper, Scissors game!")
            print("******" * 3)
            if input("Do you want to play a round? (yes/no): ").strip().lower() != 'yes':
                print("Thanks for playing! Goodbye!")
                print("******" * 3)
                break
            play_round()
        

    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")