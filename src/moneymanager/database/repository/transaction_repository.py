from dataclasses import asdict

from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.model.transaction import Transaction
from moneymanager.database.repository.repository import Repository


class TransactionRepository(BaseCsvRepository, Repository[Transaction, str]):
    def select(self, identifier: str) -> Transaction:
        # if not self.find(identifier):
        #     raise ValueError(f"Transaction with id {identifier} not found")
        with self.enter_reader() as reader:
            for row in reader:
                if row["uuid"] == identifier:
                    return self.model(**row)  # type: ignore
        raise ValueError(f"Transaction with id {identifier} not found")

    def insert(self, entity: Transaction) -> None:
        if self.find(entity.uuid):
            raise ValueError(f"Transaction with id {entity.uuid} already exists")
        row = asdict(entity)
        with self.enter_writer() as writer:
            writer.writerow(row)

    def update(self, identifier: str, entity: Transaction) -> None:
        if not self.find(identifier):
            raise ValueError(f"Transaction with id {identifier} not found")
        with self.enter_reader() as reader:
            rows = list(reader)
        with self.enter_writer("w") as writer:
            writer.writeheader()
            for row in rows:
                if row["uuid"] == identifier:
                    row = asdict(entity)
                writer.writerow(row)

    def delete(self, identifier: str) -> None:
        if not self.find(identifier):
            raise ValueError(f"Transaction with id {identifier} not found")
        with self.enter_reader() as reader:
            rows = [row for row in reader if row["uuid"] != identifier]
        with self.enter_writer("w") as writer:
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

    def select_all(self) -> list[Transaction]:
        with self.enter_reader() as reader:
            return [self.model(**row) for row in reader]  # type: ignore

    def find(self, identifier: str) -> bool:
        with self.enter_reader() as reader:
            for row in reader:
                if row["uuid"] == identifier:
                    return True
        return False

    @property
    def filename(self) -> str:
        return "transaction_history.csv"

    @property
    def model(self) -> type[Transaction]:
        return Transaction
