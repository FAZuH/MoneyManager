from __future__ import annotations
from typing import Any

from moneymanager.view.cli.base_cli_view import BaseCliView


class CliAddTransactionView(BaseCliView):
    def promt_transaction_type(self) -> int:
        """Prompts the user to choose a transaction type.

        Returns
        -------
        int
            The option the user picked
            Options:
            1. Add expense
            2. Add income
            3. Back
        """
        print(
            "Choose transaction type:",
            "------------------------",
            "1. Expense",
            "2. Income",
            "3. Back",
            sep="\n",
        )
        parsed_input = self._must_get_input("> ", int)
        return parsed_input  # type: ignore

    def input_transaction(self) -> list[Any]:
        account = self._must_get_input("Input account: ", str)
        category = self._must_get_input("Input category: ", str)
        amount = self._must_get_input("Input amount: ", float)
        comment = self._must_get_input("Input comment: ", str)
        return [account, category, amount, comment]
