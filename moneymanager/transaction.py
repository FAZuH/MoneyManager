from __future__ import annotations
from datetime import datetime
from typing import Literal


class Transaction:

    def __init__(
        self,
        id_: int,
        date: datetime,
        account: str,
        amount: float,
        type_: Literal["expense", "income"],
        category: str,
        comment: str
    ) -> None:
        self.id = id_
        self.date = date
        self.account = account
        self.amount = amount
        self.type_ = type_
        self.category = category
        self.comment = comment

    def to_list(self) -> list[str]:
        ret = [
            str(self.id),
            self.date.isoformat(),
            self.account,
            str(self.amount),
            self.type_,
            self.category,
            self.comment
        ]
        return ret

    @classmethod
    def from_list(cls, transaction_list: list[str]) -> Transaction:
        ret = cls(
            int(transaction_list[0]),
            datetime.fromisoformat(transaction_list[1]),
            transaction_list[2],
            float(transaction_list[3]),
            transaction_list[4],  # type: ignore
            transaction_list[5],
            transaction_list[6]
        )
        return ret

