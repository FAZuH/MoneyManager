from __future__ import annotations

from typing import override, TYPE_CHECKING

from moneymanager.controller.base_controller import BaseController
from moneymanager.controller.cli.cli_add_transaction_controller import CliAddTransactionController
from moneymanager.controller.cli.cli_home_controller import CliHomeController

if TYPE_CHECKING:
    from moneymanager.app.app import App


# TODO: Create separate interface for the main controller.
class MainCliController(BaseController):
    """Bootstraps other CLI controllers, and manages the main loop."""

    def __init__(self, app: App) -> None:
        super().__init__(app)
        self._home_controller = CliHomeController(app)
        self._transaction_controller = CliAddTransactionController(app)

    @override
    def run(self) -> None:
        self.run_home_controller()

    def run_home_controller(self) -> None:
        self._home_controller.run()

    def run_add_expense_controller(self) -> None:
        self._transaction_controller.transaction_type = "expense"
        self._transaction_controller.run()

    def run_add_income_controller(self) -> None:
        self._transaction_controller.transaction_type = "income"
        self._transaction_controller.run()
