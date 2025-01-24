"""Base CSV repository module."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from contextlib import contextmanager
import csv
from dataclasses import asdict
import os
from typing import Generator, override

from moneymanager.database.repository.repository import Repository
from moneymanager.database.model.model import Model


class BaseCsvRepository[ID](ABC, Repository[ID]):
    """Abstract base class of a CSV repository.

    Extend this class to create a concrete CSV repository. The concrete class should
    implement the `filename` and `model` abstract properties. The `filename` property
    should return the name of the CSV file, while the `model` property should return
    the dataclass model of the CSV file.

    Examples
    --------
    ```python
    from dataclasses import dataclass

    from moneymanager.database.base_csv_repository import BaseCsvRepository


    @dataclass
    class ConcreteModel(Model[str]):
        id: int
        col1: str
        col2: int

        @property
        def primary_key(self):
            return self.id

        @classmethod
        def primary_field(cls):
            return "id"


    class ConcreteCsvRepository(BaseCsvRepository):
        @property
        def filename(self):
            return "concrete.csv"

        @property
        def model(self):
            return ConcreteModel
    ```

    You can then use the concrete repository like this:

    >>> concrete_repo = ConcreteCsvRepository()
    >>> concrete_repo.insert(ConcreteModel(1, "value1", 100))
    >>> concrete_repo.select(1)
    ConcreteModel(id=1, col1='value1', col2=100)
    >>> concrete_repo.update(1, ConcreteModel(1, "value2", 200))
    >>> concrete_repo.select(1)
    ConcreteModel(id=1, col1='value2', col2=200)
    >>> concrete_repo.delete(1)
    >>> concrete_repo.select(1)
    ValueError: Model with key 1 is not found.
    """

    def __init__(self, base_dir: str = "userdata") -> None:
        self._base_dir = base_dir
        self._base_path = os.path.join(os.getcwd(), self._base_dir)
        """Path of the base CSV directory."""
        self._csv_path = os.path.join(self._base_path, self.filename)
        """Path of the CSV file."""
        self._fieldnames = [k for k in self.model.__dataclass_fields__]
        """Field/column names of the CSV file."""
        self._init_path()

    @property
    @abstractmethod
    def filename(self) -> str:
        """File name of the CSV."""

    @property
    @abstractmethod
    def model(self) -> type[Model[ID]]:
        """Model class of the repository."""

    @override
    def select(self, identifier: ID) -> Model[ID]:
        with self._enter_reader() as reader:
            for row in reader:
                if row[self.model.primary_field()] == identifier:
                    return self.model(**row)

        # If account with name identifier not found
        raise ValueError(f"Account with name {identifier} not found")

    @override
    def insert(self, entity: Model[ID]) -> None:  # Method for inserting a new account
        with self._enter_reader() as reader:
            for row in reader:
                if row[self.model.primary_field()] == entity.primary_key:
                    # If account name is already exist
                    raise ValueError(f"Model with key {entity.primary_field} is already exists.")

        # The account hasn't been created
        with self._enter_writer() as writer:
            writer.writerow(asdict(entity))

    @override
    def update(self, identifier: ID, entity: Model[ID]) -> None:
        new_rows = []
        found = False
        with self._enter_reader() as reader:
            for row in reader:
                if row[self.model.primary_field()] == identifier:
                    assert found is False, f"Found duplicate row with key {identifier}."
                    found = True
                    row = asdict(entity)
                new_rows.append(row)

        if found is False:
            raise ValueError(f"Model with key {identifier} is not found.")

        with self._enter_writer(mode="w") as writer:
            writer.writerows(new_rows)

    @override
    def delete(self, identifier: ID) -> None:
        found = False
        with self._enter_reader() as reader:
            rows = list(reader)

        with self._enter_writer("w") as writer:
            for row in rows:
                if row[self.model.primary_field()] != identifier:
                    writer.writerow(row)
                else:
                    found = True

        if found is False:
            raise ValueError(f"Model with key {identifier} is not found.")

    @override
    def select_all(self) -> list[Model[ID]]:
        with self._enter_reader() as reader:
            return [self.model(**row) for row in reader]  # type: ignore

    @override
    def exists(self, identifier: ID) -> bool:
        with self._enter_reader() as reader:
            for row in reader:
                if row[self.model.primary_field()] == identifier:
                    return True
        return False

    @contextmanager
    def _enter_reader(self, mode: str = "r") -> Generator[csv.DictReader, None, None]:
        """Context manager that yields a CSV reader object.

        Parameters
        ----------
        mode : `str`
            The mode to open the file in. Defaults to "r".

        Yields
        ------
        `DictReader`
            A `DictReader` object from `csv` library.

        Examples
        --------
        >>> with concrete_repo.enter_reader() as reader:
        ...     for row in reader:
        ...         print(row)
        """
        with open(self._csv_path, mode, newline="") as stream:
            reader = csv.DictReader(stream, fieldnames=self._fieldnames)
            # try:
            #     next(reader)  # Skip the header
            # except StopIteration:
            #     pass
            yield reader

    @contextmanager
    def _enter_writer(self, mode: str = "a") -> Generator[csv.DictWriter, None, None]:
        """Context manager that yields a CSV writer object.

        Parameters
        ----------
        mode : `str`
            The mode to open the file in. Defaults to "a".

        Yields
        ------
        `DictWriter`
            A `DictWriter` object from `csv` library.

        Examples
        --------
        >>> with concrete_repo.enter_writer() as writer:
        ...     writer.writerow({'column1': value1, 'column2': value2})
        """
        with open(self._csv_path, mode, newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=self._fieldnames)
            yield writer

    def _init_path(self) -> None:
        """Checks if the csv file exists, and create if not."""
        os.makedirs(self._base_path, exist_ok=True)
        if os.path.exists(self._csv_path):
            return
        with self._enter_writer():
            pass
