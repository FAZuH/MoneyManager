import csv
from typing import TYPE_CHECKING
from uuid import UUID

from moneymanager.repository.repository import Repository

if TYPE_CHECKING:
    from moneymanager.entity.transaction import Transaction


class TransactionRepository(Repository[Transaction, str]):
    TRANSACTION_HISTORY_PATH = "userdata/transaction_history.csv"

    def insert(self, entity: Transaction) -> None:
        new_transaction_list = entity.to_list()
        new_row = [*new_transaction_list]

        with open(self.TRANSACTION_HISTORY_PATH, "a", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(new_row)

    def update(self, entity: Transaction) -> None:
        pass

    def delete(self, identifier: str) -> None:
        pass

    def _read_transaction_history(self) -> list[list[str]]:
        with open(self.TRANSACTION_HISTORY_PATH) as stream:
            transactions_data = csv.reader(stream)

            transactions_list = list(transactions_data)
            return transactions_list
