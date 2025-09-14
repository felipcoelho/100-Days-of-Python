import random

# Word list for the game
word_list = ["python", "hangman", "challenge", "programming", "developer"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)  # For testing purposes, to see the chosen word

#create a "placeholder" with the same number of letters as the chosen_word and assign it to a variable called display. For example, if the chosen_word has 5 letters, display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
placeholder = ""
for _ in chosen_word:
    placeholder += "_"

print(placeholder)  # For testing purposes, to see the placeholder string

display = placeholder  # Assign the placeholder string to display variable


#todo-1: use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and display has no more "_" left. Then you can tell the user they've won.
game_over = False
while not game_over:
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    print(f"You guessed: {guess}")  # For testing purposes, to see the guessed letter

    #todo-2: change the for loop so that you keep track of the position of each letter. You'll need the range function for that.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display = display[:i] + guess + display[i+1:]

    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if "_" not in display:
        game_over = True
        print("Congratulations! You've guessed the word!")
    
    print(display)  # For testing purposes, to see the updated display list
