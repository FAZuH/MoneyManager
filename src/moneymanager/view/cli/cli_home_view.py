from moneymanager.view.cli.base_cli_view import BaseCliView


class CliHomeView(BaseCliView):
    def prompt_menu(self) -> int:
        """Prompts the user to choose a menu.

        Returns
        -------
        `int`
            The option the user picked
            Options:
            1. Add Expense
            2. Add Income
            3. Transaction History
            4. Manage Account
            5. Statistics
            6. Exit
        """
        print(
            "Pick an option",
            "--------------",
            "1. Add Expense",
            "2. Add Income",
            "3. Transaction History",
            "4. Manage Account",
            "5. Statistics",
            "6. Exit",
            sep="\n",
        )
        return self.must_get_input("> ", int)

    def display_exit_message(self) -> None:
        print("Thank you for using MoneyManager")
