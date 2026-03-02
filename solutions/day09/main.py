from art import logo
import os

print(logo)

bidders_dictionary = {}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

game_on = True
while game_on:
    name = input("What is you name?: ")
    while name in bidders_dictionary:
        name += '_2'
    bid = int(input("What is your bid?: $"))
    bidders_dictionary[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or no'.\n")
    if more_bidders == "yes":
        clear_screen()
    elif more_bidders == "no":
        for key in bidders_dictionary:
            winner = key
            if bidders_dictionary[key] > bidders_dictionary[winner]:
                winner = key
        print(f"The winner is {winner} with a bid of ${bidders_dictionary[winner]}")
        game_on = False
