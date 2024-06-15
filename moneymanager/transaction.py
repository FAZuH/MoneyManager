from datetime import datetime
from typing import Literal


class Transaction:
# no;date;account;amount;type;category;comment
    def __init__(
        self,
        date: datetime,
        account: str,
        amount: float,
        type_: Literal["expense", "income"],
        category: str,
        comment: str
    ) -> None:
        self.date = date
        self.account = account
        self.amount = amount
        self.type_ = type_
        self.category = category
        self.comment = comment

