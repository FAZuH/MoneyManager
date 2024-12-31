from dataclasses import dataclass


@dataclass
class Account:
    name: str
    balance: float

    def __post_init__(self) -> None:
        if not isinstance(self.initial_balance, float):
            self.initial_balance = float(self.initial_balance)
