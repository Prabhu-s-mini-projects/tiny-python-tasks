import art
import os

print(art.logo)
print("Welcome to the BID-AUCTION_GAME")

bidders = []


def add_new_bidder(bidder_name, bidders_amount):
    new_bidder = {
        'name': bidder_name,
        'bid_amount': bidders_amount
    }
    bidders.append(new_bidder)


BID_window_open = True
while BID_window_open:
    # Get Bidder Information
    name = input("Enter your name:\t").lower()
    bid_amount = int(input("Enter your BID_amount $:\t"))

    # Logging all the Bidders info
    add_new_bidder(name, bid_amount)

    # Making sure Everyone placed a BID.
    other_bidders = input("Are there are any other bidders?\tType 'yes' to continue or 'any key' for no ").lower()

    if other_bidders == "yes":
        os.system('clear')  # clear the screen so there won't see previous person's BID
    else:
        BID_window_open = False

# Finding the MAX bid amount and the bidder
max_bid = 0
leading_bidder = 'House'
for bidder in bidders:
    if bidder['bid_amount'] > max_bid:
        max_bid = bidder['bid_amount']
        leading_bidder = bidder['name']
    elif bidder['bid_amount'] == max_bid and max_bid > 0:  # added this condition to handle the same amount bid
        max_bid = bidder['bid_amount']
        leading_bidder += ' + ' + bidder['name']
    else:
        pass

print(f"{leading_bidder} WON the with the BID_amount: {max_bid}")
