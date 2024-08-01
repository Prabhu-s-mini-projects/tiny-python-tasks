# Password Generator

import random

#DB
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(f"\nWelcome to Password Generator\n")

number_of_letters = int(input("How many letters you would like in Password?\n"))
number_of_symbols = int(input("How many symbols you would like in password?\n"))
number_of_numbers = int(input("How many numbers you would like in password?\n"))
easy_or_hard = input("Would you like a simple password or complex? \n Type \n'S' for simple.\n'C' for complex.\n").lower()

password = ''
if easy_or_hard == 's':
    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    for letter in range(0,number_of_letters):
        password += str(letters[random.randint(0,len(letters))])
    for symbol in range(0, number_of_symbols):
        password += str(symbols[random.randint(0, len(symbols))])
    for number in range(0, number_of_numbers):
        password += str(numbers[random.randint(0, len(numbers))])

elif easy_or_hard == 'c':
    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    combined_characters = letters.copy()
    combined_characters.extend(symbols)
    combined_characters.extend(numbers)
    for character in range(0, (number_of_numbers+number_of_letters+number_of_symbols + 1)):
        password += str(combined_characters[random.randint(0, len(combined_characters))])
else:
    print("\nEnter a valid letter S or C only\n")

print(f'Here is your Password: {password}')
