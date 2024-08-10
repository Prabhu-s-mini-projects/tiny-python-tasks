import random
import Black_Jack_Database as Db


def get_another_card() -> int:
    """
    TO get a random card form deck.
    :return:
    """
    return random.choice(Db.cards)


def is_black_jack(player_cards: list, dealer_cards: list) -> (bool, str):
    """
    Check whether Both Ace and 10 is part of Cards()
    :param dealer_cards:
    :param player_cards:
    :return:
    """
    if [10, 11] in dealer_cards and [10, 11] in player_cards:
        return True, "🤯 Game TIED 🤔"
    elif [10, 11] in dealer_cards:
        return True, "Player Lose 😭"
    elif [11, 10] in player_cards:
        return True, "Player Wins 😎:"
    else:
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
        f"{Db.color_code_map.get('red')}┌─────────────┐",
        f"| {character}          " + ("|" if character > 9 else " |"),
        f"|             |",
        f"|             |",
        f"|             |",
        f"|             |",
        f"|             |",
        ("|" if character > 9 else "| ") + f"          {character} |",
        f"└─────────────┘{Db.color_code_map.get('reset')}",
    ]

    for segment in template_card:
        print(segment)

    if close_card:
        for segment in Db.close_card:
            print(segment)
