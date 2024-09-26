""" Contains password generator class"""
# Dependencies
from random import choice, randint, shuffle

# CONSTANTS
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class PasswordGenerator:
    """help to manager different passwords"""

    def __init__(self):
        self.password = None

    def generate(self)-> str:
        """generates passwords"""

        character_list = []

        character_list.extend([choice(LETTERS) for _ in range(randint(4,6))])
        character_list.extend([choice(SYMBOLS) for _ in range(randint(2,4))])
        character_list.extend([choice(NUMBERS) for _ in range(randint(2,4))])

        shuffle(character_list)

        self.password = "".join(character_list)

        return self.password
