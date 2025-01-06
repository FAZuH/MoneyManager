
from abc import ABC, abstractmethod
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
        with repo.enter_writer('w') as writer:
            writer.writeheader()
            writer.writerow(self.test_data)
        
        with repo.enter_reader() as reader:
            rows = list(reader)
            assert len(rows) == 1
            for key, value in self.test_data.items():
                assert str(value) == rows[0][key]