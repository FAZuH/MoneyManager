from __future__ import annotations

from typing import Any

from moneymanager.database.model.transaction import Transaction
from moneymanager.view.cli.base_cli_view import BaseCliView


class CliAddTransactionView(BaseCliView):
    def prompt_transaction(self) -> list[Any]:
        print("Input the transaction information, or enter 'cancel' to return to main menu:")
        account = self.must_get_input("Input account: ", str)
        category = self.must_get_input("Input category: ", str)
        amount = self.must_get_input("Input amount: ", float)
        comment = self.must_get_input("Input comment: ", str)
        return [account, category, amount, comment]

    def display_transaction_added(self, tx: Transaction) -> None:
        print(f"Transaction added successfully: {tx}")
