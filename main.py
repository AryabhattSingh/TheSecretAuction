from ascii_art import logo
import os


def clear_screen():
    os.system('cls')


other_bidders = "yes"

while other_bidders == "yes":
    clear_screen()
    print(logo)
    name = input("What is your name? : ")
    bid = float(input("What is your bid? : $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()


