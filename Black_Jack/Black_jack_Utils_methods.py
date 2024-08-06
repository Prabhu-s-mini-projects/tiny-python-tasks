import random
import Black_Jack_Database as Db


def get_a_card() -> int:
    return random.choice(Db.cards)


def is_black_jack(cards:list) -> bool:
    if '11' in cards and 'K' or 'Q' or 'J' or '10' in cards:
        return True
    else:
        return False


# To Generate other types of cards
def show_card(character: int, close_card=False) -> None:
    """Constructing CARD"""
    # Future enhancement convert this to 5X3 matrix
    template_card = [
        '┌─────────────┐',
        f'| {character}          |',
        f'|             |',
        f'|             |',
        f'|             |',
        f'|             |',
        f'|             |',
        f'|          {character} |',
        '└─────────────┘',
    ]
    for segment in template_card:
        print(segment)
    if close_card:
        for segment in Db.close_card:
            print(segment)
