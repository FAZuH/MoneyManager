from moneymanager.app.config import Config
from moneymanager.controller.cli.main_cli_controller import MainCliController


class App:
    """Bootstraps the application."""

    def __init__(self) -> None:
        self.config = Config()
        self.config.load()

        self.main_controller = MainCliController(self)
        # self.current_controller = None  # TODO: Complex implementation. Do this later.

    def run(self) -> None:
        self.main_controller.run()
