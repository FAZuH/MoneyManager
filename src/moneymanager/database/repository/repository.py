from typing import Protocol

from moneymanager.database.model.model import Model


class Repository[T: Model, ID](Protocol):
    def select(self, identifier: ID) -> T:
        """Selects an entry from the database.

        Parameters
        ----------
        identifier : `ID`
            The unique identifier of the entry to select.

        Returns
        -------
        `T`
            The selected entry.

        Raises
        ------
        `ValueError`
            If the entry with the given identifier does not exist.
        """
        ...

    def insert(self, entity: ID) -> None:
        """Inserts a new entry into the database.

        Parameters
        ----------
        entity : `T`
            The entity to insert.

        Raises
        ------
        `ValueError`
            If the entry already exists.
        """
        ...

    def update(self, identifier: ID, entity: T) -> None:
        """Updates an entry in the database.

        Parameters
        ----------
        identifier : `ID`
            The unique identifier of the entry to update.
        entity : `T`
            The new entity to replace the old one.

        Raises
        ------
        `ValueError`
            If the entry with the given identifier does not exist.
        """
        ...

    def delete(self, identifier: ID) -> None:
        """Deletes an entry from the database.

        Parameters
        ----------
        identifier : `ID`
            The unique identifier of the entry to delete.

        Raises
        ------
        `ValueError`
            If the entry with the given identifier does not exist.
        """
        ...

    def select_all(self) -> list[T]:
        """Selects all entries from the database.

        Returns
        -------
        `List[T]`
            A list of all entries in the database.
        """
        ...

    def exists(self, identifier: ID) -> bool:
        """Checks if an entry exists in the database.

        Parameters
        ----------
        identifier : `ID`
            The unique identifier of the entry to check.

        Returns
        -------
        `bool`
            `True` if the entry exists, `False` otherwise.
        """
        ...
