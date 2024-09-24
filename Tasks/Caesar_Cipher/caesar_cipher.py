""" Contains the resources need for the caesar cipher"""

import db_art_alphabet as db

# Starting GAME and load the Database(db
print(db.LOGO)
ALPHABET = db.ALPHABET

def caesar(text, shift, direction) -> str:
    """
    # Step by step break down for understanding
    #   1. alphabet[x] to get the encode/decrypt letter; X represents a new index after the shit.
    #   2. X = alphabet.index(letter) --> get the index of current letter to add it with shift.
    #   3. Shift --> should add for encoding and subtract for decrypt.
    #   4. if/else condition to handle below scenarios
    #     1. if the current index - shift goes below 0 during decrypt.
                add 26 (handled using overflow and shift)
    #     2. if the current Index + shift goes above 26 durin encoding
                sub 26 (handled using overflow and shift)
    """
    cipher_text = ''
    over_flow = 1
    if direction == 'encode':
        over_flow *= -1
    elif direction == 'decrypt':
        shift *= -1
    else:
        print(f"Type 'encode' to encrypt, type 'decode' to decrypt. not: {direction}")
    for letter in text:
        if letter in ALPHABET:
            cipher_text += ALPHABET[ALPHABET.index(letter) + shift
                            if 0 < ALPHABET.index(letter) + shift < 26
                            else (ALPHABET.index(letter) + shift + 26 * over_flow)]
        else:
            cipher_text += letter
    return cipher_text

def main()-> None:
    """
    Methods keeps the program running
    :return:
    """

    # To keep the loop running until user enter it as NO
    is_continue = 'yes'
    while is_continue == 'yes':

        # Getting User Inputs
        en_or_de = input("\nType 'encode' to encrypt, type 'decode' to decrypt:").lower()
        message_text = input("Type your message: ").lower()
        to_shift = int(input("Type the shift number: "))

        # To handle the scenario: Where user added the shift higher than 26.
        if to_shift > 26:
            to_shift %= 26  # storing the remainder.

        print(caesar(message_text, to_shift, en_or_de))
        is_continue = input('Want to restart the cipher program:\t').lower()

if __name__ == "__main__":
    main()

# _____________________________________________________________________________________________________________________
#
#  Alter NOT effective METHOD (scratch Code)
# _____________________________________________________________________________________________________________________
#
# def encrypt(text, shift) -> str:
#     cipher_text = ''
#     for letter in text:
#         cipher_text += alphabet[alphabet.index(letter) + shift
#         if alphabet.index(letter) + shift < 26
#         else (
#                 alphabet.index(letter) + shift - 26)]
#     print(f'The encoded text is {cipher_text}')
#     return cipher_text
#
#
# def decrypt(text, shift) -> str:
#     cipher_text = ''
#     for letter in text:
#         cipher_text += alphabet[alphabet.index(letter) - shift
#         if alphabet.index(letter) - shift > 0
#         else (
#                 alphabet.index(letter) - shift + 26)]
#     print(f'The decoded text is {cipher_text}')
#     return cipher_text
#
#
# if direction == 'encode':
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)
