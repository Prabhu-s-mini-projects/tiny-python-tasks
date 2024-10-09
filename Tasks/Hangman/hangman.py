"""Main script of HANGMAN Game"""

import random

import hangman_art as art
import hangman_words as word_db

# Starting the GAME and Loading the data from Database (db)
print(art.LOGO)
print('\n\n Welcome to HANGMAN GAME \n\n')


# Selecting the word for the GAME from the list
word = random.choice(word_db.WORDS).lower()

guess_word = []
# Creating a Blanks according to length of the string.
for _ in range(len(word)):
    guess_word.append('_')

level = input('Please choose the difficultly level:"EASY" or "MEDIUM" or "HARD\n').lower()
while level not in art.LIVES_FOR_EACH_LEVEL:
    print(f"You've invalid value : {level}.")
    level = input('Please choose the difficultly level:"EASY" or "MEDIUM" or "HARD\n').lower()

# Defining lives based on difficultly choose by player.
lives = art.LIVES_FOR_EACH_LEVEL.get(level)

# To keep the game running until ran out of lives or all the letters are found.
while lives > 0 and '_' in guess_word:
    print(' '.join(guess_word))
    # Get user input.
    guessed_letter = input('\nGuess the letter:\t').lower()
    if guessed_letter in word:
        if guessed_letter in guess_word:
            print(f'\nYou\'ve already entered the letter: {guessed_letter}')
        else:
            # To track the position of the letter and to handle different occurrence of same letter
            for position, letter in enumerate(word):
                # Look for the letter. If Yes, Replace the letter in same position at Guessed_letter
                if guessed_letter == word[position]:
                    guess_word[position] = guessed_letter
                    print(f"{ letter = } ")
                    
    else:
        lives -= 1
        print(f'\n Remaining lives : {lives}')
        print(art.STAGES[lives])

if '_' not in guess_word:
    print('\nYou SAVED the person')
else:
    print(f"\n\nGAME OVER\n\n Word is: {word.upper()}")
