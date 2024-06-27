from datetime import datetime
import os
import platform
from typing import Callable, Literal

from moneymanager.transaction import Transaction


def __must_get_input[T](prompt: str, type_strategy: Callable[[str], T]) -> T:
    """Prompts the user for an input. This function makes sure the user passes a valid 
    input parseable by type_strategy, then returning the parsed value.

    Args:
        prompt (str): The message to show to the user while asking for an input
        type_strategy (Callable[[str], T]): Callable that accepts a string as an argument, and returns any type 'T'

    Returns:
        T: The user input parsed into type 'T' by type_strategy
    """
    while True:
        inpt = input(prompt)

        if inpt == "exit":
            exit()

        try:
            return type_strategy(inpt)
        except ValueError:
            print("Please enter a valid input.")


def clear_view() -> None:
    current_os = platform.system()
    if current_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')


#####
# SHOW: Just prints something to the terminal
#####

def show_welcome() -> None:
    """Displays a welcome message to the user."""
    # TODO: Display ASCII art of 'MoneyManager'
    print("Welcome to MoneyManager")


#####
# CHOOSE: Prompts the user to choose an option
#####

def choose_main() -> int:
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
        "5. Exit"
    )
    inpt = input('> ')
    parsed_input = __must_get_input(inpt, int)
    return parsed_input

def choose_transaction_type() -> int:
    print(
        "Choose transaction type:"
        "------------------------"
        "1. Expense"
        "2. Income"
        "3. Back"
    )
    inpt = input('> ')
    parsed_input = __must_get_input(inpt, int)
    return parsed_input  # type: ignore


#####
# INPUT: Prompts the user for a more complete input
#####

def input_transaction(type_: Literal["expense", "income"]) -> Transaction:
    """Asks user input for adding transaction
    
    Args:
        type_ (str): Transaction type 
    """
    account = __must_get_input("Input account: ", str)
    category = __must_get_input("Input category: ", str)
    inpt = __must_get_input(f"Input {type_}: ", float)
    comment = __must_get_input("Input comment: ", str)

    # TODO: how should i do this
    # option 1: return list of answer. create Transaction object on controller (__main__)
    # option 2: create transaction object here, along with the id (increases code coupling)
    transaction = Transaction(1, datetime.now(), account, inpt, type_, category, comment)
    return transaction
