from dataclasses import dataclass
from datetime import datetime
from typing import Any, Literal


@dataclass
class Transaction:
    uuid: str  # NOTE: UUID
    date: datetime
    account: str
    amount: float
    type_: Literal["expense", "income"]
    category: str
    comment: str

    def to_list(self) -> list[Any]:
        return [
            self.uuid,
            self.date,
            self.account,
            self.amount,
            self.type_,
            self.category,
            self.comment,
        ]
