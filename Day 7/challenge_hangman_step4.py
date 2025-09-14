import random

from hangman_art import stages, logo
from hangman_words import word_list

print(logo)



#todo1: - Create a variable called lives to keep track of the number of lives left. Set it to 6.
lives = 6



#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)  # For testing purposes, to see the chosen word

#create a "placeholder" with the same number of letters as the chosen_word and assign it to a variable called display. For example, if the chosen_word has 5 letters, display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
placeholder = ""
for _ in chosen_word:
    placeholder += "_"

print(placeholder)  # For testing purposes, to see the placeholder string

display = placeholder  # Assign the placeholder string to display variable


#use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and display has no more "_" left. Then you can tell the user they've won.
game_over = False
while not game_over:
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    print(f"You guessed: {guess}")  # For testing purposes, to see the guessed letter

    #change the for loop so that you keep track of the position of each letter. You'll need the range function for that.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display = display[:i] + guess + display[i+1:]

    #todo 2: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("You've run out of lives. Game over.")
        print(stages[lives])  # Print the current stage of the hangman

    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if "_" not in display:
        game_over = True
        print("Congratulations! You've guessed the word!")
    
    print(display)  # For testing purposes, to see the updated display list
