import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
RockPaperScissors_possibilities = [rock, paper, scissors]
computers_choice = random.randint(0, 2)

print(RockPaperScissors_possibilities[int(players_choice)])
print("Computer chose: ")
print(RockPaperScissors_possibilities[computers_choice])

if int(players_choice) == computers_choice:
    print("It's a draw")
elif (players_choice == "0" and computers_choice == "2"
      or players_choice == "1" and computers_choice == "0"
      or players_choice == "2" and computers_choice == "1"):
    print("You win!")
else:
    print("You loose")