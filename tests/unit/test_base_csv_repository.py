from dataclasses import dataclass
import os

import pytest

from moneymanager.database.base_csv_repository import BaseCsvRepository


@dataclass
class TestModel:
    name: str
    value: int


class TestRepository(BaseCsvRepository):
    @property
    def filename(self) -> str:
        return "test.csv"

    @property
    def model(self) -> type:
        return TestModel


@pytest.fixture
def repo():
    repo = TestRepository("userdata_test")
    yield repo
    # Cleanup after tests
    if os.path.exists(repo._csv_path):
        os.remove(repo._csv_path)
    if os.path.exists(repo._base_path):
        os.rmdir(repo._base_path)


def test_init_creates_directory_and_file(repo):
    assert os.path.exists(repo._base_path)
    assert os.path.exists(repo._csv_path)


def test_fieldnames_match_model(repo):
    expected = ["name", "value"]
    assert repo._fieldnames == expected


def test_writer_creates_header(repo):
    with repo._enter_writer("w") as writer:
        writer.writeheader()

    with open(repo._csv_path, "r") as f:
        content = f.read()
        assert "name,value" in content


def test_write_and_read_row(repo):
    test_data = {"name": "test", "value": 42}

    with repo._enter_writer("w") as writer:
        writer.writerow(test_data)

    with repo._enter_reader() as reader:
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["name"] == test_data["name"]
        assert rows[0]["value"] == str(test_data["value"])


def test_append_mode(repo):
    data = [{"name": "first", "value": 1}, {"name": "second", "value": 2}]

    with repo._enter_writer("w") as writer:
        writer.writerow(data[0])

    with repo._enter_writer("a") as writer:
        writer.writerow(data[1])

    with repo._enter_reader() as reader:
        rows = list(reader)
        assert len(rows) == 2
        assert rows[0]["name"] == "first"
        assert rows[1]["name"] == "second"
