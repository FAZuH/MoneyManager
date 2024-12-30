from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from contextlib import contextmanager
import csv
import os
import shutil
from typing import Generator, TYPE_CHECKING

if TYPE_CHECKING:
    from _csv import _reader
    from _csv import _writer


class BaseCsvRepository(ABC):
    def __init__(self) -> None:
        self._base_dir = "userdata"
        self._base_path = os.path.join(os.getcwd(), self._base_dir)
        self._csv_path = os.path.join(self._base_path, self.filename)
        self._init_path()

    @property
    @abstractmethod
    def filename(self) -> str:
        """File name of the CSV."""

    @contextmanager
    def enter_reader(self, mode: str = "r") -> Generator[_reader, None, None]:
        """Context manager that yields a CSV reader object.

        Yields
        -------
        `csv._reader`
            A CSV reader object with line terminator set to ";"

        Examples
        --------
        >>> with obj.enter_reader() as reader:
        ...     for row in reader:
        ...         print(row)

        """
        with open(self._csv_path, mode, newline="") as stream:
            reader = csv.reader(stream, lineterminator=";\n")
            yield reader

    @contextmanager
    def enter_writer(self, mode: str = "a") -> Generator[_writer, None, None]:
        """Context manager that yields a CSV writer object.

        Yields
        -------
        `csv.writer`
            A CSV writer object with line terminator set to ";"

        Examples
        --------
        >>> with obj.enter_writer() as writer:
        ...     writer.writerow(['column1', 'column2'])
        ...     writer.writerow(['data1', 'data2'])
        """
        with open(self._csv_path, mode, newline="") as stream:
            writer = csv.writer(stream, lineterminator=";\n")
            yield writer

    def _init_path(self) -> None:
        """Checks if the path exists, and create from template if not."""
        if os.path.exists(self._csv_path):
            return

        os.makedirs(self._base_path, exist_ok=True)

        template_path = self._csv_path + ".template"
        shutil.copy(template_path, self._csv_path)
