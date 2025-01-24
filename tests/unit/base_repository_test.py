from abc import ABC
from abc import abstractmethod
import os
from typing import Any, Type

import pytest


class BaseRepositoryTest(ABC):
    @property
    @abstractmethod
    def repository_class(self) -> Type:
        """Return the concrete repository class to test"""

    @property
    @abstractmethod
    def test_data(self) -> dict[str, Any]:
        """Return sample data matching the repository's model"""

    @pytest.fixture
    def repo(self):
        repo = self.repository_class("userdata_test")
        yield repo
        if os.path.exists(repo._csv_path):
            os.remove(repo._csv_path)
        if os.path.exists(repo._base_path):
            os.rmdir(repo._base_path)

    def test_init_creates_files(self, repo):
        assert os.path.exists(repo._base_path)
        assert os.path.exists(repo._csv_path)

    def test_write_and_read(self, repo):
        with repo._enter_writer("w") as writer:
            writer.writerow(self.test_data)

        with repo._enter_reader() as reader:
            rows = list(reader)
            assert len(rows) == 1
            for key, value in self.test_data.items():
                assert str(value) == rows[0][key]

    def test_insert_duplicate(self, repo):
        test_entity = repo.model(**self.test_data)
        repo.insert(test_entity)

        with pytest.raises(ValueError):
            repo.insert(test_entity)

    def test_select_not_found(self, repo):
        with pytest.raises(ValueError):
            repo.select("nonexistent")

    def test_update_not_found(self, repo):
        with pytest.raises(ValueError):
            repo.update("nonexistent", repo.model(**self.test_data))

    def test_delete_not_found(self, repo):
        with pytest.raises(ValueError):
            repo.delete("nonexistent")
