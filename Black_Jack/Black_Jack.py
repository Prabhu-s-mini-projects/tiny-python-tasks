# ------------------ Blackjack Project ---------------------------

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ------------------ Blackjack House Rules ---------------------------

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# -------------------- Wining Terms ---------------------
# 1. If a player's hand exceeds 21, they bust and lose their bet.
# 2. If the dealer busts, all remaining players win.
# 3. If a player's hand is closer to 21 than the dealer's hand, the player wins and is paid out 1:1 on their bet.
# 4. If a player has a Blackjack (an Ace and a 10-point card) and the dealer does not, the player wins.
# 5. If both the player and dealer have hands of equal value, it's a push (tie), and the player's bet is returned.

# Loading the game
import Black_Jack_Database as Db
import Black_jack_Utils_methods as Ctrl

# Welcoming the player to the game.
print(Db.logo)
print("Welcome to BLACK JACK Game")


# Hit or stand
def decide_winner(player_cards : list, dealer_cards: list) -> None:
    dealer_cards_count = sum(dealer_cards)
    while dealer_cards_count > 17:
        dealer_cards.append(Ctrl.get_a_card())
    if dealer_cards_count > 21:
        print("Player Wins")
    else:
        if player_card_count > dealer_cards_count:
            print("Player Wins")
        elif player_card_count == dealer_cards_count:
            print("GAME TIED")
        else:
            print("Player Lose")


def is_player_count(player_cards:list) -> None:
    player_card_count = sum(player_cards)
    if player_card_count > 21:
        if 11 in player_cards:
            count_ace_as_11 = sum(player_cards)
            position_11_in_playercards = player_cards.index(11)
            player_cards[position_11_in_playercards] = 1
            count_ace_as_1 = sum(player_cards)
            if count_ace_as_1 > 21:
                print("Player Lose")
        else:
            print("Players lose")

continue_play = 'y'
while continue_play == 'y':

    dealer_cards = []
    player_cards = []

    # Dealer and player gets 2 card.
    for card in range(2):
        dealer_cards.append(Ctrl.get_a_card())
        player_cards.append(Ctrl.get_a_card())

    # Show player's cards
    print(f"Here is Player's card: {player_cards}")
    for card in player_cards:
        Ctrl.show_card(card)

    # Show dealer's card
    print(f"Here is Dealer's Card: [ * , [{dealer_cards[1]}]")
    Ctrl.show_card(dealer_cards[1], close_card=True)  # For Now, hardcoding the value to be 1

    # Check whether dealer or player got blackjack.
    is_black_jack, winner_name = Ctrl.is_black_jack(dealer_cards, player_cards)

    if is_black_jack:
        print(f"\n {winner_name}")
    else:
        player_card_count = sum(player_cards)
        if player_card_count > 21:
            is_player_count(player_cards)
        else:
            get_another_card = input("\n Do you need another card: \t").lower()
            if get_another_card == 'yes':
                player_cards.append(Ctrl.get_a_card())
                pass  # pass it back to line 86
            else:
                decide_winner(player_cards, dealer_cards)

    continue_play = 'N'
