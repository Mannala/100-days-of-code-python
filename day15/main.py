MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def take_a_drink(choice):
    """
    Takes the resources and a string and looks in the dictionary MENU for string-key and remove the needed resources (water, milk, coffee) from the machine.
    Returns True or False
    """
    drink = MENU[choice]
    ingredients = drink["ingredients"]
    for item, amount in ingredients.items():
        if resources.get(item, 0) < amount:
            print(f"Don't have enough {item}.")
            return False
    for item, amount in ingredients.items():
        resources[item] -= amount

    return True


def print_report():
    """
    Takes the dict resources as input and outputs the keywords water, milk, coffee, money as an report
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def insert_money(choice):
    """
    Takes the resources and the user choice (espresso, latte,...) as an input.
    Asks the user for money and checks if it's enough to buy coffee.
    Else responds that it's not enough
    Returns the resources
    """
    user_money = 0
    user_money += int(input("how many quarters?: ")) * 0.25
    user_money += int(input("how many dimes?: ")) * 0.10
    user_money += int(input("how many nickles?: ")) * 0.05
    user_money += int(input("how many pennies?: ")) * 0.01
    if user_money >= MENU[choice]["cost"]:
        resources["money"] += MENU[choice]["cost"]
        change_money = round(user_money - MENU[choice]["cost"], 2)
        print(f"Here is ${change_money} in change.")
        print(f"Here is your {choice}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

if __name__ == "__main__":
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice in MENU or choice == "report":
            # blabla
            if choice == "report":
                print_report()
            else:
                if take_a_drink(choice):
                    print("Please insert coins.")
                    insert_money(choice)
                else:
                    # Machine has not enough Resources
                    continue
        else:
            print("Wrong Input. Please try again")