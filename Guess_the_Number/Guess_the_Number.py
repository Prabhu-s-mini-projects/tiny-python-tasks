import Guess_the_number_database as Db
import random

print(Db.logo)

print(" Welcome to Guess the Number Game \n")
difficulty_level = input("\n Choose the difficulty Level: \n'Easy'\n'Medium'\n'Hard'\n").lower()
print(" I'm thinking of a number between 1 and 10.\n")

# Fetch it from Db
attempts = Db.number_of_attempts.get(difficulty_level)

# Computer will decide the number
number = random.choice(range(1, 100))

is_user_found = False  # To keep track whether user found the value.
while attempts > 0 and not is_user_found:

    guessed_number = int(input("\nYou Guess the Number:\t"))
    if guessed_number < number:
        print("Too low \nGuess again")
        attempts -= 1
    elif guessed_number > number:
        print("Too High \nGuess again")
        attempts -= 1
    else:
        print(f"You have found the number : {number}")
        is_user_found = True

if not is_user_found:
    print(f"Ran out of lives : number is  {number}")
