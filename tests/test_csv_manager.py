import copy
import csv
import os
from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from moneymanager import csv_manager, transaction


class TestCsvManager(TestCase):

    # override
    def setUp(self) -> None:
        csv_manager.transaction_history_path = "temp_transaction_history.csv"
        self.__init_transaction_history()

        self.transaction_no0 = 1
        self.transaction_no1 = 5

        self.mock_transaction0 = MagicMock()
        self.mock_transaction0.date = datetime.now()
        self.mock_transaction0.account = "mandiri"
        self.mock_transaction0.amount = 10000.50
        self.mock_transaction0.type_ = "expense"
        self.mock_transaction0.category = "food"
        self.mock_transaction0.comment = "ayam super"

        self.mock_transaction1 = copy.copy(self.mock_transaction0)

        self.__add_mock_transaction(self.transaction_no0, self.mock_transaction0)
        self.__add_mock_transaction(self.transaction_no1, self.mock_transaction1)

    def test_csv_to_list_return_value(self) -> None:
        transaction_list = csv_manager.csv_to_list()
        transaction = transaction_list[1]

        self.assertEqual(transaction[0], str(self.transaction_no0))
        self.assertEqual(transaction[1], self.mock_transaction0.date.isoformat())
        self.assertEqual(transaction[2], self.mock_transaction0.account)
        self.assertEqual(transaction[3], str(self.mock_transaction0.amount))
        self.assertEqual(transaction[4], self.mock_transaction0.type_)
        self.assertEqual(transaction[5], self.mock_transaction0.category)
        self.assertEqual(transaction[6], self.mock_transaction0.comment)

    def test_get_latest_transaction_number_return_value(self) -> None:
        latest_transaction_number = csv_manager._get_latest_transaction_number()

        self.assertEqual(latest_transaction_number, self.transaction_no1)

    def test_get_latest_transaction_number_on_empty_history(self) -> None:
        self.tearDown()
        self.__init_transaction_history()

        latest_transaction_number = csv_manager._get_latest_transaction_number()

        self.assertEqual(latest_transaction_number, 0)

    def test_transaction_to_list_return_value(self) -> None:
        transaction_list = csv_manager.transaction_to_list(self.mock_transaction0)

        self.assertEqual(transaction_list[0], self.mock_transaction0.date.isoformat())
        self.assertEqual(transaction_list[1], self.mock_transaction0.account)
        self.assertEqual(transaction_list[2], str(self.mock_transaction0.amount))
        self.assertEqual(transaction_list[3], self.mock_transaction0.type_)
        self.assertEqual(transaction_list[4], self.mock_transaction0.category)
        self.assertEqual(transaction_list[5], self.mock_transaction0.comment)

    def test_list_to_transaction_return_value(self) -> None:
        transaction_list = csv_manager.transaction_to_list(self.mock_transaction0)

        transaction = csv_manager.list_to_transaction(transaction_list)

        self.assertEqual(transaction_list[0], transaction.date.isoformat())
        self.assertEqual(transaction_list[1], transaction.account)
        self.assertEqual(transaction_list[2], transaction.amount)
        self.assertEqual(transaction_list[3], transaction.type_)
        self.assertEqual(transaction_list[4], transaction.category)
        self.assertEqual(transaction_list[5], transaction.comment)

    def test_insert_transaction_successful(self) -> None:
        self.tearDown()  # remove previously added mock data from setUp
        self.__init_transaction_history()

        csv_manager.insert_transaction(self.mock_transaction0)

        with open(csv_manager.transaction_history_path) as transactions:
            reader = csv.reader(transactions)
            rows = list(reader)
            self.assertEqual(len(rows), 2)  # Assert that there is exactly one row in the CSV file
            rows[1][3] = float(rows[1][3])  # type: ignore
            self.assertEqual(
                rows[1][1:], 
                [
                    self.mock_transaction0.date.isoformat(),
                    self.mock_transaction0.account,
                    self.mock_transaction0.amount,
                    self.mock_transaction0.type_,
                    self.mock_transaction0.category,
                    self.mock_transaction0.comment
                ]
            )

    def __add_mock_transaction(self, transaction_number: int, transaction: transaction.Transaction):
        with open(csv_manager.transaction_history_path, 'a') as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow([
                transaction_number,
                transaction.date.isoformat(),
                transaction.account,
                transaction.amount,
                transaction.type_,
                transaction.category,
                transaction.comment
            ])

    def __init_transaction_history(self) -> None:
        with open(csv_manager.transaction_history_path, 'w') as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(["no", "date", "account", "amount", "type", "category", "comment"])

    # override
    def tearDown(self) -> None:
        os.remove(csv_manager.transaction_history_path)
