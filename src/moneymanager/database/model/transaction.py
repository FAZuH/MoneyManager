from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from moneymanager.database.model.model import Model


@dataclass
class Transaction(Model[str]):
    uuid: str  # NOTE: UUID
    date: datetime
    account: str
    amount: float
    type_: Literal["expense", "income"]
    category: str
    comment: str

    def __post_init__(self) -> None:
        if not isinstance(self.date, datetime):
            self.date = datetime.fromisoformat(self.date)
        if not isinstance(self.amount, float):
            self.amount = float(self.amount)

    @property
    def primary_key(self) -> str:
        return self.uuid

    @classmethod
    def primary_field(cls) -> str:
        return "uuid"