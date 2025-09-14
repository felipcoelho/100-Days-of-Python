import random

# Word list for the game
word_list = ["python", "hangman", "challenge", "programming", "developer"]

#todo-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#print(chosen_word)  # For testing purposes, to see the chosen word


#todo-2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#print(f"You guessed: {guess}")  # For testing purposes, to see the guessed letter#

#todo-3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")