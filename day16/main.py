from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    first_menu = Menu()
    first_coffeemachine = CoffeeMaker()
    first_moneymachine = MoneyMachine()
    while True:
        choice = input(f"What would you like? ({first_menu.get_items()}): ")
        if choice == "report":
            first_coffeemachine.report()
            first_moneymachine.report()
        else:
            drink = first_menu.find_drink(choice)
            if drink is None:
                print("We don't have the drink. Please order something different")
                continue

            if first_coffeemachine.is_resource_sufficient(drink) is not True:
                continue
            if first_moneymachine.make_payment(drink.cost) is not True:
                continue

            first_coffeemachine.make_coffee(drink)
