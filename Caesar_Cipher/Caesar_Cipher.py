import db_art_alphabet as db


def caesar(text, shift, direction) -> str:
    cipher_text = ''
    over_flow = 1
    if direction == 'encode':
        over_flow *= -1
    elif direction == 'decrypt':
        shift *= -1
    else:
        print(f"Type 'encode' to encrypt, type 'decode' to decrypt. not: {direction}")
    for letter in text:
        if letter in alphabet:
            cipher_text += alphabet[alphabet.index(letter) + shift if 0 < alphabet.index(letter) + shift < 26 else (alphabet.index(letter) + shift + 26 * over_flow)]
        else:
            cipher_text += letter
    return cipher_text


print(db.logo)
alphabet = db.alphabet

is_continue = 'yes'
while is_continue == 'yes':
    en_or_de = input("\nType 'encode' to encrypt, type 'decode' to decrypt:").lower()
    message_text = input("Type your message: ").lower()
    to_shift = int(input("Type the shift number: "))

    if to_shift > 26:
        to_shift %= 26

    print(caesar(message_text, to_shift, en_or_de))
    is_continue = input('Want to restart the cipher program:\t').lower()


# _____________________________________________________________________________________________________________________
#
# def encrypt(text, shift) -> str:
#     cipher_text = ''
#     for letter in text:
#         cipher_text += alphabet[alphabet.index(letter) + shift if alphabet.index(letter) + shift < 26 else (
#                 alphabet.index(letter) + shift - 26)]
#     print(f'The encoded text is {cipher_text}')
#     return cipher_text
#
#
# def decrypt(text, shift) -> str:
#     cipher_text = ''
#     for letter in text:
#         cipher_text += alphabet[alphabet.index(letter) - shift if alphabet.index(letter) - shift > 0 else (
#                 alphabet.index(letter) - shift + 26)]
#     print(f'The decoded text is {cipher_text}')
#     return cipher_text
#
#
# if direction == 'encode':
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)
