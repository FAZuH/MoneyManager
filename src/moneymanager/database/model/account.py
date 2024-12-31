from dataclasses import dataclass
from typing import Any, Self


@dataclass
class Account:
    name: str
    balance: float

    def to_list(self) -> list[Any]:
        return [self.name, self.initial_balance]

    @classmethod
    def from_list(cls, data: list[Any]) -> Self:
        return cls(data[0], data[1] if isinstance(data[1], float) else float(data[1]))
