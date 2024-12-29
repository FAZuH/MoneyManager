from typing import TYPE_CHECKING, Any

from moneymanager.database.repository.repository import Repository

if TYPE_CHECKING:
    from moneymanager.database.entity.account import Account


class AccountRepository(Repository[Account, str]):
    def select(self, identifier: str) -> Account: ...

    def insert(self, entity: Account) -> None:
        return

    def update(self, entity: Account) -> None:
        return

    def delete(self, identifier: str) -> None:
        return
