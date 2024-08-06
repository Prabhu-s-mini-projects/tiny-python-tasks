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
    player_card_count = sum(player_cards)
    dealer_card_count = sum(dealer_cards)
    is_player_has_black_jack = Ctrl.is_black_jack(dealer_cards)
    is_dealer_has_black_jack = Ctrl.is_black_jack(player_cards)

    if is_player_has_black_jack or is_dealer_has_black_jack:
        if is_dealer_has_black_jack and is_player_has_black_jack:
            print("GAME TIED")
        elif is_player_has_black_jack:
            print("Player WINS")
        else:
            print("Dealer WINS")
    else:

        hit_or_stand = input("'Hit' or 'STAND'").lower()
        while 'hit' or 'stand' not in hit_or_stand:
            print(f"please entire 'hit or 'stand not :{hit_or_stand}")
            hit_or_stand = input("'Hit' or 'STAND'").lower()

        if hit_or_stand == 'hit':
            player_cards.append(Ctrl.get_a_card())
            if Ctrl.is_black_jack(player_cards):
                pass

    continue_play = 'N'
