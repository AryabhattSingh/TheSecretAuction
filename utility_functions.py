import os


def clear_screen():
    """This function clears terminal. It doesn't work in PyCharm Run window"""
    os.system('cls')


def is_bid_value_valid(bid_amount):
    """This function tries to convert "bid_amount" from string to float. If typecasting is successful,
     it returns True, else False"""
    try:
        float(bid_amount)
        return True
    except ValueError:
        print("\nKindly enter a valid number.\n")
        return False


def is_input_valid(are_there_any_other_bidder):
    """This function checks the validity of the user response to the question "Are there other bidders?"
    Expected values are "yes", "no", "y", "n"
    """
    if are_there_any_other_bidder not in ["yes", "no"]:
        return False
    return True  # this means that input to any_other_bidder is valid


def print_winner(bidder_dictionary):
    """This function takes bids_dictionary as input and print the winner name with the bid amount"""
    winner = ""
    highest_bid = float("-inf")  # Assuming highest bid to be negative infinity
    for bidder in bidder_dictionary:
        bid_value = bidder_dictionary[bidder]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(f"\nThe winner of the auction is {winner}"
          f"\nWith the bid value of ${highest_bid}\n")
