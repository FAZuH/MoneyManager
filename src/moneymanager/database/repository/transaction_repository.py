from dataclasses import asdict
from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.entity.transaction import Transaction
from moneymanager.database.repository.repository import Repository


class TransactionRepository(BaseCsvRepository, Repository[Transaction, str]):
    def select(self, identifier: str) -> Transaction:
        with self.enter_reader() as reader:
            for row in reader:
                if row["uuid"] == identifier:
                    return Transaction(**row)  # type: ignore
        raise ValueError(f"Transaction with id {identifier} not found")

    def insert(self, entity: Transaction) -> None:
        row = asdict(entity)
        with self.enter_writer() as writer:
            writer.writerow(row)

    def update(self, entity: Transaction) -> None:
        pass

    def delete(self, identifier: str) -> None:
        pass

    def select_all(self) -> list[Transaction]:
        with self.enter_reader() as reader:
            return [Transaction(**row) for row in reader]  # type: ignore

    @property
    def filename(self) -> str:
        return "transaction_history.csv"

    @property
    def model(self) -> type[Transaction]:
        return Transaction
