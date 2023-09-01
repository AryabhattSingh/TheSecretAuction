from ascii_art import logo
from utility_functions import *

bids_dictionary = {}
is_bidding_over = False

while not is_bidding_over:
    # Clearing console so that next bidder can't see the previous bid amount
    clear_screen()
    print(logo)
    name = input("What is your name? : ")

    # Keep taking "bid" input unless a valid floating point number is entered
    bid = 0
    valid_bid = False
    while not valid_bid:
        bid = input("What is your bid? : $")
        valid_bid = is_bid_value_valid(bid)

    # Now, since the "bid" value has been verified, typecasting it to float, and adding to dictionary
    bids_dictionary[name] = float(bid)

    # Keep asking for "Are there other bidders" till a valid input like - "yes", "no", "y", "n" -
    # is entered
    valid_input = False
    while not valid_input:
        any_other_bidder = input("\nAre there any other bidders? Type 'yes' or 'no' : ").lower()
        valid_input = is_input_valid(any_other_bidder)
        if not valid_input:
            print("\nKindly enter a valid value!")
        elif valid_input and any_other_bidder == "no":
            is_bidding_over = True

print_winner(bids_dictionary)
