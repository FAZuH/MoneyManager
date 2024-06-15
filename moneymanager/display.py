from typing import Callable


def ask(prompt: str) -> str:
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
        inpt (str): The user input to parse by type_strategy
        type_strategy (Callable[[str], T]): Callable that accepts a string as an argument, and returns any type 'T'

    Returns:
        T: The user input parsed into type 'T' by type_strategy
    """
    while True:
        inpt = ask(prompt)
        try:
            return type_strategy(inpt)
        except ValueError:
            print("Please enter a valid input.")

def display_welcome() -> None:
    """Displays a welcome message to the user."""
    # TODO: Display ASCII art of 'MoneyManager'
    print("Welcome to MoneyManager")

def prompt_main() -> int:
    """Prompts the user for an input. 1 Input Expenses. 2 Input Income. 3 View Account
    Balance. 4 View Expense Statistics. 5 View Income Statistics

    Returns:
        int: The option the user picked 
    """    
    print(
        "Pick an option:"
        "---------------"
        "1. Input Expenses"
        "2. Input Income"
        "3. View Account Balance"
        "4. View Expense Statistics"
        "5. View Income Statistics"
    ) 
    inpt = ask('> ')
    parsed_input = must_get_input(inpt, int)
    return parsed_input