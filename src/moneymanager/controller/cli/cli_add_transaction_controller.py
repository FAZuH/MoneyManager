from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING, override
import uuid

from moneymanager.controller.base_controller import BaseController
from moneymanager.database.entity.transaction import Transaction
from moneymanager.view.cli.cli_add_transaction_view import CliAddTransactionView

if TYPE_CHECKING:
    from moneymanager.app.app import App


class CliAddTransactionController(BaseController):
    def __init__(self, app: App) -> None:
        super().__init__(app)
        self.view = CliAddTransactionView()
        self.repository = self.app.database.transaction_repository

    @override
    def run(self) -> None:
        self.view.clear_view()
        while True:
            option = self.view.promt_transaction_type()

            if option == 1:
                type_ = "expense"
            elif option == 2:
                type_ = "income"
            elif option == 3:
                self.view.clear_view()
                return
            else:
                self.view.display_error("Invalid option")
                continue

            type_ = "expense" if option == 1 else "income"

            account, category, amount, comment = self.view.input_transaction()

            uuid_ = uuid.uuid4()
            transaction = Transaction(
                uuid=uuid_.hex,
                date=datetime.now(),
                account=account,
                amount=amount,
                type_=type_,
                category=category,
                comment=comment,
            )
            self.repository.insert(transaction)
