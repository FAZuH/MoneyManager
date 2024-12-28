from typing import TYPE_CHECKING, Any

from moneymanager.repository.repository import Repository

if TYPE_CHECKING:
    from moneymanager.entity.account import Account


class AccountRepository(Repository[Account, str]):
    def insert(self, entity: Account) -> None:
        return

    def update(self, entity: Account) -> None:
        return

    def delete(self, identifier: str) -> None:
        return
