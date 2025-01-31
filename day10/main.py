from multiprocessing.managers import convert_to_error

from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiplication,
    "/": division
    }

def calculator():
    print(logo)
    conti_mode: bool = True
    num1 = float(input("What's the first number?: "))

    while conti_mode:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == "y":
            conti_mode = True
            num1 = result
        else:
            conti_mode = False
            print("\n" * 100)
            calculator()

calculator()