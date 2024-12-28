from typing import Protocol


class Repository[T, ID](Protocol):
    def insert(self, entity: T) -> None:
        pass

    def update(self, entity: T) -> None:
        pass

    def delete(self, identifier: ID) -> None:
        pass
