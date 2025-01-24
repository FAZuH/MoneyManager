"""Base CSV repository module."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from contextlib import contextmanager
import csv
import os
from typing import Generator, TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import DataclassInstance


class BaseCsvRepository(ABC):
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


    class ConcreteCsvRepository(BaseCsvRepository):
        @property
        def filename(self):
            return "concrete.csv"

        @property
        def model(self):
            return ConcreteModel


    @dataclass
    class ConcreteModel:
        column1: str
        column2: int
    ```

    You can then use the concrete repository like this:

    >>> concrete_repo = ConcreteCsvRepository()
    >>> with concrete_repo.enter_writer() as writer:
    ...     writer.writeheader()
    ...     writer.writerow({'column1': 'value1', 'column2': 1})
    >>> with concrete_repo.enter_reader() as reader:
    ...     for row in reader:
    ...         print(row)
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
    def model(self) -> type[DataclassInstance]:
        """Model class of the CSV.

        Override this with the concrete class' own model.
        """

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
            try:
                next(reader)  # Skip the header
            except StopIteration:
                pass
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
        with self._enter_writer() as writer:
            writer.writeheader()
