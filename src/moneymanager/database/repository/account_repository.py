from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.model.account import Account
from moneymanager.database.repository.repository import Repository


class AccountRepository(BaseCsvRepository, Repository[Account, str]):
    def select(self, identifier: str) -> Account: ...

    def insert(self, entity: Account) -> None: ...

    def update(self, identifier: str, entity: Account) -> None: ...

    def delete(self, identifier: str) -> None: ...
    def select_all(self) -> list[Account]:
        with self.enter_reader() as reader:
            return [self.model(**row) for row in list(reader)[1:]]  # type: ignore

    @property
    def filename(self) -> str:
        return "accounts.csv"

    @property
    def model(self) -> type[Account]:
        return Account
