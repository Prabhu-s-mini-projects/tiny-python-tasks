""" ------------------ Blackjack House Rules ---------------------------

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
# 3. If a player's hand is closer to 21 than the dealer's hand,
    the player wins and is paid out 1:1 on their bet.
# 4. If a player has a Blackjack (an Ace and a 10-point card) and the dealer does not,
    the player wins.
# 5. If both the player and dealer have hands of equal value, it's a push (tie),
    and the player's bet is returned.
"""
# Loading the game
import black_jack_database as db
import black_jack_utils_methods as controller

def decide_winner(player_score_count: int, dealer_score_count: int) -> str:
    """ Decides the winner based on the rules"""
    if player_score_count > dealer_score_count:
        return "Player Wins 😎:"
    if player_score_count == dealer_score_count:
        return "🤯 Game TIED 🤔"

    return "Player Lose 😭"

def main()-> None:
    """
    # Task 1: Add a loop that will ask whether User/Player wants to play another game.
    # Task 2: Give 2 cards to Dealer and player.
    # Task 3: Check whether user or dealer has Black Jack. if yes game.
              print the winner and game over.
    # Task 4: Ask user whether he needs another card. (HIT or STAND)
    #         If the user has card count > 21 Player lose
    #
    # Task 5: Count Dealer's card
    #         If count is less than 17 keep hitting the card for dealer.
    #         If count goes above 21, player wins
    # Task 6: Decide the winner
    :return:
    """
    # Welcoming the player to the game.
    print(db.LOGO)
    print("Welcome to BLACK JACK Game")

    # Task 1: Add a loop that will ask whether User/Player wants to play another game.
    another_game = 'y'
    while another_game == 'y':

        # Local variables.
        player_cards = []
        dealer_cards = []
        # player_cards_count = 0
        # dealer_cards_count = 0.
        # is_black_jack = False
        game_over = False

        # Task 2: Dealer and player gets 2 card.
        for _ in range(2):
            dealer_cards.append(controller.get_another_card())
            player_cards.append(controller.get_another_card())

        # Calculating the score
        player_cards_count = sum(player_cards)
        dealer_cards_count = sum(dealer_cards)

        print(f"Player cards are ;{player_cards} --> score:{player_cards_count}")
        print(f"Dealer cards are ;{dealer_cards} --> score:{dealer_cards_count}")

        # Task 3: Check whether user or dealer has Black Jack.
        is_black_jack, winner = controller.is_black_jack(player_cards, dealer_cards)

        if not is_black_jack:
            # Task 4: Ask user whether he needs another card. (HIT or STAND)
            hit_or_stand = input("\t'HIT' or 'STAND' :\t").lower()

            # Keep it in a loop until user want to stand
            while hit_or_stand == 'hit':
                player_cards.append(controller.get_another_card())
                player_cards_count = sum(player_cards)

                print(f"Player cards are ;{player_cards} --> score:{player_cards_count}")
                # If the user has card count > 21 Player lose
                if player_cards_count > 21:
                    if 11 in player_cards:
                        player_cards.remove(11)
                        player_cards.append(1)
                        player_cards_count = sum(player_cards)
                        print(f"Player cards are ;{player_cards} --> score:{player_cards_count}")
                    else:
                        print("Player Lose 😭")
                        game_over = True
                        break

                hit_or_stand = input("\t'HIT' or 'STAND' :\t").lower()

            # Task 5: Count Dealer's card.
            while 17 > dealer_cards_count and not game_over:
                # If count is less than 17 keep hitting the card for dealer.
                dealer_cards.append(controller.get_another_card())
                dealer_cards_count = sum(dealer_cards)

                print(f"Dealer cards are ;{dealer_cards} --> score:{dealer_cards_count}")
                # If count goes above 21, player wins
                if dealer_cards_count > 21:
                    if 11 in dealer_cards:
                        dealer_cards.remove(11)
                        dealer_cards.append(1)
                        dealer_cards_count = sum(dealer_cards)
                        print(f"Dealer cards are ;{dealer_cards} --> score:{dealer_cards_count}")
                    else:
                        print("Player Wins 😎:")
                        game_over = True
                        break

            # Decide winner
            if not game_over:
                print(decide_winner(player_cards_count, dealer_cards_count))

            another_game = input("Do you want to play another came :\t"
                                 " 'y' for Yes or 'any key' for No\n").lower()


if __name__ == "__main__":
    main()
