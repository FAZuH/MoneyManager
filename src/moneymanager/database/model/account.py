from dataclasses import dataclass

from moneymanager.database.model.model import Model


@dataclass
class Account(Model[str]):
    name: str  # Primary Key
    balance: float

    def __post_init__(self) -> None:
        if isinstance(self.balance, str):
            self.balance = float(self.balance)

    @property
    def primary_key(self) -> str:
        return self.name

    @classmethod
    def primary_field(cls) -> str:
        return "name"
