from __future__ import annotations

from datetime import datetime
from typing import Literal, override, TYPE_CHECKING
import uuid

from moneymanager.controller.base_controller import BaseController
from moneymanager.database.entity.transaction import Transaction
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
                account, category, amount, comment = self.view.prompt_transaction()
            except UserCancel:
                break

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
