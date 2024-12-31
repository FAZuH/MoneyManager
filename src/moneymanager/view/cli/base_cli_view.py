from abc import ABC
import os
import platform
from typing import Callable

from moneymanager.exception import UserCancel
from moneymanager.exception import UserExit


class BaseCliView(ABC):
    def clear_view(self) -> None:
        current_os = platform.system()
        if current_os == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def display_error(self, message: str) -> None:
        """Displays an error message to the user."""
        print(f"Error: {message}")

    def display_line_separator(self, length: int = 80) -> None:
        """Displays a line separator to the user."""
        print("-" * length)

    def display_welcome(self) -> None:
        """Displays a welcome message to the user."""
        # TODO: Display ASCII art of 'MoneyManager'
        print("Welcome to MoneyManager")

    def must_get_input[T](self, prompt: str, type_strategy: Callable[[str], T]) -> T:
        """
        Prompts the user for an input.

        This method makes sure the user passes a valid input parseable by type_strategy(), before
        returning the parsed value.

        Parameters
        ----------
        prompt : `str`
            The message to show to the user while asking for an input
        type_strategy : `Callable[[str], T]`
            Callable that accepts a string as an argument, and returns any type `T`

        Returns
        -------
        `T`
            The user input parsed into type `T` by type_strategy

        Raises
        ------
        `UserExit`
            If the user inputs 'exit'
        `UserCancel`
            If the user inputs 'cancel'
        """
        while True:
            inpt = input(prompt)

            if inpt == "exit":
                raise UserExit()

            if inpt == "cancel":
                raise UserCancel

            try:
                return type_strategy(inpt)
            except ValueError:
                print("Please enter a valid input.")
