import random

from art import logo
import random


def add_card(deck):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_wert = random.choice(cards)
    deck.append(random_wert)
    if sum(deck) > 21 and 11 in deck:
        deck.remove(11)
        deck.append(1)
    return deck

def endgame_hands(deck_dealer, deck_player):
    print(f"\t\t\tYour final hand: {deck_player}, final score: {sum(deck_player)}")
    print(f"\t\t\tComputer's final hand: {deck_dealer}, final score: {sum(deck_dealer)}")

def game_finished_asap(deck_dealer, deck_player):
    if sum(deck_player) > 21:
        endgame_hands(deck_dealer, deck_player)
        print("\tYou went over. You lose")
        return True
    elif sum(deck_dealer) > 21:
        endgame_hands(deck_dealer, deck_player)
        print("\tOpponent went over. You win")
        return True
    elif len(deck_dealer) == 2 and sum(deck_dealer) == 21:
        endgame_hands(deck_dealer, deck_player)
        print("\tLose, opponent has Blackjack")
        return True
    elif len(deck_player) == 2 and sum(deck_player) == 21:
        endgame_hands(deck_dealer, deck_player)
        print("\tWin with a Blackjack")
        return True
    else:
        return False

def game_finished(deck_dealer, deck_player):
    if sum(deck_dealer) > sum(deck_player):
        endgame_hands(deck_dealer, deck_player)
        print("\tOpponent is closer to 21. You lose")
        return True
    elif sum(deck_player) > sum(deck_dealer):
        endgame_hands(deck_dealer, deck_player)
        print("\tYou are closer to 21. You win.")
        return True
    else:
        return False

def fill_deck(deck):
    if sum(deck) < 17: # 2 3
        deck = add_card(deck) # 2 3 5
        deck = fill_deck(deck)# 2 3 5 10
    return deck

game_on = True

while game_on:
    def blackjack_game():
        print(logo)
        dealer = []
        deck_player = []
        deck_dealer = []
        for _ in range(2):
            deck_dealer = add_card(deck_dealer)
            deck_player = add_card(deck_player)

        print(f"\tYour cards: {deck_player}, current score: {sum(deck_player)}")
        print(f"\tComputer's first card: {deck_dealer[1]}")
        while True:
            if game_finished_asap(deck_dealer, deck_player):
                return
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "n":
                deck_dealer = fill_deck(deck_dealer)
                if game_finished_asap(deck_dealer, deck_player) or game_finished(deck_dealer, deck_player):
                    return
                elif sum(deck_dealer) == sum(deck_player):
                    endgame_hands(deck_dealer, deck_player)
                    print("\tSame Point's. It's a draw!")
                    return True
            elif choice == "y":
                deck_player = add_card(deck_player)
            else:
                print("Wrong Input or Game Error.")
            print(f"\tYour cards: {deck_player}, current score: {sum(deck_player)}")
            print(f"\tComputer's first card: {deck_dealer[1]}")

    choice_game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice_game_on == 'y':
        blackjack_game()
    else:
        game_on = False






