import os
import platform

from abc import ABC


class BaseCliView(ABC):
    def clear_view(self) -> None:
        current_os = platform.system()
        if current_os == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def show_welcome(self) -> None:
        """Displays a welcome message to the user."""
        # TODO: Display ASCII art of 'MoneyManager'
        print("Welcome to MoneyManager")

    def _must_get_input[T](self, prompt: str, type_strategy: Callable[[str], T]) -> T:
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
