from __future__ import annotations
from typing import TYPE_CHECKING, override

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
                case 1:  # Add transaction
                    self.app.main_controller.run_add_transaction_controller()
                case 2:
                    # self.app.main_controller.run_transaction_history_controller()
                    pass
                case 3:
                    # self.app.main_controller.run_()
                    pass
                case 4:
                    # self.app.main_controller.run_statistics_controller()
                    pass
                case 5:  # Exit
                    self._view.display_exit_message()
                    break
                case _:
                    self._view.display_error("Invalid option")
