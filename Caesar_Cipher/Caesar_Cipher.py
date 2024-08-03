alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

en_or_de = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message_text = input("Type your message:\n").lower()
to_shift = int(input("Type the shift number:\n"))


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
        cipher_text += alphabet[alphabet.index(letter) + shift if 0 < alphabet.index(letter) + shift < 26 else (alphabet.index(letter) + shift + 26 * over_flow)]
    return cipher_text


print(caesar(message_text,to_shift,en_or_de))

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
