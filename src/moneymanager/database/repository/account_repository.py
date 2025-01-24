from typing import override
from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.model.account import Account


class AccountRepository(BaseCsvRepository):
    @property
    @override
    def filename(self) -> str:
        return "accounts.csv"

    @property
    @override
    def model(self) -> type[Account]:
        return Account
