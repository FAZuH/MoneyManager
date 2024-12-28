from moneymanager.entity.transaction import Transaction
from datetime import datetime
from uuid import UUID
from typing import Literal

from moneymanager.view.base_cli_view import BaseCliView


class CliTransactionView(BaseCliView):
    def promt_transaction_type(self) -> int:
        print(
            "Choose transaction type:" "------------------------" "1. Expense" "2. Income" "3. Back"
        )
        inpt = input("> ")
        parsed_input = self._must_get_input(inpt, int)
        return parsed_input  # type: ignore

    def input_transaction(self, type_: Literal["expense", "income"]) -> Transaction:
        """Asks user input for adding transaction

        Args:
            type_ (str): Transaction type
        """
        account = self._must_get_input("Input account: ", str)
        category = self._must_get_input("Input category: ", str)
        inpt = self._must_get_input(f"Input {type_}: ", float)
        comment = self._must_get_input("Input comment: ", str)

        # TODO: how should i do this
        # option 1: return list of answer. create Transaction object on controller (__main__)
        # option 2: create transaction object here, along with the id (increases code coupling)
        uuid = UUID()
        transaction = Transaction(uuid.hex, datetime.now(), account, inpt, type_, category, comment)
        return transaction
