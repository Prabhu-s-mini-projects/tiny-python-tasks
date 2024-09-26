""" Password Generator """

import random

def main()->None:
    """Generates new password"""
    #DB
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

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
    for letter in range(0, number_of_letters):
        character_list += random.choice(letters)
    for symbol in range(0, number_of_symbols):
        character_list += random.choice(symbols)
    for number in range(0, number_of_numbers):
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
