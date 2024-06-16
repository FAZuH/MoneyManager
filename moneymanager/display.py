from datetime import datetime
from typing import Callable

from moneymanager.transaction import Transaction


def exittable_input(prompt: str) -> str:
    """Asks the user for an input. Exits the program if the input is 'exit'

    Args:
        prompt (str): The message to show to the user while asking for an input

    Returns:
        str: The user's input
    """
    inpt = input(prompt)
    if inpt == "exit":
        exit()
    return inpt

def must_get_input[T](prompt: str, type_strategy: Callable[[str], T]) -> T:
    """Prompts the user for an input. This function makes sure the user passes a valid 
    input parseable by type_strategy, then returning the parsed value.

    Args:
        prompt (str): The message to show to the user while asking for an input
        type_strategy (Callable[[str], T]): Callable that accepts a string as an argument, and returns any type 'T'

    Returns:
        T: The user input parsed into type 'T' by type_strategy
    """
    while True:
        inpt = exittable_input(prompt)
        try:
            return type_strategy(inpt)
        except ValueError:
            print("Please enter a valid input.")

def display_welcome() -> None:
    """Displays a welcome message to the user."""
    # TODO: Display ASCII art of 'MoneyManager'
    print("Welcome to MoneyManager")

def input_main() -> int:
    """Prompts the user for main option.

    Returns:
        int: The option the user picked 
    """    
    print(
        "Pick an option:"
        "---------------"
        "1. Add Transaction"
        "2. Transaction History"
        "3. Account"
        "4. Statistics"
    )
    inpt = exittable_input('> ')
    parsed_input = must_get_input(inpt, int)
    return parsed_input

def input_transaction(type_: str) -> Transaction:
    """Asks user input for adding transaction
    
    Args:
        type_ (str): Transaction type 
    """
    account = must_get_input("Input account: ", str)
    category = must_get_input("Input category: ", str)
    inpt = must_get_input(f"Input {type_}: ", float)
    comment = must_get_input("Input comment: ", str)
    transaction = Transaction(datetime.now(), account, inpt, type_, category, comment)
    return transaction

def view_account_balance(account: str):
    ...

def expense_statistics():
    ...

def income_statistics():
    ...