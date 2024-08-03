import random
import hangman_words as word_db
import hangman_art as art

print(art.logo)
print('\n\n Welcome to HANGMAN GAME \n\n')


# Selecting the word for the GAME from the list
word = random.choice(word_db.word_list).lower()

guess_word = []
# Creating a Blanks according to length of the string.
for _ in range(len(word)):
    guess_word.append('_')

lives = 7
while lives > 0 and '_' in guess_word:
    print(' '.join(guess_word))
    guessed_letter = input('\nGuess the letter:\t').lower()
    if guessed_letter in word:
        if guessed_letter in guess_word:
            print(f'\nYou\'ve already entered the letter: {guessed_letter}')
        else:
            for position in range(len(word)):
                if guessed_letter == word[position]:
                    guess_word[position] = guessed_letter
    else:
        lives -= 1
        print(f'\n Remaining lives : {lives}')
        print(art.stages[lives])

if '_' not in guess_word:
    print('\nYou SAVED the person')
else:
    print(f"\n\nGAME OVER\n\n Word is: {word.upper()}")
