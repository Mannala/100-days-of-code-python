from art import logo, vs
from game_data import data
import random


def has_more_followers(compare_a, compare_b):
    """"
    Takes 2 Dictionary Inputs compare_a and compare_b and looks for the key 'follower_count".
    Returns true if the number of followers of A is bigger than B
    """
    return compare_a["follower_count"] >= compare_b["follower_count"]

def compare_followers(compare_a, compare_b):
    """
    Takes 2 Dictionary Inputs compare_a and compare_b and prints basic Information from keys 'name", 'description' and 'country'.
    Asks User, if A or B has more followers.
    Uses has_more_followers-function. Returns True, if User is right and False, if User is wrong.
    """
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")

    while True:
        choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
        if choice in ["A", "B"]:
            break
        print("Invalid input. Please type 'A' or 'B'.")

    if choice == "A":
        return has_more_followers(compare_a, compare_b)
    else:
        return has_more_followers(compare_b, compare_a)

if __name__ == "__main__":
    print(logo)
    compare_a, compare_b = random.sample(data, 2)
    score = 0
    while True:
        if compare_followers(compare_a, compare_b):
            score += 1
            print("\n" * 100)
            print(logo)
            print(f"You're right! Current score: {score}")
            compare_a = compare_b
            compare_b = random.choice([item for item in data if item != compare_a])
        else:
            print("\n" * 100)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break
