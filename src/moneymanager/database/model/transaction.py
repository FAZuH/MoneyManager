from dataclasses import dataclass
from datetime import datetime
from typing import Literal


@dataclass
class Transaction:
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
