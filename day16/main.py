from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    my_menu = Menu()
    jura = CoffeeMaker()
    juramoney = MoneyMachine()
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if my_menu.find_drink(choice) is not None or choice == "report":
            # blabla
            if choice == "report":
                jura.report()
            else:
                my_drink = my_menu.find_drink(choice)
                if jura.is_resource_sufficient(my_drink):
                    juramoney.make_payment(my_drink.cost)
                    jura.make_coffee(my_drink)
                    # print("Please insert coins.")
                    # insert_money(choice)
                else:
                    # Machine has not enough Resources
                    continue
        else:
            print("Wrong Input. Please try again")
