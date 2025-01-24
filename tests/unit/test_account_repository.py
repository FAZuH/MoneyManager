import pytest

from moneymanager.database.repository.account_repository import AccountRepository
from tests.unit.base_repository_test import BaseRepositoryTest


class TestAccountRepository(BaseRepositoryTest):
    @property
    def repository_class(self):
        return AccountRepository

    @property
    def test_data(self):
        return {"name": "Savings", "balance": "1000.50"}

    def test_insert_and_select(self, repo):
        test_account = repo.model(**self.test_data)
        repo.insert(test_account)

        result = repo.select(test_account.name)
        assert result.name == test_account.name
        assert result.balance == 1000.50
        assert isinstance(result.balance, float)

    def test_update(self, repo):
        account = repo.model(**self.test_data)
        repo.insert(account)

        updated = repo.model(name=account.name, balance="2000.00")
        repo.update(account.name, updated)

        result = repo.select(account.name)
        assert result.balance == 2000.00

    def test_delete(self, repo):
        test_entity = repo.model(**self.test_data)
        repo.insert(test_entity)

        repo.delete(test_entity.name)
        with pytest.raises(ValueError):
            repo.select(test_entity.name)

    def test_select_all(self, repo):
        accounts = [repo.model("Account1", "100.00"), repo.model("Account2", "200.00")]
        for account in accounts:
            repo.insert(account)

        results = repo.select_all()
        assert all(isinstance(a.balance, float) for a in results)
        assert sum(a.balance for a in results) == 300.00
