""" Password Generator """

import random

from Tasks.Password_Manager.Controller.password_generator import LETTERS, NUMBERS, SYMBOLS


def main()->None:
    """Generates new password"""
    #DB
    letters = LETTERS
    numbers = NUMBERS
    symbols = SYMBOLS

    print("\nWelcome to Password Generator\n")

    number_of_letters = int(input("How many letters "
                                  "you would like in Password?\n"))
    number_of_symbols = int(input("How many symbols "
                                  "you would like in password?\n"))
    number_of_numbers = int(input("How many numbers "
                                  "you would like in password?\n"))
    easy_or_hard = input("Would you like a simple password or complex?"
                         " \n Type \n'any key' for simple."
                         "\n'C' for complex.\n").lower()


    character_list = []
    for _ in range(0, number_of_letters):
        character_list += random.choice(letters)
    for _ in range(0, number_of_symbols):
        character_list += random.choice(symbols)
    for _ in range(0, number_of_numbers):
        character_list += random.choice(numbers)

    if easy_or_hard == 'C':
        # Hard Level - Order of characters randomised:
        # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
        random.shuffle(character_list)

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    # No need for additional code.
    # Above condition Will fail and appends all characters in the same order

    # Covert list into string
    password = ''.join(character_list)

    print(f'Here is your Password: {password}')

if __name__ == '__main__':
    main()
