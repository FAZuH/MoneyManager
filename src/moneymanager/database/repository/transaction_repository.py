from dataclasses import asdict

from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.model.transaction import Transaction
from moneymanager.database.repository.repository import Repository


class TransactionRepository(BaseCsvRepository, Repository[Transaction, str]):
    def select(self, identifier: str) -> Transaction:
        with self.enter_reader() as reader:
            for row in reader:
                if row["uuid"] == identifier:
                    return self.model(**row)  # type: ignore
        raise ValueError(f"Transaction with id {identifier} not found")

    def insert(self, entity: Transaction) -> None:
        row = asdict(entity)
        with self.enter_writer() as writer:
            writer.writerow(row)

    def update(self, identifier: str, entity: Transaction) -> None:
        with self.enter_reader() as reader:
            rows = [row for row in reader]
        with self.enter_writer("w") as writer:
            for row in rows:
                if row["uuid"] == identifier:
                    row = asdict(entity)
                writer.writerow(row)

    def delete(self, identifier: str) -> None:
        with self.enter_reader() as reader:
            rows = [row for row in reader if row["uuid"] != identifier]
        with self.enter_writer("w") as writer:
            for row in rows:
                writer.writerow(row)

    def select_all(self) -> list[Transaction]:
        with self.enter_reader() as reader:
            return [self.model(**row) for row in reader]  # type: ignore

    @property
    def filename(self) -> str:
        return "transaction_history.csv"

    @property
    def model(self) -> type[Transaction]:
        return Transaction
