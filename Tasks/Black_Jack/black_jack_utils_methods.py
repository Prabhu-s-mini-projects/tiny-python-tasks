""" Contains the utils methods needed  for the black jack game"""

import random
import black_jack_database as Db


def get_another_card() -> int:
    """
    TO get a random card form deck.
    :return:
    """
    return random.choice(Db.CARDS)


def is_black_jack(player_cards: list, dealer_cards: list) -> (bool, str):
    """
    Check whether Both Ace and 10 is part of Cards()
    :param dealer_cards:
    :param player_cards:
    :return:
    """
    if [10, 11] in dealer_cards and [10, 11] in player_cards:
        return True, "🤯 Game TIED 🤔"
    if [10, 11] in dealer_cards:
        return True, "Player Lose 😭"
    if [11, 10] in player_cards:
        return True, "Player Wins 😎:"

    return False, None


def show_card(character: int, close_card=False) -> None:
    """
    To print the numbers in the CARD format
    :param character:  pass the number of the card
    :param close_card: pass it as to true to display a close card.
    :return:
    """
    # Future enhancement convert this to 5X3 matrix
    template_card = [
        f"{Db.COLOR_CODE_MAP.get('red')}┌─────────────┐",
        f"| {character}          " + ("|" if character > 9 else " |"),
        "|             |",
        "|             |",
        "|             |",
        "|             |",
        "|             |",
        ("|" if character > 9 else "| ") + f"          {character} |",
        f"└─────────────┘{Db.COLOR_CODE_MAP.get('reset')}",
    ]

    for segment in template_card:
        print(segment)

    if close_card:
        for segment in Db.CLOSE_CARD:
            print(segment)
