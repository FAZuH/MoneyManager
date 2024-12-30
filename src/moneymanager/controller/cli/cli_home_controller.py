from __future__ import annotations

from typing import override, TYPE_CHECKING

from moneymanager.controller.base_controller import BaseController
from moneymanager.view.cli.cli_home_view import CliHomeView

if TYPE_CHECKING:
    from moneymanager.app.app import App


class CliHomeController(BaseController):
    def __init__(self, app: App) -> None:
        super().__init__(app)
        self._view = CliHomeView()

    @override
    def run(self) -> None:
        self._view.display_welcome()

        while True:
            option = self._view.prompt_menu()
            match option:
                case 1:  # Add expense
                    self.app.main_controller.run_add_expense_controller()
                case 2:  # Add income
                    self.app.main_controller.run_add_income_controller()
                    pass
                case 3:  # Transaction history
                    # self.app.main_controller.run_()
                    pass
                case 4:  # Manage account
                    # self.app.main_controller.run_()
                    pass
                case 5:  # Statistics
                    # self.app.main_controller.run_()
                    pass
                case 6:  # Exit
                    self._view.display_exit_message()
                    break
                case _:
                    self._view.display_error("Invalid option")
