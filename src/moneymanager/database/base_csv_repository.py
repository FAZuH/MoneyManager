from __future__ import annotations
from abc import ABC, abstractmethod
from contextlib import contextmanager
import csv
from typing import Generator, TYPE_CHECKING

if TYPE_CHECKING:
    from _csv import _reader, _writer


class BaseCsvRepository(ABC):
    @contextmanager
    def enter_reader(self) -> Generator[_reader, None, None]:
        """Context manager that yields a CSV reader object.

        Yields
        -------
        csv._reader
            A CSV reader object with line terminator set to ";"

        Examples
        --------
        >>> with obj.enter_reader() as reader:
        ...     for row in reader:
        ...         print(row)

        """
        with open(self.path, "r") as stream:
            reader = csv.reader(stream, lineterminator=";")
            yield reader

    @contextmanager
    def enter_writer(self) -> Generator[_writer, None, None]:
        """Context manager that yields a CSV writer object.

        Yields
        -------
        csv.writer
            A CSV writer object with line terminator set to ";"

        Examples
        --------
        >>> with obj.enter_writer() as writer:
        ...     writer.writerow(['column1', 'column2'])
        ...     writer.writerow(['data1', 'data2'])
        """
        with open(self.path, "w") as stream:
            writer = csv.writer(stream, lineterminator=";")
            yield writer

    @property
    @abstractmethod
    def path(self) -> str: ...
