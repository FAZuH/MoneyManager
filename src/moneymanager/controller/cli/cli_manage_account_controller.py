from __future__ import annotations

from typing import override, TYPE_CHECKING

from moneymanager.controller.base_controller import BaseController
from moneymanager.exception import UserCancel
from moneymanager.view.cli.cli_manage_account_view import CliManageAccountView

if TYPE_CHECKING:
    from moneymanager.app.app import App


class CliManageAccountController(BaseController):
    def __init__(self, app: App) -> None:
        super().__init__(app)
        self._view = CliManageAccountView()
        self._repository = self.app.database.account_repository

    @override
    def run(self) -> None:
        # clear view
        self._view.clear_view()
        # show accounts
        self._display_all_accounts()
        self._view.display_line_separator()
        # prompt action to take

        while True:
            try:
                action = self._view.prompt_action()
                self._view.display_line_separator()
                match action:
                    case 1:
                        self._add_account()
                    case 2:
                        self._edit_account()
                    case 3:
                        self._delete_account()
                    case 4:
                        return
            except UserCancel:  # For exeption UserCancel (user typing "cancel" to cancel option)
                return

    def _add_account(self) -> None:
        self._view.display_message("Enter account details:")
        name = self._view.prompt_account_name()
        balance = self._view.prompt_account_balance()
        model = self._repository.model(name, balance)

        self._repository.insert(model)

        self._view.display_message(f"\nSuccessfully added account {name} with balance ${balance}")

    def _edit_account(self) -> None:
        self._display_all_accounts()

        self._view.display_message("Enter account to edit:")

        name = self._view.prompt_account_name()

        self._view.display_line_separator()

        # TODO: handle invalid account
        try:  # Try exept for account with name (name) doesn't exist
            model = self._repository.select(name)
        except ValueError:
            print(f"The account with name {name} doesn't exist")
            self._edit_account()
            return

        self._view.display_message("Current account details:")
        self._view.display_account(model.name, model.balance)
        self._view.display_line_separator()

        self._view.display_message("Enter new details:")
        model.name = self._view.prompt_account_name()
        model.balance = self._view.prompt_account_balance()

        self._repository.update(name, model)

    def _delete_account(self) -> None:
        self._display_all_accounts()

        self._view.display_message("Enter account to delete:")
        name = self._view.prompt_account_name()

        inp = self._view.must_get_input(
            "Are you sure you want to delete this account? (y/n): ", str
        )
        if inp.lower() == "y":
            self._repository.delete(name)
            self._view.display_message(f"Successfully deleted account {name}")
        else:
            self._view.display_message("Account deletion cancelled")

    def _display_all_accounts(self) -> None:
        accounts = self._repository.select_all()
        self._view.display_message("Accounts:")
        self._view.display_line_separator()
        for acc in accounts:
            self._view.display_account(acc.name, acc.balance)
