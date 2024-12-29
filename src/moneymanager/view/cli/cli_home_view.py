from moneymanager.view.cli.base_cli_view import BaseCliView


class CliHomeView(BaseCliView):
    def prompt_menu(self) -> int:
        """
        Prompts the user to choose a menu.

        Returns
        -------
        int
            The option the user picked
            Options:
            1. Add Transaction
            2. Transaction History
            3. Account
            4. Statistics
            5. Exit
        """
        print(
            "Pick an option:",
            "---------------",
            "1. Add Transaction",
            "2. Transaction History",
            "3. Account",
            "4. Statistics",
            "5. Exit",
            sep="\n",
        )
        return self._must_get_input("> ", int)

    def display_exit_message(self) -> None:
        print("Thank you for using MoneyManager")
