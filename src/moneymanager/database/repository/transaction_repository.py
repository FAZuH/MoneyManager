from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.entity.transaction import Transaction
from moneymanager.database.repository.repository import Repository


class TransactionRepository(BaseCsvRepository, Repository[Transaction, str]):
    def select(self, identifier: str) -> Transaction:
        with self.enter_reader() as reader:
            for transaction in reader:
                if transaction[0] == identifier:
                    return Transaction.from_list(transaction)
        raise ValueError(f"Transaction with id {identifier} not found")

    def insert(self, entity: Transaction) -> None:
        row = entity.to_list()
        with self.enter_writer() as writer:
            writer.writerow(row)

    def update(self, entity: Transaction) -> None:
        pass

    def delete(self, identifier: str) -> None:
        pass

    def select_all(self) -> list[Transaction]:
        with self.enter_reader() as reader:
            return [Transaction.from_list(transaction) for transaction in reader]

    @property
    def filename(self) -> str:
        return "transaction_history.csv"
