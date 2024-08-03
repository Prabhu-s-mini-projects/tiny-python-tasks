import random
import hangman_words as word_db
import hangman_art as art

print(art.logo)
print('\n\n Welcome to HANGMAN GAME \n\n')


# Selecting the word for the GAME from the list
word = random.choice(word_db.word_list)

guess_word = []
# Appending _ to the length of the string.
for i in range(len(word)):
    guess_word.append('_')

lives = 7
while lives > 0 and '_' in guess_word:
    print(' '.join(guess_word))
    guessed_letter = input('\nGuess the letter:\t')
    if guessed_letter in word:
        if guessed_letter in guess_word:
            print(f'\nYou\'ve already entered the letter: {guessed_letter}')
        else:
            index = 0 # to track the same letter in multiple positions.
            for character in word:
                if guessed_letter == character:
                    guess_word[index] = guessed_letter
                index += 1
    else:
        lives -= 1
        print(f'\n Remaining lives : {lives}')
        print(art.stages[lives])

if '_' not  in guess_word:
    print('\nYou SAVED the person')
else:
    print("\n\nGAME OVER\n")


