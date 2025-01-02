from typing import Protocol


class Repository[T, ID](Protocol):
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

    def insert(self, entity: T) -> None:
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
