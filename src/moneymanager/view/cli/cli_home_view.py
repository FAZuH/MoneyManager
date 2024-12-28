from moneymanager.view.base_cli_view import BaseCliView


class CliHomeView(BaseCliView):
    def promt_option(self) -> int:
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
        inpt = input("> ")
        parsed_input = self._must_get_input(inpt, int)
        return parsed_input
