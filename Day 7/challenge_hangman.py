import random

# Word list for the game
word_list = ["python", "hangman", "challenge", "programming", "developer"]

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Display setup
display = ["_"] * word_length
lives = 6

print("Welcome to Hangman!")

# Main game loop
while "_" in display and lives > 0:
    print(f"\n{' '.join(display)}")
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed '{guess}'.")

    # Check guessed letter
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Wrong guess! You lose a life. Lives left: {lives}")

# End of game
if "_" not in display:
    print(f"\n{' '.join(display)}")
    print("Congratulations! You guessed the word!")
else:
    print(f"\nYou ran out of lives. The word was '{chosen_word}'. Better luck next time!")