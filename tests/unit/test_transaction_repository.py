from datetime import datetime
from uuid import uuid4

import pytest

from moneymanager.database.repository.transaction_repository import TransactionRepository
from tests.unit.base_repository_test import BaseRepositoryTest


class TestTransactionRepository(BaseRepositoryTest):
    @property
    def repository_class(self):
        return TransactionRepository

    @property
    def test_data(self):
        return {
            "uuid": "9b8cc3e0-120e-44ae-8de7-d1c912031c3f",
            "date": "2024-01-01T12:00:00",
            "account": "Cash",
            "amount": "42.50",
            "type_": "expense",
            "category": "Food",
            "comment": "Lunch",
        }

    def test_insert_and_select(self, repo):
        test_entity = repo.model(**self.test_data)
        repo.insert(test_entity)

        result = repo.select(test_entity.uuid)
        assert result.uuid == test_entity.uuid
        assert result.amount == 42.50
        assert isinstance(result.date, datetime)

    def test_update(self, repo):
        test_entity = repo.model(**self.test_data)
        repo.insert(test_entity)

        updated = repo.model(**{**self.test_data, "amount": "100.00"})
        repo.update(test_entity.uuid, updated)

        result = repo.select(test_entity.uuid)
        assert result.amount == 100.00

    def test_delete(self, repo):
        test_entity = repo.model(**self.test_data)
        repo.insert(test_entity)

        repo.delete(test_entity.uuid)
        with pytest.raises(ValueError):
            repo.select(test_entity.uuid)

    def test_select_all(self, repo):
        test_entity1 = repo.model(**self.test_data)
        test_entity2 = repo.model(**{**self.test_data, "uuid": str(uuid4())})

        repo.insert(test_entity1)
        repo.insert(test_entity2)

        results = repo.select_all()
        assert len(results) == 2
        assert all(isinstance(r, repo.model) for r in results)
