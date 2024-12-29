from moneymanager.app._ui_option import UiOption
from moneymanager.app.config import Config
from moneymanager.controller.cli.main_cli_controller import MainCliController
from moneymanager.database.money_manager_database import MoneyManagerDatabase


class App:
    """Bootstraps the application."""

    def __init__(self) -> None:
        self.config = Config()
        self.config.load()

        self.database = MoneyManagerDatabase()

        if self.config.UI is UiOption.CLI:
            self.main_controller = MainCliController(self)
        else:
            raise NotImplementedError(f"UI {self.config.UI.value} is not implemented")
        # self.current_controller = None  # TODO: Complex implementation. Do this in the future.

    def run(self) -> None:
        self.main_controller.run()
