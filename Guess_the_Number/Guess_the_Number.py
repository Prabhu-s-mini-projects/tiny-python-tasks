import Guess_the_number_database as Db
import random

print(Db.logo)

print(" Welcome to Guess the Number Game \n")
difficulty_level = input("\n Choose the difficulty Level: \n'Easy'\n'Medium'\n'Hard'\n").lower()
print(" I'm thinking of a number between 1 and 10.\n")

attempts = Db.number_of_attempts.get(difficulty_level)
is_user_found = False
number = random.choice(range(1, 100))

while attempts > 0 and not is_user_found:

    guessed_number = int(input("\nYou Guess the Number:\t"))
    if guessed_number < number:
        print("Too low \n Guess again")
        attempts -= 1
    elif guessed_number > number:
        print("Too High \n Guess again")
        attempts -= 1
    else:
        print(f"You have found the number : {number}")
        is_user_found = True

if not is_user_found:
    print(f"Ran out of lives : number is  {number}")
