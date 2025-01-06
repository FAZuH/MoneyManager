from dataclasses import dataclass


@dataclass
class Account:
    name: str
    balance: float

    def __post_init__(self) -> None:
        if isinstance(self.balance, str):
            self.balance = float(self.balance)
