import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' and 'hard': ")
    return 10 if difficulty == "easy" else 5

def number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 an 100")
    lives = choose_difficulty()
    random_number = random.randint(1, 100)
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            return
        elif guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")
        if lives > 0:
            print("Guess again")
        lives -= 1
    print(f"You've run out of guesses. Refresh the page to run again.")

if __name__ == "__main__":
    number_guessing_game()