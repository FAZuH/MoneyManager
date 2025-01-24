from moneymanager.database.repository.account_repository import AccountRepository
from moneymanager.database.repository.transaction_repository import TransactionRepository


class MoneymanagerDatabase:
    def __init__(self) -> None:
        self._transaction_repository = TransactionRepository()
        self._account_repository = AccountRepository()

    @property
    def transaction_repository(self) -> TransactionRepository:
        return self._transaction_repository

    @property
    def account_repository(self) -> AccountRepository:
        return self._account_repository
