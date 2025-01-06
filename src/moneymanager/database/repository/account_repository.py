from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.model.account import Account
from moneymanager.database.repository.repository import Repository
from dataclasses import asdict


class AccountRepository(BaseCsvRepository, Repository[Account, str]):
    def select(self, identifier: str) -> Account:
        with self.enter_reader() as reader:
            for row in reader:
                if row["name"] == identifier:
                    return self.model(**row)  # type: ignore
        raise ValueError(f"Account with name {identifier} not found")

    def insert(self, entity: Account) -> None:
        if self.find(entity.name):
            raise ValueError(f"Account with name {entity.name} already exists")
        row = asdict(entity)
        with self.enter_writer() as writer:
            writer.writerow(row)

    def update(self, identifier: str, entity: Account) -> None:
        if not self.find(identifier):
            raise ValueError(f"Account with id {identifier} not found")
        with self.enter_reader() as reader:
            rows = list(reader)
        with self.enter_writer("w") as writer:
            writer.writeheader()
            for row in rows:
                if row["name"] == identifier:
                    row = asdict(entity)
                writer.writerow(row)

    def delete(self, identifier: str) -> None:
        if not self.find(identifier):
            raise ValueError(f"Account with id {identifier} not found")
        with self.enter_reader() as reader:
            rows = [row for row in reader if row["name"] != identifier]
        with self.enter_writer("w") as writer:
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

    def select_all(self) -> list[Account]:
        with self.enter_reader() as reader:
            return [self.model(**row) for row in reader]  # type: ignore

    def find(self, identifier: str) -> bool:
        with self.enter_reader() as reader:
            for row in reader:
                if row["name"] == identifier:
                    return True
        return False

    @property
    def filename(self) -> str:
        return "accounts.csv"

    @property
    def model(self) -> type[Account]:
        return Account
