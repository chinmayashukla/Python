import random
import hangman_art
import hangman_words


def win():
    """If the user wins, the function will be called to congratulate the user"""
    print(f"The word has been identified: {guesing_word}\nCongratulations - You Win")
    exit()


def lose():
    """If the user loses, the function will be called to inform the user for the loss"""
    print("Sorry, you have no attempts left - you loose")
    print(f"The answer was: {guesing_word}")
    exit()


print(hangman_art.logo) #printing the ASCII art
guessing_word_list = random.choice(hangman_words.word_list) # getting a random word from the list of words
guesing_word = guessing_word_list #making a another copy of the list which will be used to display progress as the user starts entering the guesses
guess_list = list(guesing_word) 
word_length = len(guess_list)
display_list = []
missed_letters = []
attempts = 7

for i in range(0, word_length): #changing the list to underscores for initial display
    display_list.append("_")

while attempts != 0:
    scr_input = input("Please enter your guess:\n").lower() 
    #additional checks to be implemented to ensure it is a single character and not a word which is being entered
    if scr_input in guess_list:
        for i in range(0, word_length):
            if scr_input == guess_list[i]:
                display_list[i] = scr_input
        if "_" not in display_list:
            win()
    else:
        attempts -= 1
        missed_letters.append(scr_input)
        print("You missed - a life has been deducted")
        print(hangman_art.stages[attempts])
        if attempts == 0:
            lose()
    print(f"Current Word Status: {display_list}")
    print(f"Missed Letters = {missed_letters}\nAttempts remaining = {attempts}")
