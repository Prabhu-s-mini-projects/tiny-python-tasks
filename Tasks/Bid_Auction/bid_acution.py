"""
Game that makes user to make a bid and share the results based on the bid amount
"""

# Dependencies
import os
import art


print(art.LOGO)
print("Welcome to the BID-AUCTION_GAME")

bidders = []


def add_new_bidder(bidder_name, bidders_amount):
    """
     adds the new bidder and its amount to the bidders list.
    """
    new_bidder = {
        'name': bidder_name,
        'bid_amount': bidders_amount
    }
    bidders.append(new_bidder)

def main()-> None:
    """ Starting point of a program """
    bid_window_open:bool = True
    while bid_window_open:
        # Get Bidder Information
        name = input("Enter your name:\t").lower()
        bid_amount = int(input("Enter your BID_amount $:\t"))

        # Logging all the Bidders info
        add_new_bidder(name, bid_amount)

        # Making sure Everyone placed a BID.
        other_bidders = input("Are there are any other bidders?"
                              "\tType 'yes' to continue or 'any key' for no\n").lower()

        if other_bidders == "yes":
            # Set the TERM environment variable
            os.environ['TERM'] = 'xterm-256color'

            # clear the screen so there won't see previous person's BID
            os.system('clear')

        else:
            bid_window_open = False

    # Finding the MAX bid amount and the bidder
    max_bid:int = 0
    leading_bidder: str = 'House'
    for bidder in bidders:
        if bidder['bid_amount'] > max_bid:
            max_bid = bidder['bid_amount']
            leading_bidder = bidder['name']
        # added this condition to handle the same amount bid
        elif bidder['bid_amount'] == max_bid and max_bid > 0:
            max_bid = bidder['bid_amount']
            leading_bidder += ' + ' + bidder['name']
        else:
            pass

    print(f"{leading_bidder} WON the BID-AUCTION with the BID_amount: {max_bid}")

if __name__ == "__main__":
    main()
