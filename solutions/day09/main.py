from art import logo
import os

print(logo)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_name():
    name = input("Please enter your name: ").strip()
    if not name:
        print("You didn't enter anything. Please try again.\n")
        return get_name()
    if name in bidders_dictionary:
        print("The name already exists. Please enter a different Name.")
        return get_name
    return name

def get_bid():
    bid_string = input("What is your bid: ")
    if not bid_string:
        print("You didn't enter anything. Please try again.\n")
        return get_bid()
    try:
        bid = int(bid_string)
    except ValueError:
        print("Invalid input. Please enter an integer.\n")
        return get_bid()
    return bid

bidders_dictionary = {}

game_mode = True
while game_mode:
    name = get_name()
    bid = get_bid()
    bidders_dictionary[name] = bid
    while True:
        choice = input("Are there any other bidders? Type 'yes' or 'no'. ").strip().lower()
        if choice in ['yes', 'no']:
            break
        else:
            print("Wrong answer. Please type in 'yes' or 'no'\n")
    if choice == 'yes':
        clear_screen()
    else:
        bidder_name, bidder_value = name, bid
        for key, value in bidders_dictionary.items():
            if value > bidder_value:
                bidder_value = value
        print(f"The winner is {bidder_name} with a bid of €{bidder_value}")
        game_mode = False