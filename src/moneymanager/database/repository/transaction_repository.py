import csv

from moneymanager.database.entity.transaction import Transaction
from moneymanager.database.repository.repository import Repository


class TransactionRepository(Repository[Transaction, str]):
    TRANSACTION_HISTORY_PATH: str = "userdata/transaction_history.csv"

    def select_all(self) -> list[Transaction]:
        with open(self.TRANSACTION_HISTORY_PATH) as stream:
            transactions_data = csv.reader(stream)
            transactions_list = list(transactions_data)
            return [Transaction.from_list(transaction) for transaction in transactions_list]

    def insert(self, entity: Transaction) -> None:
        row = entity.to_list()
        with open(self.TRANSACTION_HISTORY_PATH, "a", newline="") as stream:
            writer = csv.writer(stream, lineterminator="\n")
            writer.writerow(row)

    def update(self, entity: Transaction) -> None:
        pass

    def delete(self, identifier: str) -> None:
        pass

    def select(self, identifier: str) -> Transaction:
        with open(self.TRANSACTION_HISTORY_PATH) as stream:
            transactions_data = csv.reader(stream)

            for transaction in transactions_data:
                if transaction[0] == identifier:
                    return Transaction.from_list(transaction)
        raise ValueError(f"Transaction with id {identifier} not found")

    def _read_transaction_history(self) -> list[list[str]]:
        with open(self.TRANSACTION_HISTORY_PATH) as stream:
            transactions_data = csv.reader(stream)

            transactions_list = list(transactions_data)
            return transactions_list
