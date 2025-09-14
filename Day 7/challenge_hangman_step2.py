import random

# Word list for the game
word_list = ["python", "hangman", "challenge", "programming", "developer"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)  # For testing purposes, to see the chosen word

#todo-1: create a "placeholder" with the same number of letters as the chosen_word and assign it to a variable called display. For example, if the chosen_word has 5 letters, display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
placeholder = ""
for _ in chosen_word:
    placeholder += "_"

print(placeholder)  # For testing purposes, to see the placeholder string

display = placeholder  # Assign the placeholder string to display variable


#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#print(f"You guessed: {guess}")  # For testing purposes, to see the guessed letter#

#todo-2: Update the display variable with the correctly guessed letter.
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display = display[:i] + guess + display[i+1:]

print(display)  # For testing purposes, to see the updated display list
