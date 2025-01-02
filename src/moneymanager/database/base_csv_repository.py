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
    def __init__(self) -> None:
        self._base_dir = "userdata"
        self._base_path = os.path.join(os.getcwd(), self._base_dir)
        self._csv_path = os.path.join(self._base_path, self.filename)
        self._fieldnames = [k for k in self.model.__dataclass_fields__]
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
    def enter_reader(self, mode: str = "r") -> Generator[csv.DictReader, None, None]:
        """Context manager that yields a CSV reader object.

        Parameters
        ----------
        mode : `str`
            The mode to open the file in. Defaults to "r".

        Yields
        ------
        `csv._reader`
            A CSV reader object with line terminator set to ";"

        Examples
        --------
        >>> with obj.enter_reader() as reader:
        ...     for row in reader:
        ...         print(row)
        """
        with open(self._csv_path, mode, newline="") as stream:
            reader = csv.DictReader(stream, fieldnames=self._fieldnames, lineterminator=";\n")
            next(reader)  # Skip the header
            yield reader

    @contextmanager
    def enter_writer(self, mode: str = "a") -> Generator[csv.DictWriter, None, None]:
        """Context manager that yields a CSV writer object.

        Parameters
        ----------
        mode : `str`
            The mode to open the file in. Defaults to "a".

        Yields
        ------
        `csv.writer`
            A CSV writer object with line terminator set to ";"

        Examples
        --------
        >>> with obj.enter_writer() as writer:
        ...     writer.writerow(['column1', 'column2'])
        ...     writer.writerow(['data1', 'data2'])
        """
        with open(self._csv_path, mode, newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=self._fieldnames, lineterminator=";\n")
            yield writer

    def _init_path(self) -> None:
        """Checks if the csv file exists, and create if not."""
        # NOTE: Remove this shit
        os.makedirs(self._base_path, exist_ok=True)
        if os.path.exists(self._csv_path):
            return
        with self.enter_writer() as writer:
            writer.writeheader()
