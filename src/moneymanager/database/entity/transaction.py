from dataclasses import dataclass
from datetime import datetime
from typing import Any, Literal, Self


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

    @classmethod
    def from_list(cls, data: list[Any]) -> Self:
        return cls(
            data[0],
            data[1] if isinstance(data[1], datetime) else datetime.fromisoformat(data[1]),
            data[2],
            data[3] if isinstance(data[3], float) else float(data[3]),
            data[4],
            data[5],
            data[6],
        )
