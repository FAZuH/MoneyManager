from __future__ import annotations

from datetime import datetime
from typing import Literal, override, TYPE_CHECKING
import uuid

from moneymanager.controller.base_controller import BaseController
from moneymanager.database.model.transaction import Transaction
from moneymanager.exception import UserCancel
from moneymanager.view.cli.cli_add_transaction_view import CliAddTransactionView

if TYPE_CHECKING:
    from moneymanager.app.app import App


class CliAddTransactionController(BaseController):
    def __init__(self, app: App) -> None:

        super().__init__(app)
        self.view = CliAddTransactionView()
        self.repository = self.app.database.transaction_repository
        self.transaction_type: Literal["expense", "income"]

    @override
    def run(self) -> None:
        self.view.clear_view()
        while True:
            try:
                print(
                    "Input the transaction information, or enter 'cancel' to return to main menu:"
                )
                account = self.view.must_get_input("Input account: ", str)
                self.app.database.account_repository.select(
                    account
                )  # Check if the account with name {account} is available

                category = self.view.must_get_input("Input category: ", str)
                amount = self.view.must_get_input("Input amount: ", float)
                comment = self.view.must_get_input("Input comment: ", str)
            except UserCancel:
                break
            except ValueError:  # If the account does't exist
                print(f"Account with name {account} doesn't exist")
                continue

            uuid_ = uuid.uuid4()
            tx = Transaction(
                uuid=uuid_.hex,
                date=datetime.now(),
                account=account,
                amount=amount,
                type_=self.transaction_type,
                category=category,
                comment=comment,
            )
            self.repository.insert(tx)
            self.view.display_transaction_added(tx)
            self.view.display_line_separator()
        self.view.clear_view()
