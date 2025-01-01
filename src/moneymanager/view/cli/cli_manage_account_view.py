from __future__ import annotations

from typing import Any

from moneymanager.view.cli.base_cli_view import BaseCliView


class CliManageAccountView(BaseCliView):
    def display_account(self, name: str, balance: float) -> None:
        self.display_message(f"{name}: ${balance}")

    def prompt_action(self) -> Any:
        """Prompts the user for an action.

        Returns
        -------
        `int`
            The option the user picked
            Options:
            1. Add account
            2. Edit account
            3. Delete account
            4. Back
        """
        self.display_message(
            "Pick an option",
            "--------------",
            "1. Add account",
            "2. Edit account",
            "3. Delete account",
            "4. Back",
            sep="\n",
        )
        ret = self.must_get_input("> ", int)
        return ret

    def prompt_account_name(self) -> str:
        return self.must_get_input("Account name: ", str)

    def prompt_account_balance(self) -> float:
        return self.must_get_input("Account balance: ", float)
