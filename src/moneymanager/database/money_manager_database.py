from moneymanager.database.repository.account_repository import AccountRepository
from moneymanager.database.repository.transaction_repository import TransactionRepository


class MoneyManagerDatabase:
    def __init__(self) -> None:
        self.transaction_repository = TransactionRepository()
        self.account_repository = AccountRepository()
