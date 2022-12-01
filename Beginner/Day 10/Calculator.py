from art import logo
import os




def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        the_function = operations[operation_symbol]
        answer = the_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        stop = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")

        if stop == "y":
            num1 = answer
        elif stop == 'n':
            should_continue = False
            calculator()
            os.system('cls')
        else:
            should_continue = False


calculator()
