# """"""
# File: Word_Game.
# Author: Alejandro Malvacias

# """"""

#First section of the program.
play_again = "yes"

while play_again.lower() == "yes":
    #I decide to use a while loop to play the game the times as you want.
    word = "yoda"
    counter = 0 
    guess = ""
    word_length = len(word)

    #I decided to be creative putting "yoda" in the word, its my favorite character of star wars.

    #Second section of the program.

    print("Welcome to the wordle game!")
    print("")
    print ("Guess the secret word! Here is a hint:")

    for i in range(word_length):
        print("_", end=" ")

    while guess.lower() != word.lower():
        counter += 1
        guess = input("\nWhat do you think the secret word is? ")
        guess_length = len(guess)  
        hint = ""
        #I created a hint for each letter in the secret word.

        if guess_length != word_length:
            print ("Sorry, the guess must have the same number of letters as the secret word.")
        else:
            for i, letter in enumerate(guess):
                if letter == word[i]:
                    hint += letter.upper()
                else:
                    hint += "_"
            print(hint)
            #The variable "hint" is used to print the hint, and also going to display the underscore.

    print("Congratulations! You guessed the secret word in", counter, "guesses!")
    play_again = input("Do you want to play again? (yes or no): ")
    if play_again.lower() == "no":
        print("Thanks for playing!")

