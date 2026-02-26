print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

text = input("Where do you want to go? Type \'left' or \'right'").lower()
if text == "right":
    print("Fall into a hole. Game over!")
elif text != "left" and text != "right":
    print("You have to type 'left' or 'right' you jerk!")
elif text == "left":
    text = input("There is a river. Do you wanna swim over or wait? Type 'swim' or 'wait'.").lower()
    if text == "swim":
        print("Attacked by trout. Game over!")
    elif text == "wait":
        text = input("There are three portals, where you can move forward with different colors. Type 'red', 'yellow' or 'blue'").lower()
        if text == "red":
            print("Burned by fire. Game over.")
        elif text == "blue":
            print("Eaten by beasts. Game over")
        elif text == "yellow":
            print("You Win! Hurray")
        else:
            print("Game over!")