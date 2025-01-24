from typing import override
from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.model.transaction import Transaction


class TransactionRepository(BaseCsvRepository):
    @property
    @override
    def filename(self) -> str:
        return "transaction_history.csv"

    @property
    @override
    def model(self) -> type[Transaction]:
        return Transaction
